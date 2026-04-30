import argparse
import json
import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine, text


BASE_DIR = Path(__file__).resolve().parent
DATASET_FILES = {
    "2rb": BASE_DIR / "migration" / "jabar2rb.json",
    "75rb": BASE_DIR / "migration" / "sekolah_jabar_tanpa_tk75rb.json",
}
DEFAULT_DATASET = "75rb"


def load_database_url():
    env_candidates = [
        BASE_DIR / ".env",
        BASE_DIR.parents[1] / "backend" / ".env",
    ]

    for env_path in env_candidates:
        if env_path.exists():
            load_dotenv(env_path)
            database_url = os.getenv("DATABASE_URL")
            if database_url:
                return database_url

    raise RuntimeError("DATABASE_URL tidak ditemukan di file .env")


def normalize_status(status):
    if not status:
        return "Tidak diketahui"

    value = str(status).strip().upper()
    if value == "N":
        return "Negeri"
    if value == "S":
        return "Swasta"
    return str(status).strip()


def clean_text(value, default="-"):
    if value is None:
        return default

    cleaned = str(value).strip()
    return cleaned if cleaned else default


def load_schools(json_path: Path):
    with json_path.open("r", encoding="utf-8") as file:
        payload = json.load(file)

    schools = payload.get("data", [])
    if not isinstance(schools, list):
        raise ValueError("Format output.json tidak valid: key 'data' harus berupa list")

    return schools


def prompt_dataset_choice():
    print("Pilih dataset sekolah yang akan diimport:")
    print("1. 2rb  - jabar2rb.json")
    print("2. 75rb - sekolah_jabar_tanpa_tk75rb.json")

    while True:
        choice = input("Masukkan pilihan (1/2): ").strip()
        if choice == "1":
            return "2rb"
        if choice == "2":
            return "75rb"
        print("Pilihan tidak valid. Masukkan 1 atau 2.")


def reset_school_table(conn):
    conn.execute(text("UPDATE users SET school_id = NULL WHERE school_id IS NOT NULL"))
    conn.execute(text("DELETE FROM sekolah"))
    conn.execute(text("ALTER SEQUENCE sekolah_sekolah_id_seq RESTART WITH 1"))


def insert_schools(engine, schools):
    insert_query = text("""
        INSERT INTO sekolah (
            nama_sekolah,
            npsn,
            jenjang,
            alamat,
            kecamatan,
            latitude,
            longitude,
            location,
            kuota,
            daya_tampung,
            biaya,
            status,
            akreditasi
        )
        VALUES (
            :nama_sekolah,
            :npsn,
            :jenjang,
            :alamat,
            :kecamatan,
            :latitude,
            :longitude,
            ST_SetSRID(ST_MakePoint(:longitude, :latitude), 4326)::geography,
            :kuota,
            :daya_tampung,
            :biaya,
            :status,
            :akreditasi
        )
    """)

    inserted = 0
    skipped = 0

    all_params = []
    for school in schools:
        latitude = school.get("lang")
        longitude = school.get("long")

        if latitude is None or longitude is None:
            skipped += 1
            continue

        params = {
            "nama_sekolah": clean_text(school.get("name")),
            "npsn": clean_text(school.get("npsn")),
            "jenjang": clean_text(school.get("grade")),
            "alamat": clean_text(school.get("address")),
            "kecamatan": clean_text(school.get("district_name")),
            "latitude": latitude,
            "longitude": longitude,
            "kuota": 0,
            "daya_tampung": 0,
            "biaya": 0,
            "status": normalize_status(school.get("status")),
            "akreditasi": clean_text(school.get("accreditation")),
        }
        all_params.append(params)
        inserted += 1

    with engine.connect() as conn:
        with conn.begin():
            reset_school_table(conn)

        if all_params:
            chunk_size = 1000
            for i in range(0, len(all_params), chunk_size):
                chunk = all_params[i:i + chunk_size]
                with conn.begin():
                    conn.execute(insert_query, chunk)
                print(f"Pushed {i + len(chunk)} / {len(all_params)} schools...")

    return inserted, skipped


def main():
    parser = argparse.ArgumentParser(
        description="Import data sekolah dari JSON folder 7 ke tabel sekolah."
    )
    parser.add_argument(
        "--dataset",
        choices=sorted(DATASET_FILES.keys()),
        default=DEFAULT_DATASET,
        help="Pilih dataset sekolah yang akan diimport ulang. Opsi: 2rb atau 75rb.",
    )
    parser.add_argument(
        "--json",
        default=None,
        help="Path file JSON sekolah custom. Jika diisi, akan mengabaikan --dataset.",
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Tampilkan pilihan dataset secara interaktif saat script dijalankan.",
    )
    args = parser.parse_args()

    database_url = load_database_url()
    if args.json:
        json_path = Path(args.json)
    else:
        selected_dataset = prompt_dataset_choice() if args.interactive or len(os.sys.argv) == 1 else args.dataset
        json_path = DATASET_FILES[selected_dataset]
    schools = load_schools(json_path)
    engine = create_engine(database_url)
    inserted, skipped = insert_schools(engine, schools)

    print(f"Dataset dipakai: {json_path}")
    print(f"Total data JSON: {len(schools)}")
    print(f"Berhasil insert: {inserted}")
    print(f"Dilewati: {skipped}")


if __name__ == "__main__":
    main()

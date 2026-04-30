import argparse
import json
import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine, text


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_GEOJSON_PATH = BASE_DIR / "migration" / "Salinan Jawa_Barat_Kecamatan_Only_4326.geojson"


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


def clean_text(value, default=None):
    if value is None:
        return default

    cleaned = str(value).strip()
    return cleaned if cleaned else default


def load_geojson(geojson_path: Path):
    with geojson_path.open("r", encoding="utf-8") as file:
        payload = json.load(file)

    if payload.get("type") != "FeatureCollection":
        raise ValueError("Format GeoJSON tidak valid: root harus FeatureCollection")

    features = payload.get("features", [])
    if not isinstance(features, list):
        raise ValueError("Format GeoJSON tidak valid: key 'features' harus berupa list")

    return features


def reset_zonasi_table(conn):
    conn.execute(text("DELETE FROM zonasi"))
    conn.execute(text("ALTER SEQUENCE zonasi_zonasi_id_seq RESTART WITH 1"))


def build_wilayah(props):
    parts = [
        clean_text(props.get("WADMKD")),
        clean_text(props.get("WADMKC")),
        clean_text(props.get("WADMKK")),
        clean_text(props.get("WADMPR")),
    ]
    return ", ".join(part for part in parts if part)


def insert_zonasi(engine, features):
    insert_query = text("""
        INSERT INTO zonasi (
            nama_zonasi,
            radius_meter,
            wilayah,
            keterangan,
            objectid,
            fcode,
            remark,
            metadata,
            srs_id,
            kode_kecamatan,
            kode_desa,
            kode_kabupaten,
            kode_provinsi,
            nama_kecamatan,
            nama_desa,
            nama_kabupaten,
            nama_provinsi,
            tipadm,
            luaswh,
            uupp,
            shape_length,
            shape_area,
            geom
        )
        VALUES (
            :nama_zonasi,
            :radius_meter,
            :wilayah,
            :keterangan,
            :objectid,
            :fcode,
            :remark,
            :metadata,
            :srs_id,
            :kode_kecamatan,
            :kode_desa,
            :kode_kabupaten,
            :kode_provinsi,
            :nama_kecamatan,
            :nama_desa,
            :nama_kabupaten,
            :nama_provinsi,
            :tipadm,
            :luaswh,
            :uupp,
            :shape_length,
            :shape_area,
            ST_Multi(ST_Force2D(ST_SetSRID(ST_GeomFromGeoJSON(:geometry_json), 4326)))
        )
    """)

    inserted = 0
    skipped = 0

    with engine.begin() as conn:
        reset_zonasi_table(conn)

        for feature in features:
            props = feature.get("properties") or {}
            geometry = feature.get("geometry")

            if not geometry:
                skipped += 1
                continue

            params = {
                "nama_zonasi": clean_text(props.get("NAMOBJ"), "-"),
                "radius_meter": None,
                "wilayah": build_wilayah(props),
                "keterangan": clean_text(props.get("REMARK")) or clean_text(props.get("UUPP")),
                "objectid": props.get("OBJECTID"),
                "fcode": clean_text(props.get("FCODE")),
                "remark": clean_text(props.get("REMARK")),
                "metadata": clean_text(props.get("METADATA")),
                "srs_id": clean_text(props.get("SRS_ID")),
                "kode_kecamatan": clean_text(props.get("KDCPUM")),
                "kode_desa": clean_text(props.get("KDEPUM")),
                "kode_kabupaten": clean_text(props.get("KDPKAB")),
                "kode_provinsi": clean_text(props.get("KDPPUM")),
                "nama_kecamatan": clean_text(props.get("WADMKC")),
                "nama_desa": clean_text(props.get("WADMKD")),
                "nama_kabupaten": clean_text(props.get("WADMKK")),
                "nama_provinsi": clean_text(props.get("WADMPR")),
                "tipadm": props.get("TIPADM"),
                "luaswh": props.get("LUASWH"),
                "uupp": clean_text(props.get("UUPP")),
                "shape_length": props.get("Shape_Length"),
                "shape_area": props.get("Shape_Area"),
                "geometry_json": json.dumps(geometry),
            }

            conn.execute(insert_query, params)
            inserted += 1

    return inserted, skipped


def main():
    parser = argparse.ArgumentParser(
        description="Import GeoJSON boundary ke tabel zonasi."
    )
    parser.add_argument(
        "--geojson",
        default=str(DEFAULT_GEOJSON_PATH),
        help="Path file GeoJSON. Default: 7/backend/migration/Salinan Jawa_Barat_Kecamatan_Only_4326.geojson",
    )
    args = parser.parse_args()

    database_url = load_database_url()
    geojson_path = Path(args.geojson)
    features = load_geojson(geojson_path)
    engine = create_engine(database_url)
    inserted, skipped = insert_zonasi(engine, features)

    print(f"Dataset dipakai: {geojson_path}")
    print(f"Total feature GeoJSON: {len(features)}")
    print(f"Berhasil insert: {inserted}")
    print(f"Dilewati: {skipped}")


if __name__ == "__main__":
    main()

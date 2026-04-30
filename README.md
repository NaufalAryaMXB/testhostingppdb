# PPDB Sekolah

Project ini berisi pengembangan WebGIS PPDB Jawa Barat untuk tugas akhir. Folder `7` adalah basis project aktif yang dipakai untuk backend dan frontend terbaru.

## Struktur Folder

- `backend`
  Backend FastAPI yang aktif dipakai untuk pengembangan terbaru.
- `backend/migration`
  Berisi file SQL migrasi, dataset JSON sekolah, dan GeoJSON zonasi.
- `frontend`
  gk di edit

## Kebutuhan

- Python 3.10+
- PostgreSQL
- PostGIS

Contoh package Python yang dipakai:

```powershell
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv bcrypt
```

## Menjalankan Backend

Masuk ke folder backend:

```powershell
cd "C:\Users\MSI\Documents\Code\ppdb Sekolah\7\backend"
python -m uvicorn app.main:app --reload
```

Backend akan berjalan di:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Environment

Buat file `.env` di root folder `backend`.

Contoh:

```env
DATABASE_URL="postgresql://postgres:password@localhost/ppdb"
```

## Import Data Sekolah

Script import sekolah ada di:

- [backend/import_sekolah_json.py](C:\Users\MSI\Documents\Code\ppdb Sekolah\7\backend\import_sekolah_json.py)

Saat dijalankan tanpa argumen, script akan meminta pilihan dataset:

- `2rb` dari `backend/migration/jabar2rb.json`
- `75rb` dari `backend/migration/sekolah_jabar_tanpa_tk75rb.json`

Jalankan:

```powershell
cd "C:\Users\MSI\Documents\Code\ppdb Sekolah\7\backend"
python import_sekolah_json.py
```

Atau langsung pilih dataset:

```powershell
python import_sekolah_json.py --dataset 2rb
python import_sekolah_json.py --dataset 75rb
```

Catatan:

- script akan menghapus semua isi tabel `sekolah`
- sequence id akan di-reset
- data baru akan diinsert ulang dari file JSON yang dipilih

## Import Data Zonasi GeoJSON

Script import zonasi ada di:

- [backend/import_zonasi_geojson.py](C:\Users\MSI\Documents\Code\ppdb Sekolah\7\backend\import_zonasi_geojson.py)

Default file yang dipakai:

- `backend/migration/Salinan Jawa_Barat_Kecamatan_Only_4326.geojson`

Jalankan:

```powershell
cd "C:\Users\MSI\Documents\Code\ppdb Sekolah\7\backend"
python import_zonasi_geojson.py
```

Atau pakai file GeoJSON lain:

```powershell
python import_zonasi_geojson.py --geojson "C:\path\file.geojson"
```

Catatan:

- script akan menghapus semua isi tabel `zonasi`
- sequence id akan di-reset
- geometri akan dimasukkan ke kolom `geom`

## Endpoint Utama

### Auth

- `POST /auth/register`
- `POST /auth/login`

### Sekolah

- `GET /schools`
- `GET /schools/{school_id}`
- `POST /schools`
- `PUT /schools/{school_id}`
- `PUT /schools/by-npsn/{npsn}`
- `DELETE /schools/{school_id}`

### Zonasi

- `GET /zonasi`
- `GET /zonasi/{zonasi_id}`
- `GET /zonasi/geojson`
- `GET /zonasi/{zonasi_id}/geojson`
- `POST /zonasi`
- `PUT /zonasi/{zonasi_id}`
- `DELETE /zonasi/{zonasi_id}`

### Map

- `GET /map/schools`
- `GET /map/zonasi`

## Filter Query Zonasi

Endpoint `GET /zonasi` dan `GET /zonasi/geojson` mendukung filter:

- `wilayah`
- `kecamatan`
- `kabupaten`
- `desa`
- `kode_kecamatan`
- `kode_kabupaten`

Contoh:

```text
GET /zonasi?kabupaten=Cianjur
GET /zonasi?kecamatan=Agrabinta
GET /zonasi/geojson?kabupaten=Cianjur&kecamatan=Agrabinta
```

## Catatan

- tabel `zonasi` sekarang sudah disiapkan untuk atribut GeoJSON dan geometri polygon
- endpoint `GET /zonasi/geojson` sudah cocok untuk dipakai frontend map
- jika tim frontend ingin menampilkan garis boundary di map, endpoint GeoJSON adalah endpoint yang dipakai

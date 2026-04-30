ALTER TABLE zonasi
ADD COLUMN IF NOT EXISTS objectid INTEGER,
ADD COLUMN IF NOT EXISTS fcode TEXT,
ADD COLUMN IF NOT EXISTS metadata TEXT,
ADD COLUMN IF NOT EXISTS srs_id TEXT,
ADD COLUMN IF NOT EXISTS kode_kecamatan TEXT,
ADD COLUMN IF NOT EXISTS kode_desa TEXT,
ADD COLUMN IF NOT EXISTS kode_kabupaten TEXT,
ADD COLUMN IF NOT EXISTS kode_provinsi TEXT,
ADD COLUMN IF NOT EXISTS nama_kecamatan TEXT,
ADD COLUMN IF NOT EXISTS nama_desa TEXT,
ADD COLUMN IF NOT EXISTS nama_kabupaten TEXT,
ADD COLUMN IF NOT EXISTS nama_provinsi TEXT,
ADD COLUMN IF NOT EXISTS tipadm INTEGER,
ADD COLUMN IF NOT EXISTS luaswh DOUBLE PRECISION,
ADD COLUMN IF NOT EXISTS uupp TEXT,
ADD COLUMN IF NOT EXISTS shape_length DOUBLE PRECISION,
ADD COLUMN IF NOT EXISTS shape_area DOUBLE PRECISION;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_schema = 'public'
          AND table_name = 'zonasi'
          AND column_name = 'geom'
    ) THEN
        ALTER TABLE zonasi
        ADD COLUMN geom geometry(MultiPolygon, 4326);
    END IF;
END $$;

CREATE INDEX IF NOT EXISTS idx_zonasi_geom
ON zonasi
USING GIST (geom);

CREATE INDEX IF NOT EXISTS idx_zonasi_nama_kecamatan
ON zonasi (nama_kecamatan);

CREATE INDEX IF NOT EXISTS idx_zonasi_nama_kabupaten
ON zonasi (nama_kabupaten);

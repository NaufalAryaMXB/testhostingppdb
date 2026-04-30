from api.db import SessionLocal
from sqlalchemy import text
db = SessionLocal()
try:
    count = db.execute(text("SELECT count(*) FROM sekolah")).scalar()
    print(f"TOTAL: {count}")
    cimanggis = db.execute(text("SELECT count(*) FROM sekolah WHERE kecamatan ILIKE '%Cimanggis%'")).scalar()
    print(f"CIMANGGIS: {cimanggis}")
    sample = db.execute(text("SELECT nama_sekolah, kecamatan FROM sekolah LIMIT 5")).fetchall()
    print(f"SAMPLE: {sample}")
finally:
    db.close()

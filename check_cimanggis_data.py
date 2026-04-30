import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.models import School

DB_URL = "postgresql://postgres:y4zlDg2xbjtHEkX7@db.zgoavidubxbzbnlnkfkg.supabase.co:5432/postgres"

def check_cimanggis():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    db = Session()
    try:
        # Search for Cimanggis schools
        schools = db.query(School).filter(School.kecamatan.ilike("%Cimanggis%")).limit(10).all()
        print(f"Found {len(schools)} samples in Cimanggis (or similar)")
        for s in schools:
            print(f"- ID: {s.sekolah_id}, Nama: {s.nama_sekolah}, Kec: '{s.kecamatan}', Jenjang: {s.jenjang}")
            
        # Specific check for the one in screenshot
        tech = db.query(School).filter(School.nama_sekolah.ilike("%Techno Natura%")).all()
        for t in tech:
            print(f"\nTarget School: {t.nama_sekolah}")
            print(f"Kecamatan: '{t.kecamatan}'")
            print(f"Jenjang: {t.jenjang}")
            
    finally:
        db.close()

if __name__ == "__main__":
    check_cimanggis()

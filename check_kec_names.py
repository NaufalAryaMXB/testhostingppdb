import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.models import School

DB_URL = "postgresql://postgres:y4zlDg2xbjtHEkX7@aws-1-ap-southeast-2.pooler.supabase.com:5432/postgres"

def check_kecamatan_names():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    db = Session()
    try:
        # Get samples of kecamatan names
        schools = db.query(School.kecamatan).filter(School.kecamatan.ilike("%Cimanggis%")).distinct().all()
        print(f"Distinct Kecamatan names matching 'Cimanggis':")
        for (name,) in schools:
            print(f"- '{name}'")
            
    finally:
        db.close()

if __name__ == "__main__":
    check_kecamatan_names()

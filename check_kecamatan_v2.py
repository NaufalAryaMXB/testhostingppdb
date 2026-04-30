import os
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from api.models import Base, School

# Using the pooler address which was successful before
DB_URL = "postgresql://postgres:y4zlDg2xbjtHEkX7@aws-1-ap-southeast-2.pooler.supabase.com:5432/postgres"

def count_by_kecamatan():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    db = Session()
    try:
        results = db.query(School.kecamatan, func.count(School.sekolah_id)).group_by(School.kecamatan).order_by(func.count(School.sekolah_id).desc()).all()
        print(f"Total Unique Kecamatan: {len(results)}")
        print("\nTop 10 Kecamatan by School Count:")
        for kec, count in results[:10]:
            print(f"- {kec}: {count}")
            
        cim = db.query(School).filter(School.kecamatan.ilike("%Cimanggis%")).count()
        print(f"\nSchools in Cimanggis: {cim}")
        
    finally:
        db.close()

if __name__ == "__main__":
    count_by_kecamatan()

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.models import School

DB_URL = "postgresql://postgres:y4zlDg2xbjtHEkX7@aws-1-ap-southeast-2.pooler.supabase.com:5432/postgres"

def check_bojongsoang_jenjang():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    db = Session()
    try:
        # Search for Bojongsoang schools
        schools = db.query(School).filter(School.kecamatan.ilike("%Bojongsoang%")).all()
        print(f"Found {len(schools)} schools in Bojongsoang")
        
        # Count by jenjang
        jenjang_counts = {}
        for s in schools:
            j = s.jenjang or "NULL"
            jenjang_counts[j] = jenjang_counts.get(j, 0) + 1
            
        print("\nBreakdown by Jenjang:")
        for j, count in jenjang_counts.items():
            print(f"- '{j}': {count}")
            
        # Sample of schools with their jenjang
        print("\nSamples:")
        for s in schools[:10]:
            print(f"- {s.nama_sekolah} | Jenjang: '{s.jenjang}'")
            
    finally:
        db.close()

if __name__ == "__main__":
    check_bojongsoang_jenjang()

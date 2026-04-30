from api.db import SessionLocal
from api.models import School
from sqlalchemy import func

def count_by_kecamatan():
    db = SessionLocal()
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

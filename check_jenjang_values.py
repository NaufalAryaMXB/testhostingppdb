import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.models import School

DB_URL = "postgresql://postgres:y4zlDg2xbjtHEkX7@aws-1-ap-southeast-2.pooler.supabase.com:5432/postgres"

def check_jenjang_values():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    db = Session()
    try:
        # Get distinct jenjang values
        results = db.query(School.jenjang).distinct().all()
        print(f"Distinct Jenjang values in database:")
        for (val,) in results:
            print(f"- '{val}'")
            
    finally:
        db.close()

if __name__ == "__main__":
    check_jenjang_values()

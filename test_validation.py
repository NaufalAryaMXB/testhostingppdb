from api.db import SessionLocal
from api.crud import get_schools
from api.schemas import SchoolMapResponse
import json

db = SessionLocal()
try:
    schools = get_schools(db)
    print(f"Fetched {len(schools)} schools")
    
    # Try to validate the first one
    if schools:
        s = schools[0]
        # Manually validate against schema
        validated = SchoolMapResponse.model_validate(s)
        print("Validation success for first school")
        print(validated.model_dump_json(indent=2))
        
        # Try to validate all fetched schools
        count = 0
        for s in schools:
            SchoolMapResponse.model_validate(s)
            count += 1
        print(f"Successfully validated {count} schools")
        
finally:
    db.close()

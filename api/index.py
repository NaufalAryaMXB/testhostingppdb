from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from mangum import Mangum
from api.api import router

app = FastAPI()
BASE_DIR = Path(__file__).resolve().parent.parent
INDEX_FILE = BASE_DIR / "index.html"
ASSETS_DIR = BASE_DIR / "assets"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/ping")
def ping():
    return {"status": "ok"}

@app.get("/api/debug")
def debug():
    import os
    db_url = os.getenv("DATABASE_URL", "NOT_SET")
    masked_url = db_url[:15] + "..." + db_url[-10:] if len(db_url) > 20 else db_url
    
    try:
        from api.db import SessionLocal
        from sqlalchemy import text
        db = SessionLocal()
        result = db.execute(text("SELECT 1")).scalar()
        return {"status": "ok", "url": masked_url, "db_test": result}
    except Exception as e:
        import traceback
        return {"status": "error", "url": masked_url, "error": str(e), "trace": traceback.format_exc()}

app.include_router(router, prefix="/api")

if ASSETS_DIR.exists():
    app.mount("/assets", StaticFiles(directory=ASSETS_DIR), name="assets")


def serve_index():
    if not INDEX_FILE.exists():
        raise HTTPException(status_code=404, detail="Frontend index.html tidak ditemukan")
    return FileResponse(INDEX_FILE)


@app.get("/", include_in_schema=False)
def frontend_root():
    return serve_index()


@app.get("/{full_path:path}", include_in_schema=False)
def frontend_fallback(full_path: str):
    if full_path.startswith("api/"):
        raise HTTPException(status_code=404, detail="Not Found")
    return serve_index()


# Vercel serverless handler
handler = Mangum(app, lifespan="off")

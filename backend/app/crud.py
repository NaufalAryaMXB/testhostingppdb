from sqlalchemy import text
from sqlalchemy.orm import Session
from .models import School, User, Zonasi
from .utils import hash_password, verify_password
from typing import Optional

class UserAlreadyExistsError(Exception):
    pass


def create_user(db: Session, username, email, password, role="user", npsn=None):
    existing_username = db.query(User).filter(User.username == username).first()
    if existing_username:
        raise UserAlreadyExistsError("username sudah digunakan")

    existing_email = db.query(User).filter(User.email == email).first()
    if existing_email:
        raise UserAlreadyExistsError("email sudah digunakan")

    target_school_id = None
    if npsn and role == "sekolah":
        school = db.query(School).filter(School.npsn == npsn).first()
        if school:
            target_school_id = school.sekolah_id 
    hashed = hash_password(password)
    user = User(
        username=username,
        email=email,
        password_hash=hashed,
        role=role,
        school_id=target_school_id 
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def authenticate_user(db: Session, email, password):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        return None

    if not verify_password(password, user.password_hash):
        return None
    return user


def get_schools(
    db: Session,
    jenjang: str | None = None,
    kecamatan: str | None = None,
    status: str | None = None,
    nama: str | None = None
):
    query = db.query(School)

    if jenjang:
        query = query.filter(School.jenjang.ilike(jenjang))
    if kecamatan:
        query = query.filter(School.kecamatan.ilike(f"%{kecamatan}%"))
    if status:
        query = query.filter(School.status.ilike(status))
    if nama:
        query = query.filter(School.nama_sekolah.ilike(f"%{nama}%"))

    return query.order_by(School.nama_sekolah.asc()).all()


def get_school_by_id(db: Session, school_id: int):
    return db.query(School).filter(School.sekolah_id == school_id).first()

def get_school_by_npsn(db: Session, npsn: str):
    return db.query(School).filter(School.npsn == npsn).first()

def get_zonasi(
    db: Session,
    jenjang: str | None = None,
    wilayah: str | None = None,
    kecamatan: str | None = None,
    kabupaten: str | None = None,
    desa: str | None = None,
    kode_kecamatan: str | None = None,
    kode_kabupaten: str | None = None,
):
    query = db.query(Zonasi)

    if jenjang:
        query = query.filter(Zonasi.nama_zonasi.ilike(jenjang))
    if wilayah:
        query = query.filter(Zonasi.wilayah.ilike(f"%{wilayah}%"))
    if kecamatan:
        query = query.filter(Zonasi.nama_kecamatan.ilike(f"%{kecamatan}%"))
    if kabupaten:
        query = query.filter(Zonasi.nama_kabupaten.ilike(f"%{kabupaten}%"))
    if desa:
        query = query.filter(Zonasi.nama_desa.ilike(f"%{desa}%"))
    if kode_kecamatan:
        query = query.filter(Zonasi.kode_kecamatan == kode_kecamatan)
    if kode_kabupaten:
        query = query.filter(Zonasi.kode_kabupaten == kode_kabupaten)

    return query.order_by(
        Zonasi.nama_kabupaten.asc(),
        Zonasi.nama_kecamatan.asc(),
        Zonasi.nama_desa.asc(),
        Zonasi.nama_zonasi.asc(),
    ).all()


def get_zonasi_by_id(db: Session, zonasi_id: int):
    return db.query(Zonasi).filter(Zonasi.zonasi_id == zonasi_id).first()


def get_zonasi_geojson(
    db: Session,
    wilayah: str | None = None,
    kecamatan: str | None = None,
    kabupaten: str | None = None,
    desa: str | None = None,
    kode_kecamatan: str | None = None,
    kode_kabupaten: str | None = None,
):
    conditions = []
    params: dict[str, str] = {}

    if wilayah:
        conditions.append("wilayah ILIKE :wilayah")
        params["wilayah"] = f"%{wilayah}%"
    if kecamatan:
        conditions.append("nama_kecamatan ILIKE :kecamatan")
        params["kecamatan"] = f"%{kecamatan}%"
    if kabupaten:
        conditions.append("nama_kabupaten ILIKE :kabupaten")
        params["kabupaten"] = f"%{kabupaten}%"
    if desa:
        conditions.append("nama_desa ILIKE :desa")
        params["desa"] = f"%{desa}%"
    if kode_kecamatan:
        conditions.append("kode_kecamatan = :kode_kecamatan")
        params["kode_kecamatan"] = kode_kecamatan
    if kode_kabupaten:
        conditions.append("kode_kabupaten = :kode_kabupaten")
        params["kode_kabupaten"] = kode_kabupaten

    where_sql = f"WHERE {' AND '.join(conditions)}" if conditions else ""
    query = text(f"""
        SELECT json_build_object(
            'type', 'FeatureCollection',
            'features', COALESCE(json_agg(
                json_build_object(
                    'type', 'Feature',
                    'id', zonasi_id,
                    'geometry', ST_AsGeoJSON(geom)::json,
                    'properties', json_build_object(
                        'zonasi_id', zonasi_id,
                        'nama_zonasi', nama_zonasi,
                        'radius_meter', radius_meter,
                        'wilayah', wilayah,
                        'keterangan', keterangan,
                        'objectid', objectid,
                        'fcode', fcode,
                        'remark', remark,
                        'metadata', metadata,
                        'srs_id', srs_id,
                        'kode_kecamatan', kode_kecamatan,
                        'kode_desa', kode_desa,
                        'kode_kabupaten', kode_kabupaten,
                        'kode_provinsi', kode_provinsi,
                        'nama_kecamatan', nama_kecamatan,
                        'nama_desa', nama_desa,
                        'nama_kabupaten', nama_kabupaten,
                        'nama_provinsi', nama_provinsi,
                        'tipadm', tipadm,
                        'luaswh', luaswh,
                        'uupp', uupp,
                        'shape_length', shape_length,
                        'shape_area', shape_area
                    )
                )
                ORDER BY nama_kabupaten, nama_kecamatan, nama_desa, nama_zonasi
            ), '[]'::json)
        ) AS feature_collection
        FROM zonasi
        {where_sql}
    """)
    return db.execute(query, params).scalar()


def get_zonasi_geojson_by_id(db: Session, zonasi_id: int):
    query = text("""
        SELECT json_build_object(
            'type', 'Feature',
            'id', zonasi_id,
            'geometry', ST_AsGeoJSON(geom)::json,
            'properties', json_build_object(
                'zonasi_id', zonasi_id,
                'nama_zonasi', nama_zonasi,
                'radius_meter', radius_meter,
                'wilayah', wilayah,
                'keterangan', keterangan,
                'objectid', objectid,
                'fcode', fcode,
                'remark', remark,
                'metadata', metadata,
                'srs_id', srs_id,
                'kode_kecamatan', kode_kecamatan,
                'kode_desa', kode_desa,
                'kode_kabupaten', kode_kabupaten,
                'kode_provinsi', kode_provinsi,
                'nama_kecamatan', nama_kecamatan,
                'nama_desa', nama_desa,
                'nama_kabupaten', nama_kabupaten,
                'nama_provinsi', nama_provinsi,
                'tipadm', tipadm,
                'luaswh', luaswh,
                'uupp', uupp,
                'shape_length', shape_length,
                'shape_area', shape_area
            )
        ) AS feature
        FROM zonasi
        WHERE zonasi_id = :zonasi_id
    """)
    return db.execute(query, {"zonasi_id": zonasi_id}).scalar()

# --- School CRUD ---
 
def create_school(db: Session, data) -> "School":
    school = School(
        nama_sekolah=data.nama_sekolah,
        npsn=getattr(data, "npsn", None),
        jenjang=data.jenjang,
        alamat=data.alamat,
        kecamatan=data.kecamatan,
        latitude=data.latitude,
        longitude=data.longitude,
        kuota=data.kuota,
        daya_tampung=data.daya_tampung,
        biaya=data.biaya,
        status=data.status,
        akreditasi=data.akreditasi,
    )
    db.add(school)
    db.commit()
    db.refresh(school)
    return school
 
 
def update_school(db: Session, school_id: int, data) -> Optional["School"]:
    school = db.query(School).filter(School.sekolah_id == school_id).first()
    if not school:
        return None
    # Update hanya field yang dikirim (tidak None)
    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(school, key, value)
    db.commit()
    db.refresh(school)
    return school


def update_school_by_npsn(db: Session, npsn: str, data) -> Optional["School"]:
    school = db.query(School).filter(School.npsn == npsn).first()
    if not school:
        return None
    update_data = data.model_dump(exclude_unset=True)
    if "npsn" in update_data:
        update_data.pop("npsn")
    for key, value in update_data.items():
        setattr(school, key, value)
    db.commit()
    db.refresh(school)
    return school
 
 
def delete_school(db: Session, school_id: int) -> bool:
    school = db.query(School).filter(School.sekolah_id == school_id).first()
    if not school:
        return False
    db.delete(school)
    db.commit()
    return True
 
 
# --- Zonasi CRUD ---
 
def create_zonasi(db: Session, data) -> "Zonasi":
    zonasi = Zonasi(
        nama_zonasi=data.nama_zonasi,
        radius_meter=data.radius_meter,
        wilayah=data.wilayah,
        keterangan=data.keterangan,
        objectid=data.objectid,
        fcode=data.fcode,
        remark=data.remark,
        metadata_value=data.metadata,
        srs_id=data.srs_id,
        kode_kecamatan=data.kode_kecamatan,
        kode_desa=data.kode_desa,
        kode_kabupaten=data.kode_kabupaten,
        kode_provinsi=data.kode_provinsi,
        nama_kecamatan=data.nama_kecamatan,
        nama_desa=data.nama_desa,
        nama_kabupaten=data.nama_kabupaten,
        nama_provinsi=data.nama_provinsi,
        tipadm=data.tipadm,
        luaswh=data.luaswh,
        uupp=data.uupp,
        shape_length=data.shape_length,
        shape_area=data.shape_area,
    )
    db.add(zonasi)
    db.commit()
    db.refresh(zonasi)
    return zonasi
 
 
def update_zonasi(db: Session, zonasi_id: int, data) -> Optional["Zonasi"]:
    zonasi = db.query(Zonasi).filter(Zonasi.zonasi_id == zonasi_id).first()
    if not zonasi:
        return None
    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(zonasi, key, value)
    db.commit()
    db.refresh(zonasi)
    return zonasi
 
 
def delete_zonasi(db: Session, zonasi_id: int) -> bool:
    zonasi = db.query(Zonasi).filter(Zonasi.zonasi_id == zonasi_id).first()
    if not zonasi:
        return False
    db.delete(zonasi)
    db.commit()
    return True
 
 
# --- Operator: ambil sekolah afiliasi berdasarkan user ---
 
def get_school_by_user(db: Session, user_id: int) -> Optional["School"]:
    """Ambil sekolah yang diasosiasikan ke akun operator."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user or not user.school_id:
        return None
    return db.query(School).filter(School.sekolah_id == user.school_id).first()

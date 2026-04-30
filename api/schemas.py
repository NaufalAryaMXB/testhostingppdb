from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


class RegisterSchema(BaseModel):
    username: str
    email: str
    password: str
    role: str = "user"
    admin_code: Optional[str] = None
    operator_code: Optional[str] = None
    npsn: Optional[str] = None

class LoginSchema(BaseModel):
    email: str
    password: str


class SchoolResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    sekolah_id: int
    nama_sekolah: str
    npsn: str | int | None = None
    jenjang: str | None = None
    alamat: str | None = None
    kecamatan: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    kuota: int | None = None
    daya_tampung: int | None = None
    biaya: int | None = None
    status: str | None = None
    akreditasi: str | None = None


class SchoolMapResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    sekolah_id: int
    nama_sekolah: str
    npsn: str | int | None = None
    jenjang: str | None = None
    kecamatan: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    status: str | None = None
    alamat: str | None = None
    kuota: int | None = None
    daya_tampung: int | None = None
    biaya: int | None = None
    akreditasi: str | None = None


class ZonasiResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    zonasi_id: int
    nama_zonasi: str
    radius_meter: float | None = None
    wilayah: str | None = None
    keterangan: str | None = None
    objectid: int | None = None
    fcode: str | None = None
    remark: str | None = None
    metadata: str | None = Field(default=None, validation_alias="metadata_value")
    srs_id: str | None = None
    kode_kecamatan: str | None = None
    kode_desa: str | None = None
    kode_kabupaten: str | None = None
    kode_provinsi: str | None = None
    nama_kecamatan: str | None = None
    nama_desa: str | None = None
    nama_kabupaten: str | None = None
    nama_provinsi: str | None = None
    tipadm: int | None = None
    luaswh: float | None = None
    uupp: str | None = None
    shape_length: float | None = None
    shape_area: float | None = None

# --- School CRUD schemas ---
class SchoolCreate(BaseModel):
    nama_sekolah: str
    npsn:         Optional[str] = None
    jenjang:      Optional[str] = None
    alamat:       Optional[str] = None
    kecamatan:    Optional[str] = None
    latitude:     Optional[float] = None
    longitude:    Optional[float] = None
    kuota:        Optional[int] = None
    daya_tampung: Optional[int] = None
    biaya:        Optional[int] = None
    status:       Optional[str] = None   
    akreditasi:   Optional[str] = None
 
class SchoolUpdate(SchoolCreate):
    nama_sekolah: Optional[str] = None  
 
# --- Zonasi CRUD schemas ---
class ZonasiCreate(BaseModel):
    nama_zonasi:  str
    radius_meter: Optional[float] = None
    wilayah:      Optional[str]   = None
    keterangan:   Optional[str]   = None
    objectid:     Optional[int]   = None
    fcode:        Optional[str]   = None
    remark:       Optional[str]   = None
    metadata:     Optional[str]   = None
    srs_id:       Optional[str]   = None
    kode_kecamatan: Optional[str] = None
    kode_desa:    Optional[str]   = None
    kode_kabupaten: Optional[str] = None
    kode_provinsi: Optional[str]  = None
    nama_kecamatan: Optional[str] = None
    nama_desa:    Optional[str]   = None
    nama_kabupaten: Optional[str] = None
    nama_provinsi: Optional[str]  = None
    tipadm:       Optional[int]   = None
    luaswh:       Optional[float] = None
    uupp:         Optional[str]   = None
    shape_length: Optional[float] = None
    shape_area:   Optional[float] = None
 
class ZonasiUpdate(ZonasiCreate):
    nama_zonasi: Optional[str] = None

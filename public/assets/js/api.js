/**
 * api.js — Integrasi API
 * Fetch data dari endpoint, fallback ke data lokal jika gagal.
 */

const API_BASE = '/api';  // relative — works on any domain
const API_URL = `${API_BASE}/map/schools`;
const ZONASI_URL = `${API_BASE}/zonasi`;
const ZONASI_GEOJSON_URL = `${API_BASE}/zonasi/geojson`;
const SCHOOL_URL = `${API_BASE}/schools`;

function normalize(raw) {
  return {
    // Sesuaikan mapping dengan SchoolMapResponse di backend
    id:         raw.sekolah_id ?? Math.random(),
    nama:       raw.nama_sekolah ?? 'Tanpa Nama',
    npsn:       raw.npsn ?? '-',
    jenjang:    raw.jenjang ?? '',
    kecamatan:  raw.kecamatan ?? '',
    lat:        parseFloat(raw.latitude ?? 0),
    lng:        parseFloat(raw.longitude ?? 0),
    status:     raw.status ?? '',
    akreditasi: raw.akreditasi ?? '-', 
    pendaftar:  raw.daya_tampung ?? 0, 
    kuota:      raw.kuota ?? 0,
    biaya:      raw.biaya ?? 0,
    alamat:     raw.alamat ?? '-',
  };
}

/* Fallback data — kosongkan agar hanya menggunakan data database */
const FALLBACK = [];

export async function fetchSekolah(filters = {}) {
  try {
    const params = new URLSearchParams();
    if (filters.kat) params.set('jenjang', filters.kat);
    if (filters.kecamatan) params.set('kecamatan', filters.kecamatan);
    if (filters.nama) params.set('nama', filters.nama);
    if (Number.isFinite(filters.lat)) params.set('lat', filters.lat);
    if (Number.isFinite(filters.lng)) params.set('lng', filters.lng);
    if (Number.isFinite(filters.radius)) params.set('radius', filters.radius);

    const url = params.toString() ? `${API_URL}?${params.toString()}` : API_URL;

    const ctrl = new AbortController();
    const tid  = setTimeout(() => ctrl.abort(), 30000);
    const res  = await fetch(url, {
      signal: ctrl.signal,
      cache: 'no-store',
      headers: { 'Cache-Control': 'no-cache' },
    });
    clearTimeout(tid);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const json = await res.json();
    const raw  = Array.isArray(json) ? json : (json.data ?? []);
    return { data: raw.map(normalize), fromFallback: false };
  } catch (err) {
    console.warn('[API] Gagal mengambil data dari database:', err.message);
    return { data: [], fromFallback: true };
  }
}

export async function fetchSchoolDetail(id) {
  const res = await fetch(`${SCHOOL_URL}/${id}`, {
    cache: 'no-store',
    headers: { 'Cache-Control': 'no-cache' },
  });
  const json = await res.json();
  if (!res.ok) throw new Error(json.detail || 'Gagal memuat detail sekolah');
  return normalize(json);
}

export async function fetchZonasiGeoJSON(kecamatan) {
  const params = new URLSearchParams();
  if (kecamatan) params.set('kecamatan', kecamatan);

  const url = params.toString()
    ? `${ZONASI_GEOJSON_URL}?${params.toString()}`
    : ZONASI_GEOJSON_URL;

  const response = await fetch(url);
  let result = null;

  try {
    result = await response.json();
  } catch {
    throw new Error('Server zonasi tidak merespon dengan benar');
  }

  if (!response.ok) {
    throw new Error(result?.detail || 'Gagal memuat data zonasi');
  }

  return result;
}

export async function fetchZonasiList() {
  const response = await fetch(ZONASI_URL);
  let result = null;

  try {
    result = await response.json();
  } catch {
    throw new Error('Server zonasi tidak merespon dengan benar');
  }

  if (!response.ok || !Array.isArray(result)) {
    throw new Error(result?.detail || 'Gagal memuat daftar zonasi');
  }

  return result;
}

// 18-04-2026
const AUTH_URL = `${API_BASE}/auth`;

export async function registerUser(username, email, password, role, admin_code, operator_code, npsn) {
  const response = await fetch(`${AUTH_URL}/register`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, email, password, role, admin_code, operator_code, npsn})
  });
  
  const result = await response.json();
  if (!response.ok) throw new Error(result.detail || 'Registrasi gagal');
  return result;
}

export async function loginUser(email, password) {
  try {
    const response = await fetch(`${AUTH_URL}/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });

    let result;
    try {
      result = await response.json();
    } catch {
      throw new Error('Server tidak merespon dengan benar');
    }

    if (!response.ok) {
      throw new Error(result.detail || 'Email atau password salah');
    }

    localStorage.setItem('user_session', JSON.stringify(result));
    return result;

  } catch (err) {
    //  handle network error
    if (err.message === 'Failed to fetch') {
      throw new Error('Tidak bisa terhubung ke server');
    }
    throw err;
  }
}

export async function createSchool(data) {
  const res = await fetch(SCHOOL_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  const json = await res.json();
  if (!res.ok) throw new Error(json.detail || 'Gagal menambahkan sekolah');
  return json;
}

export async function updateSchool(id, data) {
  const res = await fetch(`${SCHOOL_URL}/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  const json = await res.json();
  if (!res.ok) throw new Error(json.detail || 'Gagal memperbarui sekolah');
  return json;
}

export async function deleteSchool(id) {
  const res = await fetch(`${SCHOOL_URL}/${id}`, { method: 'DELETE' });
  if (!res.ok) { const j = await res.json(); throw new Error(j.detail || 'Gagal menghapus'); }
  return true;
}

export async function getMySchool(userId) {
  const res = await fetch(`${API_BASE}/operator/my-school`, {
    headers: { 'X-User-Id': userId }
  });
  if (!res.ok) return null;
  return res.json();
}

/**
 * Mencari koordinat berdasarkan teks alamat menggunakan Nominatim (OSM)
 */
export async function searchAddress(query) {
  if (!query || query.length < 3) return [];
  try {
    const url = `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(query)}&limit=5&countrycodes=id`;
    const resp = await fetch(url, {
      headers: { 'Accept-Language': 'id' }
    });
    const data = await resp.json();
    
    return data.map(item => ({
      display: item.display_name,
      lat: parseFloat(item.lat),
      lng: parseFloat(item.lon)
    }));
  } catch (err) {
    console.error('Alamat search error:', err);
    return [];
  }
}

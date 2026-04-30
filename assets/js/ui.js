/**
 * ui.js — Manipulasi DOM & rendering komponen UI
 */

import { formatDist, classifyDistance, detectJenjang, JENJANG_CFG } from './utils.js';
import { getUserLocation, getRadius } from './state.js';
import { haversineDistance } from './utils.js';
import { fetchSchoolDetail } from './api.js';

/* ── Toast ─────────────────────────────────────── */
let _toastT;
let _schoolDetailBound = false;
export function showToast(msg, type = 'info', ms = 3000) {
  const el = document.getElementById('toast');
  clearTimeout(_toastT);
  el.textContent = msg;
  el.className = `toast show ${type}`;
  _toastT = setTimeout(() => el.classList.remove('show'), ms);
}

/* ── Loading ────────────────────────────────────── */
export function showLoading() { document.getElementById('loading-overlay').classList.remove('hidden'); }
export function hideLoading() { document.getElementById('loading-overlay').classList.add('hidden'); }

function formatSchoolValue(value, fallback = '-') {
  return value === null || value === undefined || value === '' ? fallback : value;
}

function bindSchoolDetailModal() {
  if (_schoolDetailBound) return;
  _schoolDetailBound = true;

  document.getElementById('modal-school-detail-close')?.addEventListener('click', () => {
    document.getElementById('modal-school-detail')?.classList.add('hidden');
  });

  document.getElementById('modal-school-detail')?.addEventListener('click', (e) => {
    if (e.target.id === 'modal-school-detail') {
      e.currentTarget.classList.add('hidden');
    }
  });
}

function renderSchoolDetail(school, distance = null) {
  bindSchoolDetailModal();
  const modal = document.getElementById('modal-school-detail');
  if (!modal || !school) return;

  const kuota = Number(school.kuota || 0);
  const pendaftar = Number(school.pendaftar || 0);
  const sisa = Math.max(kuota - pendaftar, 0);
  const jenjang = detectJenjang(school.jenjang || school.nama);
  const cfg = JENJANG_CFG[jenjang] || JENJANG_CFG.other;

  const setText = (id, value) => {
    const el = document.getElementById(id);
    if (el) el.textContent = value;
  };

  setText('school-detail-name', formatSchoolValue(school.nama));
  setText('school-detail-jenjang', cfg.label);
  setText('school-detail-status', formatSchoolValue(school.status));
  setText('school-detail-distance', distance !== null ? formatDist(distance) : '-');
  setText('school-detail-address', formatSchoolValue(school.alamat, 'Alamat belum tersedia'));
  setText('school-detail-kecamatan', formatSchoolValue(school.kecamatan));
  setText('school-detail-npsn', formatSchoolValue(school.npsn));
  setText('school-detail-akreditasi', formatSchoolValue(school.akreditasi));
  setText('school-detail-kuota', kuota.toLocaleString('id-ID'));
  setText('school-detail-pendaftar', pendaftar.toLocaleString('id-ID'));
  setText('school-detail-sisa', sisa.toLocaleString('id-ID'));
  setText('school-detail-latlng', `${formatSchoolValue(school.lat)}, ${formatSchoolValue(school.lng)}`);

  const badge = document.getElementById('school-detail-jenjang');
  if (badge) {
    badge.style.background = `${cfg.color}1a`;
    badge.style.color = cfg.color;
  }

  modal.classList.remove('hidden');
}

export async function showSchoolDetail(school, distance = null) {
  renderSchoolDetail(school, distance);

  const needsRefresh = school?.id && (!school.npsn || school.npsn === '-');
  if (!needsRefresh) return;

  try {
    const freshSchool = await fetchSchoolDetail(school.id);
    renderSchoolDetail({ ...school, ...freshSchool }, distance);
  } catch {
    // Biarkan modal tetap tampil dengan data yang sudah ada.
  }
}

/* ── Navbar active link ─────────────────────────── */
export function setActiveNav(page) {
  document.querySelectorAll('.nav-link').forEach(a => {
    a.classList.toggle('active', a.dataset.page === page);
  });
  document.querySelectorAll('.bnav-btn').forEach(b => {
    b.classList.toggle('active', b.dataset.page === page);
  });
}

/* ── Search bar visibility ──────────────────────── */
export function toggleSearchBar(visible) {
  const el = document.getElementById('search-bar-row');
  if (el) el.classList.toggle('hidden', !visible);
}

/* ── Home table ─────────────────────────────────── */
export function renderHomeTable(items, page, total) {
  const tbody = document.getElementById('home-tbody');
  if (!items.length) {
    tbody.innerHTML = '<article class="school-preview-card loading-card">Tidak ada data sekolah</article>';
  } else {
    tbody.innerHTML = items.map((s) => {
      const kuota = Number(s.kuota || 0);
      const pendaftar = Number(s.pendaftar || 0);
      const sisa = Math.max(kuota - pendaftar, 0);
      const fill = kuota > 0 ? Math.min((pendaftar / kuota) * 100, 100) : 0;
      const badge = s.akreditasi ? `Akreditasi ${s.akreditasi}` : 'Data sekolah';
      const wilayah = [s.kecamatan, s.kab_kota || s.kabupaten || s.kabkota].filter(Boolean).join(', ') || 'Jawa Barat';

      return `
        <article class="school-preview-card">
          <div class="preview-top">
            <span class="preview-badge">${badge}</span>
            <span>${s.jenjang || detectJenjang(s.nama)}</span>
          </div>
          <div>
            <h4>${s.nama}</h4>
            <p>${wilayah}</p>
          </div>
          <div class="preview-meta">
            <span>Kuota ${kuota || '-'}</span>
            <span>Pendaftar ${pendaftar || '-'}</span>
            <span>Sisa ${sisa}</span>
          </div>
          <div class="preview-progress"><span style="width:${fill}%"></span></div>
          <p>${s.alamat ?? 'Alamat belum tersedia'}</p>
        </article>`;
    }).join('');
  }
  document.getElementById('home-page-info').textContent = `Page ${page} of ${total}`;
  document.getElementById('home-prev').disabled = page <= 1;
  document.getElementById('home-next').disabled = page >= total;
}

/* ── Flat list (Map & Zonasi) ───────────────────── */
export function renderFlatList(listId, pageInfoId, prevId, nextId, items, page, total, onClickItem, onHover, onOut) {
  const ul = document.getElementById(listId);
  const userLoc = getUserLocation();
  const radius  = getRadius();

  if (!items.length) {
    ul.innerHTML = '<li class="flat-list-empty">Tidak ada sekolah ditemukan</li>';
  } else {
    ul.innerHTML = '';
    items.forEach(school => {
      const dist  = userLoc
        ? haversineDistance(userLoc.lat, userLoc.lng, school.lat, school.lng)
        : null;
      const color = dist !== null ? classifyDistance(dist, radius) : 'default';
      const dotClass = color === 'default' ? '' : `dot-${color}`;

      const jenjang = detectJenjang(school.jenjang || school.nama);
      const jCfg    = JENJANG_CFG[jenjang] || JENJANG_CFG.other;

      const sisaKuota = school.kuota - school.pendaftar;
      const kuotaWarna = sisaKuota < 10 ? 'red' : 'green';

      const li = document.createElement('li');
      li.className = 'flat-list-item';
      li.dataset.id = school.id;
      li.innerHTML = `
        <span class="item-jenjang-dot" style="background:${jCfg.color}"></span>
        <div class="item-info">
          <span class="item-name">${school.nama}</span>
          <span class="item-jenjang-badge" style="background:${jCfg.color}1a;color:${jCfg.color}">${jCfg.label}</span>
        </div>
        <div class="item-meta">
          <span class="quota-info" style="color:${kuotaWarna}">
            Sisa Kuota: ${sisaKuota} (Total: ${school.kuota})
          </span>
        </div>
        ${dist !== null ? `<span class="item-dist item-dist--${color}">${formatDist(dist)}</span>` : ''}
      `;
      li.addEventListener('click',      () => onClickItem?.(school, dist));
      li.addEventListener('mouseenter', () => onHover?.(school));
      li.addEventListener('mouseleave', () => onOut?.(school));
      ul.appendChild(li);
    });
  }

  document.getElementById(pageInfoId).textContent = `Page ${page} of ${total}`;
  document.getElementById(prevId).disabled = page <= 1;
  document.getElementById(nextId).disabled = page >= total;
}

export function updateUIForLoggedInUser() {
  const userJson  = localStorage.getItem('user_session');
  const authGroup = document.querySelector('.navbar-right');
  if (!authGroup) return;

  const setText = (id, value) => {
    const el = document.getElementById(id);
    if (el) el.textContent = value;
  };

  if (!userJson) {
    document.querySelectorAll('.requires-login-nav').forEach(el => el.classList.add('hidden'));
    setText('profile-username', 'Guest');
    setText('profile-email', 'Belum login');
    setText('profile-role', 'Pengguna publik');
    setText('prof-pass', '••••••••••');

    // Belum login: tampilkan tombol Masuk & Daftar
    authGroup.innerHTML = `
      <div class="auth-buttons">
        <button class="btn-nav-auth" data-page="login">Masuk</button>
        <button class="btn-nav-auth btn-nav-auth--outline" data-page="register">Daftar</button>
      </div>`;
    return;
  }

  const user = JSON.parse(userJson);
  document.querySelectorAll('.requires-login-nav').forEach(el => el.classList.remove('hidden'));
  setText('profile-username', user.username || 'User');
  setText('profile-email', user.email || '-');
  setText('profile-role', user.role || 'user');
  setText('prof-pass', '••••••••••');

  // Sudah login: tampilkan akses profil dan logout singkat
  authGroup.innerHTML = `
    <div class="auth-buttons auth-buttons--logged">
      <button class="btn-nav-auth btn-nav-auth--outline" data-page="profile">${user.username || 'Profil'}</button>
      <button class="btn-nav-auth keluar-link" data-page="login">Keluar</button>
    </div>`;
}

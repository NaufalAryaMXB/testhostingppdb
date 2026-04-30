#!/usr/bin/env python3
"""Build new index.html - Part 1: Head + Sidebar Nav + Home + Map + Zonasi pages"""

HEAD = '''<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>ZonasiJabar — WebGIS PPDB</title>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="assets/css/style.css"/>
</head>
<body>
<div class="cosmos-bg"></div>

<div id="loading-overlay" class="loading-overlay">
  <div class="loader-ring"><div></div><div></div><div></div></div>
  <p class="loader-text">Memuat data<span class="dots"></span></p>
</div>
<div id="toast" class="toast"></div>
'''

SIDEBAR = '''
<aside class="sidebar navbar">
  <div class="sb-top">
    <div class="sb-logo"><span class="logo-icon">🗺️</span><span class="logo-label">Zonasi<br>Jabar</span></div>
    <nav class="sb-nav">
      <a href="#" class="sb-link nav-link active" data-page="home"><span class="sb-ico">🏠</span><span>Home</span></a>
      <a href="#" class="sb-link nav-link" data-page="map"><span class="sb-ico">📍</span><span>Peta</span></a>
      <a href="#" class="sb-link nav-link" data-page="zonasi"><span class="sb-ico">🎯</span><span>Zonasi</span></a>
    </nav>
  </div>
  <div class="sb-bottom">
    <div id="search-bar-row" class="sb-search-wrap">
      <input type="search" id="global-search" class="sb-search" placeholder="Cari sekolah..."/>
    </div>
    <div class="navbar-right sb-auth"></div>
    <button class="sb-profile-btn user-btn" data-page="profile" title="Profil">
      <svg width="22" height="22" viewBox="0 0 26 26" fill="none"><circle cx="13" cy="9" r="5" stroke="currentColor" stroke-width="2"/><path d="M3 23c0-5.523 4.477-10 10-10s10 4.477 10 10" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
    </button>
  </div>
</aside>
<div class="bottom-nav" style="display:none"></div>
'''

HOME = '''
<main class="main-content">

<!-- HOME -->
<section id="page-home" class="page active page-scroll">
  <div class="home-hero">
    <div class="hero-glow"></div>
    <h1 class="hero-title">Temukan Sekolah<br><span class="grad-text">Terbaik di Jabar</span></h1>
    <p class="hero-sub">Eksplorasi peta interaktif dan cek radius zonasi PPDB di seluruh Jawa Barat.</p>
    <div class="hero-btns">
      <button class="btn-glow" data-page="map">🗺️ Eksplorasi Peta</button>
      <button class="btn-ghost" data-page="zonasi">🎯 Cek Zonasi</button>
    </div>
  </div>
  <div class="home-grid">
    <div class="hcard hcard-stats">
      <div class="hcard-head"><h3>📊 Sekolah Populer</h3>
        <div class="pg-mini"><button id="home-prev" class="pg-btn">‹</button><span id="home-page-info">1/1</span><button id="home-next" class="pg-btn">›</button></div>
      </div>
      <table class="dtable"><thead><tr><th>No</th><th>Nama</th><th>Akreditasi</th><th>Pendaftar</th><th>Alamat</th></tr></thead>
      <tbody id="home-tbody"><tr><td colspan="5">Memuat…</td></tr></tbody></table>
    </div>
    <div class="hcard hcard-news">
      <div class="hcard-head"><h3>📰 Info Terkini</h3>
        <div class="pg-mini"><button id="berita-prev" class="pg-btn">‹</button><button id="berita-next" class="pg-btn">›</button></div>
      </div>
      <div class="news-placeholder"><div class="news-shimmer"></div><p>Informasi PPDB terbaru akan tampil di sini</p></div>
    </div>
  </div>
</section>

<!-- MAP (full-screen with floating panel) -->
<section id="page-map" class="page page-full">
  <div id="map-view" class="fullmap"></div>
  <div class="map-float-panel" id="map-filter-box">
    <div class="fp-header"><h2>🏫 Peta Sekolah</h2><p>Filter & jelajahi sekolah di Jawa Barat</p></div>
    <div class="fp-filters">
      <div class="fg2"><label>Kategori</label><select class="fi" id="map-kat"><option value="">Semua</option><option value="SD">SD</option><option value="SMP">SMP</option><option value="SMA">SMA</option><option value="SMK">SMK</option></select></div>
      <div class="fg2"><label>Akreditasi</label><select id="filter-akreditasi" class="fi"><option value="">Semua</option><option value="A">A</option><option value="B">B</option><option value="C">C</option></select></div>
      <div class="fg2"><label>Biaya</label><select class="fi" id="map-biaya"><option value="">Semua</option><option value="gratis">Gratis</option><option value="murah">Murah</option></select></div>
      <div class="fg2"><label>Maks Biaya</label><input type="number" id="filter-biaya" class="fi" placeholder="Rp..."></div>
      <div class="fg2 fg2-btns"><button class="btn-sm-outline" id="map-clear">Reset</button><button class="btn-sm-fill" id="map-apply">Terapkan</button></div>
    </div>
    <div class="fp-list">
      <h4>Daftar Sekolah</h4>
      <ul class="school-list" id="map-list"></ul>
      <div class="fp-pg"><button class="pg-btn" id="map-prev">‹</button><span id="map-page-info">1/1</span><button class="pg-btn" id="map-next">›</button></div>
    </div>
  </div>
</section>
'''

ZONASI = '''
<!-- ZONASI -->
<section id="page-zonasi" class="page page-full">
  <!-- Step 1 -->
  <div id="zonasi-input-step" class="zon-step1">
    <div class="zon-card glass-card">
      <div class="zon-card-icon">📍</div>
      <h2>Cek Jarak Zonasi</h2>
      <p>Tentukan titik awal untuk mencari sekolah dalam radius tertentu.</p>
      <div class="loc-tabs">
        <button class="loc-tab active" data-tab="gps">GPS</button>
        <button class="loc-tab" data-tab="koordinat">Koordinat</button>
        <button class="loc-tab" data-tab="kota">Kota/Kab</button>
      </div>
      <div class="loc-tab-panel active" id="tab-gps">
        <p class="tab-desc">Otomatis deteksi lokasi Anda.</p>
        <button class="btn-glow full-w" id="btn-geoloc">📡 Deteksi Lokasi</button>
        <div id="gps-status" class="gps-status"></div>
      </div>
      <div class="loc-tab-panel" id="tab-koordinat">
        <div class="row2"><div><label>Latitude</label><input type="number" id="input-lat" class="fi" placeholder="-6.9..."></div><div><label>Longitude</label><input type="number" id="input-lng" class="fi" placeholder="107.6..."></div></div>
        <button class="btn-glow full-w mt16" id="btn-submit-koordinat">Gunakan Koordinat</button>
      </div>
      <div class="loc-tab-panel" id="tab-kota">
        <label>Cari Kota/Kabupaten</label>
        <div class="kota-search-wrap" style="position:relative">
          <input type="search" id="input-kota-search" class="fi" placeholder="Ketik nama..."/>
          <div id="kota-dropdown" class="dropdown-list"></div>
        </div>
        <div id="kota-selected-info" class="status-text mt8"></div>
        <button class="btn-glow full-w mt16" id="btn-submit-kota" disabled>Pilih Kota</button>
      </div>
      <div class="radius-wrap mt16">
        <label>Radius (km)</label>
        <div class="radius-row"><input type="number" id="radius-num" value="5" class="fi fi-short"/><input type="range" id="radius-range" value="5" min="0.1" max="20" step="0.1" class="slider"/></div>
      </div>
    </div>
  </div>

  <!-- Step 2 -->
  <div id="zonasi-result-step" class="hidden page-full">
    <div id="zonasi-view" class="fullmap"></div>
    <div class="map-float-panel" id="zonasi-filter-box">
      <div class="fp-loc-badge">
        <div><span class="fp-loc-label">📌 Lokasi Aktif</span><span class="fp-loc-val" id="zonasi-active-loc">...</span></div>
        <div class="fp-loc-acts"><span class="rad-badge" id="zonasi-radius-badge">5 km</span><button class="btn-sm-outline" id="btn-change-loc">Ubah</button></div>
      </div>
      <div class="fp-filters">
        <div class="fg2"><label>Kategori</label><select class="fi" id="zon-kat"><option value="">Semua</option><option value="SD">SD</option><option value="SMP">SMP</option><option value="SMA">SMA</option><option value="SMK">SMK</option></select></div>
        <div class="fg2 fg2-btns"><button class="btn-sm-outline" id="zon-clear">Reset</button><button class="btn-sm-fill" id="zon-apply">Filter</button></div>
      </div>
      <div class="fp-list">
        <div class="fp-list-head"><h4>Hasil Zonasi</h4><div class="legend-mini"><span class="ld g"></span>Dalam <span class="ld y"></span>Dekat <span class="ld r"></span>Luar</div></div>
        <ul class="school-list" id="zon-list"></ul>
        <div class="fp-pg"><button class="pg-btn" id="zon-prev">‹</button><span id="zon-page-info">1/1</span><button class="pg-btn" id="zon-next">›</button></div>
      </div>
    </div>
  </div>
</section>
'''

with open("_part1.html","w",encoding="utf-8") as f:
    f.write(HEAD + SIDEBAR + HOME + ZONASI)
print("Part 1 written")

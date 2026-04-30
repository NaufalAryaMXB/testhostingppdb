import os

html_content = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>WebGIS Zonasi Sekolah - Redesigned</title>
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="assets/css/style.css" />
</head>
<body>

  <!-- BACKGROUND -->
  <div class="mesh-bg"></div>

  <!-- LOADING & TOAST -->
  <div id="loading-overlay" class="loading-overlay">
    <div class="spinner"></div><p>Memuat data…</p>
  </div>
  <div id="toast" class="toast"></div>

  <!-- FLOATING NAVBAR -->
  <header class="floating-navbar">
    <div class="nav-brand">
      <div class="logo-circle">🏫</div>
      <span class="logo-text">ZonasiJabar</span>
    </div>
    <nav class="nav-center">
      <a href="#" class="nav-link" data-page="home">Home</a>
      <a href="#" class="nav-link" data-page="map">Peta Sekolah</a>
      <a href="#" class="nav-link" data-page="zonasi">Cek Zonasi</a>
    </nav>
    <div class="nav-right">
      <input type="search" id="global-search" class="global-search" placeholder="Cari sekolah..." />
      <button class="search-icon-btn">🔍</button>
      <span class="hamburger">☰</span>
      <button class="user-btn" data-page="profile" title="Profil">
        <svg width="20" height="20" viewBox="0 0 26 26" fill="none"><circle cx="13" cy="9" r="5" stroke="currentColor" stroke-width="2"/><path d="M3 23c0-5.523 4.477-10 10-10s10 4.477 10 10" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
      </button>
    </div>
  </header>

  <!-- APP CONTAINER -->
  <main class="app-container">

    <!-- ── HOME PAGE ── -->
    <section id="page-home" class="page active">
      <div class="hero-section">
        <div class="hero-content">
          <h1>Pendidikan Terbaik<br>Dalam Genggaman Anda</h1>
          <p>Eksplorasi peta sekolah dan cek radius zonasi penerimaan siswa baru (PPDB) di seluruh area Jawa Barat dengan mudah dan transparan.</p>
          <div class="hero-actions">
            <button class="btn btn-primary" data-page="map">Eksplorasi Peta</button>
            <button class="btn btn-secondary" data-page="zonasi">Cek Zonasi Saya</button>
          </div>
        </div>
      </div>

      <div class="bento-grid">
        <!-- Berita / Informasi Card -->
        <div class="bento-card bento-berita">
          <h2>Informasi Terkini</h2>
          <div class="carousel-wrap">
            <button class="carousel-btn" id="berita-prev">&#171;</button>
            <div class="carousel-slide">
              <div class="berita-placeholder"><div class="berita-img"></div></div>
            </div>
            <button class="carousel-btn" id="berita-next">&#187;</button>
          </div>
        </div>

        <!-- Tabel Top Sekolah -->
        <div class="bento-card bento-tabel">
          <div class="table-header-modern">
            <h2>Sekolah Populer</h2>
            <div class="pagination-mini">
              <button id="home-prev" class="btn-mini">←</button>
              <span id="home-page-info">1/1</span>
              <button id="home-next" class="btn-mini">→</button>
            </div>
          </div>
          <div class="table-wrap">
            <table class="modern-table">
              <thead><tr><th>NO</th><th>Nama Sekolah</th><th>Akreditasi</th><th>Pendaftar</th><th>Alamat</th></tr></thead>
              <tbody id="home-tbody"><tr><td colspan="5" style="text-align:center">Memuat…</td></tr></tbody>
            </table>
          </div>
        </div>
      </div>
    </section>

    <!-- ── MAP PAGE (SPLIT SCREEN) ── -->
    <section id="page-map" class="page">
      <div class="split-layout">
        <!-- Left Panel -->
        <div class="split-left">
          <div class="panel-header">
            <h2>Peta Sekolah</h2>
            <p>Gunakan filter untuk mempersempit pencarian Anda.</p>
          </div>
          
          <div class="filter-card" id="map-filter-box">
            <div class="filter-grid">
              <div class="fg-item">
                <label>Kategori</label>
                <select class="modern-input" id="map-kat">
                  <option value="">Semua</option><option value="SD">SD</option><option value="SMP">SMP</option><option value="SMA">SMA</option><option value="SMK">SMK</option>
                </select>
              </div>
              <div class="fg-item">
                <label>Akreditasi</label>
                <select id="filter-akreditasi" class="modern-input">
                  <option value="">Semua</option><option value="A">A</option><option value="B">B</option><option value="C">C</option>
                </select>
              </div>
              <div class="fg-item">
                <label>Biaya</label>
                <select class="modern-input" id="map-biaya">
                  <option value="">Semua</option><option value="gratis">Gratis</option><option value="murah">Murah</option>
                </select>
              </div>
              <div class="fg-item">
                <label>Maks Biaya</label>
                <input type="number" id="filter-biaya" class="modern-input" placeholder="Rp...">
              </div>
            </div>
            <div class="filter-actions">
              <button class="btn btn-outline" id="map-clear">Reset</button>
              <button class="btn btn-primary" id="map-apply">Terapkan</button>
            </div>
          </div>

          <div class="list-section">
            <h3>Daftar Sekolah</h3>
            <ul class="school-list" id="map-list"></ul>
            <div class="list-pagination">
              <button class="btn-mini" id="map-prev">← Prev</button>
              <span id="map-page-info">1 of 1</span>
              <button class="btn-mini" id="map-next">Next →</button>
            </div>
          </div>
        </div>
        
        <!-- Right Panel (Map) -->
        <div class="split-right">
          <div id="map-view" class="leaflet-map-container"></div>
        </div>
      </div>
    </section>

    <!-- ── ZONASI PAGE (SPLIT SCREEN) ── -->
    <section id="page-zonasi" class="page">
      
      <!-- STEP 1: Input Lokasi (Floating Card over abstract bg) -->
      <div id="zonasi-input-step" class="zonasi-input-step">
        <div class="glass-card zonasi-form-card">
          <div class="form-header">
            <div class="icon-circle">📍</div>
            <h2>Cek Jarak Zonasi</h2>
            <p>Tentukan titik awal Anda untuk mencari sekolah dalam radius tertentu.</p>
          </div>

          <div class="loc-tabs">
            <button class="loc-tab active" data-tab="gps">GPS</button>
            <button class="loc-tab" data-tab="koordinat">Koordinat</button>
            <button class="loc-tab" data-tab="kota">Kota/Kab</button>
          </div>

          <!-- GPS -->
          <div class="loc-tab-panel active" id="tab-gps">
            <div class="gps-box">
              <p>Otomatis deteksi lokasi Anda saat ini.</p>
              <button class="btn btn-primary btn-full" id="btn-geoloc">Deteksi Lokasi</button>
              <div id="gps-status" class="status-text"></div>
            </div>
          </div>

          <!-- Koordinat -->
          <div class="loc-tab-panel" id="tab-koordinat">
            <div class="input-row">
              <div><label>Latitude</label><input type="number" id="input-lat" class="modern-input" placeholder="-6.9..."></div>
              <div><label>Longitude</label><input type="number" id="input-lng" class="modern-input" placeholder="107.6..."></div>
            </div>
            <button class="btn btn-primary btn-full mt-3" id="btn-submit-koordinat">Gunakan Koordinat</button>
          </div>

          <!-- Kota -->
          <div class="loc-tab-panel" id="tab-kota">
            <label>Cari Kota/Kabupaten</label>
            <div style="position:relative">
              <input type="search" id="input-kota-search" class="modern-input" placeholder="Ketik nama..."/>
              <div id="kota-dropdown" class="dropdown-list"></div>
            </div>
            <div id="kota-selected-info" class="status-text mt-2"></div>
            <button class="btn btn-primary btn-full mt-3" id="btn-submit-kota" disabled>Pilih Kota</button>
          </div>

          <!-- Radius -->
          <div class="radius-control mt-4">
            <label>Radius (km)</label>
            <div class="radius-slider">
              <input type="number" id="radius-num" value="5" class="modern-input short-input">
              <input type="range" id="radius-range" value="5" min="0.1" max="20" step="0.1" class="slider-input">
            </div>
          </div>
        </div>
      </div>

      <!-- STEP 2: Result Split Screen -->
      <div id="zonasi-result-step" class="zonasi-result-step hidden split-layout">
        <!-- Left Panel -->
        <div class="split-left">
          <div class="active-location-card">
            <div class="loc-info">
              <span class="icon">📌</span>
              <div>
                <div class="loc-label">Titik Lokasi Aktif</div>
                <div class="loc-val" id="zonasi-active-loc">Memuat...</div>
              </div>
            </div>
            <div class="loc-actions">
              <span class="badge badge-radius" id="zonasi-radius-badge">5 km</span>
              <button class="btn btn-outline btn-sm" id="btn-change-loc">Ubah</button>
            </div>
          </div>

          <div class="filter-card mt-3" id="zonasi-filter-box">
            <div class="filter-flex">
              <div style="flex:1">
                <label>Kategori Sekolah</label>
                <select class="modern-input" id="zon-kat">
                  <option value="">Semua</option><option value="SD">SD</option><option value="SMP">SMP</option><option value="SMA">SMA</option><option value="SMK">SMK</option>
                </select>
              </div>
              <div class="filter-actions-inline">
                <button class="btn btn-outline btn-sm" id="zon-clear">Reset</button>
                <button class="btn btn-primary btn-sm" id="zon-apply">Filter</button>
              </div>
            </div>
          </div>

          <div class="list-section mt-3">
            <div class="list-header-flex">
              <h3>Hasil Zonasi</h3>
              <div class="legend-dots">
                <span class="dot g"></span> Dalam <span class="dot y"></span> Dekat <span class="dot r"></span> Luar
              </div>
            </div>
            <ul class="school-list" id="zon-list"></ul>
            <div class="list-pagination">
              <button class="btn-mini" id="zon-prev">←</button>
              <span id="zon-page-info">1 of 1</span>
              <button class="btn-mini" id="zon-next">→</button>
            </div>
          </div>
        </div>

        <!-- Right Panel (Map) -->
        <div class="split-right">
          <div id="zonasi-view" class="leaflet-map-container"></div>
        </div>
      </div>
    </section>

    <!-- ── AUTH PAGES (SPLIT SCREEN) ── -->
    <section id="page-login" class="page auth-page">
      <div class="auth-split">
        <div class="auth-graphics">
          <h2>Selamat Datang Kembali</h2>
          <p>Masuk untuk mengakses dashboard pengelolaan PPDB dan fitur eksklusif lainnya.</p>
        </div>
        <div class="auth-form-side">
          <div class="auth-box">
            <h2>Login</h2>
            <form id="login-form">
              <div class="form-group">
                <label>Email</label>
                <input type="email" id="login-email" class="modern-input" required />
              </div>
              <div class="form-group">
                <label>Password</label>
                <div class="pass-wrapper">
                  <input type="password" id="login-pass" class="modern-input" required />
                  <button type="button" class="eye-btn" data-target="login-pass">👁</button>
                </div>
              </div>
              <button type="submit" class="btn btn-primary btn-full mt-4">Login</button>
              <div class="auth-links">
                Belum punya akun? <a href="#" data-page="register" class="auth-link">Daftar</a>
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>

    <section id="page-register" class="page auth-page">
      <div class="auth-split">
        <div class="auth-graphics auth-graphics-alt">
          <h2>Bergabung Bersama Kami</h2>
          <p>Daftarkan akun Anda sebagai Pengguna Umum, Sekolah, atau Admin Dinas.</p>
        </div>
        <div class="auth-form-side">
          <div class="auth-box">
            <h2>Register</h2>
            <form id="register-form">
              <div class="form-group">
                <label>Username</label>
                <input type="text" id="reg-user" class="modern-input" required />
              </div>
              <div class="form-group">
                <label>Email</label>
                <input type="email" id="reg-email" class="modern-input" required />
              </div>
              <div class="form-group">
                <label>Password</label>
                <div class="pass-wrapper">
                  <input type="password" id="reg-pass" class="modern-input" required />
                  <button type="button" class="eye-btn" data-target="reg-pass">👁</button>
                </div>
              </div>
              <div class="form-group">
                <label>Daftar Sebagai:</label>
                <select id="reg-role" class="modern-input" required>
                  <option value="user">Pengguna Umum</option>
                  <option value="sekolah">Operator Sekolah</option>
                  <option value="admin">Admin Dinas</option>
                </select>
              </div>
              <div id="extra-admin" class="form-group hidden mt-2">
                <label>Kode Admin</label>
                <input type="text" id="reg-admin-code" class="modern-input" placeholder="Kode khusus..." />
              </div>
              <div id="extra-operator" class="form-group hidden mt-2">
                <label>Kode Operator</label>
                <input type="text" id="reg-op-code" class="modern-input" placeholder="Kode khusus..." />
                <label class="mt-2 block">NPSN</label>
                <input type="text" id="reg-school-id" class="modern-input" placeholder="ID Sekolah..." />
              </div>
              <button type="submit" class="btn btn-primary btn-full mt-4">Register</button>
              <div class="auth-links">
                Sudah punya akun? <a href="#" data-page="login" class="auth-link">Login</a>
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>

    <!-- ── PROFILE ── -->
    <section id="page-profile" class="page profile-page">
      <div class="profile-card">
        <div class="profile-avatar">👤</div>
        <div class="profile-details">
          <div class="p-row"><span class="p-lbl">Username</span> <span class="p-val">User 1</span></div>
          <div class="p-row"><span class="p-lbl">Email</span> <span class="p-val">user@mail.com</span></div>
          <div class="p-row pass-row">
            <span class="p-lbl">Password</span> 
            <div><span class="p-val" id="prof-pass">••••••••</span> <button id="btn-lihat-pass" class="btn-text">Lihat</button></div>
          </div>
        </div>
        <button class="btn btn-danger btn-full mt-4 keluar-link" data-page="login">Keluar Akun</button>
      </div>
    </section>

    <!-- ── DASHBOARDS (Preserved Logic structure, modern layout hooks) ── -->
    <section id="page-admin" class="page dash-page">
      <aside class="dash-sidebar">
        <div class="dash-brand">ZonasiJabar Admin</div>
        <div class="dash-user">
          <div class="dash-avatar">A</div>
          <div><div id="admin-user-name">Admin</div><div>Dinas</div></div>
        </div>
        <nav class="dash-nav">
          <button class="dash-nav-btn active" data-panel="sekolah">Data Sekolah</button>
          <button class="dash-nav-btn" data-panel="zonasi-data">Data Zonasi</button>
          <button class="dash-nav-btn" data-panel="pengguna">Pengguna</button>
        </nav>
        <div class="dash-footer">
          <button id="admin-back-home" class="btn-text">← Ke Home</button>
          <button id="admin-logout-btn" class="btn-text text-danger">Keluar</button>
        </div>
      </aside>
      <div class="dash-content">
        <!-- Admin Panels -->
        <div class="dash-panel active" id="admin-panel-sekolah">
          <div class="dash-top">
            <h2>Data Sekolah</h2>
            <div class="dash-actions">
              <input type="search" id="admin-search-sekolah" class="modern-input" placeholder="Cari..."/>
              <select id="admin-filter-kat" class="modern-input"><option value="">Semua</option><option value="SD">SD</option><option value="SMP">SMP</option><option value="SMA">SMA</option><option value="SMK">SMK</option></select>
              <select id="admin-filter-status" class="modern-input"><option value="">Semua</option><option value="N">Negeri</option><option value="S">Swasta</option></select>
              <button id="admin-btn-tambah" class="btn btn-primary">+ Tambah</button>
            </div>
          </div>
          <div class="table-wrap mt-3"><table class="modern-table" id="admin-tbl-sekolah">
            <thead><tr><th>No</th><th>Nama</th><th>Jenjang</th><th>Status</th><th>Akreditasi</th><th>Kecamatan</th><th>Kuota</th><th>Pendaftar</th><th>Sisa</th><th>Biaya</th><th>Aksi</th></tr></thead>
            <tbody id="admin-tbody-sekolah"><tr><td colspan="11">Memuat...</td></tr></tbody>
          </table></div>
          <div class="list-pagination mt-2"><button id="admin-prev" class="btn-mini">←</button><span id="admin-page-info">1</span><button id="admin-next" class="btn-mini">→</button></div>
        </div>
        <div class="dash-panel" id="admin-panel-zonasi-data">
          <div class="dash-top"><h2>Data Zonasi</h2><button id="admin-btn-tambah-zonasi" class="btn btn-primary">+ Tambah</button></div>
          <div class="table-wrap mt-3"><table class="modern-table">
            <thead><tr><th>No</th><th>Nama</th><th>Jenjang</th><th>Radius</th><th>Wilayah</th><th>Aksi</th></tr></thead>
            <tbody id="admin-tbody-zonasi"></tbody>
          </table></div>
        </div>
        <div class="dash-panel" id="admin-panel-pengguna">
          <div class="dash-top"><h2>Pengguna</h2></div>
          <div class="table-wrap mt-3"><table class="modern-table">
            <thead><tr><th>No</th><th>User</th><th>Email</th><th>Role</th><th>Status</th><th>Aksi</th></tr></thead>
            <tbody id="admin-tbody-pengguna"></tbody>
          </table></div>
        </div>
      </div>
    </section>

    <section id="page-operator" class="page dash-page">
      <aside class="dash-sidebar">
        <div class="dash-brand">Portal Sekolah</div>
        <div class="dash-user">
          <div class="dash-avatar">O</div>
          <div><div id="op-user-name">Operator</div><div id="op-school-label">Instansi</div></div>
        </div>
        <nav class="dash-nav">
          <button class="dash-nav-btn active" data-op-panel="profil">Profil Sekolah</button>
          <button class="dash-nav-btn" data-op-panel="kuota">Kuota & Pendaftar</button>
          <button class="dash-nav-btn" data-op-panel="biaya">Data Biaya</button>
          <button class="dash-nav-btn" data-op-panel="fasilitas">Fasilitas</button>
        </nav>
        <div class="dash-footer">
          <button id="op-back-home" class="btn-text">← Ke Home</button>
          <button id="op-logout-btn" class="btn-text text-danger">Keluar</button>
        </div>
      </aside>
      <div class="dash-content">
        <!-- Op Panels -->
        <div class="dash-panel active" id="op-panel-profil">
          <div class="dash-top"><h2>Profil</h2><button id="op-btn-edit-profil" class="btn btn-outline">Edit</button></div>
          <div class="glass-card mt-3 p-4">
             <h3 id="op-school-name">Nama Sekolah</h3>
             <div><span id="op-school-jenjang" class="badge">SD</span> <span id="op-school-status" class="badge">N</span> <span id="op-school-akred" class="badge">A</span></div>
             <p>Kec: <span id="op-school-kec">-</span> | Kab: <span id="op-school-kab">-</span></p>
             <p>Alamat: <span id="op-school-alamat">-</span></p>
             <div class="stats-grid mt-3">
               <div class="stat">Kuota: <span id="op-stat-kuota">-</span></div>
               <div class="stat">Pendaftar: <span id="op-stat-pendaftar">-</span></div>
               <div class="stat">Sisa: <span id="op-stat-sisa">-</span></div>
               <div class="stat" id="op-stat-persen-card">% Terisi: <span id="op-stat-persen">-</span></div>
             </div>
             <div class="progress-bar mt-2"><div id="op-progress-fill" style="width:0; background:var(--primary); height:8px; border-radius:4px;"></div><span id="op-progress-label">0%</span></div>
          </div>
        </div>
        <div class="dash-panel" id="op-panel-kuota">
          <div class="dash-top"><h2>Kuota</h2><button id="op-btn-tambah-rombel" class="btn btn-primary">+ Tambah</button></div>
          <div class="table-wrap mt-3"><table class="modern-table">
             <thead><tr><th>No</th><th>Rombel</th><th>Kuota</th><th>Pendaftar</th><th>Sisa</th><th>Aksi</th></tr></thead>
             <tbody id="op-tbody-kuota"></tbody>
          </table></div>
          <span id="op-kuota-summary"></span>
        </div>
        <div class="dash-panel" id="op-panel-biaya">
          <div class="dash-top"><h2>Biaya</h2><button id="op-btn-edit-biaya" class="btn btn-outline">Edit</button></div>
          <div class="glass-card mt-3 p-4">
             <p>Gedung: <span id="ob-gedung">-</span></p>
             <p>Seragam: <span id="ob-seragam">-</span></p>
             <p>Buku: <span id="ob-buku">-</span></p>
             <p>Total Masuk: <span id="ob-total-masuk">-</span></p>
             <hr>
             <p>SPP: <span id="ob-spp">-</span></p>
             <p>Komite: <span id="ob-komite">-</span></p>
             <p>Total Rutin: <span id="ob-total-rutin">-</span></p>
             <p class="mt-2">Catatan: <span id="ob-catatan">-</span></p>
          </div>
        </div>
        <div class="dash-panel" id="op-panel-fasilitas">
           <div class="dash-top"><h2>Fasilitas</h2><button id="op-btn-tambah-fasilitas" class="btn btn-primary">+ Tambah</button></div>
           <div class="table-wrap mt-3"><table class="modern-table">
             <thead><tr><th>No</th><th>Nama</th><th>Jumlah</th><th>Kondisi</th><th>Aksi</th></tr></thead>
             <tbody id="op-tbody-fasilitas"></tbody>
           </table></div>
        </div>
      </div>
    </section>

  </main>

  <!-- MODAL BAREBONE FOR LOGIC -->
  <div class="modal-overlay hidden" id="modal-sekolah">
    <div class="modal-content glass-card">
       <h3 id="modal-sekolah-title">Form</h3><button id="modal-sekolah-close">X</button>
       <input type="text" id="mf-npsn"><input type="text" id="mf-nama"><select id="mf-jenjang"></select><select id="mf-status"></select>
       <select id="mf-akreditasi"></select><input type="text" id="mf-kecamatan"><input type="text" id="mf-kabupaten">
       <input type="text" id="mf-alamat"><input type="text" id="mf-lat"><input type="text" id="mf-lng"><input type="number" id="mf-kuota">
       <button id="mf-submit">Submit</button>
    </div>
  </div>

  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <script src="assets/js/api.js"></script>
  <script src="assets/js/ui.js"></script>
  <script src="assets/js/main.js"></script>
</body>
</html>
"""

with open("c:/Users/MSI/Documents/Code/ppdb Sekolah/7 - editan/frontend/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("index.html generated.")

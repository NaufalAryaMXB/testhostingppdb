#!/usr/bin/env python3
"""Build new index.html - Part 2: Auth + Profile + Dashboards + Modals"""

AUTH = '''
<!-- LOGIN -->
<section id="page-login" class="page auth-page">
  <div class="auth-wrap">
    <div class="auth-visual">
      <div class="av-orbs"><div class="orb orb1"></div><div class="orb orb2"></div><div class="orb orb3"></div></div>
      <h2>Selamat Datang<br>Kembali</h2>
      <p>Masuk untuk mengakses dashboard PPDB dan fitur eksklusif.</p>
    </div>
    <div class="auth-form-area">
      <div class="auth-box">
        <h2>Login</h2>
        <form id="login-form">
          <div class="fg"><label>Email</label><input type="email" id="login-email" class="fi" required/></div>
          <div class="fg"><label>Password</label><div class="pass-wrap"><input type="password" id="login-pass" class="fi" required/><button type="button" class="eye-btn" data-target="login-pass">👁</button></div></div>
          <button type="submit" class="btn-glow full-w mt16">Masuk</button>
          <div class="auth-alt mt16">Belum punya akun? <a href="#" data-page="register" class="auth-link">Daftar</a></div>
        </form>
      </div>
    </div>
  </div>
</section>

<!-- REGISTER -->
<section id="page-register" class="page auth-page">
  <div class="auth-wrap">
    <div class="auth-visual av-alt">
      <div class="av-orbs"><div class="orb orb1"></div><div class="orb orb2"></div><div class="orb orb3"></div></div>
      <h2>Bergabung<br>Bersama Kami</h2>
      <p>Daftarkan akun sebagai Pengguna, Operator Sekolah, atau Admin Dinas.</p>
    </div>
    <div class="auth-form-area">
      <div class="auth-box">
        <h2>Register</h2>
        <form id="register-form">
          <div class="fg"><label>Username</label><input type="text" id="reg-user" class="fi" required/></div>
          <div class="fg"><label>Email</label><input type="email" id="reg-email" class="fi" required/></div>
          <div class="fg"><label>Password</label><div class="pass-wrap"><input type="password" id="reg-pass" class="fi" required/><button type="button" class="eye-btn" data-target="reg-pass">👁</button></div></div>
          <div class="fg"><label>Daftar Sebagai:</label><select id="reg-role" class="fi" required><option value="user">Pengguna Umum</option><option value="sekolah">Operator Sekolah</option><option value="admin">Admin Dinas</option></select></div>
          <div id="extra-admin" class="fg hidden"><label>Kode Admin</label><input type="text" id="reg-admin-code" class="fi" placeholder="Kode khusus..."/></div>
          <div id="extra-operator" class="fg hidden"><label>Kode Operator</label><input type="text" id="reg-op-code" class="fi" placeholder="Kode khusus..."/><label class="mt8">NPSN</label><input type="text" id="reg-school-id" class="fi" placeholder="ID Sekolah..."/></div>
          <button type="submit" class="btn-glow full-w mt16">Register</button>
          <div class="auth-alt mt16">Sudah punya akun? <a href="#" data-page="login" class="auth-link">Login</a></div>
        </form>
      </div>
    </div>
  </div>
</section>

<!-- PROFILE -->
<section id="page-profile" class="page page-scroll profile-center">
  <div class="prof-card glass-card">
    <div class="prof-avatar">👤</div>
    <div class="prof-rows">
      <div class="pr"><span class="pr-l">Username</span><span class="pr-v">User</span></div>
      <div class="pr"><span class="pr-l">Email</span><span class="pr-v">user@mail.com</span></div>
      <div class="pr"><span class="pr-l">Password</span><div><span class="pr-v" id="prof-pass">••••••••</span> <button id="btn-lihat-pass" class="btn-link">Lihat</button></div></div>
    </div>
    <button class="btn-danger full-w mt16 keluar-link" data-page="login">Keluar Akun</button>
  </div>
</section>
'''

ADMIN = '''
<!-- ADMIN -->
<section id="page-admin" class="page dash-page">
  <aside class="dash-side">
    <div class="ds-brand">⚡ Admin</div>
    <div class="ds-user"><div class="ds-av">A</div><div><div id="admin-user-name">Admin</div><div class="ds-role">Dinas</div></div></div>
    <nav class="ds-nav">
      <button class="dash-nav-btn active" data-panel="sekolah">📋 Data Sekolah</button>
      <button class="dash-nav-btn" data-panel="zonasi-data">🎯 Data Zonasi</button>
      <button class="dash-nav-btn" data-panel="pengguna">👥 Pengguna</button>
    </nav>
    <div class="ds-foot"><button id="admin-back-home" class="btn-link">← Home</button><button id="admin-logout-btn" class="btn-link btn-link-red">Keluar</button></div>
  </aside>
  <div class="dash-main">
    <div class="dash-panel active" id="admin-panel-sekolah">
      <div class="dp-top"><h2>Data Sekolah</h2>
        <div class="dp-acts"><input type="search" id="admin-search-sekolah" class="fi fi-sm" placeholder="Cari..."/>
        <select id="admin-filter-kat" class="fi fi-sm"><option value="">Semua</option><option value="SD">SD</option><option value="SMP">SMP</option><option value="SMA">SMA</option><option value="SMK">SMK</option></select>
        <select id="admin-filter-status" class="fi fi-sm"><option value="">Semua</option><option value="N">Negeri</option><option value="S">Swasta</option></select>
        <button id="admin-btn-tambah" class="btn-sm-fill">+ Tambah</button></div>
      </div>
      <div class="dp-table"><table class="dtable" id="admin-tbl-sekolah"><thead><tr><th>No</th><th>Nama</th><th>Jenjang</th><th>Status</th><th>Akreditasi</th><th>Kecamatan</th><th>Kuota</th><th>Pendaftar</th><th>Sisa</th><th>Biaya</th><th>Aksi</th></tr></thead><tbody id="admin-tbody-sekolah"><tr><td colspan="11">Memuat...</td></tr></tbody></table></div>
      <div class="dp-pg"><button id="admin-prev" class="pg-btn">‹</button><span id="admin-page-info">1</span><button id="admin-next" class="pg-btn">›</button></div>
    </div>
    <div class="dash-panel" id="admin-panel-zonasi-data">
      <div class="dp-top"><h2>Data Zonasi</h2><button id="admin-btn-tambah-zonasi" class="btn-sm-fill">+ Tambah</button></div>
      <div class="dp-table"><table class="dtable"><thead><tr><th>No</th><th>Nama</th><th>Jenjang</th><th>Radius</th><th>Wilayah</th><th>Aksi</th></tr></thead><tbody id="admin-tbody-zonasi"></tbody></table></div>
    </div>
    <div class="dash-panel" id="admin-panel-pengguna">
      <div class="dp-top"><h2>Pengguna</h2></div>
      <div class="dp-table"><table class="dtable"><thead><tr><th>No</th><th>User</th><th>Email</th><th>Role</th><th>Status</th><th>Aksi</th></tr></thead><tbody id="admin-tbody-pengguna"></tbody></table></div>
    </div>
  </div>
</section>
'''

OPERATOR = '''
<!-- OPERATOR -->
<section id="page-operator" class="page dash-page">
  <aside class="dash-side">
    <div class="ds-brand">🏫 Portal</div>
    <div class="ds-user"><div class="ds-av">O</div><div><div id="op-user-name">Operator</div><div class="ds-role" id="op-school-label">Instansi</div></div></div>
    <nav class="ds-nav">
      <button class="dash-nav-btn active" data-op-panel="profil">📋 Profil</button>
      <button class="dash-nav-btn" data-op-panel="kuota">📊 Kuota</button>
      <button class="dash-nav-btn" data-op-panel="biaya">💰 Biaya</button>
      <button class="dash-nav-btn" data-op-panel="fasilitas">🏗️ Fasilitas</button>
    </nav>
    <div class="ds-foot"><button id="op-back-home" class="btn-link">← Home</button><button id="op-logout-btn" class="btn-link btn-link-red">Keluar</button></div>
  </aside>
  <div class="dash-main">
    <div class="dash-panel active" id="op-panel-profil">
      <div class="dp-top"><h2>Profil Sekolah</h2><button id="op-btn-edit-profil" class="btn-sm-outline">Edit</button></div>
      <div class="op-profil-card glass-card">
        <h3 id="op-school-name">Nama Sekolah</h3>
        <div class="op-badges"><span id="op-school-jenjang" class="badge">SD</span><span id="op-school-status" class="badge">N</span><span id="op-school-akred" class="badge">A</span></div>
        <p>Kec: <span id="op-school-kec">-</span> | Kab: <span id="op-school-kab">-</span></p>
        <p>Alamat: <span id="op-school-alamat">-</span></p>
        <div class="op-stats"><div class="os">Kuota<br><b id="op-stat-kuota">-</b></div><div class="os">Pendaftar<br><b id="op-stat-pendaftar">-</b></div><div class="os">Sisa<br><b id="op-stat-sisa">-</b></div><div class="os" id="op-stat-persen-card">Terisi<br><b id="op-stat-persen">-</b></div></div>
        <div class="op-bar"><div id="op-progress-fill" class="op-bar-fill"></div><span id="op-progress-label">0%</span></div>
      </div>
    </div>
    <div class="dash-panel" id="op-panel-kuota">
      <div class="dp-top"><h2>Kuota & Rombel</h2><button id="op-btn-tambah-rombel" class="btn-sm-fill">+ Tambah</button></div>
      <div class="dp-table"><table class="dtable"><thead><tr><th>No</th><th>Rombel</th><th>Kuota</th><th>Pendaftar</th><th>Sisa</th><th>Status</th><th>Aksi</th></tr></thead><tbody id="op-tbody-kuota"></tbody></table></div>
      <span id="op-kuota-summary" class="summary-text"></span>
    </div>
    <div class="dash-panel" id="op-panel-biaya">
      <div class="dp-top"><h2>Data Biaya</h2><button id="op-btn-edit-biaya" class="btn-sm-outline">Edit</button></div>
      <div class="op-biaya glass-card"><p>Gedung: <b id="ob-gedung">-</b></p><p>Seragam: <b id="ob-seragam">-</b></p><p>Buku: <b id="ob-buku">-</b></p><p>Total Masuk: <b id="ob-total-masuk">-</b></p><hr><p>SPP: <b id="ob-spp">-</b></p><p>Komite: <b id="ob-komite">-</b></p><p>Total Rutin: <b id="ob-total-rutin">-</b></p><p class="mt8">Catatan: <span id="ob-catatan">-</span></p></div>
    </div>
    <div class="dash-panel" id="op-panel-fasilitas">
      <div class="dp-top"><h2>Fasilitas</h2><button id="op-btn-tambah-fasilitas" class="btn-sm-fill">+ Tambah</button></div>
      <div class="dp-table"><table class="dtable"><thead><tr><th>No</th><th>Nama</th><th>Jumlah</th><th>Kondisi</th><th>Ket</th><th>Aksi</th></tr></thead><tbody id="op-tbody-fasilitas"></tbody></table></div>
    </div>
  </div>
</section>
'''

MODALS = '''
</main>

<!-- MODALS -->
<div class="modal-overlay hidden" id="modal-sekolah"><div class="modal-box glass-card">
  <div class="mb-head"><h3 id="modal-sekolah-title">Form Sekolah</h3><button id="modal-sekolah-close" class="mb-x">✕</button></div>
  <div class="mb-body">
    <div class="fg"><label>NPSN</label><input type="text" id="mf-npsn" class="fi"></div>
    <div class="fg"><label>Nama</label><input type="text" id="mf-nama" class="fi"></div>
    <div class="row2"><div class="fg"><label>Jenjang</label><select id="mf-jenjang" class="fi"><option value="">-</option><option>SD</option><option>SMP</option><option>SMA</option><option>SMK</option></select></div>
    <div class="fg"><label>Status</label><select id="mf-status" class="fi"><option value="N">Negeri</option><option value="S">Swasta</option></select></div></div>
    <div class="row2"><div class="fg"><label>Akreditasi</label><select id="mf-akreditasi" class="fi"><option value="-">-</option><option>A</option><option>B</option><option>C</option></select></div>
    <div class="fg"><label>Kecamatan</label><input type="text" id="mf-kecamatan" class="fi"></div></div>
    <div class="fg"><label>Kab/Kota</label><input type="text" id="mf-kabkota" class="fi"></div>
    <div class="fg"><label>Alamat</label><input type="text" id="mf-alamat" class="fi"></div>
    <div class="row2"><div class="fg"><label>Lat</label><input type="text" id="mf-lat" class="fi"></div><div class="fg"><label>Lng</label><input type="text" id="mf-lng" class="fi"></div></div>
    <div class="row2"><div class="fg"><label>Kuota</label><input type="number" id="mf-kuota" class="fi"></div><div class="fg"><label>Pendaftar</label><input type="number" id="mf-pendaftar" class="fi"></div></div>
    <div class="row2"><div class="fg"><label>Biaya</label><input type="number" id="mf-biaya" class="fi"></div><div class="fg"><label>SPP</label><input type="number" id="mf-spp" class="fi"></div></div>
  </div>
  <div class="mb-foot"><button id="modal-sekolah-batal" class="btn-sm-outline">Batal</button><button id="modal-sekolah-simpan" class="btn-sm-fill">Simpan</button></div>
</div></div>

<div class="modal-overlay hidden" id="modal-hapus"><div class="modal-box glass-card modal-sm">
  <div class="mb-head"><h3>Konfirmasi Hapus</h3><button id="modal-hapus-close" class="mb-x">✕</button></div>
  <div class="mb-body"><p>Hapus data <b id="hapus-nama-target"></b>?</p></div>
  <div class="mb-foot"><button id="modal-hapus-batal" class="btn-sm-outline">Batal</button><button id="modal-hapus-ok" class="btn-sm-danger">Hapus</button></div>
</div></div>

<div class="modal-overlay hidden" id="modal-rombel"><div class="modal-box glass-card modal-sm">
  <div class="mb-head"><h3 id="modal-rombel-title">Rombel</h3><button id="modal-rombel-close" class="mb-x">✕</button></div>
  <div class="mb-body">
    <div class="fg"><label>Kelas</label><input type="text" id="mr-kelas" class="fi"></div>
    <div class="row2"><div class="fg"><label>Kuota</label><input type="number" id="mr-kuota" class="fi"></div><div class="fg"><label>Pendaftar</label><input type="number" id="mr-pendaftar" class="fi"></div></div>
  </div>
  <div class="mb-foot"><button id="modal-rombel-batal" class="btn-sm-outline">Batal</button><button id="modal-rombel-simpan" class="btn-sm-fill">Simpan</button></div>
</div></div>

<div class="modal-overlay hidden" id="modal-biaya"><div class="modal-box glass-card modal-sm">
  <div class="mb-head"><h3>Edit Biaya</h3><button id="modal-biaya-close" class="mb-x">✕</button></div>
  <div class="mb-body">
    <div class="row2"><div class="fg"><label>Gedung</label><input type="number" id="mb-gedung" class="fi"></div><div class="fg"><label>Seragam</label><input type="number" id="mb-seragam" class="fi"></div></div>
    <div class="row2"><div class="fg"><label>Buku</label><input type="number" id="mb-buku" class="fi"></div><div class="fg"><label>SPP</label><input type="number" id="mb-spp" class="fi"></div></div>
    <div class="fg"><label>Komite</label><input type="number" id="mb-komite" class="fi"></div>
    <div class="fg"><label>Catatan</label><input type="text" id="mb-catatan" class="fi"></div>
  </div>
  <div class="mb-foot"><button id="modal-biaya-batal" class="btn-sm-outline">Batal</button><button id="modal-biaya-simpan" class="btn-sm-fill">Simpan</button></div>
</div></div>

<div class="modal-overlay hidden" id="modal-fasilitas"><div class="modal-box glass-card modal-sm">
  <div class="mb-head"><h3 id="modal-fasilitas-title">Fasilitas</h3><button id="modal-fasilitas-close" class="mb-x">✕</button></div>
  <div class="mb-body">
    <div class="fg"><label>Nama</label><input type="text" id="mfas-nama" class="fi"></div>
    <div class="row2"><div class="fg"><label>Jumlah</label><input type="number" id="mfas-jumlah" class="fi" value="1"></div><div class="fg"><label>Kondisi</label><select id="mfas-kondisi" class="fi"><option>Baik</option><option>Cukup</option><option>Rusak</option></select></div></div>
    <div class="fg"><label>Keterangan</label><input type="text" id="mfas-ket" class="fi"></div>
  </div>
  <div class="mb-foot"><button id="modal-fasilitas-batal" class="btn-sm-outline">Batal</button><button id="modal-fasilitas-simpan" class="btn-sm-fill">Simpan</button></div>
</div></div>

<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script type="module" src="assets/js/main.js"></script>
</body>
</html>
'''

with open("_part2.html","w",encoding="utf-8") as f:
    f.write(AUTH + ADMIN + OPERATOR + MODALS)
print("Part 2 written")

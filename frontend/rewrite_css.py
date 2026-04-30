import os

css_content = """/*
 * style.css — Full Ground-Up Redesign
 * Sleek WebGIS Split-Screen Layout
 */

@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@400;500;600&display=swap');

:root {
  --primary: #4F46E5;
  --primary-hover: #4338CA;
  --secondary: #0EA5E9;
  --success: #10B981;
  --danger: #EF4444;
  --warning: #F59E0B;
  
  --bg-base: #F8FAFC;
  --text-main: #0F172A;
  --text-muted: #64748B;
  
  --glass-bg: rgba(255, 255, 255, 0.7);
  --glass-border: rgba(255, 255, 255, 0.5);
  --glass-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.07);
  
  --radius-lg: 24px;
  --radius-md: 16px;
  --radius-sm: 8px;
  
  --nav-height: 70px;
  --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* ── BASE ── */
* { box-sizing: border-box; margin: 0; padding: 0; }
body, html {
  height: 100%;
  font-family: 'Outfit', 'Inter', sans-serif;
  color: var(--text-main);
  background: var(--bg-base);
  overflow: hidden; /* App feel */
}

/* ── MESH BG ── */
.mesh-bg {
  position: absolute; top: 0; left: 0; width: 100vw; height: 100vh;
  background: radial-gradient(circle at 10% 20%, rgba(79, 70, 229, 0.1), transparent 40%),
              radial-gradient(circle at 90% 80%, rgba(14, 165, 233, 0.1), transparent 40%);
  filter: blur(40px); z-index: -1; animation: mesh 10s infinite alternate;
}
@keyframes mesh { to { transform: scale(1.05) translate(20px, -20px); } }

/* ── UTILITIES ── */
.hidden { display: none !important; }
.mt-2 { margin-top: 8px; } .mt-3 { margin-top: 16px; } .mt-4 { margin-top: 24px; }
.p-4 { padding: 24px; }
.glass-card {
  background: var(--glass-bg); backdrop-filter: blur(16px);
  border: 1px solid var(--glass-border); border-radius: var(--radius-lg);
  box-shadow: var(--glass-shadow);
}
.btn {
  display: inline-flex; align-items: center; justify-content: center;
  padding: 12px 24px; font-family: 'Outfit', sans-serif; font-weight: 600;
  border-radius: 100px; cursor: pointer; transition: var(--transition);
  border: none;
}
.btn-primary { background: var(--primary); color: white; box-shadow: 0 4px 12px rgba(79,70,229,0.3); }
.btn-primary:hover { background: var(--primary-hover); transform: translateY(-2px); box-shadow: 0 6px 16px rgba(79,70,229,0.4); }
.btn-secondary { background: white; color: var(--primary); box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
.btn-secondary:hover { transform: translateY(-2px); box-shadow: 0 6px 16px rgba(0,0,0,0.1); }
.btn-outline { background: transparent; border: 1.5px solid var(--primary); color: var(--primary); }
.btn-outline:hover { background: rgba(79,70,229,0.05); }
.btn-full { width: 100%; }
.btn-mini { padding: 4px 12px; border-radius: 6px; background: white; border: 1px solid #CBD5E1; cursor: pointer; font-weight: 600; }
.btn-sm { padding: 6px 16px; font-size: 13px; }
.btn-text { background: transparent; border: none; color: var(--text-muted); cursor: pointer; font-weight: 600; }
.btn-text:hover { color: var(--primary); }
.text-danger { color: var(--danger); }
.modern-input {
  width: 100%; padding: 12px 16px; border-radius: var(--radius-sm);
  border: 1px solid #CBD5E1; font-family: 'Inter', sans-serif;
  background: rgba(255,255,255,0.8); transition: var(--transition); outline: none;
}
.modern-input:focus { border-color: var(--primary); box-shadow: 0 0 0 3px rgba(79,70,229,0.15); background: white; }

/* ── FLOATING NAVBAR ── */
.floating-navbar {
  position: fixed; top: 20px; left: 50%; transform: translateX(-50%);
  width: 90%; max-width: 1200px; height: var(--nav-height);
  background: rgba(255,255,255,0.85); backdrop-filter: blur(20px);
  border: 1px solid rgba(255,255,255,0.6); border-radius: 100px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.08);
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 24px; z-index: 1000;
}
.nav-brand { display: flex; align-items: center; gap: 10px; font-weight: 800; font-size: 20px; }
.logo-circle { width: 36px; height: 36px; background: linear-gradient(135deg, var(--primary), var(--secondary)); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 18px; }
.logo-text { background: linear-gradient(135deg, var(--primary), var(--secondary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.nav-center { display: flex; gap: 32px; }
.nav-link { text-decoration: none; color: var(--text-muted); font-weight: 600; transition: var(--transition); }
.nav-link:hover, .nav-link.active { color: var(--primary); }
.nav-right { display: flex; align-items: center; gap: 12px; }
.global-search { width: 160px; padding: 8px 16px; border-radius: 100px; border: none; background: #F1F5F9; font-size: 13px; transition: 0.3s; }
.global-search:focus { width: 200px; background: white; box-shadow: 0 0 0 2px var(--primary); }
.search-icon-btn, .hamburger { background: none; border: none; cursor: pointer; color: var(--text-muted); font-size: 16px; }
.user-btn { background: var(--primary); color: white; border: none; width: 36px; height: 36px; border-radius: 50%; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: var(--transition); }
.user-btn:hover { transform: scale(1.1); box-shadow: 0 4px 12px rgba(79,70,229,0.4); }

/* ── APP CONTAINER & PAGES ── */
.app-container {
  height: 100vh; padding-top: calc(var(--nav-height) + 40px);
  width: 100%; max-width: 1600px; margin: 0 auto;
}
.page { display: none; height: 100%; flex-direction: column; opacity: 0; animation: fadeUp 0.4s forwards; }
.page.active { display: flex; }
@keyframes fadeUp { to { opacity: 1; transform: translateY(0); } from { opacity: 0; transform: translateY(10px); } }

/* ── HOME PAGE ── */
#page-home { overflow-y: auto; padding: 0 40px 40px; }
.hero-section { text-align: center; padding: 60px 0 80px; }
.hero-section h1 { font-size: clamp(32px, 5vw, 56px); font-weight: 800; line-height: 1.1; margin-bottom: 20px; letter-spacing: -1px; }
.hero-section p { font-size: 18px; color: var(--text-muted); max-width: 600px; margin: 0 auto 32px; line-height: 1.6; }
.hero-actions { display: flex; gap: 16px; justify-content: center; }

.bento-grid { display: grid; grid-template-columns: 1fr 2fr; gap: 24px; }
.bento-card { background: white; border-radius: var(--radius-lg); padding: 32px; box-shadow: 0 4px 20px rgba(0,0,0,0.03); border: 1px solid #E2E8F0; }
.bento-card h2 { font-size: 20px; font-weight: 700; margin-bottom: 20px; }
.carousel-wrap { display: flex; gap: 12px; height: 200px; }
.carousel-btn { width: 40px; height: 40px; border-radius: 50%; border: 1px solid #E2E8F0; background: white; cursor: pointer; transition: var(--transition); }
.carousel-btn:hover { background: var(--primary); color: white; border-color: var(--primary); }
.carousel-slide { flex: 1; background: #F1F5F9; border-radius: var(--radius-md); }
.modern-table { width: 100%; border-collapse: collapse; text-align: left; }
.modern-table th { font-size: 12px; text-transform: uppercase; color: var(--text-muted); padding: 12px; border-bottom: 2px solid #F1F5F9; }
.modern-table td { padding: 16px 12px; border-bottom: 1px solid #F1F5F9; font-size: 14px; font-weight: 500; }
.table-header-modern { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }

/* ── SPLIT SCREEN (MAP & ZONASI) ── */
.split-layout { display: flex; height: calc(100vh - var(--nav-height) - 60px); margin: 0 20px 20px; gap: 20px; }
.split-left { width: 400px; background: rgba(255,255,255,0.6); backdrop-filter: blur(20px); border: 1px solid var(--glass-border); border-radius: var(--radius-lg); display: flex; flex-direction: column; overflow: hidden; box-shadow: var(--glass-shadow); flex-shrink: 0; }
.split-right { flex: 1; border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--glass-shadow); position: relative; border: 1px solid var(--glass-border); }
.leaflet-map-container { width: 100%; height: 100%; z-index: 1; }

.panel-header { padding: 24px 24px 16px; border-bottom: 1px solid rgba(226, 232, 240, 0.5); }
.panel-header h2 { font-size: 24px; font-weight: 800; }
.panel-header p { font-size: 13px; color: var(--text-muted); }

.filter-card { padding: 16px 24px; border-bottom: 1px solid rgba(226, 232, 240, 0.5); background: rgba(248, 250, 252, 0.5); }
.filter-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
.fg-item label { display: block; font-size: 12px; font-weight: 600; color: var(--text-muted); margin-bottom: 4px; }
.modern-input { padding: 10px 12px; font-size: 13px; }
.filter-actions { display: flex; justify-content: flex-end; gap: 8px; margin-top: 16px; }

.list-section { flex: 1; display: flex; flex-direction: column; overflow: hidden; }
.list-section h3 { padding: 16px 24px 8px; font-size: 16px; font-weight: 700; }
.school-list { flex: 1; overflow-y: auto; list-style: none; padding: 0 16px; margin: 0; }
.flat-list-item { background: white; padding: 16px; border-radius: 12px; margin-bottom: 8px; border: 1px solid #E2E8F0; display: flex; gap: 12px; cursor: pointer; transition: var(--transition); }
.flat-list-item:hover { border-color: var(--primary); transform: translateX(4px); box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
.item-jenjang-dot { width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0; margin-top: 6px; }
.item-info { display: flex; flex-direction: column; gap: 4px; }
.item-name { font-weight: 600; font-size: 14px; }
.item-meta { font-size: 12px; color: var(--text-muted); }
.item-jenjang-badge { font-size: 10px; font-weight: 700; padding: 2px 6px; border-radius: 4px; background: #F1F5F9; display: inline-block; }
.item-dist { font-size: 13px; font-weight: 700; background: #EEF2FF; color: var(--primary); padding: 4px 8px; border-radius: 6px; align-self: flex-start; margin-left: auto; }
.list-pagination { padding: 16px 24px; border-top: 1px solid rgba(226, 232, 240, 0.5); display: flex; justify-content: space-between; align-items: center; }

/* ── ZONASI SPECIFIC ── */
.zonasi-input-step { height: calc(100vh - var(--nav-height) - 40px); display: flex; align-items: center; justify-content: center; }
.zonasi-form-card { width: 440px; padding: 40px; }
.form-header { text-align: center; margin-bottom: 32px; }
.icon-circle { font-size: 48px; margin-bottom: 16px; }
.loc-tabs { display: flex; background: #F1F5F9; border-radius: 12px; padding: 4px; margin-bottom: 24px; }
.loc-tab { flex: 1; padding: 10px; border: none; background: transparent; font-family: 'Outfit'; font-weight: 600; color: var(--text-muted); cursor: pointer; border-radius: 8px; }
.loc-tab.active { background: white; color: var(--primary); box-shadow: 0 2px 8px rgba(0,0,0,0.05); }
.loc-tab-panel { display: none; } .loc-tab-panel.active { display: block; animation: fadeIn 0.3s; }
.input-row { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
.radius-slider { display: flex; align-items: center; gap: 16px; }
.short-input { width: 80px; text-align: center; font-weight: 700; color: var(--primary); }

.active-location-card { padding: 16px 24px; background: rgba(79, 70, 229, 0.05); border-bottom: 1px solid rgba(79, 70, 229, 0.1); display: flex; justify-content: space-between; align-items: center; }
.loc-info { display: flex; gap: 12px; align-items: center; }
.loc-label { font-size: 11px; text-transform: uppercase; font-weight: 700; color: var(--text-muted); }
.loc-val { font-weight: 600; font-size: 14px; }
.badge { padding: 4px 8px; border-radius: 100px; font-size: 12px; font-weight: 700; }
.badge-radius { background: var(--primary); color: white; margin-right: 8px; }

/* ── AUTH PAGES (SPLIT) ── */
.auth-page { height: 100vh !important; margin: 0 !important; padding: 0 !important; position: fixed; inset: 0; z-index: 1100; background: white !important; }
.auth-split { display: flex; height: 100%; width: 100%; }
.auth-graphics { flex: 1; background: linear-gradient(135deg, var(--primary), var(--secondary)); padding: 60px; color: white; display: flex; flex-direction: column; justify-content: center; }
.auth-graphics-alt { background: linear-gradient(135deg, #0F172A, var(--primary)); }
.auth-graphics h2 { font-size: 48px; font-weight: 800; line-height: 1.1; margin-bottom: 20px; }
.auth-graphics p { font-size: 18px; opacity: 0.9; max-width: 400px; }
.auth-form-side { width: 500px; background: white; display: flex; align-items: center; justify-content: center; padding: 40px; }
.auth-box { width: 100%; max-width: 360px; }
.auth-box h2 { font-size: 32px; font-weight: 800; margin-bottom: 32px; }
.form-group { margin-bottom: 16px; }
.form-group label { display: block; font-size: 13px; font-weight: 600; margin-bottom: 6px; color: var(--text-main); }
.pass-wrapper { position: relative; }
.eye-btn { position: absolute; right: 12px; top: 50%; transform: translateY(-50%); background: none; border: none; cursor: pointer; color: var(--text-muted); }
.auth-links { margin-top: 24px; text-align: center; font-size: 14px; color: var(--text-muted); }
.auth-link { color: var(--primary); font-weight: 600; text-decoration: none; }

/* ── PROFILE & DASHBOARDS ── */
.profile-page { align-items: center; padding-top: 100px; }
.profile-card { width: 400px; background: white; border-radius: var(--radius-lg); padding: 40px; text-align: center; box-shadow: 0 10px 40px rgba(0,0,0,0.05); }
.profile-avatar { width: 80px; height: 80px; border-radius: 50%; background: var(--primary); color: white; font-size: 32px; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px; }
.p-row { display: flex; justify-content: space-between; padding: 12px 0; border-bottom: 1px solid #F1F5F9; }
.p-lbl { font-size: 13px; font-weight: 600; color: var(--text-muted); }
.p-val { font-weight: 500; }

.dash-page { position: fixed; inset: 0; z-index: 1200; background: #F8FAFC; padding: 20px; display: none; gap: 20px; height: 100vh; }
.dash-page.active { display: flex; }
.dash-sidebar { width: 260px; background: white; border-radius: var(--radius-lg); padding: 24px; display: flex; flex-direction: column; box-shadow: 0 4px 20px rgba(0,0,0,0.03); }
.dash-brand { font-size: 20px; font-weight: 800; margin-bottom: 32px; color: var(--primary); }
.dash-user { display: flex; gap: 12px; align-items: center; margin-bottom: 32px; padding: 16px; background: #F1F5F9; border-radius: var(--radius-md); }
.dash-avatar { width: 40px; height: 40px; background: var(--secondary); border-radius: 50%; color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; }
.dash-nav { display: flex; flex-direction: column; gap: 8px; flex: 1; }
.dash-nav-btn { text-align: left; padding: 12px 16px; border-radius: 10px; background: transparent; border: none; font-family: 'Outfit'; font-weight: 600; color: var(--text-muted); cursor: pointer; transition: 0.2s; }
.dash-nav-btn:hover { background: #F8FAFC; color: var(--text-main); }
.dash-nav-btn.active { background: var(--primary); color: white; }
.dash-content { flex: 1; background: transparent; overflow-y: auto; border-radius: var(--radius-lg); }
.dash-panel { display: none; flex-direction: column; } .dash-panel.active { display: flex; }
.dash-top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; }
.dash-top h2 { font-size: 28px; font-weight: 800; }
.dash-actions { display: flex; gap: 12px; }
.table-wrap { background: white; border-radius: var(--radius-md); padding: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.02); overflow-x: auto; }

/* Status Badges */
.badge { background: #F1F5F9; padding: 4px 8px; border-radius: 6px; font-size: 11px; font-weight: 700; }
.progress-bar { background: #F1F5F9; height: 8px; border-radius: 4px; display: flex; align-items: center; width: 100%; position: relative; }
.stats-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; }
.stat { background: #F8FAFC; padding: 12px; border-radius: 8px; font-weight: 600; font-size: 13px; }

/* MODAL */
.modal-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.4); backdrop-filter: blur(4px); z-index: 2000; display: flex; align-items: center; justify-content: center; }
.modal-content { width: 500px; padding: 32px; }

/* LOADER & TOAST */
.loading-overlay { position: fixed; inset: 0; background: rgba(255,255,255,0.8); backdrop-filter: blur(8px); z-index: 9999; display: flex; flex-direction: column; align-items: center; justify-content: center; transition: 0.3s; }
.loading-overlay.hidden { opacity: 0; pointer-events: none; }
.spinner { width: 40px; height: 40px; border: 4px solid #E2E8F0; border-top-color: var(--primary); border-radius: 50%; animation: spin 0.8s linear infinite; }
@keyframes spin { to { transform: rotate(360deg); } }
.toast { position: fixed; bottom: 40px; left: 50%; transform: translateX(-50%) translateY(20px); background: #0F172A; color: white; padding: 12px 24px; border-radius: 100px; font-size: 14px; opacity: 0; transition: 0.3s; z-index: 9998; }
.toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }

/* LEAFLET OVERRIDES */
.leaflet-popup-content-wrapper { border-radius: 16px !important; box-shadow: 0 10px 30px rgba(0,0,0,0.15) !important; }
.leaflet-popup-content { font-family: 'Outfit', sans-serif !important; }
.leaflet-control-zoom { border: none !important; box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important; border-radius: 8px !important; overflow: hidden; }
.leaflet-control-zoom a { color: var(--text-main) !important; border-bottom: 1px solid #E2E8F0 !important; }
"""

with open("c:/Users/MSI/Documents/Code/ppdb Sekolah/7 - editan/frontend/assets/css/style.css", "w", encoding="utf-8") as f:
    f.write(css_content)

print("style.css rewritten successfully")

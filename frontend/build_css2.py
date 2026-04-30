#!/usr/bin/env python3
"""Append CSS Part 2: Zonasi, Auth, Profile, Dashboard, Modals, Leaflet"""
css2 = r'''
/* ZONASI STEP 1 */
.zon-step1{height:100%;display:flex;align-items:center;justify-content:center;position:relative}
.zon-step1::before{content:'';position:absolute;width:400px;height:400px;background:radial-gradient(circle,rgba(99,102,241,.2),transparent 70%);border-radius:50%;filter:blur(80px);top:20%;left:30%}
.zon-card{width:440px;padding:36px;background:var(--card)!important;border:1px solid var(--border)!important;border-radius:var(--radius);position:relative;z-index:2}
.zon-card-icon{font-size:48px;text-align:center;margin-bottom:12px}
.zon-card h2{text-align:center;font-size:24px;font-weight:800;margin-bottom:8px}
.zon-card>p{text-align:center;font-size:13px;color:var(--muted);margin-bottom:24px}
.loc-tabs{display:flex;background:var(--card2);border-radius:10px;padding:4px;margin-bottom:20px}
.loc-tab{flex:1;padding:8px;border:none;background:transparent;font-family:inherit;font-weight:600;color:var(--muted);cursor:pointer;border-radius:8px;font-size:13px;transition:var(--transition)}
.loc-tab.active{background:var(--primary);color:#fff;box-shadow:var(--glow)}
.loc-tab-panel{display:none}.loc-tab-panel.active{display:block;animation:fadeIn .3s}
.tab-desc{font-size:13px;color:var(--muted);margin-bottom:12px}
.gps-status{font-size:12px;margin-top:8px;color:var(--muted)}
.status-text{font-size:12px;color:var(--muted)}
.radius-wrap label{font-size:12px;font-weight:600;color:var(--muted);text-transform:uppercase;letter-spacing:.5px}
.radius-row{display:flex;align-items:center;gap:12px;margin-top:6px}
.fp-loc-badge{padding:16px 20px;background:rgba(99,102,241,.08);border-bottom:1px solid rgba(99,102,241,.2);display:flex;justify-content:space-between;align-items:center}
.fp-loc-label{display:block;font-size:10px;text-transform:uppercase;font-weight:700;color:var(--muted)}
.fp-loc-val{font-weight:600;font-size:14px}
.fp-loc-acts{display:flex;align-items:center;gap:8px}
.rad-badge{background:var(--grad);color:#fff;padding:4px 10px;border-radius:100px;font-size:11px;font-weight:700}
.legend-mini{font-size:11px;color:var(--muted);display:flex;align-items:center;gap:6px}
.ld{width:8px;height:8px;border-radius:50%;display:inline-block}
.ld.g{background:var(--green)}.ld.y{background:var(--amber)}.ld.r{background:var(--red)}
.dropdown-list{position:absolute;top:100%;left:0;right:0;background:var(--card);border:1px solid var(--border);border-radius:10px;max-height:200px;overflow-y:auto;display:none;z-index:20}
.dropdown-list.open{display:block}
.kota-option{padding:10px 14px;cursor:pointer;display:flex;justify-content:space-between;font-size:13px;transition:var(--transition)}
.kota-option:hover{background:var(--card2)}
.kota-option-kab{font-size:11px;color:var(--muted)}

/* AUTH */
.auth-page{position:fixed!important;inset:0;z-index:200;height:100vh!important}
.auth-wrap{display:flex;height:100%;width:calc(100% + var(--sidebar-w));margin-left:calc(-1 * var(--sidebar-w))}
.auth-visual{flex:1;background:var(--grad);padding:60px;display:flex;flex-direction:column;justify-content:center;position:relative;overflow:hidden}
.av-alt{background:linear-gradient(135deg,#0f172a 0%,#6366f1 100%)}
.auth-visual h2{font-size:48px;font-weight:800;line-height:1.1;color:#fff;margin-bottom:16px;position:relative;z-index:2}
.auth-visual p{font-size:16px;color:rgba(255,255,255,.85);max-width:380px;position:relative;z-index:2}
.av-orbs{position:absolute;inset:0}
.orb{position:absolute;border-radius:50%;opacity:.15}
.orb1{width:300px;height:300px;background:#fff;top:-80px;right:-80px;animation:float 15s infinite alternate}
.orb2{width:200px;height:200px;background:var(--accent);bottom:10%;left:-60px;animation:float 12s infinite alternate-reverse}
.orb3{width:150px;height:150px;background:var(--primary);bottom:-40px;right:30%;animation:float 18s infinite alternate}
.auth-form-area{width:480px;background:var(--surface);display:flex;align-items:center;justify-content:center;padding:40px}
.auth-box{width:100%;max-width:340px}
.auth-box h2{font-size:28px;font-weight:800;margin-bottom:28px}
.auth-alt{text-align:center;font-size:13px;color:var(--muted)}
.auth-link{color:var(--accent);font-weight:700;text-decoration:none}
.auth-link:hover{text-decoration:underline}

/* PROFILE */
.profile-center{align-items:center;justify-content:center;padding:40px}
.prof-card{width:400px;padding:36px;text-align:center;background:var(--card)!important;border:1px solid var(--border)!important}
.prof-avatar{width:80px;height:80px;border-radius:50%;background:var(--grad);font-size:36px;display:flex;align-items:center;justify-content:center;margin:0 auto 24px;box-shadow:var(--glow)}
.prof-rows{text-align:left}
.pr{display:flex;justify-content:space-between;align-items:center;padding:12px 0;border-bottom:1px solid var(--border)}
.pr-l{font-size:12px;font-weight:600;color:var(--muted);text-transform:uppercase}
.pr-v{font-weight:500}

/* DASHBOARD */
.dash-page{position:fixed!important;inset:0;z-index:300;background:var(--bg);display:none!important;height:100vh!important}
.dash-page.active{display:flex!important}
.dash-side{width:240px;background:var(--surface);border-right:1px solid var(--border);padding:24px;display:flex;flex-direction:column}
.ds-brand{font-size:20px;font-weight:800;margin-bottom:28px;background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.ds-user{display:flex;gap:12px;align-items:center;padding:16px;background:var(--card);border-radius:12px;margin-bottom:24px}
.ds-av{width:36px;height:36px;background:var(--grad);border-radius:10px;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:16px;color:#fff}
.ds-role{font-size:11px;color:var(--muted)}
.ds-nav{display:flex;flex-direction:column;gap:4px;flex:1}
.dash-nav-btn{text-align:left;padding:10px 14px;border-radius:10px;background:transparent;border:none;font-family:inherit;font-weight:600;color:var(--muted);cursor:pointer;font-size:13px;transition:var(--transition)}
.dash-nav-btn:hover{background:var(--card);color:var(--text)}
.dash-nav-btn.active{background:rgba(99,102,241,.15);color:var(--primary);box-shadow:inset 3px 0 0 var(--primary)}
.ds-foot{display:flex;justify-content:space-between;padding-top:16px;border-top:1px solid var(--border)}
.dash-main{flex:1;overflow-y:auto;padding:24px}
.dash-panel{display:none;flex-direction:column}.dash-panel.active{display:flex}
.dp-top{display:flex;justify-content:space-between;align-items:center;margin-bottom:20px}
.dp-top h2{font-size:24px;font-weight:800}
.dp-acts{display:flex;gap:8px;align-items:center}
.dp-table{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:16px;overflow-x:auto}
.dp-pg{display:flex;align-items:center;justify-content:center;gap:12px;padding:16px 0;font-size:13px;color:var(--muted)}
.op-profil-card{padding:24px;background:var(--card)!important;border:1px solid var(--border)!important;border-radius:var(--radius)}
.op-profil-card h3{font-size:20px;font-weight:800;margin-bottom:8px}
.op-badges{display:flex;gap:8px;margin-bottom:12px}
.badge{padding:4px 10px;border-radius:6px;font-size:11px;font-weight:700;background:var(--card2);border:1px solid var(--border)}
.op-stats{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-top:16px}
.os{background:var(--card2);padding:12px;border-radius:10px;font-size:12px;color:var(--muted);text-align:center}
.os b{display:block;font-size:18px;color:var(--text);margin-top:4px}
.op-bar{height:8px;background:var(--card2);border-radius:4px;margin-top:12px;position:relative;overflow:hidden}
.op-bar-fill{height:100%;background:var(--grad);border-radius:4px;transition:width .5s}
.op-bar span{position:absolute;right:0;top:-18px;font-size:11px;color:var(--muted)}
.op-biaya{padding:20px;background:var(--card)!important;border:1px solid var(--border)!important}
.op-biaya p{padding:6px 0;font-size:14px;color:var(--muted)}
.op-biaya b{color:var(--text)}
.op-biaya hr{border:none;border-top:1px solid var(--border);margin:8px 0}
.summary-text{display:block;padding:12px 0;font-size:13px;color:var(--muted)}
.glass-card{background:var(--card);border:1px solid var(--border);border-radius:var(--radius)}
.jenjang-pill{padding:3px 8px;border-radius:6px;font-size:10px;font-weight:700}
.status-pill{padding:3px 8px;border-radius:6px;font-size:10px;font-weight:700}
.status-aktif{background:rgba(16,185,129,.15);color:var(--green)}
.status-cukup{background:rgba(245,158,11,.15);color:var(--amber)}
.status-rusak,.status-baik-red{background:rgba(239,68,68,.15);color:var(--red)}

/* MODALS */
.modal-overlay{position:fixed;inset:0;background:rgba(0,0,0,.6);backdrop-filter:blur(6px);z-index:2000;display:flex;align-items:center;justify-content:center}
.modal-box{width:520px;max-height:85vh;overflow-y:auto;padding:0;background:var(--card)!important;border:1px solid var(--border)!important;border-radius:var(--radius)}
.modal-sm{width:400px}
.mb-head{display:flex;justify-content:space-between;align-items:center;padding:20px 24px;border-bottom:1px solid var(--border)}
.mb-head h3{font-size:18px;font-weight:700}
.mb-x{background:none;border:none;color:var(--muted);font-size:18px;cursor:pointer;transition:var(--transition)}
.mb-x:hover{color:var(--red)}
.mb-body{padding:20px 24px}
.mb-foot{padding:16px 24px;border-top:1px solid var(--border);display:flex;justify-content:flex-end;gap:8px}

/* LEAFLET */
.leaflet-popup-content-wrapper{background:var(--card)!important;color:var(--text)!important;border-radius:12px!important;box-shadow:0 8px 30px rgba(0,0,0,.5)!important;border:1px solid var(--border)!important}
.leaflet-popup-tip{background:var(--card)!important}
.leaflet-popup-content{font-family:'Outfit',sans-serif!important;color:var(--text)!important}
.leaflet-control-zoom{border:none!important;background:var(--card)!important;box-shadow:0 4px 12px rgba(0,0,0,.3)!important;border-radius:10px!important;overflow:hidden;border:1px solid var(--border)!important}
.leaflet-control-zoom a{color:var(--text)!important;background:var(--card)!important;border-color:var(--border)!important}
.leaflet-control-zoom a:hover{background:var(--card2)!important}
.map-legend{background:var(--card)!important;border:1px solid var(--border)!important;border-radius:10px!important;padding:12px!important;color:var(--text)!important;font-family:'Outfit',sans-serif!important;font-size:12px}
.leg-title,.leg-subtitle{font-weight:700;margin-bottom:6px}
.leg-row{display:flex;align-items:center;gap:6px;margin-bottom:4px}
.leg-ring{width:12px;height:12px;border-radius:50%;border:3px solid;display:inline-block}
.leg-divider{border-top:1px solid var(--border);margin:6px 0}
.user-marker-dot{width:14px;height:14px;background:var(--accent);border:3px solid #fff;border-radius:50%;box-shadow:0 0 12px var(--accent)}
.boundary-tooltip{background:var(--card)!important;color:var(--text)!important;border:1px solid var(--border)!important;border-radius:8px!important;font-family:'Outfit',sans-serif!important}

/* SCROLLBAR */
::-webkit-scrollbar{width:5px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:var(--border);border-radius:3px}
::-webkit-scrollbar-thumb:hover{background:var(--primary)}
'''
with open("assets/css/style.css","a",encoding="utf-8") as f:
    f.write(css2)
print("CSS Part 2 appended")

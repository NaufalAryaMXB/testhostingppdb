#!/usr/bin/env python3
"""Generate new style.css - Part 1: Core + Sidebar + Home + Map"""
css = r'''@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@400;500;600&display=swap');
:root{--bg:#06080f;--surface:#0e1225;--card:#151a30;--card2:#1c2340;--border:#2a3155;--text:#e8ecf4;--muted:#7b86a3;--primary:#6366f1;--accent:#22d3ee;--green:#10b981;--red:#ef4444;--amber:#f59e0b;--grad:linear-gradient(135deg,#6366f1,#06b6d4);--glow:0 0 24px rgba(99,102,241,.25);--radius:16px;--sidebar-w:80px;--transition:.3s cubic-bezier(.4,0,.2,1)}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;font-family:'Outfit','Inter',sans-serif;background:var(--bg);color:var(--text);overflow:hidden}
.hidden{display:none!important}
.mt8{margin-top:8px}.mt16{margin-top:16px}.full-w{width:100%}

/* Cosmic BG */
.cosmos-bg{position:fixed;inset:0;z-index:-1;background:var(--bg);overflow:hidden}
.cosmos-bg::before,.cosmos-bg::after{content:'';position:absolute;border-radius:50%;filter:blur(80px);animation:float 20s infinite alternate}
.cosmos-bg::before{width:600px;height:600px;top:-200px;left:-100px;background:radial-gradient(circle,rgba(99,102,241,.15),transparent 70%)}
.cosmos-bg::after{width:500px;height:500px;bottom:-150px;right:-100px;background:radial-gradient(circle,rgba(34,211,238,.12),transparent 70%)}
@keyframes float{0%{transform:translate(0,0) scale(1)}50%{transform:translate(40px,30px) scale(1.1)}100%{transform:translate(-20px,-20px) scale(.95)}}

/* SIDEBAR */
.sidebar{position:fixed;left:0;top:0;width:var(--sidebar-w);height:100vh;background:var(--surface);border-right:1px solid var(--border);display:flex;flex-direction:column;justify-content:space-between;z-index:100;padding:16px 0}
.sb-top{display:flex;flex-direction:column;align-items:center;gap:24px}
.sb-logo{display:flex;flex-direction:column;align-items:center;gap:4px;padding:8px 0}
.logo-icon{font-size:28px}
.logo-label{font-size:10px;font-weight:700;text-align:center;line-height:1.2;color:var(--accent);letter-spacing:.5px}
.sb-nav{display:flex;flex-direction:column;gap:8px;width:100%;padding:0 8px}
.sb-link{display:flex;flex-direction:column;align-items:center;gap:4px;padding:10px 4px;border-radius:12px;text-decoration:none;color:var(--muted);font-size:10px;font-weight:600;transition:var(--transition)}
.sb-link .sb-ico{font-size:20px}
.sb-link:hover{color:var(--text);background:var(--card)}
.sb-link.active{color:var(--accent);background:rgba(34,211,238,.1);box-shadow:inset 3px 0 0 var(--accent)}
.sb-bottom{display:flex;flex-direction:column;align-items:center;gap:12px;padding:0 8px}
.sb-search-wrap{display:none}
.sb-auth{display:none}
.sb-profile-btn{width:40px;height:40px;border-radius:50%;border:2px solid var(--border);background:var(--card);color:var(--accent);display:flex;align-items:center;justify-content:center;cursor:pointer;transition:var(--transition)}
.sb-profile-btn:hover{border-color:var(--accent);box-shadow:var(--glow)}

/* MAIN CONTENT */
.main-content{margin-left:var(--sidebar-w);height:100vh;position:relative}
.page{display:none;height:100%;opacity:0;animation:fadeIn .4s forwards}
.page.active{display:flex;flex-direction:column}
.page-scroll{overflow-y:auto}
.page-full{position:relative}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}

/* LOADER */
.loading-overlay{position:fixed;inset:0;background:rgba(6,8,15,.95);z-index:9999;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:20px;transition:.3s}
.loading-overlay.hidden{opacity:0;pointer-events:none}
.loader-ring{width:48px;height:48px;position:relative}
.loader-ring div{position:absolute;width:48px;height:48px;border-radius:50%;border:3px solid transparent;border-top-color:var(--accent);animation:spin 1.2s cubic-bezier(.5,0,.5,1) infinite}
.loader-ring div:nth-child(2){animation-delay:-.15s;border-top-color:var(--primary)}
.loader-ring div:nth-child(3){animation-delay:-.3s;border-top-color:rgba(99,102,241,.4)}
@keyframes spin{to{transform:rotate(360deg)}}
.loader-text{color:var(--muted);font-size:14px;font-weight:500}
.dots::after{content:'...';animation:dots 1.5s steps(4,end) infinite}
@keyframes dots{0%,20%{content:'.'}40%{content:'..'}60%,100%{content:'...'}}

/* TOAST */
.toast{position:fixed;bottom:32px;left:50%;transform:translateX(-50%) translateY(20px);background:var(--card);border:1px solid var(--border);color:var(--text);padding:12px 28px;border-radius:100px;font-size:14px;font-weight:500;opacity:0;transition:.3s;z-index:9998;box-shadow:var(--glow)}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}

/* BUTTONS */
.btn-glow{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:14px 32px;background:var(--grad);color:#fff;border:none;border-radius:100px;font-family:inherit;font-size:15px;font-weight:700;cursor:pointer;transition:var(--transition);box-shadow:var(--glow)}
.btn-glow:hover{transform:translateY(-2px);box-shadow:0 0 40px rgba(99,102,241,.4)}
.btn-ghost{padding:14px 32px;background:transparent;border:2px solid var(--border);color:var(--text);border-radius:100px;font-family:inherit;font-size:15px;font-weight:700;cursor:pointer;transition:var(--transition)}
.btn-ghost:hover{border-color:var(--accent);color:var(--accent)}
.btn-sm-fill{padding:8px 20px;background:var(--grad);color:#fff;border:none;border-radius:10px;font-family:inherit;font-weight:700;font-size:13px;cursor:pointer;transition:var(--transition)}
.btn-sm-fill:hover{box-shadow:var(--glow)}
.btn-sm-outline{padding:8px 20px;background:transparent;border:1px solid var(--border);color:var(--muted);border-radius:10px;font-family:inherit;font-weight:600;font-size:13px;cursor:pointer;transition:var(--transition)}
.btn-sm-outline:hover{border-color:var(--accent);color:var(--accent)}
.btn-sm-danger{padding:8px 20px;background:var(--red);color:#fff;border:none;border-radius:10px;font-family:inherit;font-weight:700;font-size:13px;cursor:pointer}
.btn-danger{padding:12px;background:var(--red);color:#fff;border:none;border-radius:12px;font-family:inherit;font-weight:700;cursor:pointer}
.btn-link{background:none;border:none;color:var(--muted);font-family:inherit;font-weight:600;cursor:pointer;font-size:13px;transition:var(--transition)}
.btn-link:hover{color:var(--accent)}
.btn-link-red:hover{color:var(--red)!important}
.pg-btn{width:32px;height:32px;border-radius:8px;background:var(--card2);border:1px solid var(--border);color:var(--text);font-size:16px;cursor:pointer;transition:var(--transition);display:inline-flex;align-items:center;justify-content:center}
.pg-btn:hover{border-color:var(--primary);box-shadow:var(--glow)}
.pg-btn:disabled{opacity:.3;cursor:default}

/* INPUTS */
.fi{width:100%;padding:10px 14px;background:var(--card);border:1px solid var(--border);border-radius:10px;color:var(--text);font-family:inherit;font-size:14px;outline:none;transition:var(--transition)}
.fi:focus{border-color:var(--primary);box-shadow:0 0 0 3px rgba(99,102,241,.15)}
.fi-short{width:72px;text-align:center;font-weight:700;color:var(--accent)}
.fi-sm{width:auto;min-width:100px;padding:7px 12px;font-size:13px}
.fg{margin-bottom:12px}
.fg label{display:block;font-size:12px;font-weight:600;color:var(--muted);margin-bottom:4px;text-transform:uppercase;letter-spacing:.5px}
.row2{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.pass-wrap{position:relative}
.eye-btn{position:absolute;right:10px;top:50%;transform:translateY(-50%);background:none;border:none;cursor:pointer;font-size:16px}
.slider{flex:1;accent-color:var(--primary)}

/* HOME */
.home-hero{text-align:center;padding:80px 40px 60px;position:relative}
.hero-glow{position:absolute;top:50%;left:50%;width:500px;height:300px;background:radial-gradient(ellipse,rgba(99,102,241,.15),transparent 70%);transform:translate(-50%,-50%);filter:blur(60px);pointer-events:none}
.hero-title{font-size:clamp(36px,5vw,64px);font-weight:800;line-height:1.1;letter-spacing:-2px;margin-bottom:20px;position:relative}
.grad-text{background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero-sub{font-size:18px;color:var(--muted);max-width:500px;margin:0 auto 36px;line-height:1.6}
.hero-btns{display:flex;gap:16px;justify-content:center}
.home-grid{display:grid;grid-template-columns:2fr 1fr;gap:24px;padding:0 40px 40px;max-width:1200px;margin:0 auto}
.hcard{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:24px;transition:var(--transition)}
.hcard:hover{border-color:rgba(99,102,241,.3);box-shadow:var(--glow)}
.hcard-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:16px}
.hcard-head h3{font-size:16px;font-weight:700}
.pg-mini{display:flex;align-items:center;gap:8px;font-size:13px;color:var(--muted)}
.news-placeholder{height:160px;background:var(--card2);border-radius:12px;display:flex;flex-direction:column;align-items:center;justify-content:center;color:var(--muted)}
.news-shimmer{width:80%;height:12px;background:linear-gradient(90deg,var(--card2),var(--border),var(--card2));background-size:200%;border-radius:6px;margin-bottom:12px;animation:shimmer 2s infinite}
@keyframes shimmer{0%{background-position:200% 0}100%{background-position:-200% 0}}

/* TABLE */
.dtable{width:100%;border-collapse:collapse;text-align:left;font-size:13px}
.dtable th{font-size:11px;text-transform:uppercase;letter-spacing:.5px;color:var(--muted);padding:12px;border-bottom:2px solid var(--border);font-weight:700}
.dtable td{padding:12px;border-bottom:1px solid rgba(42,49,85,.5);transition:var(--transition)}
.dtable tr:hover td{background:rgba(99,102,241,.04)}
.td-empty{text-align:center;color:var(--muted);padding:32px!important}
.aksi-col{display:flex;gap:6px}
.btn-edit,.btn-hapus{padding:4px 10px;border-radius:6px;border:1px solid var(--border);background:var(--card2);color:var(--text);font-size:11px;font-weight:600;cursor:pointer;transition:var(--transition)}
.btn-edit:hover{border-color:var(--primary);color:var(--primary)}
.btn-hapus:hover{border-color:var(--red);color:var(--red)}

/* FULL MAP + FLOATING PANEL */
.fullmap{position:absolute;inset:0;z-index:1}
.map-float-panel{position:absolute;top:20px;left:20px;bottom:20px;width:380px;z-index:10;background:rgba(14,18,37,.92);backdrop-filter:blur(20px);border:1px solid var(--border);border-radius:var(--radius);display:flex;flex-direction:column;overflow:hidden;box-shadow:0 8px 40px rgba(0,0,0,.4)}
.fp-header{padding:24px 20px 16px;border-bottom:1px solid var(--border)}
.fp-header h2{font-size:20px;font-weight:800;margin-bottom:4px}
.fp-header p{font-size:12px;color:var(--muted)}
.fp-filters{padding:16px 20px;border-bottom:1px solid var(--border);display:grid;grid-template-columns:1fr 1fr;gap:10px}
.fg2 label{display:block;font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted);margin-bottom:3px}
.fg2-btns{display:flex;gap:8px;align-items:flex-end;grid-column:1/-1}
.fp-list{flex:1;display:flex;flex-direction:column;overflow:hidden;padding-top:8px}
.fp-list h4{padding:8px 20px;font-size:14px;font-weight:700}
.fp-list-head{display:flex;justify-content:space-between;align-items:center;padding:8px 20px}
.fp-pg{padding:12px 20px;border-top:1px solid var(--border);display:flex;align-items:center;justify-content:center;gap:12px;font-size:13px;color:var(--muted)}
.school-list{list-style:none;flex:1;overflow-y:auto;padding:0 12px}
.flat-list-item{display:flex;gap:10px;padding:12px;margin-bottom:6px;background:var(--card);border:1px solid var(--border);border-radius:12px;cursor:pointer;transition:var(--transition)}
.flat-list-item:hover{border-color:var(--primary);transform:translateX(4px);box-shadow:var(--glow)}
.flat-list-empty{text-align:center;padding:32px;color:var(--muted)}
.item-jenjang-dot{width:8px;height:8px;border-radius:50%;flex-shrink:0;margin-top:6px}
.item-info{display:flex;flex-direction:column;gap:3px;flex:1;min-width:0}
.item-name{font-weight:600;font-size:13px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.item-jenjang-badge{font-size:9px;font-weight:700;padding:2px 6px;border-radius:4px;display:inline-block;width:fit-content}
.item-meta{font-size:11px;color:var(--muted)}
.item-dist{font-size:12px;font-weight:700;padding:4px 8px;border-radius:6px;align-self:flex-start;white-space:nowrap}
.item-dist--green{background:rgba(16,185,129,.15);color:var(--green)}
.item-dist--yellow{background:rgba(245,158,11,.15);color:var(--amber)}
.item-dist--red{background:rgba(239,68,68,.15);color:var(--red)}
'''
with open("assets/css/style.css","w",encoding="utf-8") as f:
    f.write(css)
print("CSS Part 1 written")

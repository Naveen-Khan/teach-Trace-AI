"""Shared TeachTrace AI theme — Linear / Vercel / Notion dark-mode system."""

import streamlit as st

# Palette used by CSS and Altair charts
COLORS = {
    "bg": "#0A0A0B",
    "surface": "#111113",
    "elevated": "#161618",
    "hover": "#1C1C1F",
    "border": "#232326",
    "border_strong": "#2E2E32",
    "text": "#EDEDEF",
    "muted": "#8A8F98",
    "accent": "#5E6AD2",
    "accent_hover": "#6E79DB",
    "high": "#EB5757",
    "medium": "#F2C94C",
    "low": "#4CB782",
    "grid": "#1C1C1F",
}

NAV_PAGES = [
    "Dashboard",
    "Analyze answers",
    "Learning gap map",
    "Reteaching plans",
    "Reassessment",
]

NAV_ICONS = {
    "Dashboard": "▣",
    "Analyze answers": "⇪",
    "Learning gap map": "◎",
    "Reteaching plans": "✎",
    "Reassessment": "↗",
}

NAV_LABELS = {
    "Dashboard": "Dashboard",
    "Analyze answers": "Analyze answers",
    "Learning gap map": "Learning gap map",
    "Reteaching plans": "Reteaching plans",
    "Reassessment": "Reassessment",
}

_CSS = f"""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  :root {{
    --tt-bg: {COLORS["bg"]};
    --tt-surface: {COLORS["surface"]};
    --tt-elevated: {COLORS["elevated"]};
    --tt-hover: {COLORS["hover"]};
    --tt-border: {COLORS["border"]};
    --tt-border-strong: {COLORS["border_strong"]};
    --tt-text: {COLORS["text"]};
    --tt-muted: {COLORS["muted"]};
    --tt-accent: {COLORS["accent"]};
    --tt-accent-hover: {COLORS["accent_hover"]};
    --tt-high: {COLORS["high"]};
    --tt-medium: {COLORS["medium"]};
    --tt-low: {COLORS["low"]};
    --tt-radius: 8px;
    --tt-radius-lg: 12px;
    --tt-space-1: 4px;
    --tt-space-2: 8px;
    --tt-space-3: 12px;
    --tt-space-4: 16px;
    --tt-space-5: 24px;
    --tt-space-6: 32px;
    --tt-shadow: 0 1px 0 rgba(255,255,255,.04), 0 8px 24px rgba(0,0,0,.35);
  }}

  html, body, .stApp, [data-testid="stAppViewContainer"] {{
    background: var(--tt-bg) !important;
    color: var(--tt-text);
    font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;
  }}
  [data-testid="stHeader"] {{ background: transparent !important; }}
  footer {{ visibility: hidden; height: 0; }}
  .block-container {{
    padding: var(--tt-space-5) var(--tt-space-6) var(--tt-space-6) !important;
    max-width: 1180px;
  }}

  h1, h2, h3, h4, p, label, span, div {{
    font-family: Inter, system-ui, sans-serif !important;
  }}
  h1 {{
    font-size: 28px !important;
    font-weight: 650 !important;
    letter-spacing: -0.045em !important;
    color: var(--tt-text) !important;
    margin: 0 !important;
  }}
  h3 {{
    font-size: 14px !important;
    font-weight: 600 !important;
    letter-spacing: -0.01em;
    color: var(--tt-text) !important;
  }}

  /* Sidebar */
  section[data-testid="stSidebar"] {{
    background: var(--tt-surface) !important;
    border-right: 1px solid var(--tt-border);
  }}
  section[data-testid="stSidebar"] > div {{
    background: var(--tt-surface) !important;
  }}
  section[data-testid="stSidebar"] .block-container {{
    padding: var(--tt-space-4) var(--tt-space-3) var(--tt-space-5) !important;
  }}

  .tt-brand {{
    display: flex; align-items: center; gap: 10px;
    padding: 4px 6px 18px;
  }}
  .tt-mark {{
    width: 28px; height: 28px; border-radius: 7px;
    background: var(--tt-accent);
    color: #fff; font-size: 11px; font-weight: 800;
    display: grid; place-items: center;
    letter-spacing: -0.04em;
  }}
  .tt-brand-name {{ font-size: 13px; font-weight: 650; color: var(--tt-text); }}
  .tt-brand-sub {{ font-size: 11px; color: var(--tt-muted); margin-top: 1px; }}

  .tt-nav-label, .tt-side-label {{
    font-size: 11px; font-weight: 600; color: var(--tt-muted);
    letter-spacing: 0.08em; text-transform: uppercase;
    padding: 4px 8px 8px;
  }}
  .tt-side-group {{
    margin-top: 16px;
    padding-top: 16px;
    border-top: 1px solid var(--tt-border);
  }}
  .tt-tip {{
    margin-top: 16px;
    padding: 12px;
    border-radius: var(--tt-radius);
    background: var(--tt-elevated);
    border: 1px solid var(--tt-border);
    color: var(--tt-muted);
    font-size: 12px;
    line-height: 1.5;
  }}
  .tt-tip strong {{ color: var(--tt-text); font-weight: 600; }}

  section[data-testid="stSidebar"] div[role="radiogroup"] {{
    gap: 2px !important;
  }}
  section[data-testid="stSidebar"] div[role="radiogroup"] label {{
    background: transparent !important;
    border: 1px solid transparent;
    border-radius: var(--tt-radius) !important;
    padding: 8px 10px !important;
    color: var(--tt-muted) !important;
    font-size: 13px !important;
    font-weight: 500 !important;
  }}
  section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {{
    background: var(--tt-hover) !important;
    color: var(--tt-text) !important;
  }}
  section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {{
    background: rgba(94,106,210,.12) !important;
    border-color: rgba(94,106,210,.35) !important;
    color: var(--tt-text) !important;
    font-weight: 600 !important;
  }}
  section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) p,
  section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) span {{
    color: var(--tt-text) !important;
  }}
  section[data-testid="stSidebar"] [data-testid="stRadio"] {{
    margin-bottom: 4px;
  }}

  /* Page chrome */
  .tt-hero {{
    display: flex; justify-content: space-between; align-items: flex-end;
    gap: var(--tt-space-5); margin-bottom: var(--tt-space-5); flex-wrap: wrap;
  }}
  .tt-kicker {{
    font-size: 11px; font-weight: 600; color: var(--tt-muted);
    letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 8px;
  }}
  .tt-lead {{
    margin: 8px 0 0; color: var(--tt-muted); font-size: 14px; max-width: 56ch; line-height: 1.5;
  }}
  .tt-meta {{ display: flex; gap: 8px; flex-wrap: wrap; }}
  .tt-pill {{
    background: var(--tt-elevated); border: 1px solid var(--tt-border);
    border-radius: 999px; padding: 6px 12px; font-size: 12px; color: var(--tt-muted);
  }}
  .tt-pill b {{ color: var(--tt-text); font-weight: 650; }}
  .tt-pill.danger {{ border-color: rgba(235,87,87,.35); color: var(--tt-high); }}

  /* KPI cards */
  .tt-kpis {{
    display: grid; grid-template-columns: repeat(4, 1fr);
    gap: var(--tt-space-3); margin-bottom: var(--tt-space-5);
  }}
  .tt-kpi {{
    background: var(--tt-surface);
    border: 1px solid var(--tt-border);
    border-radius: var(--tt-radius-lg);
    padding: 16px 16px 14px;
    box-shadow: var(--tt-shadow);
    position: relative;
    overflow: hidden;
    transition: border-color .15s ease, background .15s ease;
  }}
  .tt-kpi:hover {{ border-color: var(--tt-border-strong); background: var(--tt-elevated); }}
  .tt-kpi .bar {{
    position: absolute; left: 0; top: 0; bottom: 0; width: 2px;
    background: var(--tt-accent);
  }}
  .tt-kpi.warn .bar {{ background: var(--tt-high); }}
  .tt-kpi .row {{ display: flex; justify-content: space-between; align-items: flex-start; }}
  .tt-kpi .icon {{
    width: 28px; height: 28px; border-radius: 7px;
    background: var(--tt-elevated); border: 1px solid var(--tt-border);
    display: grid; place-items: center; font-size: 13px; color: var(--tt-muted);
  }}
  .tt-kpi .label {{
    font-size: 12px; font-weight: 500; color: var(--tt-muted); margin-bottom: 10px;
  }}
  .tt-kpi .value {{
    font-size: 28px; font-weight: 700; letter-spacing: -0.05em; line-height: 1;
  }}
  .tt-kpi .delta {{ font-size: 12px; margin-top: 8px; color: var(--tt-muted); }}
  .tt-kpi .delta.up {{ color: var(--tt-low); }}
  .tt-kpi .delta.down {{ color: var(--tt-high); }}

  /* Surfaces / lists */
  .tt-panel {{
    background: var(--tt-surface);
    border: 1px solid var(--tt-border);
    border-radius: var(--tt-radius-lg);
    padding: 16px 16px 8px;
    box-shadow: var(--tt-shadow);
    height: 100%;
  }}
  .tt-panel h3 {{ margin: 0 0 2px; font-size: 13px !important; }}
  .tt-panel .sub {{ color: var(--tt-muted); font-size: 12px; margin: 0 0 12px; }}

  .tt-row {{
    display: flex; justify-content: space-between; align-items: center; gap: 12px;
    padding: 10px 8px; margin: 0 -8px 4px;
    border-radius: var(--tt-radius);
    transition: background .12s ease;
  }}
  .tt-row:hover {{ background: var(--tt-hover); }}
  .tt-row .name {{ font-size: 13px; font-weight: 600; }}
  .tt-row .count {{ font-size: 12px; color: var(--tt-muted); margin-top: 2px; }}

  .tt-badge {{
    font-size: 11px; font-weight: 650; padding: 3px 8px; border-radius: 999px;
    border: 1px solid transparent; white-space: nowrap;
  }}
  .tt-badge.high {{ background: rgba(235,87,87,.12); color: #FF7B7B; border-color: rgba(235,87,87,.25); }}
  .tt-badge.med {{ background: rgba(242,201,76,.12); color: #F2C94C; border-color: rgba(242,201,76,.25); }}
  .tt-badge.low {{ background: rgba(76,183,130,.12); color: #4CB782; border-color: rgba(76,183,130,.25); }}

  .tt-card {{
    background: var(--tt-surface);
    border: 1px solid var(--tt-border);
    border-radius: var(--tt-radius-lg);
    padding: 16px;
    margin-bottom: 12px;
    box-shadow: var(--tt-shadow);
    transition: border-color .15s ease, background .15s ease, transform .15s ease;
  }}
  .tt-card:hover {{
    border-color: var(--tt-border-strong);
    background: var(--tt-elevated);
    transform: translateY(-1px);
  }}
  .tt-card.high {{ border-left: 2px solid var(--tt-high); }}
  .tt-card.med {{ border-left: 2px solid var(--tt-medium); }}
  .tt-card.low {{ border-left: 2px solid var(--tt-low); }}
  .tt-card h3 {{ font-size: 14px !important; margin: 10px 0 8px !important; }}
  .tt-card p {{ color: var(--tt-muted); font-size: 13px; line-height: 1.55; margin: 0 0 12px; }}
  .tt-card-top {{ display: flex; justify-content: space-between; align-items: center; gap: 8px; }}
  .tt-type {{ font-size: 12px; color: var(--tt-muted); }}
  .tt-meta-row {{ display: flex; justify-content: space-between; font-size: 12px; color: var(--tt-text); font-weight: 600; }}
  .tt-track {{ height: 6px; background: var(--tt-hover); border-radius: 99px; overflow: hidden; margin-top: 8px; }}
  .tt-track i {{ display: block; height: 100%; border-radius: 99px; }}

  .tt-alert {{
    background: var(--tt-surface);
    border: 1px solid rgba(242,201,76,.28);
    border-radius: var(--tt-radius-lg);
    padding: 16px 18px;
    margin-top: 4px;
  }}
  .tt-alert .kicker {{ color: var(--tt-medium); font-size: 11px; font-weight: 650; letter-spacing: .08em; text-transform: uppercase; }}
  .tt-alert h3 {{ margin: 8px 0 !important; }}
  .tt-alert .q {{ color: var(--tt-text); font-style: italic; font-size: 13px; }}
  .tt-split {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }}
  .tt-mini {{ font-size: 11px; font-weight: 650; color: var(--tt-muted); letter-spacing: .06em; text-transform: uppercase; margin-bottom: 6px; }}

  .tt-step {{
    background: var(--tt-surface);
    border: 1px solid var(--tt-border);
    border-radius: var(--tt-radius-lg);
    padding: 16px;
    min-height: 148px;
    transition: border-color .15s ease, background .15s ease;
  }}
  .tt-step:hover {{ border-color: var(--tt-border-strong); background: var(--tt-elevated); }}
  .tt-n {{
    width: 22px; height: 22px; border-radius: 6px;
    background: rgba(94,106,210,.15); color: #A4ACF2;
    display: grid; place-items: center; font-size: 11px; font-weight: 700; margin-bottom: 10px;
  }}
  .tt-q {{
    background: var(--tt-surface);
    border: 1px solid var(--tt-border);
    border-radius: var(--tt-radius-lg);
    padding: 16px;
    min-height: 112px;
    transition: border-color .15s ease;
  }}
  .tt-q:hover {{ border-color: var(--tt-border-strong); }}
  .tt-q b {{ color: var(--tt-accent); font-size: 11px; letter-spacing: .08em; }}
  .tt-q p {{ color: var(--tt-text); font-size: 13px; line-height: 1.5; margin: 8px 0 0; }}

  /* Improvement block */
  .tt-improve {{
    background: var(--tt-surface);
    border: 1px solid var(--tt-border);
    border-radius: var(--tt-radius-lg);
    padding: 20px 20px 18px;
    box-shadow: var(--tt-shadow);
    margin-top: 8px;
  }}
  .tt-improve-head {{
    display: flex; justify-content: space-between; align-items: center; gap: 12px; flex-wrap: wrap;
    margin-bottom: 14px;
  }}
  .tt-improve-head .side {{ font-size: 12px; color: var(--tt-muted); }}
  .tt-improve-head .side b {{ display: block; color: var(--tt-text); font-size: 22px; letter-spacing: -0.04em; margin-top: 2px; }}
  .tt-delta {{
    display: flex; align-items: center; gap: 8px;
    background: rgba(76,183,130,.12);
    border: 1px solid rgba(76,183,130,.28);
    color: var(--tt-low);
    border-radius: 999px;
    padding: 6px 12px;
    font-size: 13px; font-weight: 700;
  }}
  .tt-improve-track {{
    position: relative; height: 10px; background: var(--tt-hover);
    border-radius: 99px; overflow: hidden; margin: 6px 0 12px;
  }}
  .tt-improve-track .fill {{
    position: absolute; left: 0; top: 0; bottom: 0;
    background: var(--tt-accent); border-radius: 99px;
  }}
  .tt-improve-track .marker {{
    position: absolute; top: -3px; bottom: -3px; width: 2px;
    background: var(--tt-text); opacity: .85; border-radius: 2px;
  }}
  .tt-improve p {{ color: var(--tt-muted); font-size: 13px; margin: 0; line-height: 1.5; }}

  /* Widgets */
  .stButton > button {{
    border-radius: var(--tt-radius) !important;
    font-family: Inter, system-ui, sans-serif !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    border: 1px solid var(--tt-border) !important;
    background: var(--tt-elevated) !important;
    color: var(--tt-text) !important;
  }}
  .stButton > button:hover {{
    border-color: var(--tt-border-strong) !important;
    background: var(--tt-hover) !important;
  }}
  .stButton > button[kind="primary"] {{
    background: var(--tt-accent) !important;
    border-color: var(--tt-accent) !important;
    color: #fff !important;
  }}
  .stButton > button[kind="primary"]:hover {{
    background: var(--tt-accent-hover) !important;
    border-color: var(--tt-accent-hover) !important;
  }}
  [data-testid="stFileUploader"] {{
    background: var(--tt-surface);
    border: 1px dashed var(--tt-border-strong);
    border-radius: var(--tt-radius-lg);
    padding: 8px 10px;
  }}
  [data-testid="stTextArea"] textarea,
  textarea {{
    background: var(--tt-elevated) !important;
    color: var(--tt-text) !important;
    border-radius: var(--tt-radius) !important;
  }}
  [data-testid="stSelectbox"] > div {{ border-radius: var(--tt-radius) !important; }}
  [data-testid="stDataFrame"], .stDataFrame {{
    border: 1px solid var(--tt-border);
    border-radius: var(--tt-radius-lg);
    overflow: hidden;
  }}
  div[data-testid="stExpander"] {{
    background: var(--tt-surface);
    border: 1px solid var(--tt-border) !important;
    border-radius: var(--tt-radius-lg) !important;
    margin-bottom: 8px;
  }}
  div[data-testid="stExpander"]:hover {{
    border-color: var(--tt-border-strong) !important;
  }}
  div[data-testid="stMetric"] {{
    background: var(--tt-surface);
    border: 1px solid var(--tt-border);
    border-radius: var(--tt-radius-lg);
    padding: 12px 14px;
  }}

  @media (max-width: 980px) {{
    .tt-kpis {{ grid-template-columns: 1fr 1fr; }}
    .tt-split {{ grid-template-columns: 1fr; }}
  }}
  @media (max-width: 640px) {{
    .tt-kpis {{ grid-template-columns: 1fr; }}
    .block-container {{ padding: 16px !important; }}
  }}
</style>
"""


def load_css() -> None:
    st.markdown(_CSS, unsafe_allow_html=True)


def render_sidebar() -> str:
    st.sidebar.markdown(
        """
        <div class="tt-brand">
            <div class="tt-mark">Tt</div>
            <div>
                <div class="tt-brand-name">TeachTrace AI</div>
                <div class="tt-brand-sub">Classroom intelligence</div>
            </div>
        </div>
        <div class="tt-nav-label">Navigation</div>
        """,
        unsafe_allow_html=True,
    )
    selected = st.sidebar.radio(
        "Navigate",
        NAV_PAGES,
        format_func=lambda key: f"{NAV_ICONS[key]}    {NAV_LABELS[key]}",
        label_visibility="collapsed",
    )
    st.sidebar.markdown(
        '<div class="tt-side-group"><div class="tt-side-label">Active class</div></div>',
        unsafe_allow_html=True,
    )
    st.sidebar.selectbox(
        "Active class",
        ["Grade 8-A — Mathematics", "Grade 7-B — Science", "Grade 9-A — English"],
        key="selected_class",
        label_visibility="collapsed",
    )
    st.sidebar.markdown(
        '<div class="tt-tip"><strong>Tip.</strong> Don\'t just trace the marks. Diagnose why the class is stuck — then reteach in 15 minutes.</div>',
        unsafe_allow_html=True,
    )
    return selected


def altair_axis():
    return {
        "labelColor": COLORS["muted"],
        "titleColor": COLORS["muted"],
        "gridColor": COLORS["grid"],
        "domainColor": COLORS["border"],
        "tickColor": COLORS["border"],
        "titleFont": "Inter",
        "labelFont": "Inter",
        "labelFontSize": 11,
        "titleFontSize": 11,
        "titleFontWeight": 600,
    }

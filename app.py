from datetime import datetime

import altair as alt
import pandas as pd
import streamlit as st

from gap_map import render_gap_map
from intervention import generate_intervention_materials
from rag_analysis import analyze_student_answers
from reassessment import evaluate_reassessment

st.set_page_config(
    page_title="TeachTrace AI — Classroom Intelligence",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,650&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
    :root {
        --bg: #090c14;
        --panel: #10151f;
        --card: #161d2b;
        --card-2: #1c2436;
        --line: rgba(255,255,255,.08);
        --text: #eef2ff;
        --muted: #93a0b8;
        --mint: #3ddc97;
        --mint-dim: rgba(61,220,151,.14);
        --blue: #7aa2ff;
        --rose: #ff6b7a;
        --amber: #ffc857;
    }
    html, body, [data-testid="stAppViewContainer"], .stApp {
        background: var(--bg) !important;
        color: var(--text);
        font-family: "Manrope", sans-serif;
    }
    [data-testid="stAppViewContainer"] {
        background:
            radial-gradient(1200px 500px at 10% -10%, rgba(61,220,151,.12), transparent 50%),
            radial-gradient(900px 400px at 100% 0%, rgba(122,162,255,.12), transparent 45%),
            var(--bg) !important;
    }
    [data-testid="stHeader"] { background: transparent !important; }
    #MainMenu, footer, [data-testid="stToolbar"] { visibility: hidden; height: 0; }
    .block-container { padding-top: 1.4rem !important; max-width: 1280px; }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0d121c 0%, #0a0e16 100%) !important;
        border-right: 1px solid var(--line);
    }
    section[data-testid="stSidebar"] .block-container { padding-top: 1.2rem; }

    .brand {
        display: flex; gap: 12px; align-items: center;
        padding: 4px 4px 18px;
    }
    .logo {
        width: 42px; height: 42px; border-radius: 12px;
        background: linear-gradient(135deg, #3ddc97, #2bb4ff);
        color: #062016; font-weight: 800; display: grid; place-items: center;
        letter-spacing: -1px; font-size: 15px;
        box-shadow: 0 8px 24px rgba(61,220,151,.25);
    }
    .brand-name { font-weight: 800; font-size: 16px; letter-spacing: -.3px; }
    .brand-sub { color: var(--muted); font-size: 12px; margin-top: 1px; }

    .mission {
        background: var(--mint-dim);
        border: 1px solid rgba(61,220,151,.22);
        border-radius: 14px;
        padding: 12px 14px;
        color: #c9f7e2;
        font-size: 13px;
        line-height: 1.45;
        margin-top: 8px;
    }

    .hero {
        display: flex; justify-content: space-between; gap: 24px; align-items: flex-end;
        margin-bottom: 22px; flex-wrap: wrap;
    }
    .eyebrow {
        color: var(--mint); font-size: 12px; font-weight: 700;
        letter-spacing: .14em; text-transform: uppercase; margin-bottom: 8px;
    }
    .hero h1, h1 {
        font-family: "Fraunces", serif !important;
        font-weight: 650 !important;
        letter-spacing: -.04em;
        font-size: 2.15rem !important;
        margin: 0 !important;
        color: var(--text) !important;
    }
    .hero-copy, .page-copy {
        color: var(--muted); margin: 8px 0 0 !important; font-size: 15px; max-width: 58ch;
    }
    .hero-pills { display: flex; gap: 10px; flex-wrap: wrap; }
    .pill {
        background: var(--card); border: 1px solid var(--line); border-radius: 14px;
        padding: 10px 14px; min-width: 110px;
    }
    .pill span { display: block; color: var(--muted); font-size: 11px; font-weight: 600; }
    .pill b { font-size: 20px; }
    .pill.warn { border-color: rgba(255,107,122,.28); background: rgba(255,107,122,.08); }

    .kpi-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; margin-bottom: 18px; }
    .kpi {
        background: linear-gradient(180deg, var(--card) 0%, #121826 100%);
        border: 1px solid var(--line);
        border-radius: 18px;
        padding: 16px 18px 18px;
        position: relative;
        overflow: hidden;
    }
    .kpi:before {
        content: ""; position: absolute; inset: auto auto 0 0; height: 3px; width: 46%;
        background: linear-gradient(90deg, var(--mint), transparent);
    }
    .kpi.alert:before { background: linear-gradient(90deg, var(--rose), transparent); width: 70%; }
    .kpi .k { color: var(--muted); font-size: 12px; font-weight: 600; }
    .kpi .v { font-size: 30px; font-weight: 800; letter-spacing: -.04em; margin: 6px 0 4px; }
    .kpi .d { font-size: 12px; color: #9aa8c2; }
    .kpi .d.up { color: var(--mint); }
    .kpi .d.down { color: var(--rose); }

    .panel {
        background: var(--card);
        border: 1px solid var(--line);
        border-radius: 20px;
        padding: 18px 18px 8px;
        height: 100%;
    }
    .panel h3 { margin: 0 0 4px; font-size: 16px; }
    .panel p.sub { color: var(--muted); font-size: 13px; margin: 0 0 12px; }

    .gap-row {
        display: flex; justify-content: space-between; gap: 10px; align-items: center;
        padding: 12px 0; border-bottom: 1px solid var(--line);
    }
    .gap-row:last-child { border-bottom: 0; }
    .chip {
        font-size: 11px; font-weight: 700; padding: 3px 8px; border-radius: 999px;
        letter-spacing: .02em;
    }
    .chip.high { background: rgba(255,107,122,.15); color: #ff8b96; }
    .chip.med { background: rgba(255,200,87,.14); color: #ffd27a; }
    .chip.low { background: var(--mint-dim); color: #7af0bd; }

    .gap-card, .glass, .alert-card, .step-card, .q-card {
        background: var(--card);
        border: 1px solid var(--line);
        border-radius: 18px;
        padding: 18px;
        margin-bottom: 14px;
    }
    .gap-card h3 { font-size: 17px; margin: 10px 0 8px; }
    .gap-card p { color: var(--muted); font-size: 13.5px; line-height: 1.55; margin: 0 0 12px; }
    .gap-top { display: flex; justify-content: space-between; align-items: center; }
    .gap-type { color: var(--muted); font-size: 12px; }
    .gap-meta { display: flex; justify-content: space-between; color: #c5d0e6; font-size: 12px; font-weight: 600; }
    .bar { height: 7px; background: #0e1420; border-radius: 99px; overflow: hidden; margin-top: 8px; }
    .bar i { display: block; height: 100%; border-radius: 99px; }
    .gap-card.high { box-shadow: inset 3px 0 0 var(--rose); }
    .gap-card.med { box-shadow: inset 3px 0 0 var(--amber); }
    .gap-card.low { box-shadow: inset 3px 0 0 var(--mint); }

    .alert-card {
        background: linear-gradient(180deg, rgba(255,200,87,.08), var(--card));
        border-color: rgba(255,200,87,.28);
        margin-top: 8px;
    }
    .alert-kicker { color: var(--amber); font-size: 11px; font-weight: 800; letter-spacing: .12em; text-transform: uppercase; }
    .alert-card h3 { margin: 8px 0; }
    .alert-card .q { color: #dbe4f5; font-style: italic; }
    .alert-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
    .mini-label { color: var(--muted); font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: .08em; margin-bottom: 6px; }

    .step-card { min-height: 150px; }
    .step-n {
        width: 28px; height: 28px; border-radius: 8px; background: var(--mint-dim); color: var(--mint);
        display: grid; place-items: center; font-weight: 800; font-size: 13px; margin-bottom: 10px;
    }

    .q-card { background: #121826; }
    .q-card b { color: var(--blue); }

    .compare {
        display: grid; grid-template-columns: 1fr 1fr; gap: 8px; align-items: end; height: 140px;
        margin: 8px 0 4px;
    }
    .col-bar { background: #223049; border-radius: 10px 10px 4px 4px; }
    .col-bar.post { background: linear-gradient(180deg, #3ddc97, #1f8f63); }

    div[data-testid="stMetric"] {
        background: var(--card); border: 1px solid var(--line); border-radius: 16px; padding: 12px 14px;
    }
    .stButton > button {
        border-radius: 12px !important;
        font-weight: 700 !important;
        border: 1px solid var(--line) !important;
    }
    .stButton > button[kind="primary"] {
        background: linear-gradient(90deg, #2ecf8a, #2aa0ff) !important;
        color: #062016 !important;
        border: 0 !important;
    }
    [data-testid="stFileUploader"] { background: var(--card-2); border-radius: 14px; padding: 8px; }
    textarea, [data-baseweb="textarea"] textarea {
        background: #0e1420 !important; color: var(--text) !important;
    }
    .stDataFrame, [data-testid="stDataFrame"] { border-radius: 16px; overflow: hidden; }

    @media (max-width: 900px) {
        .kpi-grid { grid-template-columns: 1fr 1fr; }
        .alert-grid { grid-template-columns: 1fr; }
    }
</style>
""",
    unsafe_allow_html=True,
)

if "analysis_data" not in st.session_state:
    st.session_state.analysis_data = None
if "intervention_data" not in st.session_state:
    st.session_state.intervention_data = None
if "reassessment_data" not in st.session_state:
    st.session_state.reassessment_data = None

PAGES = [
    "Dashboard",
    "Analyze answers",
    "Learning gap map",
    "Reteaching plans",
    "Reassessment",
]

st.sidebar.markdown(
    """
    <div class="brand">
        <div class="logo">Tt</div>
        <div>
            <div class="brand-name">TeachTrace AI</div>
            <div class="brand-sub">Trace the learning gap</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

selected_view = st.sidebar.radio("Navigate", PAGES, label_visibility="collapsed")
st.sidebar.selectbox(
    "Active class",
    ["Grade 8-A — Mathematics", "Grade 7-B — Science", "Grade 9-A — English"],
    key="selected_class",
)
st.sidebar.markdown(
    '<div class="mission">Don\'t just trace the marks. Diagnose why the class is stuck — then reteach in 15 minutes.</div>',
    unsafe_allow_html=True,
)

hour = datetime.now().hour
greeting = "Good evening" if hour >= 17 else ("Good afternoon" if hour >= 12 else "Good morning")


def ensure_analysis():
    if not st.session_state.analysis_data:
        st.session_state.analysis_data = analyze_student_answers(None, True, "")
    return st.session_state.analysis_data


if selected_view == "Dashboard":
    st.markdown(
        f"""
        <div class="hero">
            <div>
                <div class="eyebrow">{st.session_state.selected_class}</div>
                <h1>{greeting}, Ms. Khan</h1>
                <p class="hero-copy">Fractions is the pressure point this week. 18 students still add denominators directly.</p>
            </div>
            <div class="hero-pills">
                <div class="pill"><span>Today</span><b>Sun 13</b></div>
                <div class="pill warn"><span>Priority</span><b>High</b></div>
            </div>
        </div>
        <div class="kpi-grid">
            <div class="kpi"><div class="k">Total students</div><div class="v">32</div><div class="d">Active enrolled</div></div>
            <div class="kpi"><div class="k">Assessments analyzed</div><div class="v">7</div><div class="d up">+3 this month</div></div>
            <div class="kpi alert"><div class="k">Class performance</div><div class="v">64%</div><div class="d down">-4% vs last test</div></div>
            <div class="kpi alert"><div class="k">Need support</div><div class="v">18/32</div><div class="d down">High priority cluster</div></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    left, right = st.columns([1.55, 1], gap="large")
    with left:
        st.markdown(
            '<div class="panel"><h3>Topic mastery</h3><p class="sub">Average score by unit — red bars are below 50%.</p></div>',
            unsafe_allow_html=True,
        )
        chart_df = pd.DataFrame(
            {
                "Topic": ["Arithmetic", "Fractions", "Algebra", "Geometry", "Word problems"],
                "Score": [78, 42, 68, 59, 53],
            }
        )
        chart = (
            alt.Chart(chart_df)
            .mark_bar(cornerRadiusTopLeft=8, cornerRadiusTopRight=8, size=42)
            .encode(
                x=alt.X("Topic:N", sort=None, title=None, axis=alt.Axis(labelAngle=0, labelColor="#93a0b8")),
                y=alt.Y("Score:Q", title=None, scale=alt.Scale(domain=[0, 100])),
                color=alt.condition(alt.datum.Score < 50, alt.value("#FF6B7A"), alt.value("#3DDC97")),
                tooltip=["Topic", "Score"],
            )
            .properties(height=280)
            .configure_view(strokeWidth=0)
            .configure_axis(gridColor="#1c2436", domainColor="#1c2436", labelColor="#93a0b8", tickColor="#1c2436")
        )
        st.altair_chart(chart, width="stretch")

    with right:
        st.markdown(
            """
            <div class="panel">
                <h3>Urgent gaps</h3>
                <p class="sub">Live from the last fractions paper.</p>
                <div class="gap-row"><div><b>Fractions & denominators</b><br><span class="hero-copy">18 students</span></div><span class="chip high">High</span></div>
                <div class="gap-row"><div><b>Correlation vs causation</b><br><span class="hero-copy">12 students</span></div><span class="chip med">Medium</span></div>
                <div class="gap-row"><div><b>Terminology / vocabulary</b><br><span class="hero-copy">9 students</span></div><span class="chip med">Medium</span></div>
                <div class="gap-row"><div><b>Reasoning steps</b><br><span class="hero-copy">7 students</span></div><span class="chip low">Low</span></div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.caption("Open Learning gap map from the sidebar to inspect evidence and question wording.")

elif selected_view == "Analyze answers":
    st.markdown(
        """
        <div class="hero">
            <div>
                <div class="eyebrow">RAG + linguistic analysis</div>
                <h1>Upload & diagnose</h1>
                <p class="hero-copy">Drop student scripts next to the answer key. TeachTrace reads grammar, vocabulary, reasoning, and misconceptions.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col_up1, col_up2 = st.columns(2, gap="large")
    with col_up1:
        st.markdown('<div class="panel"><h3>Student responses</h3><p class="sub">CSV, PDF, or TXT.</p></div>', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Answer file", type=["csv", "txt", "pdf"], label_visibility="collapsed")
        sample_data = st.checkbox("Use demo class (30 students — fractions test)", value=True)
    with col_up2:
        st.markdown('<div class="panel"><h3>Reference & answer key</h3><p class="sub">Learning objectives the model retrieves against.</p></div>', unsafe_allow_html=True)
        reference_notes = st.text_area(
            "Reference notes",
            value="""Topic: Fraction Addition & Denominators
Core Concept: When adding fractions, students must find a common denominator before adding numerators.
Common Misconception: Adding numerators directly and denominators directly (e.g., 1/2 + 1/3 = 2/5).
Correct Method: 1/2 + 1/3 = 3/6 + 2/6 = 5/6.""",
            height=180,
            label_visibility="collapsed",
        )

    if st.button("Run RAG & linguistic analysis", type="primary", width="stretch"):
        with st.spinner("Reading linguistic patterns, reasoning steps, and misconceptions…"):
            st.session_state.analysis_data = analyze_student_answers(uploaded_file, sample_data, reference_notes)
            st.session_state.intervention_data = None
        st.success("Analysis ready. Open Learning gap map for the class picture.")

    if st.session_state.analysis_data:
        st.markdown("#### Individual diagnostics")
        df_resp = pd.DataFrame(st.session_state.analysis_data["student_responses"])
        st.dataframe(df_resp, width="stretch", hide_index=True)

elif selected_view == "Learning gap map":
    render_gap_map(ensure_analysis())

elif selected_view == "Reteaching plans":
    data = ensure_analysis()
    if not st.session_state.intervention_data:
        st.session_state.intervention_data = generate_intervention_materials(data)
    inter = st.session_state.intervention_data

    st.markdown(
        f"""
        <div class="hero">
            <div>
                <div class="eyebrow">15-minute reteach</div>
                <h1>Intervention studio</h1>
                <p class="hero-copy">Built from the primary gap: <b style="color:#3ddc97">{inter['concept']}</b></p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    s1, s2, s3 = st.columns(3)
    steps = [
        ("01", "Visual area model", "Use pizza / pie charts to show why 1/2 + 1/3 cannot be 2/5 — 2/5 is smaller than 1/2."),
        ("02", "Denominators as units", "1 apple + 1 orange is not 2 apploranges. Convert to a shared unit first."),
        ("03", "Sort & explain", "Students classify same-denominator vs convert-first problems, then justify."),
    ]
    for col, (n, title, body) in zip((s1, s2, s3), steps):
        with col:
            st.markdown(
                f'<div class="step-card"><div class="step-n">{n}</div><h3>{title}</h3><p class="hero-copy">{body}</p></div>',
                unsafe_allow_html=True,
            )

    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.markdown("#### Classroom activity")
        st.markdown(inter["activity_text"])
    with c2:
        st.markdown("#### Misconception check")
        st.markdown(inter["diagnostic_question"])

elif selected_view == "Reassessment":
    ensure_analysis()
    st.markdown(
        """
        <div class="hero">
            <div>
                <div class="eyebrow">Did it work?</div>
                <h1>Reassessment</h1>
                <p class="hero-copy">Three questions aimed only at the fractions denominator gap.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    q1, q2, q3 = st.columns(3)
    questions = [
        ("Q1", "Calculate 2/5 + 1/4. Show every common-denominator step."),
        ("Q2", "Why is 1/3 + 1/3 = 2/3, but 1/3 + 1/2 is not 2/5?"),
        ("Q3", 'Find the mistake in “3/8 + 2/8 = 5/16”.'),
    ]
    for col, (code, text) in zip((q1, q2, q3), questions):
        with col:
            st.markdown(f'<div class="q-card"><b>{code}</b><p>{text}</p></div>', unsafe_allow_html=True)

    if st.button("Process follow-up results", type="primary", width="stretch"):
        st.session_state.reassessment_data = evaluate_reassessment()

    if st.session_state.reassessment_data:
        res = st.session_state.reassessment_data
        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric("Before", f"{res['pre_score']}%")
        with m2:
            st.metric("After", f"{res['post_score']}%", delta=f"+{res['post_score'] - res['pre_score']}%")
        with m3:
            st.metric("Status", "Improved")
        pre_h = int(res["pre_score"] * 1.2)
        post_h = int(res["post_score"] * 1.2)
        st.markdown(
            f"""
            <div class="glass">
                <div class="mini-label">Lift after a 15-minute reteach</div>
                <div class="compare">
                    <div>
                        <div class="col-bar" style="height:{pre_h}px"></div>
                        <div class="mini-label">Pre {res['pre_score']}%</div>
                    </div>
                    <div>
                        <div class="col-bar post" style="height:{post_h}px"></div>
                        <div class="mini-label">Post {res['post_score']}%</div>
                    </div>
                </div>
                <p>Accuracy on fraction addition moved from 43% to 78%. {res['remaining_gaps']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

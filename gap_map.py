import streamlit as st


def _severity_meta(severity: str):
    if severity == "High":
        return "high", "#FF6B7A", "Critical"
    if severity == "Medium":
        return "med", "#FFC857", "Watch"
    return "low", "#3DDC97", "Stable"


def render_gap_map(analysis_data):
    gaps = analysis_data["gaps_summary"]
    high_count = sum(1 for g in gaps if g["severity"] == "High")
    students = analysis_data.get("student_responses", [])
    avg = analysis_data.get("class_average", 64)

    st.markdown(
        f"""
        <div class="hero">
            <div>
                <div class="eyebrow">Classroom intelligence</div>
                <h1>Learning Gap Map</h1>
                <p class="hero-copy">Root causes behind wrong answers — not just who scored low.</p>
            </div>
            <div class="hero-pills">
                <div class="pill"><span>Class average</span><b>{avg}%</b></div>
                <div class="pill warn"><span>Critical gaps</span><b>{high_count}</b></div>
                <div class="pill"><span>Responses</span><b>{len(students) or 30}</b></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns(2)
    for i, gap in enumerate(gaps):
        cls, color, label = _severity_meta(gap["severity"])
        try:
            affected_n = int(str(gap["affected"]).split("/")[0].strip())
        except ValueError:
            affected_n = 0
        pct = min(100, round(affected_n / 30 * 100))
        with cols[i % 2]:
            st.markdown(
                f"""
                <div class="gap-card {cls}">
                    <div class="gap-top">
                        <span class="chip {cls}">{label}</span>
                        <span class="gap-type">{gap['type']}</span>
                    </div>
                    <h3>{gap['concept']}</h3>
                    <p>{gap['evidence']}</p>
                    <div class="gap-meta">
                        <span>{gap['affected']} students</span>
                        <span>{pct}% of class</span>
                    </div>
                    <div class="bar"><i style="width:{pct}%;background:{color}"></i></div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    amb = analysis_data["question_ambiguity"]
    if amb["flagged"]:
        st.markdown(
            f"""
            <div class="alert-card">
                <div class="alert-kicker">Question ambiguity detector</div>
                <h3>This prompt is being misread</h3>
                <p class="q">{amb['question']}</p>
                <div class="alert-grid">
                    <div>
                        <div class="mini-label">What's happening</div>
                        <p>{amb['issue']}</p>
                    </div>
                    <div>
                        <div class="mini-label">Suggested rewrite</div>
                        <p>{amb['recommendation']}</p>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.success("All test questions were clear and unambiguous.")

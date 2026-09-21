import streamlit as st
from pipeline import run_research_pipeline

APP_NAME = "Atlas"
TAGLINE = "Multi-Agent Research System"

st.set_page_config(page_title=f"{APP_NAME} — {TAGLINE}", page_icon="🧭", layout="wide")

# ---------- styling ----------
st.markdown(
    """
    <style>
      :root {
        --atlas-teal: #14B8A6;
        --atlas-amber: #F59E0B;
        --atlas-slate: #1E293B;
        --atlas-muted: #94A3B8;
      }
      .atlas-header {
        display: flex; align-items: baseline; gap: 0.75rem;
        border-bottom: 1px solid rgba(148,163,184,0.2);
        padding-bottom: 0.75rem; margin-bottom: 1.25rem;
      }
      .atlas-title {
        font-size: 2.4rem; font-weight: 700; letter-spacing: -0.02em;
        color: var(--atlas-teal); margin: 0;
      }
      .atlas-tagline { color: var(--atlas-muted); font-size: 1rem; }
      .atlas-pipeline {
        display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1.5rem;
      }
      .atlas-step {
        background: var(--atlas-slate); border-left: 3px solid var(--atlas-teal);
        border-radius: 6px; padding: 0.5rem 0.85rem; font-size: 0.85rem;
        color: #CBD5E1;
      }
      .atlas-step b { color: var(--atlas-amber); }
      div.stButton > button, div.stFormSubmitButton > button {
        background: var(--atlas-teal); color: #042F2E; font-weight: 600;
        border: none; border-radius: 8px;
      }
      div.stButton > button:hover, div.stFormSubmitButton > button:hover {
        background: #0D9488; color: #F0FDFA;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="atlas-header">
      <span class="atlas-title">🧭 {APP_NAME}</span>
      <span class="atlas-tagline">{TAGLINE}</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="atlas-pipeline">
      <div class="atlas-step"><b>1</b> &nbsp;Search agent</div>
      <div class="atlas-step"><b>2</b> &nbsp;Reader agent</div>
      <div class="atlas-step"><b>3</b> &nbsp;Writer</div>
      <div class="atlas-step"><b>4</b> &nbsp;Critic</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- state ----------
if "state" not in st.session_state:
    st.session_state.state = None
if "topic" not in st.session_state:
    st.session_state.topic = ""

# ---------- input ----------
with st.form("research_form"):
    topic = st.text_input(
        "Research topic",
        placeholder="e.g. Impact of AI on renewable energy grids",
    )
    submitted = st.form_submit_button("Run Research", use_container_width=True)

if submitted:
    if not topic.strip():
        st.warning("Please enter a topic first.")
    else:
        st.session_state.topic = topic
        status = st.empty()
        status.info("Agents are working — search → read → write → critique. This can take a minute.")
        try:
            with st.spinner("Running pipeline..."):
                st.session_state.state = run_research_pipeline(topic)
            status.empty()
            st.success("Research complete.")
        except Exception as e:
            status.empty()
            st.error(f"Pipeline failed: {e}")
            st.session_state.state = None

# ---------- output ----------
state = st.session_state.state

if state:
    tab_report, tab_feedback, tab_search, tab_scraped = st.tabs(
        ["📄 Report", "🧐 Critique", "🌐 Sources", "📃 Scraped Content"]
    )

    with tab_report:
        st.markdown(state.get("report", "_No report generated._"))
        st.download_button(
            "Download report (.md)",
            data=state.get("report", ""),
            file_name=f"atlas_{st.session_state.topic.replace(' ', '_')[:40]}.md",
            mime="text/markdown",
        )

    with tab_feedback:
        st.markdown(state.get("feedback", "_No feedback generated._"))

    with tab_search:
        st.text(state.get("search_results", "No search results."))

    with tab_scraped:
        st.text(state.get("scraped_content", "No scraped content."))
else:
    st.info("Enter a topic above and click **Run Research** to start.")
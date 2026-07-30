"""
Lecture 12 Exercise — Extend the Dashboard with a Third Page
=============================================================
Run with: streamlit run app.py

STARTER CODE: this folder contains the complete 2-page dashboard built in
class (app.py, utils.py, pages/01, pages/02). Pages 1 and 2 are unmodified —
the third page below adds the next level of the BBD squiggle:

    pages/03_demand.py  →  "Where is guest demand strongest?"

market summary (p1) → neighbourhood story (p2) → demand drill-down (p3).
"""

import streamlit as st

# Page config + CSS — applied ONCE here; app.py runs on every page switch
st.set_page_config(page_title="London Airbnb Analytics", page_icon="🏠",
                   layout="wide", initial_sidebar_state="expanded")


# ─────────────────────────────────────────────────────────────────────────────
# Navigation — all three pages registered
# ─────────────────────────────────────────────────────────────────────────────
pg = st.navigation([
    st.Page("pages/01_market.py",
            title="What does a night in London cost?",   icon="🏠"),
    st.Page("pages/02_drilldown.py",
            title="Which neighbourhoods drive the premium?", icon="📍"),
    st.Page("pages/03_demand.py",
            title="Where is guest demand strongest?", icon="🔥"),
])
pg.run()

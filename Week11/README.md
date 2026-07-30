# Week 11 — Multi-Page & Multi-Tab Streamlit App (Gapminder)

A 3-page Streamlit dashboard built on Plotly's built-in Gapminder dataset, following the
BBD "squiggle" structure — summary → trend → detail.

## Structure
```
app.py              ← entry point, defines navigation
utils.py            ← @st.cache_data data loading — shared across all pages
pages/
  01_overview.py     ← "How do countries compare today?"  (summary snapshot)
  02_trends.py       ← "How has life expectancy changed?"  (trend over time)
  03_compare.py      ← "What explains the differences?"    (country drill-down)
requirements.txt
```

## Run it
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Checklist
- [x] Page titles are questions, not topic labels
- [x] 3 pages = summary → trend → detail (the squiggle)
- [x] `utils.py` with `@st.cache_data`
- [x] `st.session_state` used (page 3 — persists highlighted country across tabs)
- [x] `st.tabs()` used (page 3 — GDP vs Life Expectancy / Continent comparison)
- [x] Colour type named in a comment on each chart (categorical vs. highlight)

# Week 12 — Dashboard Design & Polish (London Airbnb)

A 3-page Streamlit dashboard on the Inside Airbnb London dataset, following the
BBD "squiggle": market summary → neighbourhood story → demand drill-down.

Pages 1 and 2 were the starter code built in lecture (unmodified). **Page 3 —
`pages/03_demand.py` — is the exercise deliverable**, completed from the stub.

## Structure
```
app.py                   ← entry point, 3-page navigation + page config
utils.py                 ← @st.cache_data loader, shared sidebar filters
airbnb_london.csv
requirements.txt
pages/
  01_market.py            ← "What does a night in London cost?"      (market summary)
  02_drilldown.py          ← "Which neighbourhoods drive the premium?" (neighbourhood story)
  03_demand.py             ← "Where is guest demand strongest?"       (demand drill-down — NEW)
```

## Run it
```bash
pip install -r requirements.txt
streamlit run app.py
```

## What page 3 does
- Calls the shared `sidebar_filters()` — same room type / neighbourhood / price
  filters as pages 1 and 2, carried straight over.
- Adds its own persisted widget: a room-type focus (`st.radio`, `key='sel_room'`),
  kept alive across page switches with a guard in case the sidebar filters
  remove the previously selected room type.
- KPI row: listings, median reviews/month vs. the filtered market, median price
  for the focused room type.
- One `px.scatter` of price vs. reviews/month (reviews as the demand proxy),
  highlight column (blue = focused room type, grey = everything else) —
  no red/green, no pies, no packed bubbles.

## BBD checklist
- [x] Page title is a question, not a topic label
- [x] Registered in `app.py` navigation with an icon
- [x] `sidebar_filters()` called at the top — shared filters persist
- [x] Own widget persisted (keep-alive + guard for filtered-out values)
- [x] Colour type named in a comment (highlight: blue vs grey)
- [x] No red/green as only differentiator, no pies, no packed bubbles
- [x] KPI row passes the 5-second test
- [x] Insight title on the chart, white background, Arial

## Note
The starter `utils.py` hard-coded an absolute Windows path
(`C:\Users\Sakshit\Desktop\...`) to load the CSV — that only works on that one
machine. Fixed here to build the path relative to `utils.py` itself, so it runs
on any machine (and on Streamlit Community Cloud) as long as `airbnb_london.csv`
sits alongside it.

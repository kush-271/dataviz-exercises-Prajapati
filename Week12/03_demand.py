# pages/03_demand.py — demand drill-down (BBD squiggle level 3: demand story)
import streamlit as st
import plotly.express as px
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from utils import load_data, sidebar_filters

# ─────────────────────────────────────────────────────────────────────────────
# Load data + shared sidebar — same filters as pages 1 and 2, carried over
# ─────────────────────────────────────────────────────────────────────────────
df, p95 = load_data()
filtered = sidebar_filters(df, p95)

st.title('Where is guest demand strongest?')
st.caption('Reviews per month as a proxy for booking demand — '
           'from the neighbourhood story to a room-type focus')

# ─────────────────────────────────────────────────────────────────────────────
# A persisted widget of our own: focus on one room type
# initialise once, keep alive across pages, guard against a value the
# sidebar filters may have removed
# ─────────────────────────────────────────────────────────────────────────────
room_types_avail = sorted(filtered['room_type'].unique())

if 'sel_room' not in st.session_state:
    st.session_state.sel_room = room_types_avail[0]
st.session_state.sel_room = st.session_state.sel_room   # keep alive across pages

if st.session_state.sel_room not in room_types_avail:    # guard: filters may have
    st.session_state.sel_room = room_types_avail[0]      # removed the saved choice

st.radio('Focus on a room type', room_types_avail, key='sel_room', horizontal=True)
room = st.session_state.sel_room
room_df = filtered[filtered['room_type'] == room]

# ─────────────────────────────────────────────────────────────────────────────
# KPI row — 5-second test: the metrics alone should answer the question
# ─────────────────────────────────────────────────────────────────────────────
k1, k2, k3 = st.columns(3)
k1.metric('Listings', f'{len(room_df):,}')
k2.metric('Median Reviews/Month', f"{room_df['reviews_per_month'].median():.2f}",
          f"{room_df['reviews_per_month'].median()-filtered['reviews_per_month'].median():+.2f} "
          'vs filtered market')
k3.metric('Median Price', f"£{room_df['price'].median():.0f}/night")

st.divider()

# ─────────────────────────────────────────────────────────────────────────────
# One chart — demand story: price vs reviews/month, focused room type
# highlighted against the rest of the filtered market
# BBD HIGHLIGHT colour: blue for the focused room type, grey for everything else
# BBD CVD: blue vs grey — no red-green combination, no pies, no packed bubbles
# ─────────────────────────────────────────────────────────────────────────────
plot_df = filtered.copy()
plot_df['highlight'] = plot_df['room_type'].apply(
    lambda r: room if r == room else 'Other room types')

fig = px.scatter(
    plot_df, x='price', y='reviews_per_month', color='highlight',
    color_discrete_map={room: '#2E75B6', 'Other room types': '#AAAAAA'},
    category_orders={'highlight': ['Other room types', room]},  # focused drawn on top
    labels={'price': 'Nightly Price (£)', 'reviews_per_month': 'Reviews per Month'},
    title=f'{room} listings get booked just as often as everything else — '
          f'demand doesn\u2019t track with price',
    height=600
)
fig.update_traces(marker=dict(size=8, opacity=0.7, line=dict(width=0)))
fig.update_layout(plot_bgcolor='white', paper_bgcolor='white',
                  font=dict(family='Arial', size=12),
                  xaxis=dict(gridcolor='#EEEEEE'),
                  yaxis=dict(gridcolor='#EEEEEE'),
                  legend=dict(orientation='h', y=1.08, title=''))
st.plotly_chart(fig, use_container_width=True)

# TEST: pick a room type, switch to page 1, change a filter,
# come back — both the filters AND the room-type focus must be where you left them.

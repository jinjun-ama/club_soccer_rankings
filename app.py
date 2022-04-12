import pandas as pd
import streamlit as st
import plotly_express as px

df = pd.read_csv("club_soccer_rankings.csv")

# filter only top 25 teams by avg. ratings
df = df.loc[df.team.isin(df.groupby(['team']).agg({'rating':'mean'}).reset_index().sort_values('rating',ascending=False).head(25)['team'].tolist())]

st.title("Global Soccer Club Rankings Overtime")

fig = px.line(
  df, x="data", y="rating", color="team", render_mode="svg", line_shape="spline"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown('[Data Credit: FiveThirtyEight Global Soccer Club Rankings](https://projects.fivethirtyeight.com/soccer-predictions/global-club-rankings/)')

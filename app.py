import os
import pandas as pd
import streamlit as st

DATA_URL = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-04-20/netflix_titles.csv"
LOCAL_PATH = os.path.join("data", "netflix_titles.csv")

st.set_page_config(page_title="Netflix Data Analysis", page_icon="🎬", layout="wide")

@st.cache_data
def load_data():
    if os.path.exists(LOCAL_PATH):
        return pd.read_csv(LOCAL_PATH)
    return pd.read_csv(DATA_URL)

df = load_data()
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
df["added_year"] = df["date_added"].dt.year
df["movie_minutes"] = pd.to_numeric(df["duration"].str.extract(r"(\d+)")[0], errors="coerce")

st.title("🎬 Netflix Data Analysis Dashboard")
st.caption("Exploratory analysis of Netflix movies and TV shows")

st.sidebar.header("Filters")

types = st.sidebar.multiselect(
    "Content Type",
    sorted(df["type"].dropna().unique()),
    default=sorted(df["type"].dropna().unique())
)

ratings = sorted(df["rating"].dropna().unique())
selected_ratings = st.sidebar.multiselect("Rating", ratings, default=[])

min_year = int(df["release_year"].min())
max_year = int(df["release_year"].max())
year_range = st.sidebar.slider("Release Year", min_year, max_year, (min_year, max_year))

filtered = df[
    df["type"].isin(types)
    & df["release_year"].between(year_range[0], year_range[1])
]

if selected_ratings:
    filtered = filtered[filtered["rating"].isin(selected_ratings)]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Titles", f"{len(filtered):,}")
c2.metric("Movies", f"{(filtered['type'] == 'Movie').sum():,}")
c3.metric("TV Shows", f"{(filtered['type'] == 'TV Show').sum():,}")
c4.metric("Unique Release Years", f"{filtered['release_year'].nunique():,}")

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Content Type")
    st.bar_chart(filtered["type"].value_counts())

with right:
    st.subheader("Titles by Release Year")
    st.line_chart(filtered["release_year"].value_counts().sort_index())

st.subheader("Top Countries")
countries = (
    filtered["country"].dropna()
    .str.split(", ")
    .explode()
    .value_counts()
    .head(10)
)
st.bar_chart(countries)

st.subheader("Top Genres")
genres = (
    filtered["listed_in"].dropna()
    .str.split(", ")
    .explode()
    .value_counts()
    .head(10)
)
st.bar_chart(genres)

st.subheader("Explore Titles")
show_cols = ["title", "type", "release_year", "rating", "country", "duration"]
st.dataframe(
    filtered[show_cols].sort_values("release_year", ascending=False).head(100),
    use_container_width=True,
    hide_index=True
)

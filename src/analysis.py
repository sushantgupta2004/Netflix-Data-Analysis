import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATA_URL = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-04-20/netflix_titles.csv"
LOCAL_PATH = os.path.join("data", "netflix_titles.csv")
FIG_DIR = "figures"

os.makedirs(FIG_DIR, exist_ok=True)

def load_data():
    if os.path.exists(LOCAL_PATH):
        return pd.read_csv(LOCAL_PATH)
    return pd.read_csv(DATA_URL)

def clean_data(df):
    df = df.copy()
    df = df.drop_duplicates()

    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
    df["added_year"] = df["date_added"].dt.year
    df["added_month"] = df["date_added"].dt.month_name()

    # Numeric movie duration
    df["movie_minutes"] = pd.to_numeric(
        df["duration"].str.extract(r"(\d+)")[0], errors="coerce"
    )

    # Numeric TV seasons
    df["seasons"] = pd.to_numeric(
        df["duration"].str.extract(r"(\d+)")[0], errors="coerce"
    )

    return df

def save_chart(fig, filename):
    fig.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, filename), dpi=150, bbox_inches="tight")
    plt.close(fig)

def main():
    df = clean_data(load_data())

    print("Rows:", len(df))
    print("Columns:", len(df.columns))
    print("\nContent type:\n", df["type"].value_counts())
    print("\nMissing values:\n", df.isna().sum().sort_values(ascending=False).head(10))

    # 1. Content type
    counts = df["type"].value_counts()
    fig, ax = plt.subplots(figsize=(7, 5))
    counts.plot(kind="bar", ax=ax)
    ax.set_title("Netflix Content: Movies vs TV Shows")
    ax.set_xlabel("Content Type")
    ax.set_ylabel("Number of Titles")
    save_chart(fig, "01_content_type.png")

    # 2. Titles added by year
    yearly = df["added_year"].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(9, 5))
    yearly.plot(kind="line", marker="o", ax=ax)
    ax.set_title("Netflix Titles Added by Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Titles Added")
    save_chart(fig, "02_titles_added_by_year.png")

    # 3. Top countries
    country = (
        df["country"].dropna()
        .str.split(", ")
        .explode()
        .value_counts()
        .head(10)
    )
    fig, ax = plt.subplots(figsize=(9, 5))
    country.sort_values().plot(kind="barh", ax=ax)
    ax.set_title("Top 10 Countries by Netflix Titles")
    ax.set_xlabel("Titles")
    save_chart(fig, "03_top_countries.png")

    # 4. Ratings
    rating = df["rating"].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(9, 5))
    rating.sort_values().plot(kind="barh", ax=ax)
    ax.set_title("Most Common Netflix Ratings")
    ax.set_xlabel("Titles")
    save_chart(fig, "04_ratings.png")

    # 5. Genres
    genres = (
        df["listed_in"].dropna()
        .str.split(", ")
        .explode()
        .value_counts()
        .head(10)
    )
    fig, ax = plt.subplots(figsize=(9, 5))
    genres.sort_values().plot(kind="barh", ax=ax)
    ax.set_title("Top 10 Genres")
    ax.set_xlabel("Titles")
    save_chart(fig, "05_top_genres.png")

    # 6. Release year trend
    release = df["release_year"].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(9, 5))
    release.plot(ax=ax)
    ax.set_title("Netflix Titles by Release Year")
    ax.set_xlabel("Release Year")
    ax.set_ylabel("Titles")
    save_chart(fig, "06_release_year_trend.png")

    # 7. Movie duration
    movies = df[df["type"].eq("Movie")]["movie_minutes"].dropna()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(movies, bins=30)
    ax.set_title("Movie Duration Distribution")
    ax.set_xlabel("Minutes")
    ax.set_ylabel("Number of Movies")
    save_chart(fig, "07_movie_duration.png")

    # 8. TV seasons
    shows = df[df["type"].eq("TV Show")]["seasons"].dropna()
    fig, ax = plt.subplots(figsize=(8, 5))
    shows.value_counts().sort_index().head(10).plot(kind="bar", ax=ax)
    ax.set_title("TV Shows by Number of Seasons")
    ax.set_xlabel("Seasons")
    ax.set_ylabel("Shows")
    save_chart(fig, "08_tv_seasons.png")

    print("\nAnalysis complete. Charts saved to:", FIG_DIR)

if __name__ == "__main__":
    main()

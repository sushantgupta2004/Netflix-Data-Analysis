# 🎬 Netflix Data Analysis — Python, SQL & Streamlit

An end-to-end portfolio project analyzing Netflix movies and TV shows using **Python, Pandas, Matplotlib, SQL, and Streamlit**.

## 📌 Project Objective

The goal is to explore Netflix's content catalogue and answer practical business questions such as:

- How is the catalogue divided between Movies and TV Shows?
- How has Netflix content changed over the years?
- Which countries contribute the most titles?
- Which ratings are most common?
- What are the most common genres?
- How does movie duration vary?
- How many TV shows have multiple seasons?
- Which months see the most content additions?

## 🛠️ Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- SQL / MySQL
- Streamlit
- Jupyter Notebook

## 📂 Project Structure

```text
Netflix_Data_Analysis_Project/
│
├── data/
│   └── README.md
│
├── figures/
│   └── .gitkeep
│
├── notebooks/
│   └── Netflix_Data_Analysis.ipynb
│
├── sql/
│   └── netflix_analysis.sql
│
├── src/
│   └── analysis.py
│
├── app.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## 📊 Dataset

The project uses the public **Netflix Movies and TV Shows** dataset distributed through the TidyTuesday project. The notebook loads the CSV directly from the public raw-data URL, so the dataset does not need to be committed to this repository.

Dataset reference:
https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-04-20/netflix_titles.csv

The dataset contains fields such as title, content type, director, cast, country, date added, release year, rating, duration, genres and description.

## 🔍 Analysis Performed

### 1. Data Cleaning
- Checked missing values
- Removed duplicate records
- Converted `date_added` to datetime
- Extracted month and year from `date_added`
- Parsed numeric movie duration
- Parsed TV-show season counts

### 2. Exploratory Data Analysis
- Movie vs TV Show distribution
- Titles added by year
- Top content-producing countries
- Rating distribution
- Top genres
- Release-year trend
- Movie-duration distribution
- TV-show season distribution
- Monthly content additions
- Top directors

### 3. SQL Analysis
The SQL folder contains MySQL-compatible business questions and queries for:
- Content-type distribution
- Year-wise title counts
- Top countries
- Rating analysis
- Longest movies
- Multi-season TV shows
- Genre-related analysis

### 4. Streamlit Dashboard
Run:

```bash
pip install -r requirements.txt
streamlit run app.py
```

The dashboard includes filters for content type, release year and rating, plus summary KPIs and charts.

## 🚀 Run the Project

### Option 1 — Jupyter Notebook

```bash
pip install -r requirements.txt
jupyter notebook
```

Open:

```text
notebooks/Netflix_Data_Analysis.ipynb
```

### Option 2 — Python Script

```bash
python src/analysis.py
```

Charts will be generated inside the `figures/` folder.

### Option 3 — Streamlit

```bash
streamlit run app.py
```

## 💼 Business Value

This project demonstrates how a data analyst can turn raw catalogue data into business-oriented insights around:

- Content strategy
- Regional content distribution
- Audience segmentation
- Content mix
- Release trends
- Catalogue planning

## 👨‍💻 Skills Demonstrated

**Python | Pandas | NumPy | Matplotlib | SQL | MySQL | EDA | Data Cleaning | Data Visualization | Streamlit | Business Analysis**

## 📌 Portfolio Note

This is an educational portfolio project based on a public dataset. Netflix branding and the dataset are used only for analysis/learning purposes.

## 👤 Author

**Sushant Gupta**

BCA Graduate | Data Analytics / Business Analytics

LinkedIn: Add your LinkedIn URL  
GitHub: Add your GitHub URL

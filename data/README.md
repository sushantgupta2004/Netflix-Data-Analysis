# Dataset

The notebook and application load the public Netflix dataset directly from:

https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-04-20/netflix_titles.csv

The raw CSV is intentionally not duplicated in this repository. This keeps the GitHub repository lightweight and makes the source explicit.

If you want a local copy, download the CSV and save it as:

`data/netflix_titles.csv`

The analysis code will use the local file if it exists; otherwise it loads the public source URL.

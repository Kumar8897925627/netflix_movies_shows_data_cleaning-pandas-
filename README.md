# netflix_movies_shows_data_cleaning-pandas-
Designed and implemented SQL queries to analyze large-scale Amazon sales datasets for insights into product performance, customer trends, and revenue patterns. 
# 🎬 Netflix Movies and TV Shows — Data Cleaning & Analysis (Pandas Project)

This project focuses on cleaning and preparing the *Netflix Titles dataset* from [Kaggle](https://www.kaggle.com/shivamb/netflix-shows) for further analysis.

---

## 📊 Dataset Overview
The dataset contains metadata about movies and TV shows available on Netflix, including:
- show_id
- type (Movie or TV Show)
- title
- director, cast, country
- date_added, release_year, rating
- duration
- listed_in (genre/category)
- description

---

## 🧹 Data Cleaning Performed
- Removed or handled *missing values* in date_added, rating, duration, and other columns  
- Converted date_added into proper *datetime* format  
- Standardized duration (minutes/seasons) into separate numeric columns  
- Cleaned string formatting and stripped unnecessary whitespace  
- Extracted year_added and month_added for analysis  
- Ensured the dataset is ready for *visualization and reporting*

---

## 🛠 Tech Stack
- *Python 3.x*
- *Pandas*
- *VS Code*

---

## 📈 Future Scope
- Perform Exploratory Data Analysis (EDA)
- Visualize trends like most popular genres, release trends by year, etc.
- Build dashboards using Power BI / Tableau

---

## 📂 Files in this Repository
| File Name | Description |
|------------|--------------|
| netflix_titles.csv | Raw dataset from Kaggle |
| clean_netflix_data.py | Python script for data cleaning |
| cleaned_netflix.csv | Cleaned dataset output |
| README.md | Project documentation |

---

## 🧑‍💻 Author
*Kumar Saripalli*  
📧 Feel free to connect for collaboration or feedback!

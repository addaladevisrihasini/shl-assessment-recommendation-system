# SHL Assessment Recommendation Engine

## Problem Statement
Recruiters often struggle to choose the most relevant assessments from a large catalog based on job roles and required skills.
The objective of this project is to build a recommendation system that suggests suitable SHL assessments given a recruiter’s
skill requirements or job description.


## Solution Overview
This project implements a content-based recommendation engine using Natural Language Processing (NLP).
It analyzes SHL’s assessment catalog and matches it with user queries using text similarity techniques.


## Key Features
- Converts SHL assessment data from Excel to CSV
- Preprocesses assessment text data
- Uses TF-IDF vectorization for text representation
- Computes cosine similarity to rank relevant assessments
- Returns top matching assessments for a given query


## Recommendation Approach
1. All assessment attributes are combined into a single text field
2. TF-IDF is applied to convert text into numerical vectors
3. Cosine similarity measures relevance between query and assessments
4. Top matching assessments are returned



## Project Structure


shl-assessment-recommendation-system/
├── api/ - FastAPI service (optional)

├── crawler/ - SHL catalog scraping script

├── data/ - Dataset and preprocessing scripts

├── recommender/ - Recommendation logic

├── requirements.txt - Python dependencies

├── README.md

## How to Run the Project

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Convert Excel Dataset to CSV
```bash
python3 data/convert_excel.py
```

### 3. Run Recommendation Engine
```bash
python3 recommender/recommend.py
```

## Sample Query
```bash
python data science entry level
```


## Technologies Used
- Python
- Pandas
- Scikit-learn
- FastAPI


## Frontend 
A minimal Streamlit-based frontend is provided to demonstrate interactive querying of the assessment recommendation engine.
The UI allows users to enter skill or job-role queries and view recommended assessments with clickable URLs.

### Run Frontend Locally
```bash
streamlit run app.py
```


### WEB APPLICATION URL
```bash
https://github.com/addaladevisrihasini/shl-assessment-recommendation-system
```


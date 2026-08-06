# Banking Risk Analytics

## Overview

Banking Risk Analytics is an end-to-end data analytics project built to analyze customer data, generate business insights, and predict whether a customer is likely to subscribe to a term deposit.

The project combines SQL, MongoDB, Machine Learning, and Streamlit into a single workflow. It starts with raw banking data, stores it in databases, performs business analysis, trains machine learning models, and finally presents the results through an interactive dashboard.

The main objective of this project is to demonstrate how different data technologies can be integrated to solve a real-world business problem.

---

## Problem Statement

Banks run marketing campaigns to encourage customers to subscribe to term deposits. However, contacting every customer is expensive and inefficient.

Using historical customer data, this project analyzes customer characteristics and builds a prediction model that helps identify customers who are more likely to subscribe. This allows marketing efforts to be more focused and cost-effective.

---

## Features

- Import and process raw banking data
- Store customer records in SQLite
- Perform SQL-based business analysis
- Generate Excel reports
- Import data into MongoDB
- Execute MongoDB aggregation queries
- Train multiple Machine Learning models
- Predict customer subscription using the best-performing model
- Interactive Streamlit dashboard for visualization and analysis

---

## Technologies Used

- Python
- Pandas
- NumPy
- SQLite
- SQL
- MongoDB
- Scikit-learn
- Streamlit
- Plotly
- OpenPyXL
- Joblib
- Git
- GitHub

---

## Project Structure

```
BankingRiskAnalytics/

├── data/
│   └── raw/
│       └── bank-full.csv
│
├── excel/
│   └── Banking_Report.xlsx
│
├── models/
│   └── saved_models/
│       └── best_model.pkl
│
├── python/
│   ├── create_database.py
│   ├── sql_queries.py
│   ├── advanced_sql.py
│   ├── window_functions.py
│   ├── export_excel.py
│   ├── mongodb_import.py
│   ├── mongodb_queries.py
│   └── machine_learning.py
│
├── streamlit/
│   ├── app.py
│   └── pages/
│
├── requirements.txt
├── banking.db
└── README.md
```

---

## Dataset

The project uses the **Bank Marketing Dataset**, which contains customer information collected during direct marketing campaigns conducted by a Portuguese banking institution.

The dataset includes customer demographics, financial information, campaign details, and whether the customer subscribed to a term deposit.

Target Variable:

```
y
```

Possible values:

```
yes
no
```

---

## Workflow

### 1. Data Loading

The raw CSV dataset is loaded using Pandas.

### 2. Database Creation

The dataset is stored inside an SQLite database to perform SQL analysis.

### 3. SQL Analytics

Several SQL queries are executed to answer business questions such as:

- Customer distribution by job
- Education analysis
- Marital status analysis
- Loan analysis
- Customer counts

### 4. Excel Report Generation

Business reports are exported to Excel for easier reporting.

### 5. MongoDB

The same dataset is imported into MongoDB to demonstrate NoSQL operations and aggregation queries.

### 6. Machine Learning

The dataset is preprocessed before training multiple classification models.

Models used:

- Logistic Regression
- Decision Tree
- Random Forest

The best-performing model is saved using Joblib.

### 7. Streamlit Dashboard

The trained model is integrated into a Streamlit dashboard that provides:

- Dataset exploration
- SQL analytics
- Business dashboards
- Customer prediction
- Interactive visualizations

---

## Machine Learning Pipeline

1. Load dataset
2. Data preprocessing
3. Encode categorical variables
4. Split into training and testing data
5. Train multiple models
6. Compare model performance
7. Save the best model
8. Use the saved model for prediction

---

## Dashboard Pages

### Home

Overview of the project and key performance indicators.

### Dataset Explorer

Search, filter, and download customer data.

### SQL Analytics

Visualizations generated from SQL queries.

### Machine Learning

Business dashboards and model insights.

### Prediction

Predict whether a customer is likely to subscribe to a term deposit.

---

## How to Run

Clone the repository

```bash
git clone https://github.com/ganeshkukkala7615/BankingRiskAnalytics.git
```

Move into the project directory

```bash
cd BankingRiskAnalytics
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run streamlit/app.py
```

---

## Skills Demonstrated

- Data Cleaning
- Data Analysis
- SQL Query Writing
- SQLite
- MongoDB
- Machine Learning
- Model Deployment
- Data Visualization
- Dashboard Development
- Git Version Control

---

## Future Improvements

- Deploy the dashboard online
- Add user authentication
- Connect to a live banking database
- Add more machine learning algorithms
- Improve model explainability using SHAP
- Create automated reporting

---

## Author

**Ganesh Kukkala**

B.Tech, Electrical Engineering

Indian Institute of Technology Madras

GitHub:
https://github.com/ganeshkukkala7615

---

## License

This project is released under the MIT License.
 
 

# Churn Prediction Project

## Overview
This project performs a comprehensive data analysis and predictive modeling task on a customer churn dataset. The objective is to understand the customer behavior patterns that lead to churn and build a machine learning model that can predict if a customer is likely to leave the service.

## Dataset Description
The dataset includes customer-level information from a telecom company, such as:

Demographics (gender, senior citizen status)

Service details (internet, phone, streaming)

Account information (contract type, monthly charges, tenure)

Churn label (Yes/No)

## Tools and Libraries Used
- Python

- Pandas

- NumPy

- Matplotlib

- Seaborn

- Scikit-learn

## Steps Performed
- Data Inspection

- Loaded dataset using Pandas

- Used .info() and .describe() to understand structure and statistics

- Identified null values and data types

- Data Cleaning

- Handled missing values in the TotalCharges column

- Converted non-numeric types to numeric

- Removed unnecessary rows and columns

- Feature Engineering

- Encoded categorical features

- Split data into features and labels

- Scaled numerical columns if needed

- Model Building

- Hyperparameter tuning

- Applied classification models such as logistic regression

- Used train-test split for evaluation

- Measured performance with accuracy, precision, recall

## Insights

- Customers with longer contracts are less likely to churn

- Higher monthly charges often correlate with churn

- Majority of customers who are about to churn have used services for up to 18 months.

## Conclusion
The project demonstrates a typical churn prediction pipeline including data preprocessing, feature engineering, and model training. The insights and model can help telecom providers proactively retain customers.

## Author
Tajwinder Singh

## Linkedin
Tajwinder (Taj) Singh


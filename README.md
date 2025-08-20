# Customer Churn Prediction Project

## Overview
This project analyzes customer behavior and predicts churn for a telecom company. It includes data preprocessing, feature engineering, machine learning modeling, and a Flask-based web application deployed on AWS Elastic Beanstalk for real-time predictions.

## Dataset Description
The dataset includes customer-level information such as:

- **Demographics:** gender, senior citizen status  
- **Service details:** internet, phone, streaming  
- **Account information:** contract type, monthly charges, tenure  
- **Churn label:** Yes/No  

## Tools and Libraries Used
- Python 3.12  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scikit-learn 1.7.1  
- Flask  
- Gunicorn  
- AWS Elastic Beanstalk  

## Steps Performed

### 1. Data Inspection
- Loaded dataset using Pandas  
- Explored data with `.info()` and `.describe()`  
- Identified missing values and data types  

### 2. Data Cleaning
- Handled missing values in `TotalCharges`  
- Converted non-numeric columns to numeric where necessary  
- Removed unnecessary rows/columns  

### 3. Feature Engineering
- Encoded categorical features  
- Split data into features and target (churn label)  
- Scaled numerical columns when needed  

### 4. Model Building
- Applied classification models such as Logistic Regression  
- Hyperparameter tuning to optimize performance  
- Used train-test split for evaluation  
- Measured performance using accuracy, precision, recall  

### 5. Key Insights
- Customers with longer contracts are less likely to churn  
- Higher monthly charges correlate with churn  
- Majority of customers who churned had tenure up to 18 months  

### 6. Web App Deployment
- Created `app.py` using Flask to serve the churn prediction model  
- Saved preprocessing objects and trained model as pickles (e.g., `ct_ohe.pickle`, `standard_scaler.pickle`, `best_model.pickle`) using **Scikit-learn 1.7.1**  
- Created `requirements.txt` for dependencies  
- Added `Procfile` for Gunicorn: web: gunicorn app:application
- Initialized AWS Elastic Beanstalk environment:  
- Platform: Python 3.12 running on 64bit Amazon Linux 2023  
- Region: ap-south-1  
- Deployed using `eb init`, `eb create`, and `eb deploy`  
- Verified the EB URL and tested endpoints  

## Deployment Instructions for Future Users  
1. Clone the repository.  
2. Install dependencies:  
   pip install -r requirements.txt
3. Initialize Elastic Beanstalk:
   eb init

Choose Python 3.12 on 64bit Amazon Linux 2023
Choose your region (ap-south-1)

4. Create the environment and deploy:
   eb create <environment-name>
   eb deploy

5. Access the app using the provided EB URL.

## Author
Tajwinder Singh

## LinkedIn
https://www.linkedin.com/in/tajwinder-singh-?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BDuXVqgdxTaycCeffmt54iw%3D%3D
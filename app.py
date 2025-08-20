from flask import Flask, render_template, request, url_for
import pandas as pd
import numpy as np 
import pickle

with open("ct_ohe.pickle", "rb") as f:
    ohe =  pickle.load(f)

with open("standard_scaler.pickle", "rb") as f:
    scaler =  pickle.load(f)

with open("best_model.pickle", "rb") as f:
    best_model =  pickle.load(f)


skewedFeatures = ['tenure', 'MonthlyCharges', 'TotalCharges']

app = Flask(__name__)
application = app

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    data = request.form
    X_test = pd.DataFrame([{
        "gender": data["gender"],
        "SeniorCitizen": data["SeniorCitizen"],
        "Partner": data["Partner"],
        "Dependents": data["Dependents"],
        "tenure": int(data["tenure"]),
        "PhoneService": data["PhoneService"],
        "MultipleLines": data["MultipleLines"],
        "InternetService": data["InternetService"],
        "OnlineSecurity": data["OnlineSecurity"],
        "OnlineBackup": data["OnlineBackup"],
        "DeviceProtection": data["DeviceProtection"],
        "TechSupport": data["TechSupport"],
        "StreamingTV": data["StreamingTV"],
        "StreamingMovies": data["StreamingMovies"],
        "Contract": data["Contract"],
        "PaperlessBilling": data["PaperlessBilling"],
        "PaymentMethod": data["PaymentMethod"],
        "MonthlyCharges": float(data["MonthlyCharges"]),
        "TotalCharges": float(data["TotalCharges"])
    }])
    
    X_test_log = X_test.copy()
    for feature in skewedFeatures:
        X_test_log[feature] = np.log1p(X_test_log[feature])

    X_test_encoded = ohe.transform(X_test_log)
    X_test_scaled = scaler.transform(X_test_encoded)
    predicted_prob = best_model.predict_proba(X_test_scaled)[:, 1][0]
    if (predicted_prob > 0.46):
        return "The customer will churn."

    else:
        return "The customer will not churn."

if __name__== "__main__":
    app.run(debug=True)




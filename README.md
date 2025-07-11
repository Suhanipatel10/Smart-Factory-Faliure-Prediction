# Smart Factory Filure Prediction

⚙️ Smart Factory Failure Predictor (Streamlit App)
A simple and intelligent machine failure prediction web app built using Streamlit and a trained Random Forest model. It simulates predictive maintenance in a smart factory setting using real-time inputs from sensors like Torque, Tool Wear, Temperature, and Rotational Speed.

**1. Purpose**
This project simulates a Smart Factory environment where machine failure is predicted in advance using sensor data. It supports predictive maintenance by:

Minimizing unplanned downtime

Alerting operators before critical failure

Explaining which parameters lead to breakdowns

Useful for internships and jobs related to:

Smart Factory / Industry 4.0

Business Intelligence / Manufacturing Analytics

Predictive Maintenance Engineer

Data Science in Industrial IoT

🚀 Live Demo (Try It Now)
[🌐 Launch the App on Streamlit Cloud](https://smart-factory-filure-prediction-6rxhryfpufjdcweuembhxb.streamlit.app/)


**2. Tech Stack**
Layer	Tool
ML Model:-	Random Forest (Scikit-learn)
Web App:-	Streamlit
Data Prep:-	Pandas, NumPy
File Handling:-	Pickle

**3. Dataset**
Name: AI4I 2020 Predictive Maintenance Dataset

Source: UCI Repository

Description: Sensor data from a manufacturing line, with labels indicating machine failure.

🔧 Features Used:
Torque [Nm]

Rotational speed [rpm]

Tool wear [min]

Air temperature [K]

Process temperature [K]

Machine failure (target)

📊 Model Performance
  1. Random Forest Classifier
  2. ROC-AUC Score: 0.98
  3. The model demonstrates excellent classification ability in predicting machine failure based on real-world sensor data.

**4. Features**
1. User Input Interface

Users enter real-time values for temperature, torque, tool wear, etc.

Optionally pre-filled test cases

2. Prediction Output

Displays whether the machine is likely to fail or run normally

Shows suggestion messages (e.g., "High torque + tool wear → Likely breakdown")

3. Input Summary

Recap of user-entered values

Suggestions based on thresholds (e.g., tool wear too high)

**5. How to Use**
Enter the values for torque, speed, tool wear, air/process temperature

Click Predict

View:

Pass/Fail Prediction

Suggestions to avoid failure

**6. Sample Snapshot**
<img width="1558" height="838" alt="Screenshot 2025-07-11 115427" src="https://github.com/user-attachments/assets/96529980-e087-412e-8c13-88aca28896cf" />

**7. Inference & Business Value**
Torque and Tool Wear are often the strongest predictors of machine failure.

High rotational speed combined with tool fatigue increases failure risk.

Helps factories switch from reactive to predictive maintenance.

Reduces unexpected breakdowns, saving cost and improving uptime.

Model performance (ROC-AUC = 0.98) indicates strong reliability in production use.


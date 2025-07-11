import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("rf_model.pkl", "rb"))

# Title
st.title("🔧 Smart Factory Failure Predictor")
st.markdown("Enter machine parameters to predict failure status.")

# Sidebar inputs
st.sidebar.header("Machine Sensor Inputs")
air_temp = st.sidebar.number_input("Air Temperature [K]", 290.0, 330.0, step=0.5)
process_temp = st.sidebar.number_input("Process Temperature [K]", 290.0, 340.0, step=0.5)
rotational_speed = st.sidebar.slider("Rotational Speed [rpm]", 0, 3000, 1500)
torque = st.sidebar.slider("Torque [Nm]", 0.0, 100.0, 40.0)
tool_wear = st.sidebar.slider("Tool Wear [min]", 0, 250, 100)

st.sidebar.subheader("Component Failures (1 = Yes)")
hdf = st.sidebar.selectbox("HDF Failure", [0, 1])
osf = st.sidebar.selectbox("OSF Failure", [0, 1])
pwf = st.sidebar.selectbox("PWF Failure", [0, 1])
twf = st.sidebar.selectbox("TWF Failure", [0, 1])
rnf = st.sidebar.selectbox("RNF Failure", [0, 1])

st.sidebar.subheader("Machine Type")
type_option = st.sidebar.selectbox("Select Type", ["L", "M", "H"])
type_L = 1 if type_option == "L" else 0
type_M = 1 if type_option == "M" else 0

# Predict button
if st.button("🔍 Predict Failure"):
    features = np.array([[air_temp, process_temp, rotational_speed, torque, tool_wear,
                          hdf, osf, pwf, twf, rnf, type_L, type_M]])
    prediction = model.predict(features)[0]
    
    if prediction == 1:
        st.error("❌ Machine Failure Predicted!")
    else:
        st.success("✅ Machine is Operating Normally.")

    st.subheader("Input Summary")
    st.write({
        "Air Temp": air_temp, "Process Temp": process_temp,
        "Speed": rotational_speed, "Torque": torque, "Tool Wear": tool_wear,
        "Failures": {"HDF": hdf, "OSF": osf, "PWF": pwf, "TWF": twf, "RNF": rnf},
        "Type": type_option
    })
    st.subheader("Potential Failure Insights")

    insights = []
    if tool_wear > 200:
        insights.append("⚠️ High Tool Wear – consider maintenance soon.")
    if torque > 60:
        insights.append("⚠️ Excessive Torque – could damage components.")
    if rotational_speed > 2800:
        insights.append("⚠️ Very High Speed – may cause overheating.")
    if process_temp > 330:
        insights.append("⚠️ High Process Temperature – risk of thermal failure.")
    if hdf or osf or pwf or twf or rnf:
        insights.append("⚠️ Previous component failures detected – possible degradation.")

    if insights:
        for insight in insights:
            st.write(insight)
    else:
        st.write("No immediate issues detected from input parameters.")


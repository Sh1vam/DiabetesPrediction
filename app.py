import csv
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
import streamlit as st

# Ignore all warnings
import warnings
warnings.filterwarnings("ignore")

# Load the trained model
model = joblib.load("Diabetese_Prediction.joblib")
scaler = StandardScaler()

# Define columns
columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Predicted_Outcome']

def write_to_csv(input_data, prediction):
    try:
        with open('Diabetes_Predictions.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(columns)
            writer.writerow(input_data + [prediction])
    except Exception as e:
        st.error(f"Error writing to CSV: {str(e)}")

def predict_diabetes(input_data):
    try:
        # Transform input data using the scaler
        input_data_scaled = scaler.fit_transform(np.array(input_data).reshape(1, -1))
        
        # Predict using the trained model
        prediction = model.predict(input_data_scaled)
        
        # Return prediction result
        return prediction[0],"Has Diabetes" if prediction[0] == 1 else "Does Not Have Diabetes"
    except Exception as e:
        st.error(f"Error predicting: {str(e)}")

def diabetes_prediction_page():
    st.title("Diabetes Prediction")

    # Input fields
    pregnancies = st.number_input("Pregnancies", min_value=0, step=1)
    glucose = st.number_input("Glucose", min_value=0)
    blood_pressure = st.number_input("Blood Pressure", min_value=0)
    skin_thickness = st.number_input("Skin Thickness", min_value=0)
    insulin = st.number_input("Insulin", min_value=0)
    bmi = st.number_input("BMI", min_value=0.0)
    diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", min_value=0.0)
    age = st.number_input("Age", min_value=0, step=1)

    # Prediction button
    if st.button("Predict"):
        try:
            # Predict diabetes
            input_data = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]
            prediction, result = predict_diabetes(input_data)
            
            # Write prediction to CSV
            write_to_csv(input_data, prediction)

            st.success(f"Prediction: {result}")
        except Exception as e:
            st.error(f"Error: {str(e)}")

def main():
    st.set_page_config(page_title="Diabetes Prediction App", layout="wide")

    # Render the Diabetes Prediction page
    diabetes_prediction_page()

if __name__ == "__main__":
    main()

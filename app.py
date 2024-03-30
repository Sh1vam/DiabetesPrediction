# Import necessary libraries
import csv
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier
import eel
# Ignore all warnings
import warnings
warnings.filterwarnings("ignore")

# Initialize Eel
eel.init('web')  # 'web' is the folder name where your HTML and JavaScript files are located

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
        print(f"Error writing to CSV: {str(e)}")

def predict_diabetes(input_data):
    try:
        # Transform input data using the scaler
        input_data_scaled = scaler.fit_transform(np.array(input_data).reshape(1, -1))
        
        # Predict using the trained model
        prediction = model.predict(input_data_scaled)
        
        # Return prediction result
        return prediction[0],"Has Diabetes" if prediction == 1 else "Does Not Have Diabetes"
    except Exception as e:
        return "Error predicting"

@eel.expose
def Diabetes_Prediction(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
    try:
        # Convert input data to suitable format
        Pregnancies = int(Pregnancies)
        Age = int(Age)
        input_data = [Pregnancies, float(Glucose), float(BloodPressure), float(SkinThickness), float(Insulin), float(BMI), float(DiabetesPedigreeFunction), Age]
        
        # Predict diabetes
        prediction,result = predict_diabetes(input_data)
        
        # Write prediction to CSV
        write_to_csv(input_data, prediction)
        
        # Return prediction result
        return result
    except Exception as e:
        return f"Error processing input: {str(e)}"

# Start the Eel application
try:
    eel.start('app.html', size=(800, 600))
except Exception as e:
    print(f"Error starting Eel: {e}")

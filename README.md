# [DiabetesPrediction Using Machine Learning](https://diabetesprediction-fk7h4hbozcemgafgipkv3d.streamlit.app/)
pima-indians-diabetes prediction using ML
## External Library Used 
### Pandas,Seaborn,Numpy,Scikit-Learn,Eel,MatplotLib
#### Installing :- go to Terminal/CommandPrompt type ```pip install -r reqdment.txt``` or run ```installer.py```

**Creating Jupyter Environment**
1) Download Suitable Python installer from [Python.Org](https://www.python.org/)
2) When Installing It in Windows **MUST SELECT ADD PYTHON TO PATH OPTION**
3) Open Terminal/Command Prompt type ```pip install virtualenv```
4) After Installation is completed Type ```virtualenv <Virtual_Environment_Folder_Name_of_Your_Choice (example : venv)>```
5) For Linux User type in terminal ```source path_to/venv/bin/activate``` for windows user type in command prompt```path_to\venv\Scripts\activate```
6) after acivating virtual environment type ```pip install jupyterlab```
7) after jupyterlab is installed run it by typing ```jupyter lab```
___Hence Jupyter Environment Is Created___

## About Dataset

### Source :- https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database

Context :_

This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective of the dataset is to diagnostically predict whether or not a patient has diabetes, based on certain diagnostic measurements included in the dataset. Several constraints were placed on the selection of these instances from a larger database. In particular, all patients here are females at least 21 years old of Pima Indian heritage.

Content :-

The datasets consists of several medical predictor variables and one target variable, Outcome. Predictor variables includes the number of pregnancies the patient has had, their BMI, insulin level, age, and so on.

Features :-
        
+ Pregnancies -Number of times pregnant
+ Glucose - Plasma glucose concentration a 2 hours in an oral glucose tolerance test
+ BloodPressure - Diastolic blood pressure (mm Hg)
+ SkinThickness -Triceps skin fold thickness (mm)
+ Insulin - 2-Hour serum insulin (mu U/ml)
+ BMI - Body mass index (weight in kg/(height in m)^2)
+ DiabetesPedigreeFunction
+ Age (years)
+ Outcome - Class variable (0 or 1) 268 of 768 are 1, the others are 0


Software Requirements :-
           [Python](https://www.python.org/) ,
           [Chromium](https://www.kali.org/tools/chromium/) / [Chrome](https://www.google.com/intl/en_in/chrome/) Browser

# Future Scope

+ Ask User if the Output is correct to not and then add/record user response to CSV File. <p>
+ Add Obesity Prediction based on BMI and also predict its Category. <p>
+ Predict if person is UnderWeight or not based on BMI. <p>
+ Add Explaination for given output.

from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)

model = pickle.load(open('random_forest_classification_model_top.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    overtime=0
    if request.method == 'POST':
        Age = int(request.form['Age'])
        MonthlyIncome=int(request.form['MonthlyIncome'])
        YearsAtCompany=int(request.form['YearsAtCompany'])
        TotalWorkingYears=int(request.form['TotalWorkingYears'])
        NumCompaniesWorked=int(request.form['NumCompaniesWorked'])

        overtime=request.form['overtime']
        if(overtime=='Yes'):
            overtime=1
            overtime=0
        else:
            overtime=0
            overtime=1

        DistanceFromHome = int(request.form['DistanceFromHome'])

        JobSatisfaction=request.form['JobSatisfaction']
        if(JobSatisfaction=='1'):
            JobSatisfaction=1
        elif(JobSatisfaction=='2'):
            JobSatisfaction=2
        elif (JobSatisfaction == '3'):
            JobSatisfaction = 3
        else:
            JobSatisfaction = 4

        EnvironmentSatisfaction = request.form['EnvironmentSatisfaction']
        if (EnvironmentSatisfaction == '1'):
            EnvironmentSatisfaction = 1
        elif (EnvironmentSatisfaction == '2'):
            EnvironmentSatisfaction = 2
        elif (EnvironmentSatisfaction == '3'):
            EnvironmentSatisfaction = 3
        else:
            EnvironmentSatisfaction = 4

        RelationshipSatisfaction = request.form['RelationshipSatisfaction']
        if (RelationshipSatisfaction == '1'):
            RelationshipSatisfaction = 1
        elif (RelationshipSatisfaction == '2'):
            RelationshipSatisfaction = 2
        elif (RelationshipSatisfaction == '3'):
            RelationshipSatisfaction = 3
        else:
            RelationshipSatisfaction = 4

        prediction=model.predict([[ overtime, Age, TotalWorkingYears, MonthlyIncome, JobSatisfaction, YearsAtCompany, EnvironmentSatisfaction, RelationshipSatisfaction, DistanceFromHome, NumCompaniesWorked]])
        print(prediction)

        if prediction != 1:
            return render_template('index.html',prediction_text="No Attrition - Safe Zone")
        else:
            return render_template('index.html',prediction_text="Attrition Possible - Danger Zone")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)


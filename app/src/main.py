from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle
import os

# with open('../models/diabetes_model','rb') as file:
#     classifier = pickle.load(file)

df_diabetes = pd.read_csv('../data/diabetes_prediction_dataset.csv',nrows=2)

df_columns = df_diabetes.columns.tolist()

# df_columns = [
#     'gender',
#     'age',
#     'hypertension',
#     'heart_disease',
#     'smoking_history',
#     'bmi',
#     'HbA1c_level',
#     'blood_glucose_level',
#     'diabetes'
# ]

target = 'diabetes'


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/notebook-page')
def notebook_page():
    return render_template("notebook.html")

@app.route('/notebook-file')
def notebook_file():
    return render_template("diabetes_notebook.html")

@app.route('/predict', methods=['POST'])
def make_prediction():
    if request.method == "POST":
        classifier = pickle.load(open('../models/diabetes_model','rb'))

        height = float(request.form.get('height'))
        weight = float( request.form.get('weight'))

        bmi = weight / (height/100)**2

        request_values_dict_for_df = {k:[request.form.get(k)] for k in request.form.to_dict()}
        request_values_dict_for_df['bmi'] = [bmi]

        df_for_model_prediction = pd.DataFrame.from_dict(request_values_dict_for_df)

        prediction = classifier.predict_proba(df_for_model_prediction)[0][1]
        print(prediction)
    

        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
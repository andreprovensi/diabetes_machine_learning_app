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
    input_data = request.get_json()

    classifier = pickle.load(open('../models/diabetes_model','rb'))

    dict_for_input_dataframe = {feature:[input_data.get(feature)] for feature in df_columns}

    df_input_pipeline = pd.DataFrame.from_dict(dict_for_input_dataframe)

    prediction = classifier.predict_proba()[:,1]

    
# colunas = None
# @app.route('/cotacao/',methods=['POST'])
# def cotacao():
#     dados = request.get_json()
#     dados_input = [dados[col] for col in colunas]
#     print(dados_input)
#     preco = classifier.predict([dados_input])
#     return jsonify(preco=preco[0])

if __name__ == '__main__':
    app.run()
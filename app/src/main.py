from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle
import os

# with open('../models/diabetes_model','rb') as file:
#     classifier = pickle.load(file)

df_columns = [
    'gender',
    'age',
    'hypertension',
    'heart_disease',
    'smoking_history',
    'bmi',
    'HbA1c_level',
    'blood_glucose_level',
    'diabetes'
]

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
from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle
import os


def create_API():

    df_diabetes = pd.read_csv('../data/diabetes_prediction_dataset.csv',nrows=2)

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

        with open('../models/diabetes_model','rb') as serialized_model:
        # serialized_model = open('../models/diabetes_model','rb')
            classifier = pickle.load(serialized_model)

            height = float(request.form.get('height'))
            weight = float( request.form.get('weight'))

            bmi = weight / (height/100)**2

            request_values_dict_for_df = {k:[request.form.get(k)] for k in request.form.to_dict()}
            request_values_dict_for_df['bmi'] = [bmi]

            df_for_model_prediction = pd.DataFrame.from_dict(request_values_dict_for_df)

            prediction = classifier.predict_proba(df_for_model_prediction)[0][1]
            print(prediction)
            
            # serialized_model.close()
            
            return jsonify({'prediction':str(round(prediction*100,1))})
    
    return app

if __name__ == '__main__':
    
    API = create_API()
    API.run(debug=True)

from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle
import os

def create_API():

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
        
        if __name__ == "__main__":
            path_to_app = '\\'.join(os.getcwd().split('\\')[:-1])
            model_path = os.path.join(path_to_app,'models','diabetes_model')
        else:
            script_dir = os.path.dirname(os.path.abspath('__file__'))
            model_path = os.path.join(script_dir,'models','diabetes_model')
        
        with open(model_path,'rb') as serialized_model:
       
            classifier = pickle.load(serialized_model)

            height = float(request.form.get('height'))
            weight = float( request.form.get('weight'))

            bmi = weight / (height/100)**2

            request_values_dict_for_df = {k:[request.form.get(k)] for k in request.form.to_dict()}
            request_values_dict_for_df['bmi'] = [bmi]

            df_for_model_prediction = pd.DataFrame.from_dict(request_values_dict_for_df)

            prediction = classifier.predict_proba(df_for_model_prediction)[0][1]
                        
            return jsonify({'prediction':str(round(prediction*100,1))})
    
    return app

if __name__ == '__main__':
    
    API = create_API()
    API.run(debug=True)

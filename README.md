# ML Diabetes Prediction Portfolio Project

Welcome to my Machine Learning Diabetes Prediction Portfolio Project! The project includes a Jupyter notebook for the model development, a Flask-based backend for making predictions, and features an XGBoost model tuned with Optuna while tracking experiments with MLflow.

## Project Overview



- **Machine Learning Model Development:**
  - I have created a XGBoost model for diabetes prediction. The model has been fine-tuned using Optuna, an optimization framework, to enhance its performance. It leverages machine learning techniques to make predictions based on features such as gender, age, hypertension, heart disease, smoking history, BMI, HbA1c level, blood glucose level, and more.

- **Jupyter Notebook:**
  - The model development process is thoroughly documented in a Jupyter notebook (`diabetes_notebook.ipynb`). It covers the steps taken, feature engineering, XGBoost model creation, and the application of Optuna for hyperparameter tuning.

- **Flask Backend:**
  - The backend of the project is built using Flask, a lightweight web framework in Python. The Flask app provides an API endpoint ("/predict") for making predictions using the trained XGBoost model. 

- **Optuna Hyperparameter Tuning:**
  - The XGBoost model's hyperparameters have been fine-tuned using Optuna, an automatic hyperparameter optimization framework. This ensures the model achieves optimal performance and generalization.

- **MLflow Experiment Tracking:**
  - Experiments during model development were tracked using MLflow, an open-source platform for managing the end-to-end machine learning lifecycle. This allows for reproducibility and easy comparison of different model iterations.

## Project Structure

- **`app`:**
  - The Flask backend is organized in this directory. The main Flask application file is `src/main.py`. It includes the '/predict' route for making predictions using the trained XGBoost model.

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/andreprovensi/diabetes_machine_learning_app.git
   cd diabetes_machine_learning_app
   
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Run the Flask App:**
   ```bash
   python app/src/main.py



   
 

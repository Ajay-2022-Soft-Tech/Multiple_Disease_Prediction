# Multiple_Disease_Prediction
This repository contains a web application built using Streamlit that predicts the likelihood of diabetes, heart disease, and Parkinson's disease using machine learning models. The application provides a user-friendly interface for inputting medical data and viewing prediction results.

Multi-Disease Prediction Web App
This web application uses machine learning models to predict multiple diseases, including Diabetes, Heart Disease, and Parkinson's Disease. The application is built using Streamlit for the front end and various machine learning algorithms for the back end.

Features
Diabetes Prediction
Heart Disease Prediction
Parkinson's Disease Prediction
Demo

Requirements
Python 3.7+
Streamlit
Pandas
Numpy
Scikit-learn
Pickle
Installation
Clone the repository
bash
Copy code
git clone https://github.com/yourusername/multi-disease-prediction.git
cd multi-disease-prediction
Create and activate a virtual environment
bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
Install the required packages
bash
Copy code
pip install -r requirements.txt
Usage
Run the Streamlit app
bash
Copy code
streamlit run app.py
Open your browser
Go to http://localhost:8501 to view the app.

Project Structure
kotlin
Copy code
multi-disease-prediction/
│
├── models/
│   ├── diabetes_model.sav
│   ├── heart_disease_model.sav
│   ├── parkinson_model.sav
│
├── app.py
├── requirements.txt
├── README.md
└── data/
Models
The machine learning models for predicting each disease are stored in the models/ directory. They are loaded into the app using Pickle.

Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

License
This project is licensed under the MIT License.

Contact
For any issues or questions, please contact [your email address].

Step-by-Step Instructions to Run the ML App
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/multi-disease-prediction.git
cd multi-disease-prediction
Create a Virtual Environment:

bash
Copy code
python -m venv venv
Activate the Virtual Environment:

On Windows:
bash
Copy code
venv\Scripts\activate
On macOS and Linux:
bash
Copy code
source venv/bin/activate
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Streamlit App:

bash
Copy code
streamlit run app.py
Open the App in Your Browser:
Open your browser and go to http://localhost:8501 to use the multi-disease prediction app.

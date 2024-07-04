# Multi-Disease Prediction Web App

This web application uses machine learning models to predict multiple diseases, including Diabetes, Heart Disease, and Parkinson's Disease. The application is built using Streamlit for the front end and various machine learning algorithms for the back end.

## Features

- **Diabetes Prediction**
- **Heart Disease Prediction**
- **Parkinson's Disease Prediction**

## Demo

![App Demo](link_to_demo_gif_or_image)

## Requirements

- Python 3.7+
- Streamlit
- Pandas
- Numpy
- Scikit-learn
- Pickle

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/multi-disease-prediction.git
cd multi-disease-prediction
Create and activate a virtual environment
bash
Always show details

Copy code
python -m venv venv
source venv/bin/activate   # On Windows use `venv\\Scripts\\activate`
Install the required packages
bash
Always show details

Copy code
pip install -r requirements.txt
Usage
Run the Streamlit app
bash
Always show details

Copy code
streamlit run app.py
Open your browser
Go to http://localhost:8501 to view the app.

Project Structure
kotlin
Always show details

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


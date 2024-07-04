# Multi-Disease Prediction System

This web app predicts diabetes, heart disease, and Parkinson's disease using machine learning models. It's built with Streamlit and uses a trained model saved as `trained_model.sav`.

## Features

- **Diabetes Prediction**
- **Heart Disease Prediction**
- **Parkinson's Disease Prediction**

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- Anaconda (recommended for environment management)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/multi-disease-prediction.git
    cd multi-disease-prediction
    ```

2. Create a virtual environment and activate it:

    ```bash
    conda create --name disease-prediction-env python=3.8
    conda activate disease-prediction-env
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Demo
<img src="https://github.com/Ajay-2022-Soft-Tech/Multiple_Disease_Prediction/assets/113298640/77e6b20e-df2d-4465-a427-40b7d251f641"  width="1000" height="400" />

<img src="https://github.com/Ajay-2022-Soft-Tech/Multiple_Disease_Prediction/assets/113298640/1b28e646-0513-4d7d-a638-09ff5d9f78d1"  width="1000" height="400" />

<img src="https://github.com/Ajay-2022-Soft-Tech/Multiple_Disease_Prediction/assets/113298640/e40ba427-8162-4387-8585-46411006fc99"  width="1000" height="400" />



### Configuration

1. Download the trained model file `trained_model.sav` and place it in the project directory.

2. Update the model path in `Multiple_Disease_Pred.py`:

    ```python
    import pickle

    # Load the trained model
    model_path = "path_to_your_model/trained_model.sav"
    model = pickle.load(open(model_path, 'rb'))
    ```

    Replace `path_to_your_model/trained_model.sav` with the actual path to your `trained_model.sav` file.

### Running the App

1. Activate the virtual environment (if not already activated):

    ```bash
    conda activate disease-prediction-env
    ```

2. Run the Streamlit app:

    ```bash
    streamlit run path_to_/Multiple_Disease_Pred.py
    ```

3. Open the app in your browser:

    Streamlit will provide a local URL (usually http://localhost:8501) where you can interact with the web app.

## File Structure

- `Multiple_Disease_Pred.py`: Main application file for Streamlit.
- `trained_model.sav`: Pre-trained machine learning model.
- `requirements.txt`: List of required Python packages


Contributing
- `Feel free to fork and submit a pull request.`

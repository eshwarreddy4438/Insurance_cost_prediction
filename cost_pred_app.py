import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open('ins.pkl', 'rb'))

# Custom CSS for styling with black background
st.markdown(
    """
    <style>
    .main {
        background-color: #000000;
        padding: 2rem;
        border-radius: 10px;
    }
    .title {
        font-family: 'Arial';
        color: #4CAF50;
        text-align: center;
    }
    .subheader {
        font-family: 'Arial';
        color: #FFFFFF;
        margin-bottom: 0.5rem;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-size: large;
        padding: 0.75rem;
        border-radius: 5px;
        margin-top: 1rem;
        width: 100%;
    }
    .stNumberInput label, .stSelectbox label {
        color: #FFFFFF;
    }
    .stNumberInput input, .stSelectbox input {
        background-color: #333333;
        color: #FFFFFF;
    }
    </style>
    """, unsafe_allow_html=True
)

# App title with enhanced styling
st.markdown('<h1 class="title">Insurance Cost Predictor</h1>', unsafe_allow_html=True)

# Organizing input fields using columns
col1, col2 = st.columns(2)

with col1:
    age = st.number_input('Age', min_value=0, max_value=100)
    gender = st.selectbox('Gender', ['Male', 'Female'])
    gender_val = 0 if gender == 'Male' else 1

with col2:
    bmi = st.number_input("BMI", min_value=0.0, max_value=100.0, value=25.0, step=0.1)
    children = st.number_input('No of Children', min_value=0, max_value=10, value=0, step=1)

smoker = st.selectbox('Is Smoker', ['Yes', 'No'])
smoker_val = 1 if smoker == 'Yes' else 0

regions = ["Southeast", "Southwest", "Northeast", "Northwest"]
selected_region = st.selectbox("Select your region", regions)
region_value = regions.index(selected_region)

# Button for prediction
if st.button('Predict'):
    # Prepare input data for prediction
    input_data = [age, gender_val, bmi, children, smoker_val, region_value]
    input_data_numpy = np.asarray(input_data).reshape(1, -1)

    # Make the prediction
    prediction = model.predict(input_data_numpy)

    # Display the prediction result with a success message
    st.success(f'Estimated Insurance Cost: ${prediction[0]:,.2f}')

import streamlit as st
from prediction_helper import predict

st.title("Health insurance prediction App")

categorical_options = {
    'Gender':['Male','Female'],
    'Marital status':['Unmarried', 'Married'],
    'BMI Category':['Normal','obesity','underweight','overweight'],
    'Smoking Status':['No Smoking','Regular','Occasional'],
    'Employment Status':['Salaried','Self Employed','Freelancer',''],
    'Region':['Northwest','Southeast','Northeast','Southwest'],
    'Medical History':['No Disease','Diabetes','High Blood pressure','Diabetes & High Blood pressure',
                       'Thyroid','Heart Disease','High Blood pressure & Heart disease','Diabetes & Thyroid',
                       'Diabetes & Heart Disease'],
    'Insurance plan':['Bronze','Silver','Gold']

}

row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

#assign inputs to grid

with row1[0]:
    age = st.number_input('Age',min_value=18,step=1,max_value=100)

with row1[1]:
    number_of_dependants = st.number_input('Number of Dependants', min_value=0,step=1,max_value=20)
with row1[2]:
    income_lakhs = st.number_input('Income in lakhs',step=1,min_value=0,max_value=200)
with row2[0]:
    genetical_risk = st.number_input('Genetical Risk',step=1,min_value=0,max_value=5)
with row2[1]:
    insurance_plan = st.selectbox('Insurance Plan',categorical_options['Insurance plan'])
with row2[2]:
    employment_status =st.selectbox('Employment Status',categorical_options['Employment Status'])

with row3[0]:
    gender = st.selectbox('Gender',categorical_options['Gender'])
with row3[1]:
    marital_status = st.selectbox('Marital Status',categorical_options['Marital status'])
with row3[2]:
    bmi_category = st.selectbox('BMI Category',categorical_options['BMI Category'])

with row4[0]:
    smoking_status= st.selectbox('Smoking Status',categorical_options['Smoking Status'])
with row4[1]:
    region= st.selectbox('Region',categorical_options['Region'])
with row4[2]:
    medical_history=st.selectbox('Medical History', categorical_options['Medical History'])

input_dict = {
    'Age':age,
    'Number of dependants':number_of_dependants,
    'Income in Lakhs':income_lakhs,
    'Genetical Risk':genetical_risk,
    'Insurance Plan':insurance_plan,
    'Employment status':employment_status,
    'Gender':gender,
    'Marital Status':marital_status,
    'BMI category': bmi_category,
    'Smoking Status':smoking_status,
    'Region':region,
    'Medical History': medical_history
}

if st.button('Predict'):
    prediction = predict(input_dict)
    st.success(f"Predicted Output: {prediction}")



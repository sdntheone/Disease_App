import pickle
import streamlit as st
# import sklearn

diabetes_model = pickle.load(open('diabetes_model.pkl','rb'))
heart_disesae_model = pickle.load(open('heart_disease_model.pkl','rb'))

st.set_page_config(layout='wide',page_title='Disease Prediction')

option=st.sidebar.selectbox('Select the Disease',['Diabetes','Heart Disease'])

if option=='Diabetes':
    btn1=st.sidebar.button('Check Diabetes')

    st.title('Check, you have Diabetes or Not')
    col1,col2,col3,col4=st.columns(4)
    with col1:
        Pregnancies =st.text_input('enter pregnencies')
    with col2:
        Glucose =st.text_input('enter Glucose level')
    with col3:
        BloodPressure =st.text_input('enter Blood Pressure')
    with col4:
        SkinThickness =st.text_input('enter Skin thickness')

    with col1:
        Insulin =st.text_input('enter Insulin value')
    with col2:
        BMI =st.text_input('enter  BMI level')
    with col3:
        DiabetesPedigreeFunction =st.text_input('enter DiabetesPedigreeFunction')
    with col4:
        Age =st.text_input('enter your age')

        if st.button('Diabetes Test Result'):
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

            if (diab_prediction[0] == 1):
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'

            st.success(diab_diagnosis)


elif option=='Heart Disease':
    btn2=st.sidebar.button('Check Heart Health')

    st.title('Check, your heart is working fine or not')
    col1,col2,col3=st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disesae_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])

        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)











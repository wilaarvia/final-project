# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 12:19:04 2022

@author: rifqi arman
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved model
loan_model = pickle.load(open('trained_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Home Loan Prediction System',
                          
                          ['Loan Prediction',
                           'About the project',
                           'About the author'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Loan Prediction'):
    
    # page title
    st.title('Loan Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(5)
    
    with col1:
        Gender = st.number_input('what is your gender')
        
    with col2:
        Married = st.number_input('are you married')
    
    with col3:
        Dependents = st.number_input('are you dependents')
    
    with col1:
        Education = st.number_input('your education')
    
    with col2:
        Self_Employed = st.number_input('are you self employed')
    
    with col3:
        ApplicantIncome = st.number_input('how much your applicant income')
    
    with col1:
        CoapplicantIncome = st.number_input('how much your coapplicant income')
    
    with col2:
        LoanAmount = st.number_input('how much your loan amount')
        
    with col3:
        Loan_Amount_Term = st.number_input('how much your loan amount in term')
    
    with col1:
        Credit_History = st.number_input('how your credit history')
        
    with col2:
        Property_Area_Rural = st.number_input('your property area in rural?')
        
    with col3:
        Property_Area_Semiurban = st.number_input('your property area in semi urban?')
        
    with col1:
        Property_Area_Urban = st.number_input('your property area in urban?')
    
    # code for Prediction
    prediction = ''
    
    # creating a button for Prediction
    
    if st.button('Loan Test Result'):
        loan_prediction = loan_model.predict([[Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area_Rural, Property_Area_Semiurban, Property_Area_Urban]])
        
        if (loan_prediction[0] == 1):
          prediction = 'The person is diabetic'
        else:
          prediction = 'The person is not diabetic'
        
    st.success(prediction)
    
# Heart Disease Prediction Page
if (selected == 'About the project'):
    
    # page title
    st.title('home loan Prediction using ML')
    
    st.text('Dream Housing Finance company deals in all home loans. They have a presence across all urban, semi-urban, and rural areas. Customer-first applies for a home loan after that company validates the customer eligibility for a loan')
    st.text('The company wants to automate the loan eligibility process (real-time) based on customer detail provided while filling the online application form.')
    st.text('These details are Gender, Marital Status, Education, Number of Dependents, Income, Loan Amount, Credit History, and others.')
    st.text('To automate this process, they have given a problem to identify the customers segments, those are eligible for loan amount so that they can specifically target these customers. Here they have provided a partial data set')
    
    st.text('what you should input in the tables')
    st.text('Gender : input 0 if you are Female or input 1 if you are male')
    st.text('Married : input 0 if you are not married or input 1 if you are married')
    st.text('Dependents : input the Number of your dependents, if it more than 3 then just input 3')
    st.text('Education : input 0 if you are Graduate or input 1 if you are Under Graduate')
    st.text('Self_Employed : input 0 if you are not a Self-employed or input 1 if you are Self-employed ')
    st.text('ApplicantIncome : input how much your Applicant incomest')
    st.text('CoapplicantIncome : input how much your Coapplicant income ')
    st.text('LoanAmount : input how much your Loan amount in thousands')
    st.text('Loan_Amount_Term : how much your Term of a loan in months')
    st.text('Credit_History : credit history meets guidelines')
    st.text('Property_Area : Urban/ Semi-Urban/ Rural')
    st.text('Loan_Status : Loan approved (Y/N)')
    
# Heart Disease Prediction Page
if (selected == 'About the author'):
    
    # page title
    st.title('about the author')
    st.text('hi, my name is wila. nice to meet you')
        
        

import pandas 
import pickle
import streamlit as st

st.title('Bank Churning Prediction')

# load transform OneHotEncoder
#transform_in = open("OneHotEncoder.pkl","rb")
#OneHotEncoder=pickle.load(transform_in)

# load ML model
#pickle_in = open("model.pkl","rb")
#classifier=pickle.load(pickle_in)


gender = st.radio("Gender",('Male', 'Female'))
Education = st.radio("Education",('High School', 'Graduate', 'Uneducated', 'Unknown', 'College',
       'Post-Graduate', 'Doctorate'))
marital_status = st.radio("Marital Status",('Married', 'Single', 'Unknown', 'Divorced'))
card_category= st.radio("Card Category",('Blue', 'Gold', 'Silver', 'Platinum'))
income_category= st.radio("Income Category",('$60K - $80K', 'Less than $40K', '$80K - $120K', '$40K - $60K',
       '$120K +', 'Unknown'))

age= st.slider("Customer Age",20,80)
dependent_count= st.slider("Dependent Count",0,6)
months_on_book = st.slider("Customer Since",10,60)
months_inactive= st.slider("Inactivity In Last 12 Months",0,12)
contacts_count= st.slider("Contacted Customer In Last 12 Months",0,12)
total_transaction_count= st.slider("",20,80)
credit_limit= st.number_input("Credit Limit",min_value=1000,max_value=35000)
total_revolving_balance= st.number_input("Total Revolving Balance",min_value=0,max_value=4000)
avg_open_to_buy= st.number_input('Average Open To Buy',min_value=0,max_value=40000)
total_transaction_amount= st.number_input('Total Transaction amount',min_value=500,max_value=20000)
average_utilization_ratio= st.number_input("Average Utilization Ratio",min_value=0.0,max_value=1.0)
total_relationship_count= st.number_input("Total Relationship Count",min_value=1,max_value=6)
total_ct_chng =st.number_input("Total Count change",min_value=0.0,max_value=4.0) 
total_amt_chng= st.number_input("Total Amount Change",min_value=0.0,max_value=4.0)


print(age)
print(dependent_count)
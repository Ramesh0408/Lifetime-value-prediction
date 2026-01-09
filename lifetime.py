import pandas as pd
import streamlit as st
import joblib

model=joblib.load('Lifetime_value.pkl')
st.title("Lifetime_Value_Prediction")
st.write("Input")
#inputs=
loginfrequency=st.number_input('Login_Frequency',min_value=0.0)
session=st.number_input('Session_Duration_Avg',min_value=0.0)
pages=st.number_input('Pages_Per_Session',min_value=0.0)
wishlist=st.number_input('Wishlist_Items',min_value=0.0)
Avg_order_value=st.number_input('Average_Order_Value',min_value=0.0)
returns=st.number_input('Returns_Rate',min_value=0.0)
cart_abdt_rate=st.number_input('Cart_Abandonment_Rate',min_value=0.0)
customer_service=st.number_input('Customer_Service_Calls',min_value=0.0)
last_day_purchase=st.number_input('Days_Since_Last_Purchase',min_value=0.0)
email_rate=st.number_input('Email_Open_Rate',min_value=0.0)
discount=st.number_input('Discount_Usage_Rate',min_value=0.0)
prod_review_written=st.number_input('Product_Reviews_Written',min_value=0.0)
churned=st.selectbox('Churned',[True,False])
#dataframe
frame=pd.DataFrame([{'Login_Frequency':loginfrequency,'Session_Duration_Avg':session,'Pages_Per_Session':pages,'Wishlist_Items':wishlist,'Average_Order_Value':Avg_order_value,'Returns_Rate':returns,'Cart_Abandonment_Rate':cart_abdt_rate,'Customer_Service_Calls':customer_service,'Days_Since_Last_Purchase':last_day_purchase,'Email_Open_Rate':email_rate,'Discount_Usage_Rate':discount,'Product_Reviews_Written':prod_review_written,'Churned':churned}])

# Prediction
if st.button("Predict"):
    prediction = model.predict(frame)[0]
    st.success(f"Predicted_Lifetime_Value: {prediction}")

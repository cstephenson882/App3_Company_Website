import streamlit as st
from send_Email import send_email
from validate_email import validate_email
import pandas as pd


st.header('Contact Us')

with st.form(key = 'email_forms'):
    user_email = st.text_input('Your email address', placeholder='example@domain.com')

    df = pd.read_csv('category.csv', sep=',')
    topic_option = st.selectbox("",df['Topic'])

    user_message = st.text_area('Your message',placeholder='How can we help ...?')
    button = st.form_submit_button('Submit')
    print(button)
    if button:
        # Validate the email address using validate_email library
        #is_valid = validate_email(email=user_email, verify=True)
        # Check if the validation result is False
        send_email(user_email, topic_option, user_message)
        st.success("Your email was sent sucessfully")





# Import Modules
import streamlit as st
from send_email import send_email
import pandas

# Create header 'Contact Us'.
st.header('Contact Us')
# store topics csv file inside variable
df = pandas.read_csv('topics.csv')
# Create email form.
with st.form(key='email_form'):
    user_email = st.text_input('Your email address')
    topic = st.selectbox('Topic to discuss', df['topic'])
    user_message = st.text_area('Your message')
    button = st.form_submit_button()
    email = f"""\
    Subject: Email from {user_email}

    From: {user_email}
    Topic for discussion: {topic}
    {user_message} 
    """
    if button:
        send_email(email)
        st.info('Email was sent successfully.')

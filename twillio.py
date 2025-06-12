import streamlit as st
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from dotenv import load_dotenv
import os
import time
import logging

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(filename='whatsapp.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Twilio credentials
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
FROM_WHATSAPP = os.getenv("TWILIO_WHATSAPP_FROM")
TO_WHATSAPP = os.getenv("TO_WHATSAPP_NUMBER")

client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Streamlit UI
st.title("📲 WhatsApp Message Sender via Twilio")
message_input = st.text_area("Type your message here:")

if st.button("Send Message"):
    if message_input.strip() == "":
        st.warning("⚠️ Please type a message before sending.")
    else:
        try:
            with st.spinner("Sending your message..."):
                time.sleep(1.5)  # simulate some processing delay
                message = client.messages.create(
                    body=message_input,
                    from_=FROM_WHATSAPP,
                    to=TO_WHATSAPP
                )
                st.success(f"✅ Message sent! SID: {message.sid}")
                logging.info(f"Message sent to {TO_WHATSAPP}: {message_input}")
        except TwilioRestException as e:
            st.error("❌ Failed to send message.")
            logging.error(f"Error sending message: {str(e)}")

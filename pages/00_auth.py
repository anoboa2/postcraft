import streamlit as st
import requests as r

INSTAGRAM_APP_ID = st.secrets["INSTAGRAM_APP_ID"]
INSTAGRAM_APP_SECRET = st.secrets["INSTAGRAM_APP_SECRET"]
REDIRECT_URI = st.secrets["REDIRECT_URI"]

# Initialize session state. This will be run once per session.
if 'authorization_code' not in st.session_state:
  st.session_state.authorization_code = None
if 'form_send_processing' not in st.session_state:
  st.session_state.form_send_processing = False

# Declare callback functions
def handleFormSubmit():
  if 'authorization_code' in st.session_state:
    st.session_state.authorization_code = None
  st.session_state.form_send_processing = True

  response = r.post(
    url = f"https://llt5p2q5qj.execute-api.us-east-1.amazonaws.com/Prod/",
    json = {
      "authorization_code": st.session_state.authorization_code,
    }
  )
  st.session_state.short_lived_access_token = response.json()['short_lived_access_token']
  st.session_state.short_lived_access_token_expires_in = response.json()['slat-expiration']
  st.session_state.instagram_data = response.json()['instagram_data']

# Parse query string parameters
st.session_state.authorization_code = st.experimental_get_query_params()['code'][0] if 'code' in st.experimental_get_query_params() else None


##### START OF PAGE CONTENT #####
st.title("Welcome to Postcraft")

url = f'https://api.instagram.com/oauth/authorize?client_id={INSTAGRAM_APP_ID}&redirect_uri={REDIRECT_URI}&scope=user_profile,user_media&response_type=code'

st.markdown(f"[Connect to Instagram]({url})")

if st.session_state.authorization_code is not None:
  with st.form("authorization_code_exchange"):
    st.text_input("Authorization code", value=st.session_state.authorization_code, disabled=True)
    submit_button = st.form_submit_button(
      label='Complete Authorization',
      help='Exchanges the authorization code for an access token.',
      on_click=handleFormSubmit,
      kwargs={'authorization_code': st.session_state.authorization_code},
      disabled=st.session_state.form_send_processing
    )

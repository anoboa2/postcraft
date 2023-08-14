import streamlit as st
import requests as r

# Initialize session state. This will be run once per session.
if 'short_lived_access_token' not in st.session_state:
  st.session_state.short_lived_access_token = ''
if 'short_lived_access_token_expires_in' not in st.session_state:
  st.session_state.short_lived_access_token_expires_in = ''
if 'ig_user_id' not in st.session_state:
  st.session_state.ig_user_id = ''
if 'instagram_data' not in st.session_state:
  st.session_state.instagram_data = None

# Declare callback functions
def handleGetInstagramPhotos():
  response = r.post(
    url = f"https://llt5p2q5qj.execute-api.us-east-1.amazonaws.com/Prod/",
    json = {
      "authorization_code": st.session_state.authorization_code,
    }
  )
  st.session_state.short_lived_access_token = response.json()['short_lived_access_token']
  st.session_state.short_lived_access_token_expires_in = response.json()['slat-expiration']
  st.session_state.instagram_data = response.json()['instagram_data']


##### START OF PAGE CONTENT #####
st.title("Welcome to Postcraft")

if st.session_state.short_lived_access_token_expires_in != '':
  st.button(
    label="Get Instagram Photos",
    help="Get Instagram photos from the user's profile.",
    on_click=handleGetInstagramPhotos,
    kwargs={},
    disabled=st.session_state.instagram_data is not None
  )

if st.session_state.instagram_data is not None:
  st.write(st.session_state.instagram_data)



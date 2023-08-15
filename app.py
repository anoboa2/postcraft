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
  print("do nothing")


##### START OF PAGE CONTENT #####
st.title("Welcome to Postcraft")

st.write(st.session_state.short_lived_access_token)
st.write(st.session_state.short_lived_access_token_expires_in)
st.write(st.session_state.ig_user_id)

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



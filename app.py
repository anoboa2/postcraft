import streamlit as st
import requests as r

# Initialize session state. This will be run once per session.
if 'short_lived_access_token' not in st.session_state:
  st.session_state.short_lived_access_token = ''
if 'short_lived_access_token_expires_in' not in st.session_state:
  st.session_state.short_lived_access_token_expires_in = ''
if 'instagram_data' not in st.session_state:
  st.session_state.instagram_data = None

# Declare callback functions
def handleGetInstagramPhotos():
  response = r.get(
    f"https://graph.instagram.com/me/media?fields=media_url&access_token={st.session_state.short_lived_access_token}"
  )
  st.session_state.instagram_data = response.json()

# Parse query string parameters
st.session_state.short_lived_access_token = st.experimental_get_query_params()['slat'][0] if 'slat' in st.experimental_get_query_params() else ''
st.session_state.short_lived_access_token_expires_in = st.experimental_get_query_params()['expiry'][0] if 'expiry' in st.experimental_get_query_params() else ''


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



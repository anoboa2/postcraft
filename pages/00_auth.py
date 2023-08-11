import streamlit as st

# Initialize session state. This will be run once per session.
if 'authorization_code' not in st.session_state:
  st.session_state.authorization_code = None
if 'form_send_processing' not in st.session_state:
  st.session_state.form_send_processing = False

# Declare callback functions
def handleFormSubmit():
  st.session_state.authorization_code = None
  st.session_state.form_send_processing = True

# Parse query string parameters
st.session_state.authorization_code = st.experimental_get_query_params()['code'][0] if 'code' in st.experimental_get_query_params() else None


##### START OF PAGE CONTENT #####
st.title("Welcome to Postcraft")

st.markdown("[Connect to Instagram](https://www.instagram.com)")

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

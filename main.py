import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.session_state['answers']=[]

st.markdown('''
            # What animal are you?
           
            ### by anastasia 😎
           ---                   ''')


st.image('cutepanda.webp')

if st.button('Next Page'):
    switch_page('game')


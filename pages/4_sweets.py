import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.image('UGLypanda.webp')

st.markdown('# What is your favourite sweet')

sweets = st.radio('',['Moam', 'Haribo', 'Skittles', 'Sour Patch Kids'])
if sweets == 'Sour Patch Kids':
    animal = 'Gorilla'
elif sweets == 'Haribo':
    animal = 'Eagle'
elif sweets == 'Skittles':
    animal = 'Wolf'
elif sweets == 'Moam':
    animal = 'Hippo'



st.session_state['answers'].append(animal)


if st.button('Next Page'):
    switch_page('animal')
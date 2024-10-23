import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.image('seal.webp')

st.markdown('# What is your animal')

animals = st.radio('',['Armadilo', 'Sumatran Elephant', 'Albino Gorilla', 'Piranha'])
if animals == 'Albino Gorilla':
    animal = 'Gorilla'
elif animals == 'Armadilo':
    animal = 'Eagle'
elif animals == 'Sumatran':
    animal = 'Wolf'
elif animals == 'Piranha':
    animal = 'Hippo'


st.session_state['answers'].append(animal)



if st.button('Next Page'):
    switch_page('answer')
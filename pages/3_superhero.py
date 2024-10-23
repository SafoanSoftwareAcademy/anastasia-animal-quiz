import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.image('MONKEYA.webp')

st.markdown('# Who is your favourite superhero')

superhero = st.radio('',['Batman', 'Spiderman', 'Superman', 'Robin'])
if superhero == 'Batman':
    animal = 'Gorilla'
elif superhero == 'Spiderman':
    animal = 'Eagle'
elif superhero == 'Superman':
    animal = 'Wolf'
elif superhero == 'Robin':
    animal = 'Hippo'


st.session_state['answers'].append(animal)



if st.button('Next Page'):
    switch_page('sweets')
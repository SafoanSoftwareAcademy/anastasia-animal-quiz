import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.image('shrimpball.webp')


st.markdown('# What is your favourite game?')

game = st.radio('',['Fortnite', 'Minecraft', 'Roblox', 'COD'])

animal = ''
if game == 'Fornite':
    animal = 'Gorilla'
elif game == 'Minecraft':
    animal = 'Eagle'
elif game == 'COD':
    animal = 'Wolf'
elif game == 'Roblox':
    animal = 'Hippo'

st.session_state['answers'].append(animal)

if st.button('Next Page'):
    switch_page('food')



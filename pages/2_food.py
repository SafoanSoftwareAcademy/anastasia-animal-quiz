import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.image('monkeu.png')

st.markdown('# What is your favourite fast food')

food = st.radio('',['KFC', 'Mcdonalds', 'Subway', 'BurgerKing'])

if food == 'KFC':
    animal = 'Gorilla'
elif food == 'Mcdonalds':
    animal = 'Eagle'
elif food == 'BurgerKing':
    animal = 'Wolf'
elif food == 'Subway':
    animal = 'Hippo'


st.session_state['answers'].append(animal)



if st.button('Next Page'):
    switch_page('superhero')

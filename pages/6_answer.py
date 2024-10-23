import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from collections import Counter
result = Counter(st.session_state['answers']).most_common(1)[0][0]



st.markdown(f'<h1 style="font-size:100px;">YOU ARE A {result.upper()}</h1>', unsafe_allow_html=True)

if result == 'Gorilla':
	st.image('c.webp')
elif result == 'Eagle':
	st.image('b.webp')
elif result == 'Hippo':
	st.image('a.webp')
elif result == 'Wolf':
	st.image('d.webp')
	
if st.button('START AGAIN'):
	switch_page('main')
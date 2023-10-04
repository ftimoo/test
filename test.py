import streamlit as st

word1 = st.text_input('Movie title', 'Life of Brian')

word2 = st.text_input('Movie title', 'Life of Brian')

word3 = st.text_input('Movie title', 'Life of Brian')

st.button("Reset", type="primary")
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

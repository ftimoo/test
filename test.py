import streamlit as st

word1 = st.text_input('word1', '')

word2 = st.text_input('word2', '')

word3 = st.text_input('word3', '')

st.button("Reset", type="primary")
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

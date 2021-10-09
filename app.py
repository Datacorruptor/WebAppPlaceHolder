import streamlit as st
import German

name = st.text_input("Введите число немецкими словами")

if not name:
    st.warning("необходимо ввести число")
else:
    try:
        x = German.convert(name)
        st.warning(German.convert(name))
    except Exception as e:
        st.warning(e)


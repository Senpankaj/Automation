import streamlit as st

st.title('✌ My First App')

st.name = st.sidebar.text_input('Enter your name', key='Name')

#st.write(f'Hello {st.name}'+ ' 😜 ')

st.write('Hello ', st.name, ' 😜 ')


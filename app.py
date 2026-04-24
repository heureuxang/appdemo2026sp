import streamlit as st


# Title and Header
st.title("Hello")
st.header("ISOM3400")

st.write("**Bold Text** and *Italic Text*")

st.write("Hello, Streamlit!")
st.write(12345)
st.write({"Name": "Alice", "Age": 30})

age = st.number_input("Enter your age:",
                      min_value=0,
                      max_value=120,
                      value=25)
st.write(f"Your age is {age}")

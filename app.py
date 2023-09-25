import streamlit as st

import pickle

st.write("""## To Check Input is EVEN OR ODD""")

st.header('User Input Parameters')

def user_input_features():
    number = st.number_input("Enter the Positive Number",min_value=0,max_value=100000000000 ,step=1)
    result=None
    if st.button("Check"):
        result = "Even" if number%2 == 0 else "Odd"
    st.success(f"The given number is {result}")
    return number
user_input_features()

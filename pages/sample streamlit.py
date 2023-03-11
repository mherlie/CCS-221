import streamlit as st

# Define your Python code
my_code = """
def say_hello():
    print("Hello, world!")
    
say_hello()
"""

# Use the code function to display your code
st.code(my_code, language='python')

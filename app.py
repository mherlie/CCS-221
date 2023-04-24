import streamlit as st

# Your Python code goes here
def greet(name):
    print(f"Hello, {name}!")

# Display your Python code in Streamlit
st.code("""
    def greet(name):
        print(f"Hello, {name}!")
        
    greet("world")
""")

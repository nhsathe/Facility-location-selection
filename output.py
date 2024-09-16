import streamlit as st
import importlib
import pyomo.environ as pyo
from pyomo.environ import *
import pandas as pd

def load_model(objective):
    if objective == "P-Median":
        module = importlib.import_module('output_obj1')
    elif objective == "K-Center":
        module = importlib.import_module('output_obj2')
    elif objective == "MCLP":
        module = importlib.import_module('output_obj3')
    return module.model, module.Zipcode1

def main():
    st.title("Facility Location Selection")

    # Initialize session state
    if 'P' not in st.session_state:
        st.session_state.P = 3

    # Create a dropdown for objective selection
    o = st.selectbox(
        "Select objective",
        options=["P-Median", "K-Center", "MCLP"]
    )

    P = st.slider("Select number of support centers to be built", min_value=1, max_value=18, value=st.session_state.P)
    st.session_state.P = P  # Update session state

    d = pd.read_csv('Database.csv')
    st.write("Input data:")
    st.table(d)

    if st.button("Run Model"):
       
        model, Zipcode1 = load_model(o)
        
  
        st.write(f"Running {o} model with P = {P}")
     
        
        st.write("Model executed successfully. Results would be displayed here.")

if __name__ == "__main__":
    main()

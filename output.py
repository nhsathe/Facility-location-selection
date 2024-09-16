import streamlit as st
import importlib
import pyomo.environ as pyo
from pyomo.environ import *
import pandas as pd

def load_model(objective):
    # Reload the module to avoid caching issues
    if objective == "P-Median":
        module = importlib.import_module('output_obj1')
        importlib.reload(module)
    elif objective == "K-Center":
        module = importlib.import_module('output_obj2')
        importlib.reload(module)
    elif objective == "MCLP":
        module = importlib.import_module('output_obj3')
        importlib.reload(module)
    return module.model, module.Zipcode1

def main():
    st.title("Facility Location Selection")

    # Initialize session state if not set
    if 'P' not in st.session_state:
        st.session_state.P = 3

    # Create a dropdown for objective selection
    o = st.selectbox(
        "Select objective",
        options=["P-Median", "K-Center", "MCLP"]
    )

    # Slider for number of support centers
    P = st.slider("Select number of support centers to be built", min_value=1, max_value=18, value=st.session_state.P)
    st.session_state.P = P  # Update session state

    # Display input data
    d = pd.read_csv('Database.csv')
    st.write("Input data:")
    st.table(d)

    # Run model when button is clicked
    if st.button("Run Model"):
        # Load and run the model based on the selected objective
        model, Zipcode1 = load_model(o)
      

if __name__ == "__main__":
    main()

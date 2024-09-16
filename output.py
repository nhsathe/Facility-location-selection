# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 07:48:56 2022

@author: Nishank
"""

import streamlit as st
import importlib
import pyomo.environ as pyo
from pyomo.environ import *
import pandas as pd

if 'P' not in st.session_state:
    st.session_state.P = 3 

def clear_session_state():
    """Clears all keys in the session state."""
    for key in list(st.session_state.keys()):
        del st.session_state[key]


def main():
    st.title("Facility Location Seletion")

    # Create a dropdown for objective selection
    o = st.selectbox(
        "Select objective",
        options=["P-Median", "K-Center", "MCLP"]
    )
    P = st.slider("Select number of support centers to be built", min_value=1, max_value=18, value=st.session_state.P)
    st.session_state.P = P  # Update session state
    d=pd.read_csv ('Database.csv')
    st.write("Input data:")
    st.table(d)
    if st.button("Run Model"):  
        # Import the appropriate model based on user selection
        if o == "P-Median":
            from output_obj1 import model, Zipcode1
        elif o == "K-Center":
            from output_obj2 import model, Zipcode1
        elif o == "MCLP":
            from output_obj3 import model, Zipcode1
        else:
            pass
    clear_session_state()
    st.rerun()         
if __name__ == "__main__":
        main()

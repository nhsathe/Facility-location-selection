# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 07:48:56 2022

@author: Nishank
"""

import streamlit as st
import importlib
import pyomo.environ as pyo
from pyomo.environ import *

def main():
    st.title("Pyomo Model Selector")

    # Create a dropdown for objective selection
    o = st.selectbox(
        "Select objective number",
        options=[1, 2, 3],
        format_func=lambda x: f"Objective {x}"
    )

    if st.button("Run Model"):
        # Import the appropriate model based on user selection
        if o == 1:
            from output_obj1 import model, Zipcode1
        elif o == 2:
            from output_obj2 import model, Zipcode1
        else:
            from output_obj3 import model, Zipcode1
    pass
if __name__ == "__main__":
    main()

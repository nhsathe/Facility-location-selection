# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 07:48:56 2022

@author: Nishank
"""

import pyomo.environ as pyo
from pyomo.environ import *


import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
o=simpledialog.askinteger(title="User input",prompt="Enter objective number(e.g. 1,2,3):")

if o==1:
    from output_obj1 import model,Zipcode1 
elif o==2:
    from output_obj2 import model,Zipcode1
else:
    from output_obj3 import model,Zipcode1    
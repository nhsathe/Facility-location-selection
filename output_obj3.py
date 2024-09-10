
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 19:16:00 2022

@author: Nishank
"""

import pyomo.environ as pyo
from pyomo.environ import *
from projectcode_obj3 import model,Zipcode1 

solver= SolverFactory('glpk')
solver.solve(model)
print("Support centers should be built at zipcode locations:")
for i in model.I:
    if value(model.y[i]==1):print(Zipcode1[i-1])
         
   
for i in model.I: 
    if value(model.y[i]==1):
         print("Zipcodes assigned to support center at location",Zipcode1[i-1],"are:")
         for j in model.J:
             if value(model.x[i,j]==1):
                 print(Zipcode1[j-1])
                 
for i in model.I: 
    if value(model.y[i]==1):
         print("Distance of support center at location",Zipcode1[i-1],"from demand zipcode")
         for j in model.J:
             if value(model.x[i,j]==1):
                 print(Zipcode1[j-1],"is=",pyo.value(model.d[i,j]),"miles")                 

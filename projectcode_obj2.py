# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 19:36:18 2022

@author: Nishank
"""
import pyomo.environ as pyo
from pyomo.environ import *
from pulp import *
model = ConcreteModel(name = "Greenville_zip_codes")
import pandas as pd
import sys
import numpy as np
import streamlit as st
import plotly.express as px
P = st.session_state.P
d=pd.read_csv ('Database.csv')


d1=d.to_dict()

Zipcode = d1 ['zip code']
population = d1 ['estimated_population']
latitude = d1 ['latitude']
longitude = d1 ['longitude']



Zipcode1=d["zip code"].tolist()
population1 = d["estimated_population"].tolist()
latitude1= d["latitude"].tolist()
longitude1 = d["longitude"].tolist()



def spherical_dist(pos1, pos2, r=3958.75):
    
  
    pos1 = np.array(pos1,dtype=float)
    pos2 = np.array(pos2,dtype=float)
    pos1 = pos1 * np.pi / 180
    pos2 = pos2 * np.pi / 180
    cos_lat1 = np.cos(pos1[..., 0])
    cos_lat2 = np.cos(pos2[..., 0])
    cos_lat_d = np.cos(pos1[..., 0] - pos2[..., 0])
    cos_lon_d = np.cos(pos1[..., 1] - pos2[..., 1])
    return r * np.arccos(cos_lat_d - cos_lat1 * cos_lat2 * (1 - cos_lon_d))



 #Emtpy dataframe
dat = pd.DataFrame({'zip_code': Zipcode1 , 'lat':latitude1,  'lon':longitude1 })
dist_mat = pd.DataFrame(0, index=dat.zip_code, columns=dat.zip_code)
dist_mat




 #Populate
for i in range(18):
    for j in range(18):
        dist_mat.iloc[i, j] = spherical_dist([dat.iloc[i, 1], dat.iloc[i, 2]], [dat.iloc[j, 1], dat.iloc[j, 2]])
  
    print(dist_mat)      
    df = pd.DataFrame(dist_mat).T
#df.to_excel(excel_writer = "D:/MSIE sem 1/IE 8030 Engineering optimaiztion and applications/IE8030 Project/distance.xlsx")
#df.to_csv("D:/MSIE sem 1/IE 8030 Engineering optimaiztion and applications/IE8030 Project/distance.csv")
print(df)
st.write("Distance matrix:")
st.table(df)
#Create model
model= ConcreteModel(name = "Support center optimization")
model.I=Set(initialize=range(1,19))
model.J= Set(initialize=range(1,19))
#P=int(input("Enter number of support centers to be built:"))






model.x= Var(model.I,model.J, within=Binary)
model.y= Var(model.I, within=Binary)
model.p= Var(model.J, within=NonNegativeIntegers)
model.p= Set(initialize=population1) 
model.d= Var(model.I, model.J, within=NonNegativeReals)




for i in range(18):
     for j in range(18):
           
         model.d[i+1,j+1]= spherical_dist([dat.iloc[i, 1], dat.iloc[i, 2]], [dat.iloc[j, 1], dat.iloc[j, 2]])

                                                         



mu=sum(sum(model.x[i,j]*pyo.value(model.d[i,j]) for i in model.I) for j in model.J)
model.object= Objective(expr=mu,sense=minimize)
    
                        



def dual_objective_enforcement_rule(model,i,j):
        return (sum(sum(model.x[i,j]*pyo.value(model.d[i,j]) for i in model.I) for j in model.J)<=mu)
model.dual_objective_enforcement= Constraint(model.I,model.J,rule=dual_objective_enforcement_rule)

def zip_code_assignment_rule(model,j):
    return sum(model.x[i,j] for i in model.I)==1
model.zip_code_assignment= Constraint(model.J,rule=zip_code_assignment_rule)    


model.number_support_center= Constraint(expr =sum (model.y[i] for i in model.I)==P)
    
          
                        
    
def restrict_zipcode_assigment_rule(model,i,j):
    return model.x[i,j] <= model.y[i]   

model.restrict_zipcode_assigment= Constraint(model.I,model.J,rule=restrict_zipcode_assigment_rule)


support_centerlist = []   
    
#Solve
solver= SolverFactory('glpk')
solver.solve(model)

for i in model.I:
    if pyo.value(model.y[i]==1):
        print("Support center should be built at zipcodes", Zipcode1[i-1]) 
        #st.write(Zipcode1[i-1])
        zipcode = Zipcode1[i-1] 
        support_centerlist.append(zipcode)


st.write("Support centers should be built at zipcodes:") 
matched_data = d[d['zip code'].isin(support_centerlist)]
result = matched_data[['zip code', 'latitude', 'longitude']]
st.table(result)

fig = px.scatter_mapbox(result, lat='latitude', lon='longitude', hover_name='zip code',
                        zoom=10, height=800)
fig.update_layout(mapbox_style="open-street-map")
st.plotly_chart(fig)       
model.pprint()

 
print("Obj value =" +str(pyo.value(model.object)))
        
      
        
        
        
        









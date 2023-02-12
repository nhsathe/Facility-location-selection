Greenville County Outreach2all support center optimization model run guide.


This optimization model contains overall 7 python files. 

projectcode_obj1.py ---> Contains code for optimization based on objective 1 i.e. 'minimize overall distance'

projectcode_obj2.py --->Contains code for optimization based on objective 2 i.e. 'minimize maximum distance'

projectcode_obj3.py --->Contains code for optimization based on objective 3 i.e. 'maximize served population within 5 miles'

output_obj1.py ---> Contains code that handles display of optimization results of objective 1 in readable user freindly format 

output_obj2.py ---> Contains code that handles display of optimization results of objective 2 in readable user freindly format

output_obj3.py ---> Contains code that handles display of optimization results of objective 3 in readable user freindly format

output.py  ----> Contains code that allows user to select objective for optimization from above mentioned objectives i.e. 1,2,3 and displays results in  				readable user freindly format.This code provides flexibility of dynamically choosing objective function from single run.


Requirements : Anaconda with Spyder version 5.3.3 (Spyder version 5.3.3 is required to allow dynamic input from user), Pyomo, Gurobi solver, Pandas, 					tkinter(for dynamic user input), Numpy, Pulp.



Code imports data from a csv file named as 'Database.csv' that has data with column labels 'zip code', 'estimated_population', 'latitude', 'longitude'

Distance is calculated by using Haversine formula in python. Calculated distance is stored in a matrix dist_mat and exported to a csv file distance.csv (while running the code for the first time user has to set the directory in each projectcode_obj file)


User can either run individual output_obj file for respective objective funtion or a single output file 'output.py' that takes user input to select objective function.

When individual output_obj file is run a pop up window asks for number of support centers to be built i.e value of 'P'(e.g. 1,2,3 etc). User can input integer value.

When 'output.py' is run a pop up window will ask user to select objective for optimization. The input value and objective selection is as follows:

Value entered by user 						Objective selected
	1							'minimize overall distance'
	2							'minimize maximum distance'
	3							'maximize served population within 5 miles'

After selection of objective another pop up window asks for number of support centers to be built i.e value of 'P'(e.g. 1,2,3 etc). User can input integer value.

Objective value, selected support center locations, assignment of zipcodes to a particular support center and distance of each zipcode from the assigned support center are displayed on console in user readabel format.


Note: Python file 'alternate_projectcode_obj3.py' contains another approach for the formulation of objective 3. This formulation not only maximizes the served population within 5 miles but also allocates nearest support center to the zip codes that are not in 5 mile radius of any of the support center


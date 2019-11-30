import pandas as pd
import numpy as np
import math
import sys

# Dict of the assignment grades, since the grades are in percentages for zybooks 
# and we want them to be in points for canvas 
points_per_assignment = {"E8": 193, "E9": 110, "E10": 185}


def upload_grade(zy_file, final_file):
	grades = pd.read_csv(zy_file, encoding="utf-8")
	key = list(grades.Name)
	grade_dict = {}

	# hardcoded for each of the file values
	for k in key: 
		x = list ( round(( grades.loc[grades.Name == k, "E8"] / 100 ) * points_per_assignment.get("E8")) )
		y = list ( round(( grades.loc[grades.Name == k, "E9"] / 100 )  * points_per_assignment.get("E9")) )
		z = list ( round(( grades.loc[grades.Name == k, "E10"] / 100 ) * points_per_assignment.get("E10")) )
		add = x + y + z
		grade_dict[k] = add
	
	final = pd.read_csv(final_file, encoding="utf-8")
	for i in range(len(final)): 
		key_to_look_for = final["Student"][i]
		# print(key_to_look_for)
		try:
			grade = grade_dict[key_to_look_for]
			# set the grade
			final.loc[final.Student == key_to_look_for, 'E8 (4819005)'] = grade[0]
			final.loc[final.Student == key_to_look_for, 'E9 (4819007)'] = grade[1]
			final.loc[final.Student == key_to_look_for, 'E10 (4819008)'] = grade[2]
		except: 
			pass
	
	# write to file
	final.to_csv(final_file, encoding="utf-8")



def main():
	try: 
		# if args
		upload_grade(sys.argv[1]+".csv", sys.argv[3]+".csv")
		upload_grade(sys.argv[2]+".csv", sys.argv[3]+".csv")
	except: 
		# else
		# increases based on number of sections
		upload_grade("zybooks.csv", "final.csv")
		upload_grade("zybooks2.csv", "final.csv")



main()


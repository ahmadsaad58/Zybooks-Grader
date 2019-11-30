import pandas as pd
import numpy as np
import math
import sys

def upload_grade(id_file, test_file):
	grades = pd.read_csv(test_file, encoding="utf-8")
	key = list(grades.ID)
	value = list(grades.T2)
	# EID and Grade
	grade_dict = dict(zip(key, value))

	final = pd.read_csv(id_file, encoding="utf-8")
	for i in range(len(final)): 
		key_to_look_for = final["SIS Login ID"][i]
		try:
			grade = grade_dict[key_to_look_for]
			# set the grade
			final.loc[final.SIS == key_to_look_for, 'T2 (4834345)'] = int(grade)
		except: 
			pass
	
	# write to file
	final.to_csv(id_file, encoding="utf-8")



def main():
	try: 
		# if args
		upload_grade(sys.argv[1]+".csv", sys.argv[2]+".csv")
	except: 
		# else
		upload_grade("zybooks.csv", "final.csv")



main()


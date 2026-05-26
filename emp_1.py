employess={"emp_1":{ "emp_id":"MR01","emp_name":"Rakesh","emp_age":25,"emp_bg":["10->95%","Inter->92%","BTech->90%"],"emp_sal":100000,"emp_dep_id":1,
"emp_exp":2},
"emp_2":{ "emp_id":"MR02","emp_name":"Ram","emp_age":27,"emp_bg":["10->85%","Inter->92%","BTech->90%"],"emp_sal":100000,"emp_dep_id":2,
"emp_exp":2},
"emp_3":{ "emp_id":"MR03","emp_name":"Reehan","emp_age":29,"emp_bg":["10->90%","Inter->90%","BTech->90%"],"emp_sal":90000,"emp_dep_id":1,
"emp_exp":2},
"emp_4":{ "emp_id":"MR04","emp_name":"Manchu","emp_age":23,"emp_bg":["10->95%","Inter->92%","BTech->90%"],"emp_sal":70000,"emp_dep_id":3,
"emp_exp":1},
"emp_5":{ "emp_id":"MR05","emp_name":"Rocky","emp_age":25,"emp_bg":["10->80%","Inter->82%","BTech->80%"],"emp_sal":500000,"emp_dep_id":3,
"emp_exp":1} }
emp_info=input("Enter employye ID : ")
if emp_info==employess["emp_1"]["emp_id"]:
	print("Employee information is : \n",employess["emp_1"])
elif emp_info==employess["emp_2"]["emp_id"]:
	print("Employee information is : \n",employess["emp_2"])
elif emp_info==employess["emp_3"]["emp_id"]:
	print("Employee information is : \n",employess["emp_3"])
elif emp_info==employess["emp_4"]["emp_id"]:
	print("Employee information is : \n",employess["emp_4"])
elif emp_info==employess["emp_5"]["emp_id"]:
	print("Employee information is : \n",employess["emp_5"])
else:
	print("Invalid Employee ID ")

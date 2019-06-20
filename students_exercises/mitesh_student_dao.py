# Insert Staements(Insert random 100 students and then insert specific students)

def utility(studentinfo):
	st = ""
	for key in studentinfo.keys():
		if key == 'name':
			st = st + key + " = '" + studentinfo[key] + "', "
		elif key == 'id':
			continue
		else:
			st = st + key + " = " + str(studentinfo[key]) + ", "
	print "---------------- ", st
	return st
	
def insertrandomstudents(number):
	#st = ""
	for count in range(1, number):
		st = "INSERT INTO student (id, name, age) VALUES ('" + str(count) + "', " + "'name_" + str(count) + "', '" + str(count) + "');"
		print st
		
		
insertrandomstudents(10)
	
studentinfo = {'name': 'mitesh', 'age': 30, 'id': 1, 'phnumber':123}

def insertspecificstudent(studentinfo):
	st = "INSERT INTO student ("
	for key in studentinfo.keys():
		st = st + key + ", "
	
	st1 = st[:-2] + ") VALUES ("
	for key in studentinfo.keys():
		if studentinfo.keys() == 'name':
			st1 = st1 + "'" + studentinfo[key] + "',"
		else:
			st1 = st1 + "'" + str(studentinfo[key]) + "',"
	st2 = st1[:-1] + ");"
	print st2
insertspecificstudent(studentinfo)

# Update Student Records

studentinfo = {'name': 'mitesh', 'age': 30, 'id': 1}
def updatestudentrecords(studentinfo, id):
	st = "UPDATE student set "
	for key in studentinfo.keys():
		if key == 'name':
			st = st + key + " = '" + studentinfo[key] + "', "
		elif key == 'id':
			continue
		else:
			st = st + key + " = " + str(studentinfo[key]) + ", "
	st1 = st[: -2] + " where id = " + str (id)
	print st1

updatestudentrecords(studentinfo, 1)

id = [1,2,3]
def updatemultiplerecords(studentinfo, ids):
	st = "UPDATE student set "
	
	st = st + utility(studentinfo)
			
	in_condition = ""
	for id in ids:
		in_condition += str(id) + ","
	
	print st + in_condition

updatemultiplerecords(studentinfo, id)



	
studentinfo["asfdsdsd"] = "asdfsdfsdff"
studentinfo["asfdsdsdfsdfsdsd"] = "asdfsdfsdfxgfdfgdfgf"
utility(studentinfo)

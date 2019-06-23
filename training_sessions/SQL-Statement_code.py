# Insert Staements(Insert random 100 students and then insert specific students)

def utilityupdate(studentinfo):
	st = ""
	for key in studentinfo.keys():
		if key == 'name':
			st = st + key + " = '" + studentinfo[key] + "', "
		elif key == 'id':
			continue
		else:
			st = st + key + " = " + str(studentinfo[key]) + ", "
	return st

def utilityselect(studentinfo):
	st = ""
	for key in studentinfo.keys():
		if key == 'name':
			st = st + key + " = " + "'" + studentinfo[key] + "'" + "AND "
		elif key == id:
			continue
		elif key == 'age':
			st = st + key + " = " + "'" + str(studentinfo[key]) + "'" + " AND "
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

# Update Single Student Records

studentinfo = {'name': 'mitesh', 'age': 30, 'id': 1}
def updatestudentrecords(studentinfo, id):
	st = "UPDATE student set "
	st = st + utilityupdate(studentinfo)
	st = st[: -2] + " where id = "
	if studentinfo.has_key('id'):
		st = st + str(studentinfo[id])
	print st

updatestudentrecords(studentinfo, 1)

# Update multiple Student Records

id = [1,2,3]
def updatemultiplerecords(studentinfo, id):
	st = "UPDATE student set "
	st = st + utilityupdate(studentinfo)		
	st = st + " where id in ("
	for item in id:
		st = st + str(item) + ","
	st = st[:-1] + ");"
	print st
updatemultiplerecords(studentinfo, id)

# Select Student Records

def selectstudent(studentinfo):
	st = "SELECT * FROM student where "
	st = st + utilityselect(studentinfo) 
	st = st[:-4] + ";"
	print st
selectstudent(studentinfo)

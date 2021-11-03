import csv         #comma seperated file (creating a excel sheet)
with open("students.csv","w",newline="") as f:
	wri = csv.writer(f)   #function-->writer(file name)
	wri.writerow(["S_ID","S_NAME","S_ADREES"])
	count = int(input("Enter no. of students :"))
	for i in range(count):
		print("student", i+1)
		sid=int(input("enter ID: "))
		sname=input("Enter name: ")
		address=input("Enter Adress: ")
		wri.writerow([sid,sname,address])
f.close()

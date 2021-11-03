#pickle
import pickle
class Student:
	def __init__(self,sid,sname,saddress):
		self.sid=sid
		self.sname=sname
		self.saddress=saddress
	def display(self):
		print(self.sname)
with open("sdu.dat","wb") as f:
	s1 =Student(101,"abcvcd","chennai")
	pickle.dump(s1, f)     #picklng
with open("sdu.dat","rb") as f:
	ob=pickle.load(f)      #unpickling
	ob.display()

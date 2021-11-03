#file is there ,or not in loctaion
import os,sys
location=input("Enter file name with location: ")
if os.path.isfile(location):
	print("yes present..✔️")
	f=open(location,"r")
	lineCount=0
	charCount=0
	for line in f:
		charCount=charCount+len(line)
		lineCount+=1
	print(lineCount)
	print(charCount)  #counting white sapce , remove space--> split() function to using
	#print(f.read())
else:
	print("not present..❌️")

with open("name.txt","r") as f: #creating in read mode
	lines=f.readlines()
	for line in lines:
		print(line, end=" ")
	print(f.read(2))
	print(f.readline())
	print(f.read(3))
	
f.close()

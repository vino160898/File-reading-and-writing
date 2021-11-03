#binary datas(images) read and other location write
#image-->read-->bytes-->write-->image
f=open("/home/vino/Pictures/gcd.jpeg","rb")  #-->rb read binary mode
f2=open("/home/vino/Desktop/Untitled/123.png","wb")  #--.wb write binary mode
bytes=f.read()
f2.write(bytes)

file=open("ncsc.txt","a")
list=["\nB.tech","\nB.sc","\nM.sc","\nM.Tech"]
file.writelines(list)
file.close()
file2=open("ncsc.txt","r")
print(file2.read())
file2.close()

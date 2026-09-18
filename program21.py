file=open("ncsc.txt","w")
file.write("one\ntwo\nthree\nfour")
file.close()
file2=open("ncsc.txt","r")
print(file2.read())
file2.close

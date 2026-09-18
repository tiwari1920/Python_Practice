file=open("ncsc.txt","a")
file.write("\nfive\nsix\nseven")
file.close()
file2=open("ncsc.txt","r")
print(file2.read())
file2.close

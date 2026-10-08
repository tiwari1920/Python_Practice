# File concept in python to add new data (append) into an existing file using read() display data

file = open("myfile.txt", "a")  # Open a file in append mode
file.write("This is the third line of the file.\n")  # Append new data
file.write("This is the fourth line of the file.\n")  # Append another line
file.close()  # Close the file to save changes
file2 = open("myfile.txt", "r")  # Open the file in read
print(file2.read())  # Read and print the content of the file
file2.close()  # Close the file

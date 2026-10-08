# File concept in python to add new data(appending) to file using writelines() and readlines() to display data

file = open("myfile.txt", "a")  # Open a file in append mode
lines_to_append = ["This is the fifth line of the file.\n", "This is the sixth line of the file.\n"]  # Lines to append
file.writelines(lines_to_append)  # Append new data using writelines()
file.close()  # Close the file to save changes
file2 = open("myfile.txt", "r")  # Open the file in read mode
lines = file2.readlines()  # Read all lines of the file into a list
print("".join(lines))  # Print the content of the file
file2.close()  # Close the file

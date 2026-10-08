# File concept in python to create a file to write data into it

file = open("myfile.txt", "w")  # Open a file in write mode
file.write("Hello, this is a sample text.\n")  # Write data to the file
file.write("This is the second line of the file.\n")  # Write another line
file.close()  # Close the file to save changes
file2 = open("myfile.txt", "r")  # Open the file in read mode
content = file2.read()  # Read the content of the file
file2.close()  # Close the file
print(content)  # Print the content of the file

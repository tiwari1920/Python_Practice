# Python Program using the tkinter module to create a Student Registration Form with fields for Name, Age, Gender, and Course. The form includes a Submit button that saves the entered data to a file named "students.txt" and displays a success message upon submission.


import tkinter as tk
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("700x700")
root.configure(bg="lightblue")

#UID Portions

uidlabel = tk.Label(root, text="UID", font=("Arial", 12), bg="lightblue").place(x=100, y=50)
uidentry = tk.Entry(root, font=("Arial", 12)).place(x=200, y=50)

#Name Portions

namelabel = tk.Label(root, text="Name", font=("Arial", 12), bg="lightblue").place(x=100, y=100)
nameentry = tk.Entry(root, font=("Arial", 12)).place(x=200, y=100)

#Gender Portions
genderlabel = tk.Label(root, text="Gender", font=("Arial", 12), bg="lightblue").place(x=100, y=150)
gender = tk.StringVar()
gendermale = tk.Radiobutton(root, text="Male", variable=gender, value="Male", font=("Arial", 12), bg="lightblue").place(x=200, y=150)
genderfemale = tk.Radiobutton(root, text="Female", variable=gender, value="Female", font=("Arial", 12), bg="lightblue").place(x=300, y=150)

# Hobbies Portions
hobbieslabel = tk.Label(root, text="Hobbies", font=("Arial", 12), bg="lightblue").place(x=100, y=200)
hobby1 = tk.IntVar()
hobby2 = tk.IntVar()
hobby3 = tk.IntVar()
hobby4 = tk.IntVar()
tk.Checkbutton(root, text="Reading", variable=hobby1, font=("Arial", 12), bg="lightblue").place(x=200, y=200)
tk.Checkbutton(root, text="Traveling", variable=hobby2, font=("Arial", 12), bg="lightblue").place(x=300, y=200)
tk.Checkbutton(root, text="Sports", variable=hobby3, font=("Arial", 12), bg="lightblue").place(x=400, y=200)
tk.Checkbutton(root, text="Music", variable=hobby4, font=("Arial", 12), bg="lightblue").place(x=500, y=200)

#Registration Button
registerbutton = tk.Button(root, text="Register", font=("Arial", 12), bg="green", fg="white",).place(x=200, y=250)

#Mainloop
root.mainloop()
class   student:
  def  __init__(self,uid,name,course,marks):
    self.uid=uid
    self.name=name
    self.course=course
    self.marks=marks
  def display(self):
      print("uid=",self.uid)
      print("name=",self.name)
      print("course=",self.course)
      print("marks=",self.marks)
s1=student(48,"TIWARI","NCSC",100)
s1.display()
s2=student(10,"SATYAM","NCSC",10)
s2.display()

class   customer:
  def  __init__(self,Name,Ac_no,Balance):
    self.Name=Name
    self.Ac_no=Ac_no
    self.Balance=Balance
  def display(self):
      print("customer Name=",self.Name)
      print("Account No=",self.Ac_no)
      print("Account Balance=",self.Balance)
s1=customer("TIWARI",111725036048,100000)
s1.display()

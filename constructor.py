class add:
    def __init__(self,f,s):
     self.first = f
     self.second = s
    def display(self):
     print("First Number = ",self.first)
     print("Second Number = ",self.second)
     print("sum = ",self.first+self.second)
dc = add(10,20)
dc.display()

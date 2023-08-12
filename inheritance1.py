class employee:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark
        
    def show(self):
        print(f"The name is {self.name} mark in exam {self.mark}")
    
class programmer(employee):
        
      
 obj = employee("Tushar Davane",90.12)
 obj.show()        

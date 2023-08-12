class employee:
    def __init__(self,name):
       self.name = name
    def __len__(self):
     return self.name
    
    def __str__(self):
       return f"The name is employee is the {self.name}"
    def __repr__(self):
       return f"Employee '{(self.name)}'"
       
    def __call__(self):
       print("Hey i am good person")


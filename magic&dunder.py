# class employee:
#     def __init__(self):
#        self.name = "Tushar"


#     def __len__(self):
#      return self.name


#✔uppear code in the emplo.py file this code import in this file given below
from emplo  import employee


e = employee("Tushar")
print(e)
#method of counting the character __len__():
print("The lenght is",len(e.name))     
print(repr(e))
e()
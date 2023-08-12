class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def fromstr(cls,String):
        return cls(String.split("-")[0],String.split("-")[1])

e1 = employee("Tushar",120000)
print(e1.name)
print(e1.salary)

String = "Abhi-12333443"#abhi is the string.split("-")[0]&&&&&&1233343 is string.split("-")[1]

e2 = employee.fromstr(String)
print(e2.name)
print(e2.salary)

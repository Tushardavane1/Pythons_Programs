#dir()
x=[1,3,4,6,6]
print(dir(x))


#dict method used to convert the dictionary
class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
e1 = employee("Tushar",120000)
print(e1.__dict__)



#help() method in programm 



print(help(employee))

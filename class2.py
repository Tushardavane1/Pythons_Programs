class employee:
    def __init__(self,name,id,salay):
        self.name = name
        self.id = id
        self.salay = salay
           
    def show(self):
        print(f"The employee name is {self.name} and id is {self.id} and increase by salary is {self.salay}")
    def incre(self):
        if self.salay <= 45000:
            print("your salary is the increase by the 3000 ")

        else:
            print("No increment ")    
print("Enter your salary ")
a = employee("tushar Davane",122,int(input()))
a.incre()
a.show()  



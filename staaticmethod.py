class employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and wrok in the {self.company}") 
    @classmethod
    def changecom(cls,newcompany):
        cls.company = newcompany


e1= employee()
e1.name = "Tushar"
e1.changecom("Tesla")
e1.show()
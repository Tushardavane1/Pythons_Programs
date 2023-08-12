class employee:
    companyname = "infoses" #instance vari
    noofemployee = 0
    def __init__(self,name):
        self.name = name
        self.raise_amount= 0.02
        employee.noofemployee += 1

    def show(self):
        print(f"{self.name} is the wroking in {self.companyname} raise is the {self.raise_amount}")   
emp1 = employee("Tushar davane")
emp1.show()
emp2=employee("shubham Patil")
emp2.show()
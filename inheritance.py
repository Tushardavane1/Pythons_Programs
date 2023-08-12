class person:
    def __init__(self,surname,mark):
        self.surname = surname
        self.mark = mark
        
    def show(self):
        print(f"{self.surname} got the in exam {self.mark}")

class programmer(person):
    def showlan(self):
        print("default lan is the python")

e1=person(" Tushar Davane",90.12)
e1.show()
e2=programmer("Tushar Davane ",78.9)
e2.showlan()
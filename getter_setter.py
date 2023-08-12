class person:
    def __init__(self,surname,mark,name):
        self.surname = surname
        self.mark = mark
        self.name = name
    def name(self):
        return self.name
        
    def show(self):
        print(f"{self.name} {self.surname} got the in exam {self.mark}")

o=person("Davane",90.12,"Tushar")
o.show()



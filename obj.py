class person:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def student(self):
         print(f"student name is the {self.name} marks is the {self.marks}")

obj1=person("Tushar",91.22)
obj2=person("Amol",67.23)
obj1.student()
obj2.student()
list=[obj1.student,obj2.student]
print("list is the ",list)
          
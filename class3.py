class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        if marks >= 72:
            print("The first distruct class")
            cal = marks/10
            print("Ypur cgpa is the ",cal)
        else:
            cal = marks/10
            print("your cgpa is the ",cal) 
            print("First class ")    
    def shows(self):
        print(f"The student name is {self.name} and marks is {self.marks}")
obj = student("Tushar",89.00)
obj.shows()        

obj1 = student("Abhi",70.34)
obj1.shows()
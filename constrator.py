class person():

    def __init__(self,n,o):
       # print("hey i am a person")
        self.name = n
        self.occ = o
    def info(self):
        print(f"{self.name} is the {self.occ}")

a=person("tushar","developer")
b=person("shubham ","HR")
a.info()
b.info()

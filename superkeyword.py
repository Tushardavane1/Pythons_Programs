class parent:
    def parent_met(self):
        print("this the parent class ")
class child(parent):
    def child(self):
       print("this the child class")
       super().parent_met()
par = parent()
ch = child()



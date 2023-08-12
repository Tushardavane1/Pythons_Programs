
#keyword Argments of the function in pytohn
def info(name, age):
    print("Hii, my name is", name)
    print("My age is the ", age)
print("Case-1")
info("Tushar",34)
#in bottom is the wrong way the define invalid position arguments in the function in python
info(31,"Tushar")
    


# Python program to illustrate
# *args for variable number of arguments
def myFun(*argv):
    for arg in argv:
        print(arg)
 
 
myFun('Hello', 'Welcome', 34, 'GeeksforGeeks')  

num = int(input("Entre the numberto print"))
for i in range(1,num+1):
    if i == 34:
        break
    print(i)
        
i+=1  

#break state in python in break statement the loop will the break in example of break statement in python
num = int(input("Entre the numberto print"))

while True:
    if i == 34:
        break
    print(i)
i+=1    
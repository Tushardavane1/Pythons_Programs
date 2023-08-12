def add(x,y):
   return x + y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def mod(x,y):
    return x%y

print("select an operatoin")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
print("5.mod")

choice=input("enter the (1/2/3/4/5)")
num1=input("enter the  first number")
num2=input("enter the  second number")
if choice=='1':
    print(add(num1,num2))
elif choice=='2':
    print(sub(num1,num2))
elif choice=='3':
    print(mul(num1,num2))
elif choice=='4':
    print(div(num1,num2))
elif choice=='5':
    print(mod(num1,num2))


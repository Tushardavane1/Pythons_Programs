#walrus operator in python 3.8 
a = True
print(a:=False)

numbers = [1,2,3,4,5]

while(n := len(numbers)) > 0:
    print(numbers.pop())
    

#
names = ["Tushar","Abhi","Tushars"]

if(name := input("enter the names")) in names:
    print(f"hello {name}")

else:
    print("name is not found ")    



# foods = list()
# while True:
#     food = input("enter the fruits list::::--")
#     if food == "quit":
#         break
#     f=foods.append(food)


    #uppear program using the walrus operator
    foods = list()
    while (food := input("enter the fruit do you like")) != "quit":
        foods.append(food)
    
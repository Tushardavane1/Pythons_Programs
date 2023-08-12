#. Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.

a = 10
b = 4
c = 10

sum = a+b+c
print(sum)
for i in a,b,c:
    if i==10:
     sum=0
     print(sum)
else:
    print("nUMBERS ARE the not  equals")


# Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.

d = 10
e = 7
sum = d+e
print(sum)  


if sum>15 and sum<20:
   print(20)
else:
   print("not in the between 15 and 20")



#Write a Python program to add two objects if both objects are integers.

a = int(input("Enter the first object"))
b = int(input("enter tne second number"))

if a or b == int:
   sum = a+b
   print(sum)

else:
   print("Not addable")   
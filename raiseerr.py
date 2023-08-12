a=int(input("Enter the number between 5 and 12:::::"))


if (a<5):
    print("thank you122222quit")


elif (a<5  or  a>12):
      raise ModuleNotFoundError("you enter the wrong range value ")


else:
     for i in range(1,11):
         c=a*i
         print(f"{a}*{i}=",c)

print("thank you ")
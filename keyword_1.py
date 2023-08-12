def tushar():
   try:
      l=[1,2,3,4,5,5]
      i=int(input("enter the index::"))
      print(l[i])
      return 1
   except:
      print("some error occured")
      return 0
   finally:
      print(' i am executed in final\n')

x=tushar()
print(x)      
tu="welcome to my pa"
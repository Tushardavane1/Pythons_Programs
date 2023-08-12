def new_func():
        x=int(input("enter the x value "))
        match x:
            case 0:
                print("is zero")
            case 3 if x<4:
                print("is greater than 10")
            case _:
               print("weiyfye")
new_func()

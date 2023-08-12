def root(list):
    squre = []
    for i in list:
        squre.append(i**2)
    return squre    
mylist=[23,45,67]
result = root(mylist)
print(result)
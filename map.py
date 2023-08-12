def cube(x):
    return x*x
print(cube(6))

l=[1,2,3,4,5]

newl=list(map(cube,l))
print(newl)


#filter
def tush(a):
    return a>2
newl1= list(filter(tush,l))
print(newl1)
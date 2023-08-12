# def histogram( items ):
#     for n in items:
#         output = ''
#         times = n
#         while( times > 0 ):
#           output += '*'
#           times = times - 1
#         print(output)

# histogram([2, 3, 6, 5])



#finding the even numbers in given list


numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

for x in numbers:
    if x == 237:
        print(x)
        break
    elif x % 2 == 0:
        print(x)

#compute the area of the triangle
base = int(input("enter the base"))
height = int(input("Enter the height?"))

area= base*height

print(area)


#check the same element in the two list
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1.difference(color_list_2))
print("\nDifferenct of color_list_2 and color_list_1:")
print(color_list_2.difference(color_list_1))
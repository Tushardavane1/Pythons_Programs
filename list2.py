marks=[12,34,56]
print(marks)
print(type(marks))
print(marks[-3])
if 34 in marks :
    print("yes")
else:
    print("No")
new=12
marks.append(new)
print(marks)

# if "ushar" in "tushar":
#     print("yes")
# else:
#     print("No")
marks.sort()    
print(marks)
marks.count(12)
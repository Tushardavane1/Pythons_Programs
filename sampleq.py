# first and last element of the list
color_list = ["Red","Green","White" ,"Black"]
print(color_list[::-3])

#displaying the exam scedule

exam_st_date = (11, 12, 2014)
print(":%i / %i / %i"%exam_st_date)



#print month by given user

import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))
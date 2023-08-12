import time
import webbrowser
print("Enter website URL")
a=input("")
time.sleep(2)  

print("Enter the time  to waiting in second the website")

b = time.sleep(int(input()))


webbrowser.open(a)

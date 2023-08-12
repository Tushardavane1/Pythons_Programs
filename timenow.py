
from datetime import datetime
 
now_method = datetime.now()

# the current time.
currentTime = now_method.strftime("%H:%M:%S")
print("Current Time =", currentTime)
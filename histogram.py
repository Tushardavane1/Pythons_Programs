import matplotlib.pyplot as plt
x=[10,20,30,40,50,60,70,80,90,100]

plt.hist(x,bins=5)

plt.title("Histogram")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()
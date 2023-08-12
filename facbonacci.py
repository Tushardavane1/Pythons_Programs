nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

if nterms<=0:
    print("Enter the positive number")

else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
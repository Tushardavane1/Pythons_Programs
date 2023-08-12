# location of the file in the python 
import imp
print("Location of Python os module sources:")
print(imp.find_module('os'))
print("\nLocation of Python sys module sources:")
print(imp.find_module('datetime'))

r = float(input("Enter the radius of circle"))
a = lambda r:3.142*r*r
print(a(r))

   
def a_function( string ):    
    "This prints the value of length of string"    
    return len(string)    
    
# Calling the function we defined    
print( "Length of the string Functions is: ", a_function( "Functions" ) )    
print( "Length of the string Python is: ", a_function( "Python" ) )    
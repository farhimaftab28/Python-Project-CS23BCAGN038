#Arithmetic Operations:
a = 10
b = 5
print("Addition:", a + b)        
print("Subtraction:", a - b)      
print("Multiplication:", a * b)   
print("Division:", a / b)         

#Quadratic Operation:

import math
a = 1
b = -3
c = 2
d = b**2 - 4*a*c
if d >= 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("Roots are:", root1, "and", root2)
else:
    print("Roots are imaginary (complex numbers)")

#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("SOLVED EXAMPLE:")
print("Calculate the area of a circle with radius 5.5")
import math
radius = 5.5
area = math.pi * radius ** 2
print(f"Radius: {radius}")
print(f"Area: {area:.2f}")
print("-" * 50)


# In[6]:


import math
print("area of circle with radius 5.5")
r = 5.5
area = math.pi*r**2
print(f"The area of circle with radius 5.5 is {area:.4f}")


# In[12]:


print("Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577")
num = [3.14, 2.718, 1.618, 0.577]
n = len(num)
sum_num = sum(num)
average = (sum(num))/n

print(f"the average of given numbers is {average:.4f}")


# In[15]:


print("\nQuestion 2: Convert 98.6 Fahrenheit to Celsius")
 # (F = C * 9/5 + 32) #
Fahrenheit = 98.6
Celsius = 5/9*(Fahrenheit - 32)
print(Celsius)


# In[16]:


print("\nQuestion 3: Calculate compound interest on $1000 at 5.5% for 3 years")
P = 1000        # Principal
r = 5.5         # Interest rate (%)
t = 3           # Time (years)

# Compound interest calculation
A = P * (1 + r / 100) ** t
CI = A - P

# Output
print(f"Compound Interest after {t} years is: ${CI:.2f}")
print(f"Total Amount after {t} years is: ${A:.2f}")


# In[18]:


print("\nQuestion 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2")
a = 3.5
b = 4.2
hypotenuse = math.sqrt(a**2 + b**2)

print(f"The hypotenuse of a right triangle with sides 3.5 and 4.2 is {hypotenuse:.2f}")


# In[23]:


print("\nQuestion 5: Calculate the volume of a sphere with radius 7.8")
r = 7.8
volume_of_sphere = 4/3*(math.pi*r**3)
print(f"The volume of a sphere with radius 7.8 is {volume_of_sphere:.4f}")


# In[24]:


print("\nQuestion 6: Round 3.14159 to 3 decimal places")
num = 3.14159
print(f"{num:.3f}")


# In[27]:


print("\nQuestion 7: Calculate the percentage: 45 out of 67")
percentage = (45/67)*100
print(f"The percentage: 45 out of 67 is {percentage:.2f}%")


# In[30]:


print("\nQuestion 8: Find the square root of 23.456")
num = 23.456
square_root = num**(1/2)
print(f"The square root of 23.456 is {square_root:.2f}")


# In[31]:


print("\nQuestion 9: Calculate simple interest: Principal=2500, Rate=6.5%, Time=2.5 years")
P=2500
R=6.5
T=2.5
simple_intrest = (P * R * T) / 100
print(f"simple intrest = {simple_intrest:.2f}")


# In[34]:


print("\nQuestion 10: Convert 45.7 degrees to radians")

import math
degrees = 45.7
radians = math.radians(degrees)
print(f"45.7 degrees to radians is {radians:.3f}")


# In[ ]:





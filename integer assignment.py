#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("SOLVED EXAMPLE:")
print("Calculate the sum of first 5 even numbers")
first_5_even = [2, 4, 6, 8, 10]
sum_even = sum(first_5_even)
print(f"First 5 even numbers: {first_5_even}")
print(f"Sum: {sum_even}")
print("-" * 50)


# In[3]:


print("SOLVED EXAMPLE:")
print("Calculate the sum of first 5 even numbers")
sum_even = 0
for i in range(1, 6):
    sum_even += i * 2
print(sum_even)


# In[48]:


n = 5
  # formula to calculate sum of n even numbers is n*(n+1) #
sum_of_even = n*(n+1)
print(f"The sum first 5 even numbers is {sum_of_even} ")


# In[14]:


print("Question 1: Calculate the product of first 10 natural numbers")
def product(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

first_10_natural_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
product_of_numbers = product(first_10_natural_numbers)
print(f"First 10 natural numbers: {first_10_natural_numbers}")
print(f"Product: {product_of_numbers}")


# In[50]:


import math

n = 10
product = math.factorial(n)
print(f"Product of first 10 natural numbers is: {product}")


# In[20]:


print("Question 1: Calculate the product of first 10 natural numbers")
product = 1
for num in range(1, 11):
    product *= num
print(product)


# In[23]:


print("\nQuestion 2: Find the remainder when 156 is divided by 7")
remainder = 156 % 7
print(f"\n The remainder when 156 is divided by 7 is {remainder}")


# In[27]:


print("\nQuestion 3: Calculate the square of 25")
num=25**2
print(f" The square of 25 is {num}")


# In[37]:


print("\n Question 4: Find the cube root of 125")
num = 125**(1/3)
print(f" The cube root of 125 is {num}")


# In[38]:


print("\n Question 5:Calculate the sum of digits in number 12345")
num = [1, 2 ,3, 4, 5]
sum_of_digits = sum(num)
print(f"the sum of digits in number 12345 is {sum_of_digits}")


# In[15]:


print("\nQuestion 6: Check if 97 is a prime number")
number = 97
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


# In[30]:


print("\nQuestion 7: Find the factorial of 8")
import math

print("Factorial of 8 is", math.factorial(8))


# In[31]:


num = 8
print(f"The factorial of 8 is ",math.factorial(num))


# In[33]:


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
num = 8
print(f"Factorial of {number} is {factorial(number)}")


# In[34]:


num = 8
print(f"Factorial of {number} is {factorial(number)}")


# In[38]:


print("\nQuestion 8: Calculate the average of numbers: 15, 23, 31, 42, 56")
num = [15, 23, 31, 42, 56]
sum_num=sum(num)
n = len(num) 
average = (sum_num)/n
print(f"The average of the numbers (15, 23, 31, 42, 56) is {average}")


# In[39]:


print("\nQuestion 9: Find the greatest common divisor (GCD) of 48 and 36")

import math

a = 48
b = 36
gcd = math.gcd(a,b)

print(f"the greatest common divisor (GCD) of 48 and 36 is {gcd}")


# In[45]:


print("\nQuestion 10: Calculate the sum of first 20 odd numbers")
odd_numbers = [2 * i + 1 for i in range(20)]
print(f"the first 20 odd numbers are {odd_numbers}")
sum_num=sum(odd_numbers)
print(f"Sum of first 20 odd numbers is {sum_num}")


# In[47]:


num = 20
  # formula to calculate sum of n odd numbers is (n)^2 #
sum_of_odd = num**2
print(f"The sum of first 20 odd numbers is {sum_of_odd} ")


# In[ ]:





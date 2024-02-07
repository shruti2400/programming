#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Write a Python program to convert kilometers to miles?

km = 8
miles = km/1.60934

print("km to miles :" , miles)


# In[3]:


# 2.Write a Python program to convert Celsius to Fahrenheit?

c = 27
f = (9*c/5)+32

print("For Celsius = {} equivalent Fahrenheit = {}".format(c, f))


# In[7]:


# 3. Write a Python program to display calendar?
import calendar

year = 2024
month = 1

print(calendar.month(year,month))


# In[8]:


year = 2024
print(calendar.calendar(year))


# In[11]:


# 4. Write a Python program to solve quadratic equation?
import cmath

# Input coefficients of the quadratic equation
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the constant c: "))

# Calculate the discriminant
d = (b**2) - (4*a*c)

# Calculate roots
root1 = (-b + cmath.sqrt(d)) / (2*a)
root2 = (-b - cmath.sqrt(d)) / (2*a)

# Print the roots
print('\nFor quadratic equation {}x^2 + {}x + {}:'.format(a, b, c))
print("Root 1:", root1)
print("Root 2:", root2)


# In[12]:


# 5. Write a Python program to swap two variables without temp variable?

a = 8
b = 9

a , b = b, a

print("after swap a is : " , a)
print("after swap b is : " , b)



# In[ ]:





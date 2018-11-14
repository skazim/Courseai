

import sys
print ("Python version",sys.version)



# # Getting Started

# ### Two types Data type
# ##### Immutables and Immutables
# 
# #### Immutables Data types : Their address cannot be changed
# #### While Mutables Data Types : Their address can be changed 

# Example for Mutable Data types

class Person:
    def __init__(self, age):
        self.age= age

fab= Person(age=25)
print("Person Age is ",fab.age)
print("Person Address in Memory", id(fab),"Person age Address in Memory", id(fab.age))

print("++++++++++++++++++++++++++++++++++++")
fab.age= 26  # here age is changed
print("Person Age is ",fab.age)
print("Person Address in Memory", id(fab),"Person age Address in Memory", id(fab.age))
print("++++++++++++++++++++++++++++++++++++")

print("Notice that Person address In Memory is same while the age before it was pointing to 25 of Address" 
      " in Memory \nBut now it is pointing to 26 of Address in Memory")


# In[20]:


# Example for Mutable Data Types
x = 10
print(id(x))
y = 10
print(id(y))

x= 12 # here address is changed because x is pointing to 12 now
print(id(x)) 


# In[35]:


# Example for Immutable Data Types
n = [1,2,2,34,54,4,1]
print(n, type(n),id(n))
m= n 
print(m, type(m), id(m))
n.pop()
print(id(n), id(m)) # Since poping Element from a list does not changes the address of list (Immutables)


# ### Lets start with the Data types

# In[36]:


# Integer
a = 2 
print(a, type(a))


# In[44]:


# String 
name = "Syed Kazim Hussain"
print(name, type(name))

# Accessing element in string
print(name[0]) # Zeroth element
print(name[:10]) # from Zero to element 9, 10 exclusive
print(name[1:10:2]) # from index 1 to 9 , steps 2(skip one element then other)
print(name[1:10:3]) # from index 1 to 9


# In[47]:


# Boolean
a = True
print(a, type(a))
a = 1 
print(bool(a))


# In[63]:


# List
# # way of initializing List
a= list() 
print(a,type(a))

b= [1,2,3,4,5,6,7]
print(b,type(b))

c = [x for x in range(10)]
print(c,type(c))

d = list("Hello World")
print(d,type(d))

d.append('.')
print(d)
print(d.count('l'))


str1= 'lets learning python' 
[d.append(x) for x in str1]
print(d.count('l'))

# more methods
# t.index('K') tells the position of K
# t.insert(0,'M') inserts M at 0 position
# t.pop() remove last element in the list
# t.remove('K') removes K from List
# t.reverse() reverse the list
# t.sort() sorts the list
# t.clear() empty the list


# In[69]:


# Dictionary 

released = {
"iphone" : 2007,
"iphone 3G" : 2008,
"iphone 3GS" : 2009,
"iphone 4" : 2010,
"iphone 4S" : 2011,
"iphone 5" : 2012
}

for release in released:
    print (release)
    
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
for key,val in released.items():
    print (key, "=> ", val)
    
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

if 'iphone 4S' in released:
    print(released['iphone 4S'])
    released['iphone 4S'] = 'kazim'
    print(released['iphone 4S'])
    
    

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
testDict = {x: x**2 for x in range(1,10)}
print(type(testDict),testDict)

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# Ways of Initializing Dictionaries
a = dict(A=1, Z=-1)
b = {'A': 1, 'Z': -1}
c = dict(zip(['A', 'Z'], [1, -1]))
d = dict([('A', 1), ('Z', -1)])
e = dict({'Z': -1, 'A': 1})
print("Are they all same?")
print("Yes") if a == b == c == d == e else print("No") # Conditional Statement for 


# In[91]:


# List Comprehensions
# Example 1 for numbers from 0 to 10 
x = [a for a in range(10)]
print("Numbers from 0 to 10",x)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")



# Example 2 for Even numbers only
x = [a for a in range(10) if a % 2 == 0]
print("Even Numbers",x)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")



# Example 2 for Odd numbers only
x = [a for a in range(10) if a % 2 != 0]
print("Odd Numbers ",x)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")


# Example 3 
nums = [1,2,3,4,5]
letters = ['A','B','C','D','E']
multiples = [[n,l] for n in nums for l in letters]
print(multiples)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")



# Dictionary Comprehension
y = {x:x**2 for x in range(10) }
print("Dictionary for Squares",y)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# creating dict using loop
some_dict = {x:chr(65+x) for x in range(0,11)}
print(some_dict)


# In[94]:


# Functions
def even(x):
    evenList = [x for x in range(x* 2) if x % 2 == 0]
    return evenList
def odd(x):
    oddList = [x for x in range(x* 2) if x % 2 != 0]
    return oddList

def isprime(num):
    if num > 1:
        for i in range(2,num):
            if (num/2 )% i == 0:
                print(num, "is not a prime number")
                print(i,"times", num//i, "is", num)
                break
        else:
            print(num, "is a prime number")
def fabonacii(rang):
    #print("0 1")
    a= 0
    b= 1
    fabList=list()
    fabList.append(a)
    fabList.append(b)
    for i in range(1,rang):
        c = a + b
        fabList.append(c)
        a= b 
        b = c
    return fabList
print(even(10)) # Start 10 Even Numbers
print(odd(10)) # Start 10 Odd Numbers
isprime(10)
fabonacii(10)


# In[108]:



# Matrix Multiplication Simple
a = [[1, 2], [3, 4]]
b= [[5] ,[6]]
result = list()
for r in a: 
    for c in zip(*b):
        d = list()
        for i, j in zip(r,c):  
            d.append(i*j)
        result.append(sum(d))
print("Simple Matrix Multiplication",result)

# Matrix Multiplication using List Comprehension
def matrix_mult(a,b):
    return [[sum(i * j for i, j in zip(r, c)) for c in zip(*b)] for r in a]
result = matrix_mult(a,b)
print("Matrix Multiplication using List Comprehension",result)

# Matrix Multiplication using Library
import numpy as np
c = np.matmul(a,b)
print("Matrix Multiplication using Library",c)


# In[15]:


# lambda Functions 
double = lambda x : x*2 # double is function
print(double(4),type(double))

# Above function is same as 
def double(x):
    return x * 2
print(double(4))

# Some more Examples 

# Example 1 
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)

# Example 2 
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)


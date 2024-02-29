#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 1


# def keyword is used to create a function.

# In[27]:


def test_odd(l):
    l = []
    for i in range(1,25):
        if i % 2 == 0:
            l.append(i)
    return l


# In[28]:


test_odd(range(1,25))


# In[29]:


#Question 2


# *args is used to pass a variable number of arguments to a function whereas *kwargs is used to pass a keyword and variable length argument list.

# In[36]:


def test_arg(*args):
    return args


# In[38]:


test_arg('s',23,456)


# In[45]:


def test_kwargs(**kwargs):
    return kwargs


# In[46]:


test_kwargs(k='sonu',k1='monu')


# In[47]:


#Question 3


# Object that can be iterate from the collection of data is called iterator in python.
# iter() and next() function is used for iteration.

# In[65]:


l = [2,4,6,8,10,12,14,16,18,20]


# In[67]:


l = iter(l)


# In[68]:


for i in range(0,5):
    print(next(iter(l)))


# In[69]:


#Question 4


# The function which gives faster and easier way to iterate a object is called generator.
# The value returned by a yield does not save in main memory and it saves in local variable for the fast computation.

# In[74]:


def test_gen(m,n):
    for i in range(m,n):
        yield i


# In[76]:


for i in test_gen(0,10):
    print(i)


# In[77]:


#Question 5


# In[21]:


def prime():
    primes_list = [2]
    for i in range(2, 1000):
        is_prime = True
        for prime in primes_list:
            if i % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes_list.append(i)
            yield i


# In[28]:


for i in prime():
    print(i)


# In[29]:


for i in range(20):
    print(next(prime_gen))


# In[30]:


#Question 6


# In[32]:


n = 10
a,b = 0,1
counter = 0
while counter < n :
    print(a)
    c = a+b
    a = b
    b = c
    counter = counter + 1


# In[33]:


#Question 7


# In[35]:


s = "pwskills"


# In[38]:


[i for i in s]


# In[39]:


#Question 8


# In[45]:


num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("Palindrome")
else:
    print("Not a palindrome")


# In[42]:


#Question 9


# In[43]:


[i for i in range(0,100) if i%2 != 0]


# In[ ]:





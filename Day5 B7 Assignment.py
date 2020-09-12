#!/usr/bin/env python
# coding: utf-8

# # Make a Function for prime numbers and use Filter to filter out all the prime numbers from 1-2500

# In[1]:


def isPrime(x):
    for n in range(2,x):
        if x%n==0:
            return False
        else:
            return True

fltrObj=filter(isPrime, range(2500))
print ('Prime numbers between 1-2500:', list(fltrObj))


# # Make a Lambda function for capitalizing the whole sentence passed using arguments And map all the sentences in the List, with the lambda functions

# In[10]:


lst= ["hey this is sai" ,"i am in mumbai ,...."]


# In[11]:


lst


# In[12]:


lst_new=map(lambda x: x.title(),lst)


# In[13]:


list(lst_new)


# # Write a program to identify sub list [1,1,5] is there in the given list in the same order, if yes print “it’s a Match” if no then print “it’s Gone” in function.

# In[18]:


def list_contains(List1, List2): 
    check = "it’s Gone"
    for m in List1: 
        for n in List2: 
            if m == n: 
                check = "it’s a Match"
                return check                    
    return check 

List1 = [1,5,6,4,1,2,3,5] 
List2 = [1,1,5] 
print("Test Case#1 ", list_contains(List1, List2)) 

List1 = [4,3,6,7,9,2,3.6] 
List2 = [1,1,5] 
print("Test Case#2 ", list_contains(List1, List2)) 


# # samples for checking other methods using sublist

# In[19]:


test_list = [1,5,6,4,1,2,3,5]
sub_list = [1,1,5] 
  
print ("Original list : " + str(test_list)) 
print ("Original sub list : " + str(sub_list)) 
flag = 0
if(set(sub_list).issubset(set(test_list))): 
    flag = 1
      
# printing result 
if (flag) : 
    print ("Yes, it's a match") 
else : 
    print ("No, it's gone") 


# In[20]:


test_list = [1,5,6,5,1,2,3.6]
sub_list = [0,2,9] 
   
print ("Original list : " + str(test_list)) 
print ("Original sub list : " + str(sub_list)) 
flag = 0
if(set(sub_list).issubset(set(test_list))): 
    flag = 1
      
# printing result 
if (flag) : 
    print ("Yes, it's a match") 
else : 
    print ("No, it's gone") 


# In[ ]:





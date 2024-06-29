#!/usr/bin/env python
# coding: utf-8

# # General Instructions
# Change the filenames to LastName-FirstName_Section_M-N_2324_ITMGT2503 <br>
# __Ex. GAW-Adriel_SectionM_2324_ITMGT2503__

# # Question 1: Watch Your Words
# Your task is to count the number of times that each word was used in a movie script! Please be guided by the instructions below!

# #### 1a

# In[1]:


# First, to help guide you, here is a list containing tuples. Run this block of code to initialize the list
list_of_tuples = [('A',59),('B',100),('C',20),('D',88),('E',25),('F',38)]

list_of_tuples


# If we want to __sort this tuple according to the numerical value__, using the sort() without any other arguments will not suffice. But, diving a bit deeper into the sort() function, we can see that it can accept two parameters: 
# 
# - `key` which is what will be used as the basis for sorting
# - `reverse` which accepts a Boolean value to determine if the sorting will be ascending or descending
# 

# In[3]:


# execute this cell to see how the two arguments help us achieve the desired result

list_of_tuples.sort(key=lambda x: x[1], reverse=True)

print(list_of_tuples)


# #### 1b

# In[ ]:


# To formally start this problem:
# Load the "script.json" file and store it in the `jsondata` variable. 
# The dictionary will contain the "line number" (starting from 0) as the key, 
# and the lines itself as the value



# In[412]:


import json
with open(r"C:\Users\leeso\Downloads\script.json","r") as file:
    jsondata = json.load(file)

print(jsondata)


# #### 1c

# In[500]:


# To process the lines in the script, you need to do the following in chronological order:
#### Convert all characters to uppercase characters
#### Remove the following pieces of text: <P>, </P>, <B>, </B>, <I>, </I>
#### Remove all the unnecessary punctuation symbols denoted in the string below
unnecessary_punctuation = r"&$@[].,#()-\"!?’_;:/"

import json
with open(r"C:\Users\leeso\Downloads\script.json","r") as file:
    jsondata = json.load(file)

for k in jsondata:
    type(jsondata[k]) == str
    if type(jsondata[k]) == str: jsondata[k] = jsondata[k].upper()

listt = ['<P>', '</P>', '<B>', '</B>', '<I>', '</I>']
punctuations = list(unnecessary_punctuation)
keys = jsondata.keys()

for x in keys:
    for i in listt:
        jsondata[x]=jsondata[x].replace(i,"")

for x in keys:
    for s in punctuations:
        jsondata[x]=jsondata[x].replace(s," ")
        jsondata[x]=jsondata[x].replace(" '"," ")
        jsondata[x]=jsondata[x].replace("' "," ")
        jsondata[x]=jsondata[x].replace("\n"," ")

print(jsondata)


# In[ ]:





# #### 1d

# In[496]:


# From here, create a dictionary called `wordcount_dictionary` that will have the key:value pair of word:count
# But, only include words that are three (3) letters or more 
#[word:count]

wordcount_dictionary = {}
values = list(jsondata.values())

allvalues = ' '.join(values)
newallvalues = allvalues.split(" ")
words_set = set(newallvalues)

for x in words_set:
    newallvalues.count(x)
    wordcount_dictionary[x] = newallvalues.count(x)

wordcount_dictionary_list = list(wordcount_dictionary.items())
wordcount_dictionary_list.sort(key=lambda x: x[1], reverse=False)
wordcount_dictionary = dict(wordcount_dictionary_list)
wordcount_dictionary.popitem()

wordcount_dictionary_list = list(wordcount_dictionary.items())
wordcount_dictionary_list.sort(key=lambda x: x[1], reverse=True)
wordcount_dictionary = dict(wordcount_dictionary_list)


# In[498]:


# If there were no errors in the way you processed your data, 
# this should output "Looks Good!"  

import numpy as np
import pandas as pd 

df1 = pd.read_json("output_dictionary_Q1.json",typ="dictionary").sort_values()
df2 = pd.Series(wordcount_dictionary).sort_values()

assert df1.equals(df2), "The dictionaries are not equal. Please check your code again."

print("Looks Good!")


# #### 1e

# In[ ]:


# Afterwards, we want to convert that dictionary to a list containing tuples
# Create a list called "final_wordlist_of_tuples" containing tuples 
# Each tuple should be as follows: (word,count)
# Sort the list by `count` (the second element of the tuple) in descending order
# A correct sample is shown in the markdown cell below
# Hint: this can be done using lambda but you can use a regular function definition. 
# Make sure you go through the mini-tutorial at the start of this problem.




# ___<div align="center">Once sorted, this should be the output of the first five items.</div>___
# 
# |         |             |
# |:--------|------------:|
# | THE     |         830 |
# | JOY     |         585 |
# | AND     |         351 |
# | RILEY   |         326 |
# | SADNESS |         274 |

# # Question 2: Wait... What is LP Doing Here?
# I swear you don't need to do LP here. In fact, the LP formulation is already shown below! 

# #### LP Problem
# In the realm of Sanctoria, nestled deep within the misty forests and craggy mountains, lies the legendary dungeon of The Lost King. It is said to be filled with untold riches, ancient relics, and formidable monsters guarding its treasures. As the wise and benevolent ruler of Sanctoria, King Hexter has decided to assemble a daring raiding party to plunder the depths of the dungeon and reclaim its treasures for the kingdom.
# 
# As the illustrious ruler of Sanctoria, King Hexter is faced with the daunting task of assembling a formidable dungeon raiding party. The success of the raid hinges upon the careful selection and allocation of resources to hire Fighters, Rangers, and Clerics for the expedition into the depths of the Lost King’s home.
# 
# In the planning of this dungeon raid, the King’s advisors have provided him with the following: Gold: The kingdom's treasury can afford to spend no more than 18000 gold coins on hiring adventurers. Each Fighter costs 1000 gold coins, each Ranger costs 600 gold coins, and each Cleric costs 750 gold coins. Lumber: The construction of necessary equipment for each troop requires ample quality lumber. The kingdom has 12000 units of lumber available for the raid. Each Fighter requires 500 units, each Ranger requires 750 units, and each Cleric requires 300 units. Food: The raid will last several weeks so food must be kept and stored during the raid. The raid will be able to carry 1500 units of food available for the raid. Each Fighter requires 50 units, each Ranger requires 45 units, and each Cleric requires 75 units. Power: The power of the raiding party will dictate the level of the raid’s success. Each Fighter gives 10 points, each Ranger gives 12 points, each Cleric gives 16 points.
# 
# The King’s military advisors have also discussed strategies that will be employed in the raid: Having more Fighters than Rangers will bolster the raiding party's frontline defense To avoid casualties, each Cleric must have at most 3 Fighters that they are supporting

# # LP Formulation
# 
# **Decision Variables:**
# - (F): Number of Fighters
# - (R): Number of Rangers
# - (C): Number of Clerics
# 
# **Objective:** Maximize the power of the raiding party.
# 
# $$ \text{Maximize Z:  } 10F + 12R + 16C $$
# 
# 
# **Subject to:**
# 
# \begin{aligned}
# 1000F + 600R + 750C &\leq 18000 && \text{(Gold constraint)} \\
# 500F + 750R + 300C &\leq 12000 && \text{(Lumber constraint)} \\
# 50F + 45R + 75C &\leq 1500 && \text{(Food constraint)} \\
# F, R, C &\geq 0 && \text{(Non-negativity constraints)}
# \end{aligned}
# 

# In[288]:


# With the LP Formulation as a basis, find the optimal solution to the problem using Python
# Use the variable `optimal_Z` to store the value of the Maximum Z
# Use the variables `optimal_F`, `optimal_R`, and `optimal_C` to store 
# the optimal solution of Fighters, Rangers, and Clerics respectively
# Note: There may be multiple configurations of F, R, C to attain the Maximum Z. 
# Hint: Don't use your DecSci brain, use your Python programming brain

optimal_F = 0
optimal_R = 0
optimal_C = 0
zlist = []
for f in range(0,int(min(18000/1000,12000/500,1500/50))+1):
    for r in range(0,int(min(18000/600,12000/750,1500/45))+1):
        for c in range(0,int(min(18000/750,12000/300,1500/75))+1):      
            if 1000*f+600*r+750*c<=18000 and 500*f+750*r+300*c<=12000 and 50*f+45*r+75*c<=1500:
                zlist.append(10*f+12*r+16*c)

optimal_Z = max(zlist)

for f in range(0,int(min(18000/1000,12000/500,1500/50))+1):
    for r in range(0,int(min(18000/600,12000/750,1500/45))+1):
        for c in range(0,int(min(18000/750,12000/300,1500/75))+1):      
            if 10*f+12*r+16*c == optimal_Z and 1000*f+600*r+750*c<=18000 and 500*f+750*r+300*c<=12000 and 50*f+45*r+75*c<=1500:
                optimal_F = f
                optimal_R = r
                optimal_C = c


# In[502]:


# If there were no errors in the way you processed your data, 
# this should output "Looks Good!"  

assert optimal_Z == 344
assert (1000*optimal_F + 600*optimal_R + 750*optimal_C) <= 18000
assert (500*optimal_F + 750*optimal_R + 300*optimal_C) <= 12000
assert (50*optimal_F + 45*optimal_R + 75*optimal_C) <= 1500
print("Looks Good!")


# # Question 3: Collatz

# #### 3a

# The __Collatz Conjecture__ is a mathematical sequence defined as follows:
# 
# 1. Start with any positive integer n.
# 2. If n is even, divide it by 2 to get n / 2.
# 3. If n is odd, multiply it by 3 and add 1 to get 3n + 1.
# 4. Repeat the process with the resulting number.
# 5. The conjecture states that no matter which positive integer you start with, you will always eventually reach 1.

# As an example, the number 5 will follow this sequence:
# - Start at __`5`__
# - 5 is odd, so we multiply by 3 and adds 1 to get __`16`__
# - 16 is even, so we divide by 2 to get __`8`__
# - 8 is even, so we divide by 2 to get __`4`__
# - 4 is even, so we divide by 2 to get __`2`__
# - 2 is even, so we divide by 2 to get __`1`__
# - Since the number is 1, we stop the sequence. 
# 
# For the purposes of this problem, let's call the list containing the numbers __[5, 16, 8, 4, 2, 1]__ the __`Collatz Sequence`__. 
# 
# This sequence also has a __`Collatz Length`__ of 6, since the sequence cycled through 6 numbers.
# 
# The sequence also had a __`Max Collatz`__ of 16, since that was the highest number in the sequence. 
# 
# Lastly, the sequence had a __`Sequence Sum`__ of 36, since that is the sum of all the numbers in the sequence.

# In[274]:


def Collatz(start_number):
    '''
    Create a SINGLE FUNCTION that will return the
    `Collatz Sequence`, the `Collatz Length`,
    and the `Max Collatz` in a dictionary.

    The key-value pairs will be the following:
    "collatz_sequence": the list containing the numbers of the sequence
    "collatz_length": the length of the sequence
    "max_collatz": the maximum number achieved in the sequence
    "sequence_sum": the sum of all the numbers in the sequence 

    Parameters
    ----------
    start_number: int
        the number used to start the sequence

    Returns
    -------
    dictionary
        the dictionary containing the key-value pairs of the
        collatz_sequence, collatz_length, max_collatz, and sequence_sum
    '''
    n = start_number
    collatz_sequence = [start_number]

    while n!=1:
        if n%2 == 0:
            collatz_sequence.append(int(n/2))
            n = n/2
        if n%2 == 1 and n != 1:
            collatz_sequence.append(int(3*n+1))
            n = 3*n+1

    dictionary = {}
    dictionary["collatz_sequence"]=collatz_sequence
    dictionary["collatz_length"]=len(collatz_sequence)
    dictionary["max_collatz"]=max(collatz_sequence)
    dictionary["sequence_sum"]=sum(collatz_sequence)
    
    return(dictionary)


# In[ ]:





# #### 3b

# In[402]:


def Collatz_winner(number_list):
    '''
    Given a list of positive integers, return the `winner`
    among them. The `winner` is categorized as such:
        
        1. The number has the largest `collatz_length`; and
        2. The number has the largest `max_collatz`

    If there is no winner, then the function must return None

    Parameters
    ----------
    number_list: list
        a list of positive integers

    Returns
    -------
    integer (or NoneType)
        the "winner" that follows the specific criteria above
        returns a None if it does not meet all the criteria above
    '''
    number_list = list(number_list)
     
    dictionary = {}
    for x in number_list:
        dictionary[x]=[]

    for x in number_list:
        n = x
        collatz_sequence = [x]
        while n!=1:
            if n%2 == 0:
                collatz_sequence.append(int(n/2))
                n = n/2
            if n%2 == 1 and n != 1:
                collatz_sequence.append(int(3*n+1))
                n = 3*n+1
        dictionary[x].append(len(collatz_sequence))
        dictionary[x].append(max(collatz_sequence))

    length_list = []
    max_list = []

    for x in number_list:
        length_list.append(dictionary[x][0])
        max_list.append(dictionary[x][1])
        
    answer = -1
    for x in number_list:
        if dictionary[x][0] == max(length_list) and dictionary[x][1] == max(max_list):
            answer = x
    
    if answer == -1:
        answer = "None"

    return(answer)


# In[504]:


assert Collatz_winner(range(1,51)) == 27
assert Collatz_winner(range(1,10)) == 9
assert Collatz_winner(range(50,100)) == 97
assert Collatz_winner(range(50,100,4)) == 54
assert Collatz_winner(range(20,131,5)) == 110
assert Collatz_winner(range(75,180,9)) == 129


# In[ ]:





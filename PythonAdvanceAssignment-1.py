#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. Write a function that takes a list of lists and returns the value of all of the symbols in it, where each symbol adds or takes something from the total score. Symbol values:

# = 5
O = 3
X = 1
get_ipython().system(' = -1')
get_ipython().getoutput(' = -3')
get_ipython().getoutput('! = -5')

A list of lists containing 2 #s, a O, and a !!! would equal (0 + 5 + 5 + 3 - 5) 8.

If the final score is negative, return 0 (e.g. 3 #s, 3 !!s, 2 !!!s and a X would be (0 + 5 + 5 + 5 - 3 - 3 - 3 - 5 - 5 + 1) -3, so return 0.

Examples

check_score([
  ["#", "!"],
  ["!!", "X"]
]) ➞ 2

check_score([
  ["!!!", "O", "!"],
  ["X", "#", "!!!"],
  ["!!", "X", "O"]
]) ➞ 0


# In[1]:


d={'#':5,'O':3,'X':1,'!':-1,'!!':-3,'!!!':-5}
def flatten(t):
    #t=list(input("enter A list"))
    l = []
    a=[]
    for sublist in t:
        #print(sublist)
        for item in sublist:
            #print(item)
            l.append(item)
    #return flat_list
    for k,v in d.items():
        for i in l:
            if i==k:
                a.append(v)
            
    b=sum(a)
    if b<0:
        return 0
    else:
        return b  
    
    
flatten([["#","#","#"],["!!", "!!","!!"],["!!!","!!!","X"]])    


# 2.Create a function that takes a variable number of arguments, each argument representing the number of items in a group, and returns the number of permutations (combinations) of items that you could get by taking one item from each group.
# 
# Examples
# 
# combinations(2, 3) ➞ 6
# 
# combinations(3, 7, 4) ➞ 84
# 
# combinations(2, 3, 4, 5) ➞ 120
# 

# In[2]:


def combinations(*args):
    Multiply=1
    for i in args:
        Multiply=i*Multiply
    return Multiply

combinations(3, 7, 4)


# In[ ]:


3.Create a function that takes a string as an argument and returns the Morse code equivalent.

Examples

encode_morse("EDABBIT CHALLENGE") ➞ ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."

encode_morse("HELP ME !") ➞ ".... . .-.. .--.   -- .   -.-.--"

This dictionary can be used for coding:

char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}


# In[3]:


char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}
def encode_morse(string):
    l=[]
    for i in string:
        for k,v in char_to_dots.items():
            if i in k:
                l.append(v)
                combine=' '.join(l)
    return combine
            
            
encode_morse("EDABBIT CHALLENGE")


# 4.Write a function that takes a number and returns True if it's a prime; False otherwise. The number can be 2^64-1 (2 to the power of 63, not XOR). With the standard technique it would be O(2^64-1), which is much too large for the 10 second time limit.
# 
# Examples
# 
# prime(7) ➞ True
# 
# prime(56963) ➞ True
# 
# prime(5151512515524) ➞ False
# 

# In[4]:


def prime(num):
    # If given number is greater than 1
    if num > 1:

        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):
            # If num is divisible by any number between 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False
    
    
prime(5151512515524)


# In[ ]:


5.Create a function that converts a word to a bitstring and then to a boolean list based on the following criteria:

    1. Locate the position of the letter in the English alphabet (from 1 to 26).
    2. Odd positions will be represented as 1 and 0 otherwise.
    3. Convert the represented positions to boolean values, 1 for True and 0 for False.
    4. Store the conversions into an array.

Examples

to_boolean_list("deep") ➞ [False, True, True, False]
# deep converts to 0110
# d is the 4th alphabet - 0
# e is the 5th alphabet - 1
# e is the 5th alphabet - 1
# p is the 16th alphabet - 0

to_boolean_list("loves") ➞ [False, True, False, True, True]

to_boolean_list("tesh") ➞ [False, True, True, False]


# In[5]:


from string import ascii_lowercase
LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)}
def to_boolean_list(text):
    text = text.lower()
    numbers = [LETTERS[character] for character in text if character in LETTERS]
    ZeroOne=[0 if int(i)%2==0 else 1 for i in numbers]
    boolean=[True if i==1 else False for i in ZeroOne]
    return boolean

to_boolean_list("loves")


# In[ ]:





# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3.10.6 64-bit
#     language: python
#     name: python3
# ---
import streamlit as st
st.markdown('# Exercises')
#
# **Important**: Try to think of a recursive solution to the problems below yourself. Do not use the Internet, because you will ruin all the fun.

# ## 1. Sum
#
# Write a recursive function `sum(n)` that computes the sum of all numbers from 1 to n, where n is given as a parameter.
# +
code = """
def sum(n):
    if(n==1):
        return 1
    else:
        return n + sum(n-1)
"""
st.code(code, language='python')
def sum(n):
    if(n==1):
        return 1
    else:
        return n + sum(n-1)

print(sum(5))
# -

# ## 2. Sum_array
#
# Write a recursive function `sum_array(numbers)` that computes and returns the sum of all elements in an array, where the array is given as a parameter. You can return all elements except the first one of an array using:

names = ["Jeff", "Peter", "April"]
print(names[1:])

# +
numbers = [5, 7, 6, 5, 2, 1]

def sum_array(numbers):
    if(len(numbers) ==1):
        return numbers[0]
    return numbers[0] + sum_array(numbers[1:])

    
print(sum_array(numbers))
# -

# ## 3. Minimum
#
# Write a recursive function `minimum(numbers)` that finds and returns the minimum element in an array, where the array is given as a parameter.

# +
numbers = [5, 7, 2, 5, 15, 10]

def min(numbers,b=None):
    if(len(numbers) == 0):
        return b
    if(b == None):
        return min(numbers[1:],numbers[0])
    if(numbers[0]<b):
        return min(numbers[1:],numbers[0])
    return min(numbers[1:],b)
print(min(numbers))
# -

# ## 4. Reverse
#
# Write a function `reverse(word)` to reverse a string using recursion.

# +
animal = "hippopotamus"


    
# -

# ## 5. Is_palindrome
#
# Write a recursive function `is_palindrome(sentence)` that determines whether a string is a palindrome. A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward, such as madam or racecar or the number 10801.

# +
import re

original = "A man, a plan, a canal, Panama!"
# original = "Gate man sees name, garage man sees name tag."

sentence = re.sub('[^A-Za-z]', '', original)
sentence = sentence.lower()
print (sentence)


    
# -

# ## 6. Fibonacci
#
# Write a recursive function `fibonacci(n)` to print the Fibonacci sequence. In the Fibonacci sequence, each number is the sum of the previous two numbers:
#                                                                
# 1  1  2  3  5  8  13  21  34  55
#
# So fibonacci(9) gives 55.

# +



# -

# ## 7. Print_tree
#
# Consider the following `Node` class.

class Node:
    def __init__(self, name, parent = None):
        self.name = name
        self.children = []
        self.parent = parent
        if parent is not None:
            parent.add_child(self)

    def add_child(self, node):
        self.children.append(node)
        
    def get_children(self):
        return self.children


# Now use this class to code the following tree:
#         
# <img src="./resources/tree.png"  style="height: 250px"/>

udo = Node("Udo")
marc = Node("Marc", parent=udo)
# ...

# Finally write a recursive function `print_tree(node)` that prints all the descendants of a given node.

# +

    

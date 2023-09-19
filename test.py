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

# # Recursion
#
# Our first lesson is about recursion, a common method of simplification to divide a problem into subproblems of the same type.
# As a computer programming technique, this is called __divide and conquer__ and is the key to the design of many important algorithms. Recursion is not really needed to implement AI, but the knowledge of this programming technique will help us to understand the AI algorithms we will use in the following lessons. At the end of this lesson you will use recursion to solve your first pseudo-AI problem, namely _The Towers of Hanoi_.

# ## The Towers of Hanoi
#
# The Towers of Hanoi is a mathematical game or puzzle. It consists of three rods and a number of disks of different sizes. The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top.
#
# <img src="./resources/towers.jpg"  style="height: 250px"/>
#
# The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
#
# - Only one disk can be moved at a time.
# - Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
# - No larger disk may be placed on top of a smaller disk.

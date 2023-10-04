import streamlit as st
from simpleai.search import CspProblem, backtrack

word1 = st.text_input('word1', '')

word2 = st.text_input('word2', '')

word3 = st.text_input('word3', '')

def constraint_unique(variables, values):
    return len(values) == len(set(values))  # remove repeated values and count

def createNum(values):
    returnval = ""
    for i in values:
        returnval += str(values[i])
    return int(returnval)

def constraint_add(variables, values):
    factor1 = int(''.join(str(values[variables.index(c)]) for c in word1))
    factor2 = int(''.join(str(values[variables.index(c)]) for c in word2))
    result = int(''.join(str(values[variables.index(c)]) for c in word3))
    return (factor1 + factor2) == result

if word1 and word2 and word3:
    variables = []
    domains = {}
    for var in word1[0]+word2[0]+word3[0]:
        if var not in variables:
            variables.append(var.upper())
            domains[var] = list(range(1, 10))
    for var in word1+word2+word3:
        if var not in variables:
            variables.append(var.upper())
            domains[var] = list(range(0, 10))
    
    assert len(variables)<=10  , "To many diffyrent letter"
        
        
    # the list of values that each variable can take
    
    
    
    
    constraints = [
        (tuple(variables), constraint_unique),
        (tuple(variables), constraint_add),
    ]
    
    
    problem = CspProblem(tuple(variables), domains, constraints)
    
    output = backtrack(problem)
    st.write('\nSolutions:', output)


# coding: utf-8

# In[25]:

import nltk, re, pprint
import sys,os
import numpy as np

#nltk.download()
#sudo apt-get install python3-pil.imagetk #installation for tree visualization


# In[26]:

#Recursion

grammar = nltk.CFG.fromstring("""
  S  -> NP VP
  NP -> Det Nom | PropN
  Nom -> Adj Nom | N
  VP -> V Adj | V NP | V S | V NP PP
  PP -> P NP
  PropN -> 'Buster' | 'Chatterer' | 'Joe'
  Det -> 'A'
  N -> 'villager' | 'city' | 'property' | 'wife.'
  Adj  -> 'along' 
  V ->  'went' | 'sell' | 'city'
  P -> 'his' | 'with' | 'to' 
  """)

# sent = "the angry bear chased the frightened little squirrel"
sent = "A villager went to city to sell his property along with his wife."
tokens = sent.split()

#Parsing algorithm

# parser = nltk.RecursiveDescentParser(grammar)
# parser = nltk.ChartParser(grammar)
# parser = nltk.ChartParser(grammar, trace=2)
# parser = nltk.ShiftReduceParser(grammar)
parser = nltk.parse.BottomUpLeftCornerChartParser(grammar)

for tree in parser.parse(tokens):
    print(tree)
    tree.draw()


#If the command print(tree) produces no output, this is probably 
#because your sentence sent is not admitted by your grammar.


#To investigate call the parser with tracing set to be on...
#You can also check what productions are currently in the grammar 
#with the command


# for p in grammar2.productions():
#     print(p)


# In[35]:

groucho_grammar = nltk.CFG.fromstring("""
    S -> NP VP
    PP -> P NP | TO
    NP -> Det N | Det N PP | 'I' 
    VP -> V NP | VP PP | Adj
    Det -> 'A'
    N -> 'villager' | 'city' | 'property' | 'wife.'
    V -> 'went' | 'sell' | 'city'
    P -> 'his' | 'with' | 'to' 
    Adj  -> 'along' 
    """)

sent = "A villager went to city to sell his property along with his wife."
tokens = sent.split()
parser = nltk.ChartParser(groucho_grammar)
#parser = nltk.parse.BottomUpChartParser(grammar)
#parser = nltk.parse.BottomUpChartParser(grammar)
for tree in parser.parse(tokens):
    print(tree)
    tree.draw()


# In[34]:

groucho_grammar = nltk.CFG.fromstring("""
  S  -> NP VP
  NP -> Det Nom | PropN
  Nom -> Adj Nom | N
  VP -> V Adj | V NP | V S | V NP PP
  PP -> P NP
  PropN -> 'Buster' | 'Chatterer' | 'Joe'
  Det -> 'A'
  N -> 'villager' | 'city' | 'property' | 'wife.'
  Adj  -> 'along' 
  V ->  'went' | 'sell' | 'city'
  P -> 'his' | 'with' | 'to' 
 """)

sent = ['A', 'villager', 'went',  'to', 'city', 'to', 'sell', 'his', 'property', 'along', 'with', 'his', 'wife.']
parser = nltk.ChartParser(groucho_grammar)
for tree in parser.parse(sent):
    print(tree)
    tree.draw()


# In[ ]:




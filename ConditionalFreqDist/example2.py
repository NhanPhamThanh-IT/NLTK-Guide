# import ConditionalFreqDist() method from nltk 
from nltk.probability import ConditionalFreqDist 
from nltk.tokenize import word_tokenize 
     
# Create a reference variable for Class SExprTokenizer 
tk = ConditionalFreqDist() 
     
# Create a string input 
example = "N L P"
     
for word in word_tokenize(example): 
   condition = len(word) 
   tk[condition][word] += 1
     
print(tk)
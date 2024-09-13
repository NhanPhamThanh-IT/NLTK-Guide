# import StanfordTokenizer() method from nltk 
from nltk.tokenize.stanford import StanfordTokenizer 
     
# Create a reference variable for Class StanfordTokenizer 
tk = StanfordTokenizer() 
     
# Create a string input 
example = "This is your great author."
     
# Use tokenize method 
result = tk.tokenize(example) 
     
print(result) 
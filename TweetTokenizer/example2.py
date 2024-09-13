# import TweetTokenizer() method from nltk 
from nltk.tokenize import TweetTokenizer 
  
# Create a reference variable for Class TweetTokenizer 
tk = TweetTokenizer() 
  
# Create a string input 
example = ":-) <> () {} [] :-p"
  
# Use tokenize method 
result = tk.tokenize(example) 
  
print(result) 
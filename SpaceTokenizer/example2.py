# import SpaceTokenizer() method from nltk 
from nltk.tokenize import SpaceTokenizer 
     
# Create a reference variable for Class SpaceTokenizer 
tk = SpaceTokenizer() 
     
# Create a string input 
example = "The price\t of burger \nin BurgerKing is Rs.36.\n"
     
# Use tokenize method 
result = tk.tokenize(example) 
     
print(result) 
# import WhitespaceTokenizer() method from nltk 
from nltk.tokenize import WhitespaceTokenizer 
     
# Create a reference variable for Class WhitespaceTokenizer 
tk = WhitespaceTokenizer() 
     
# Create a string input 
example = "The price\t of burger \nin BurgerKing is Rs.36.\n"
     
# Use tokenize method 
result = tk.tokenize(example) 
     
print(result) 
# import TabTokenizer() method from nltk 
from nltk.tokenize import TabTokenizer 
     
# Create a reference variable for Class TabTokenizer 
tk = TabTokenizer() 
     
# Create a string input 
example = "The price\t of burger \tin BurgerKing is Rs.36.\n"
     
# Use tokenize method 
result = tk.tokenize(example) 
     
print(result) 
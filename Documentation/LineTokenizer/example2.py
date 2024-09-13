# import LineTokenizer() method from nltk 
from nltk.tokenize import LineTokenizer 
     
# Create a reference variable for Class LineTokenizer 
tk = LineTokenizer(blanklines ='keep') 
     
# Create a string input 
example = "The price\n\n of burger \nin BurgerKing is Rs.36.\n"
     
# Use tokenize method 
result = tk.tokenize(example) 
     
print(result)
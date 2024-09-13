# import WhitespaceTokenizer() method from nltk 
from nltk.tokenize import WhitespaceTokenizer 
     
# Create a reference variable for Class WhitespaceTokenizer 
tk = WhitespaceTokenizer() 
     
# Create a string input 
example = "Nhan Pham \nis\t a student"
     
# Use tokenize method 
result = tk.tokenize(example) 
     
print(result) 
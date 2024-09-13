# import TabTokenizer() method from nltk 
from nltk.tokenize import TabTokenizer 
     
# Create a reference variable for Class TabTokenizer 
tk = TabTokenizer() 
     
# Create a string input 
example = "Geeksfor\tGeeks..\t.$$&* \nis\t for geeks"
     
# Use tokenize method 
result = tk.tokenize(example) 
     
print(result) 
# import MWETokenizer() method from nltk 
from nltk.tokenize import MWETokenizer 
   
# Create a reference variable for Class MWETokenizer 
tk = MWETokenizer([('n', 'i', 's'), ('nhan', 'is', 'student')]) 
tk.add_mwe(('who', 'are', 'you')) 
   
# Create a string input 
example = "who are you at nhan is student"
   
# Use tokenize method 
result = tk.tokenize(example.split()) 
   
print(result)
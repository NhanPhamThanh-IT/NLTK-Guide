# import MWETokenizer() method from nltk 
from nltk.tokenize import MWETokenizer 
   
# Create a reference variable for Class MWETokenizer 
tk = MWETokenizer([('n', 'i', 's'), ('nhan', 'is', 'student')]) 
   
# Create a string input 
example = "nhan is student n i s"
   
# Use tokenize method 
result = tk.tokenize(example.split()) 
   
print(result)
# import LineTokenizer() method from nltk 
from nltk.tokenize import LineTokenizer 
     
# Create a reference variable for Class LineTokenizer 
tk = LineTokenizer() 
     
# Create a string input 
example = "Nhan Pham...$$&* \nis\n a student."
     
# Use tokenize method 
result = tk.tokenize(example) 
     
print(result) 
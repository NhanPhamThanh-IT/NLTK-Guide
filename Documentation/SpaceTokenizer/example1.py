# import SpaceTokenizer() method from nltk 
from nltk.tokenize import SpaceTokenizer 
     
# Create a reference variable for Class SpaceTokenizer 
tk = SpaceTokenizer() 
     
# Create a string input 
example = "Thanh Nhan Pham.. .$$&* \nis\t a student"
     
# Use tokenize method 
result = tk.tokenize(example) 
     
print(result)
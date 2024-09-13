import nltk   
from nltk.metrics.distance import edit_distance 

nltk.download('words') 
from nltk.corpus import words 
correct_words = words.words() 

# list of incorrect spellings 
# that need to be corrected  
incorrect_words=['happpy', 'azmaing', 'intelliengt'] 
  
# loop for finding correct spellings 
# based on edit distance and 
# printing the correct words 
for word in incorrect_words: 
    temp = [(edit_distance(word, w),w) for w in correct_words if w[0]==word[0]] 
    print(sorted(temp, key = lambda val:val[0])[0][1]) 
import nltk   
from nltk.metrics.distance import edit_distance 

# Downloading and importing package 'words' 
nltk.download('words') 
from nltk.corpus import words 
correct_words = words.words() 
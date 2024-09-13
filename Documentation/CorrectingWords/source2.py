# Downloading and importing package 'words' from nltk corpus 
import nltk

nltk.download('words') 
from nltk.corpus import words 

correct_words = words.words()

print(correct_words)
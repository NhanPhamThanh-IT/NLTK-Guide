from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
 
# Another sample text
new_text = "The quick brown fox jumps over the lazy dog."
 
# Tokenize the new text using NLTK
new_words = word_tokenize(new_text)
 
# Remove stopwords using NLTK
new_filtered_words = [
    word for word in new_words if word.lower() not in stopwords.words('english')]
 
# Join the filtered words to form a clean text
new_clean_text = ' '.join(new_filtered_words)
 
print("Original Text:", new_text)
print("Text after Stopword Removal:", new_clean_text)
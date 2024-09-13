from gensim.parsing.preprocessing import remove_stopwords
 
# Another sample text
new_text = "The majestic mountains provide a breathtaking view."
 
# Remove stopwords using Gensim
new_filtered_text = remove_stopwords(new_text)
 
print("Original Text:", new_text)
print("Text after Stopword Removal:", new_filtered_text)
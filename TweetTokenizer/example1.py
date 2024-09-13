from nltk.tokenize import TweetTokenizer

# Create a reference variable for class TweetTokenizer
tk = TweetTokenizer()

# Create a string input
example = "Pham Thanh Nhan"

# Use tokenize method
result = tk.tokenize(example)

print(result)
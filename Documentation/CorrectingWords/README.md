<div align="justify">

__nltk__ stands for Natural Language Toolkit and is a powerful suite consisting of libraries and programs that can be used for statistical natural language processing. The libraries can implement tokenization, classification, parsing, stemming, tagging, semantic reasoning, etc. This toolkit can make machines understand human language. 

We are going to use two methods for spelling correction. Each method takes a list of misspelled words and gives the suggestion of the correct word for each incorrect word. It tries to find a word in the list of correct spellings that has the shortest distance and the same initial letter as the misspelled word. It then returns the word which matches the given criteria. The methods can be differentiated on the basis of the distance measure they use to find the closest word.  ‘words’ package from nltk is used as the dictionary of correct words.

## Method 1: Using Jaccard distance Method

Jaccard distance, the opposite of the Jaccard coefficient, is used to measure the dissimilarity between two sample sets. We get Jaccard distance by subtracting the Jaccard coefficient from 1. We can also get it by dividing the difference between the sizes of the union and the intersection of two sets by the size of the union. We work with Q-grams (these are equivalent to N-grams) which are referred to as characters instead of tokens. Jaccard Distance is given by the following formula.

<div align="center">
    <img src="https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-ee197189b1464aa2bb166f8234c6ee66_l3.svg">
</div>

### Stepwise implementation

__Step 1__: First, we install and import the nltk suite and Jaccard distance metric that we discussed before. ‘ngrams’ are used to get a set of co-occurring words in a given window and are imported from nltk.utils package.

<a href=""><strong>Click here to view source code</strong></a>

__Step 2__: Now, we download the ‘words’ resource (which contains the list of correct spellings of words) from the nltk downloader and import it through nltk.corpus and assign it to correct_words.

<a href=""><strong>Click here to view source code</strong></a>

__Step 3__: We define the list of incorrect_words for which we need the correct spellings. Then we run a loop for each word in the incorrect words list in which we calculate the Jaccard distance of the incorrect word with each correct spelling word having the same initial letter in the form of bigrams of characters. We then sort them in ascending order so the shortest distance is on top and extract the word corresponding to it and print it.

<a href=""><strong>Click here to view source code</strong></a>

## Method 2: Using Edit distance Method

Edit Distance measures dissimilarity between two strings by finding the minimum number of operations needed to transform one string into the other. The transformations that can be performed are:

### Inserting a new character

```
bat -> bats (insertion of 's')
```

### Deleting an existing character

```
care -> car (deletion of 'e')
```

### Substituting an existing character

```
bin -> bit (substitution of n with t)
```

### Transposition of two existing consecutive characters

```
sing -> sign (transposition of ng to gn)
```

### Stepwise implementation

__Step 1__: First of all, we install and import the nltk suite.

<a href=""><strong>Click here to view source code</strong></a>

__Step 2__: Now, we download the ‘words’ resource (which contains correct spellings of words) from the nltk downloader and import it through nltk.corpus and assign it to correct_words.

<a href=""><strong>Click here to view source code</strong></a>

__Step 3__: We define the list of incorrect_words for which we need the correct spellings. Then we run a loop for each word in the incorrect words list in which we calculate the Edit distance of the incorrect word with each correct spelling word having the same initial letter. We then sort them in ascending order so the shortest distance is on top and extract the word corresponding to it and print it.

<a href=""><strong>Click here to view source code</strong></a>

</div>
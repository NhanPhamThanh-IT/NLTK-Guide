<div align="justify">

## Tokenization

Tokenization refers to break down the text into smaller units. It entails splitting paragraphs into sentences and sentences into words. It is one of the initial steps of any NLP pipeline. Let us have a look at the two major kinds of tokenization that NLTK provides:

### Work Tokenization

It involves breaking down the text into words.

```
"I study Machine Learning on GeeksforGeeks." will be word-tokenized as
['I', 'study', 'Machine', 'Learning', 'on', 'GeeksforGeeks', '.']. 
```

### Sentence Tokenization

It involves breaking down the text into individual sentences.

__Example__

"I study Machine Learning on GeeksforGeeks. Currently, I'm studying NLP" will be sentence-tokenized as ['I study Machine Learning on GeeksforGeeks.', 'Currently, I'm studying NLP.']

In Python, both these tokenizations can be implemented in NLTK as follows:

```py
# Tokenization using NLTK
from nltk import word_tokenize, sent_tokenize
sent = "GeeksforGeeks is a great learning platform.\
It is one of the best for Computer Science students."
print(word_tokenize(sent))
print(sent_tokenize(sent))
```

__Output__

```
['GeeksforGeeks', 'is', 'a', 'great', 'learning', 'platform', '.','It', 'is', 'one', 'of', 'the', 'best', 'for', 'Computer', 'Science', 'students', '.']
['GeeksforGeeks is a great learning platform.', 'It is one of the best for Computer Science students.']
```

## Stemming and Lemmatization

When working with Natural Language, we are not much interested in the form of words – rather, we are concerned with the meaning that the words intend to convey. Thus, we try to map every word of the language to its root/base form. This process is called canonicalization.

__E.g__. The words ‘play’, ‘plays’, ‘played’, and ‘playing’ convey the same action – hence, we can map them all to their base form i.e. ‘play’

Now, there are two widely used canonicalization techniques: __Stemming__ and __Lemmatization__.

### Stemming

Stemming generates the base word from the inflected word by removing the affixes of the word. It has a set of pre-defined rules that govern the dropping of these affixes. It must be noted that stemmers might not always result in semantically meaningful base words.  Stemmers are faster and computationally less expensive than lemmatizers. 

In the following code, we will be stemming words using Porter Stemmer – one of the most widely used stemmers:

```py
from nltk.stem import PorterStemmer

# create an object of class PorterStemmer
porter = PorterStemmer()
print(porter.stem("play"))
print(porter.stem("playing"))
print(porter.stem("plays"))
print(porter.stem("played"))
```

__Output__

```
play
play
play
play
```

We can see that all the variations of the word ‘play’ have been reduced to the same word  – ‘play’. In this case, the output is a meaningful word, ‘play’. However, this is not always the case. Let us take an example. 

Please note that these groups are stored in the lemmatizer; there is no removal of affixes as in the case of a stemmer.

```py
from nltk.stem import PorterStemmer
# create an object of class PorterStemmer
porter = PorterStemmer()
print(porter.stem("Communication"))
```

__Output__

```
commun
```

The stemmer reduces the word ‘communication’ to a base word ‘commun’ which is meaningless in itself.

### Lemmatization

Lemmatization involves grouping together the inflected forms of the same word. This way, we can reach out to the base form of any word which will be meaningful in nature. The base from here is called the Lemma.

Lemmatizers are slower and computationally more expensive than stemmers.

__Example__

```
'play', 'plays', 'played', and 'playing' have 'play' as the lemma.
```

In Python, both these tokenizations can be implemented in NLTK as follows:

```py
from nltk.stem import WordNetLemmatizer
# create an object of class WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("plays", 'v'))
print(lemmatizer.lemmatize("played", 'v'))
print(lemmatizer.lemmatize("play", 'v'))
print(lemmatizer.lemmatize("playing", 'v'))
```

__Output__

```
play
play
play
play
```

Please note that in lemmatizers, we need to pass the Part of Speech of the word along with the word as a function argument.

Also, lemmatizers always result in meaningful base words. Let us take the same example as we took in the case for stemmers.

```py
from nltk.stem import WordNetLemmatizer

# create an object of class WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("Communication", 'v'))
```

__Output__

```
Communication
```

## Part of Speech Tagging

Part of Speech (POS) tagging refers to assigning each word of a sentence to its part of speech. It is significant as it helps to give a better syntactic overview of a sentence.

__Example__

```
"GeeksforGeeks is a Computer Science platform."
Let's see how NLTK's POS tagger will tag this sentence.
```

In Python, both these tokenizations can be implemented in NLTK as follows:

```py
from nltk import pos_tag
from nltk import word_tokenize

text = "GeeksforGeeks is a Computer Science platform."
tokenized_text = word_tokenize(text)
tags = tokens_tag = pos_tag(tokenized_text)
tags
```

__Output__

```
[('GeeksforGeeks', 'NNP'),
 ('is', 'VBZ'),
 ('a', 'DT'),
 ('Computer', 'NNP'),
 ('Science', 'NNP'),
 ('platform', 'NN'),
 ('.', '.')]
```

## Conclusion

In conclusion, the Natural Language Toolkit (NLTK) works as a powerful Python library that a wide range of tools for Natural Language Processing (NLP). From fundamental tasks like text pre-processing to more advanced operations such as semantic reasoning, NLTK provides a versatile API that caters to the diverse needs of language-related tasks.

</div>
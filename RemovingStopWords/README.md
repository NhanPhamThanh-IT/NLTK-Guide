<div align="justify">

In __natural language processing (NLP)__, stopwords are frequently filtered out to enhance text analysis and computational efficiency. Eliminating stopwords can improve the accuracy and relevance of NLP tasks by drawing attention to the more important words, or content words. The article aims to explore stopwords.

Certain words, like “the,” “and,” and “is,” are thought to be ineffective for communicating important information. The objective of eliminating words that add little or nothing to the comprehension of the text is to expedite text processing, even though the list of stopwords may differ.

### What are Stop words?

A stop word is a commonly used word (such as “the”, “a”, “an”, or “in”) that a search engine has been programmed to ignore, both when indexing entries for searching and when retrieving them as the result of a search query.

We would not want these words to take up space in our database or take up valuable processing time. For this, we can remove them easily, by storing a list of words that you consider to stop words. NLTK(Natural Language Toolkit) in Python has a list of stopwords stored in 16 different languages. You can find them in the nltk_data directory. home/PratimaPython/nltk_data/corpora/stopwords are the directory address. or (Do not forget to change your home directory name)

### Need to remove the Stopwords

The necessity of removing stopwords in NLP is contingent upon the specific task at hand. For text classification tasks, where the objective is to categorize text into distinct groups, excluding stopwords is common practice. This is done to channel more attention towards words that truly convey the essence of the text. As illustrated earlier, certain words like “there,” “book,” and “table” contribute significantly to the text’s meaning, unlike less informative words such as “is” and “on.”.

Conversely, for tasks like machine translation and text summarization, the removal of stopwords is not recommended. In these scenarios, every word plays a pivotal role in preserving the original meaning of the content.

### Types of Stopwords

Stopwords are frequently occurring words in a language that are frequently omitted from natural language processing (NLP) tasks due to their low significance for deciphering textual meaning. The particular list of stopwords can change based on the language being studied and the context. The following is a broad list of stopword categories:

- __Common Stopwords__: These are the most frequently occurring words in a language and are often removed during text preprocessing. Examples include “the,” “is,” “in,” “for,” “where,” “when,” “to,” “at,” etc.
- __Custom Stopwords__: Depending on the specific task or domain, additional words may be considered as stopwords. These could be domain-specific terms that don’t contribute much to the overall meaning. For example, in a medical context, words like “patient” or “treatment” might be considered as custom stopwords.
- __Numerical Stopwords__: Numbers and numeric characters may be treated as stopwords in certain cases, especially when the analysis is focused on the meaning of the text rather than specific numerical values.
- __Single-Character Stopwords__: Single characters, such as “a,” “I,” “s,” or “x,” may be considered stopwords, particularly in cases where they don’t convey much meaning on their own.
- __Contextual Stopwords__: Words that are stopwords in one context but meaningful in another may be considered as contextual stopwords. For instance, the word “will” might be a stopword in the context of general language processing but could be important in predicting future events.

### Checking English Stopwords List

An English stopwords list typically includes common words that carry little semantic meaning and are often excluded during text analysis. Examples of these words are “the,” “and,” “is,” “in,” “for,” and “it.” These stopwords are frequently removed to focus on more meaningful terms when processing text data in natural language processing tasks such as text classification or sentiment analysis.

#### To check the list of stopwords you can type the following commands in the python shell.

<a href="https://github.com/NhanPhamThanh-IT/NLTK-Guide/blob/main/RemovingStopWords/example1.py"><strong>Click here to view source code</strong></a>

__Note__: You can even modify the list by adding words of your choice in the English .txt. file in the stopwords directory. 

### Removing stop words with NLTK

The following program removes stop words from a piece of text:

<a href="https://github.com/NhanPhamThanh-IT/NLTK-Guide/blob/main/RemovingStopWords/example2.py"><strong>Click here to view source code</strong></a>

The provided Python code demonstrates stopword removal using the Natural Language Toolkit (NLTK) library. In the first step, the sample sentence, which reads “This is a sample sentence, showing off the stop words filtration,” is tokenized into words using the word_tokenize function. The code then filters out stopwords by converting each word to lowercase and checking its presence in the set of English stopwords obtained from NLTK. The resulting filtered_sentence is printed, showcasing both lowercased and original versions, providing a cleaned version of the sentence with common English stopwords removed.

### Removing stop words with SpaCy

<a href="https://github.com/NhanPhamThanh-IT/NLTK-Guide/blob/main/RemovingStopWords/example3.py"><strong>Click here to view source code</strong></a>

The provided Python code utilizes the spaCy library for natural language processing to remove stopwords from a sample text. Initially, the spaCy English model is loaded, and the sample text, “There is a pen on the table,” is processed using spaCy. Stopwords are then filtered out from the processed tokens, and the resulting non-stopword tokens are joined to create a clean version of the text.

The provided Python code utilizes the spaCy library for natural language processing to remove stopwords from a sample text. Initially, the spaCy English model is loaded, and the sample text, “There is a pen on the table,” is processed using spaCy. Stopwords are then filtered out from the processed tokens, and the resulting non-stopword tokens are joined to create a clean version of the text.

### Removing stop words with Genism

<a href="https://github.com/NhanPhamThanh-IT/NLTK-Guide/blob/main/RemovingStopWords/example4.py"><strong>Click here to view source code</strong></a>

The provided Python code utilizes Gensim’s remove_stopwords function to preprocess a sample text. In this specific example, the original text is “The majestic mountains provide a breathtaking view.” The remove_stopwords function efficiently eliminates common English stopwords, resulting in a filtered version of the text, which is then printed alongside the original text.

### Removing stop words with SkLearn

<a href="https://github.com/NhanPhamThanh-IT/NLTK-Guide/blob/main/RemovingStopWords/example5.py"><strong>Click here to view source code</strong></a>

The provided Python code combines scikit-learn and NLTK for stopword removal and text processing. First, the sample text, “The quick brown fox jumps over the lazy dog,” is tokenized into words using NLTK’s word_tokenize function. Subsequently, common English stopwords are removed by iterating through the tokenized words and checking their absence in the NLTK stopwords set. The final step involves joining the non-stopword tokens to create a clean version of the text. This approach integrates scikit-learn’s CountVectorizer could be utilized for further text analysis, such as creating a bag-of-words representation.

</div>

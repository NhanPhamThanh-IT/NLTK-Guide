import nltk

# Tokenize and tag some text

sentence = """At eight o'clock on Thursday morning
... Arthur didn't feel very good."""

tokens = nltk.word_tokenize(sentence)

print(tokens)

'''
['At', 'eight', "o'clock", 'on', 'Thursday', 'morning',
'Arthur', 'did', "n't", 'feel', 'very', 'good', '.']
'''

###################################################################

'''
You should run this code for this step:
nltk.download('averaged_perceptron_tagger_eng')
'''

tagged = nltk.pos_tag(tokens)

print(tagged[0:6])

'''
[('At', 'IN'), ('eight', 'CD'), ("o'clock", 'JJ'), ('on', 'IN'),
('Thursday', 'NNP'), ('morning', 'NN')]
'''

# Identify named entities

'''
You should run this code for this step:
nltk.download('maxent_ne_chunker_tab')
'''

entities = nltk.chunk.ne_chunk(tagged)

print(entities)
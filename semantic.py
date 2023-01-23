import spacy

nlp = spacy.load('en_core_web_md')
#nlp = spacy.load('en_core_web_sm')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


tokens = nlp('cat apple monkey banana potato brick')
for token1 in tokens:
 for token2 in tokens:
      print(token1.text, token2.text, token1.similarity(token2))

#brick has very low similarity with other objects as it is not living
#potato has good similarity with banana and apple

#with sm, bricks and others similarity to the other objects is greater

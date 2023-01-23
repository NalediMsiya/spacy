import spacy
nlp = spacy.load("en_core_web_sm")

# creating a string of garden path sentences
gardenpathsentences = u'''The florist sent the flowers was pleased, The sour drink from the ocean, We painted the wall with cracks ,The girl told the story cried
I convinced her children are noisy, Hellen is expecting tomorrow to be a bad day'''

sentence = nlp(gardenpathsentences)

# tokenising the sentences, here words will be split and punctuation marks are exculded 
print([token.orth_ for token in sentence if not token.is_punct | token.is_space])

#identifying entities in sentence 
print([(x, x.label_, x.label) for x in sentence.ents])

# The entities  were : PERSON(Hellen), DATE (Tommorrow), Date(a bad day)
# I was not expecting "a bad day " to be categorised as a date

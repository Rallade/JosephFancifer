from nltk import word_tokenize
from nltk import pos_tag

sent = word_tokenize("where shall we have lunch")
pos = pos_tag(sent)
print(pos)
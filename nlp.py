from nltk import word_tokenize
from nltk import pos_tag
import json
import requests
from pprint import pprint

def fancify(sentence):
    sent = word_tokenize(sentence)
    pos = pos_tag(sent)
    #print(pos)

    url = ""


    for i in range(len(pos)):
        if pos[i][1] == 'JJ' or pos[i][1] == 'JJR':
            print(pos[i][0])
            response = requests.get(
                'http://words.bighugelabs.com/api/2/2f4c074d909c567177c1be9f93882113/' + pos[i][0].lower() + '/json')
            synonyms = response.json()
            try:
                syn = max(synonyms['adjective']['syn'], key=len)
                pos[i] = (syn, 'JJ')
            except:
                print(pos[i])

        elif pos[i][1] == 'NN':
            print(pos[i][0])
            response = requests.get(
                'http://words.bighugelabs.com/api/2/2f4c074d909c567177c1be9f93882113/' + pos[i][0].lower() + '/json')
            synonyms = response.json()
            try:
                syn = max(synonyms['noun']['syn'], key=len)
                pos[i] = (syn, 'NN')
            except:
                print(pos[i])
        elif pos[i][1] == 'RB':
            print(pos[i][0])
            response = requests.get(
                'http://words.bighugelabs.com/api/2/2f4c074d909c567177c1be9f93882113/' + pos[i][0].lower() + '/json')
            synonyms = response.json()
            try:
                syn = max(synonyms['adverb']['syn'], key=len)
                pos[i] = (syn, 'RB')
            except:
                print(pos[i])
        elif pos[i][1] == 'NNS':
            print(pos[i][0])
            response = requests.get(
                'http://words.bighugelabs.com/api/2/2f4c074d909c567177c1be9f93882113/' + pos[i][0].lower() + '/json')
            synonyms = response.json()
            try:
                syn = max(synonyms['noun']['syn'], key=len)
                pos[i] = (syn+'(s)', 'NN')
            except:
                print(pos[i])

    detuple = [i[0] for i in pos]
    return " ".join(str(x) for x in detuple)

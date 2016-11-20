import math
from random import random
import re
import numpy as np  # linear algebra
import pickle
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)x
from sklearn.naive_bayes import MultinomialNB  # function to split the data for cross-validation
from sklearn.cross_validation import train_test_split  # function for transforming documents into counts
from sklearn.feature_extraction.text import CountVectorizer  # function for encoding categories
from sklearn.preprocessing import LabelEncoder

def evaluatePubs(pubs, counts):
    print('reading data...')
    pubData = pd.read_csv("../pubInfo.csv")

    maxC = max(counts)
    biases = [0 for i in range(len(pubs))]
    creds  = [0 for i in range(len(pubs))]

    knownPubs = {}
    for i in range(len(pubData['publisher'])):
        knownPubs[pubData['publisher'][i]] = (pubData['bias'][i], pubData['cred'][i])

    for i in range(len(pubs)):
        if(pubs[i] in knownPubs.keys() and not math.isnan(knownPubs[pubs[i]][0])):
                biases[i] = knownPubs[pubs[i]][0]
                creds[i] = knownPubs[pubs[i]][1]
        else:
            biases[i] = round((2*random() - 1)*100)
            creds[i] = round(100*random()*(counts[i]/maxC)**(1/3))

#    print(pubs)
#    print(counts)
#    print(creds)
#    print(biases)

    d = {'PUBLISHER':pubs, 'COUNT':counts, 'BIAS':biases, 'CRED':creds}
    return(pd.DataFrame(data = d))

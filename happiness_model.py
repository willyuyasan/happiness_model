import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import random


def happiness_model(name,words,age):
    name = name
    words = words
    age = age
    #genre = genre
    #labor_status = labor_status

    total_sents = (name + ' ' + words)
    corpus = total_sents.split(' ')
    #print(corpus)

    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(corpus)
    n1=0
    n1 = vectors.sum(axis = 0).sum()

    ls_agesr = [
        '18-23 años',
        '23-30 años',
        '30-40 años',
        '40-50 años',
        '50-70 años',
        'Mas de 70 años',]

    i=0
    n2=0
    for ag in ls_agesr:
        i = i+1
        if age == ag:
            n2 = i

    n3=0
    n3 = len(total_sents)
    
    seed_ = n1*n2*n3
    random.seed(int(seed_))
    probability = random.randint(70, 99)

    print(probability)
    return probability


#name = "William Uyasan"
#words = "Hola Mundo"
#age = "30-40 años"
#happiness_model(name,words,age)




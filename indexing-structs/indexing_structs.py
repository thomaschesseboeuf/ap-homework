import random as rd
import numpy as np 
import pandas as pd


def parse(filename):
    L=[]
    with open(filename, 'r') as f:
        for line in f:
            person={}
            line = line.split()
            person['Firstname'] = line[0]
            person['Lastname'] = line[1]
            person['Birthdate'] = line[2:]
            L.append(person)
    return L

def date_random():
    day = list(np.arange(1,29))
    month = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
    year = list(np.arange(2000,2005))
    return rd.sample(day,1)[0], rd.sample(month,1)[0], rd.sample(year,1)[0]


def data_generation():
    with open('first_names.txt','r', encoding='utf-8') as f, open('last_names.txt','r', encoding='utf-8') as l:
        #encoding='utf-8' sinon il y a des problèmes avec les accents
        F,L = [], []
        for firstname in f:
            F.append(firstname.strip())
        for lastname in l:
            L.append(lastname.strip())
        
    S = set()
    while len(S) < 10000:
        S.update([(rd.choice(F), rd.choice(L), *date_random())])
    
    with open('data-big.txt','w') as output:  
        for people in S:
            print(*people, file = output)

# à éxécuter dans un jupyter notebook
# %%timeit 
#data_generation()

def nb_different_firstname():
    d = parse('data-big.txt')
    df = pd.DataFrame(d)
    return len(df.Firstname.unique())



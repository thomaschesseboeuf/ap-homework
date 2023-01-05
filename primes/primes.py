#!/usr/bin/env python
# coding: utf-8
# %% [markdown]
#
# # <div class="licence">
# # <span>Licence CC BY-NC-ND</span>
# # <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# # <span><img src="media/both-logos-small-alpha.png" /></span>
# # </div>
#
# # # Exercice - niveau avancé
#
# # ## itérateurs et générateurs
# # 
# # **Tous les exercices** de ce notebook vous demandent d'écrire
# # des fonctions qui **construisent des itérateurs**.

# %% [markdown]
#
#
# import itertools
#
#
# # ## 1. Nombres premiers
#
# # On vous demande d'écrire un générateur qui énumère les nombres premiers.
# # 
# # Naturellement il existe de nombreuses biliothèques pour cela, mais on vous demande ici d'écrire votre propre algorithme, même s'il est naïf.

# %% [markdown]
#
#
# from corrections.gen_primes import exo_primes
# exo_primes.example()
#
#
# # Le générateur ne s'arrête donc jamais, c'est un générateur infini comme `itertools.count()`.
# # Le système de correction automatique est capable d'extraire certaines parties du flux du générateur, avec une convention voisine de `range()` et/ou du *slicing*.
# # 
# # Ainsi par exemple le deuxième jeu de test, sous-titré `1 → 5 / 2`, va retenir les éléments énumérés par le générateur aux itérations *1, 3 et 5* - en commençant bien sûr à compter à 0.
#
# # **NOTES**
# # 
# # * Évidemment, il vous faut retourner un itérateur, et la correction automatique vérifiera ce point.
# # * Notez aussi que, lorsqu'on cherche à déterminer si $n$ est entier, on a nécessairement déjà fait ce travail sur tous les entiers plus petits que $n$. Il est donc tentant, et fortement recommandé, de profiter de cette information pour accélérer l'algorithme.
# # * Si votre algorithme est très lent ou faux, vous pouvez *perdre* le *kernel* (en français noyau), c'est-à-dire qu'il calcule pendant très longtemps (ou pour toujours) ; dans ces cas-là, la marge gauche indique `In [*]:` et l'étoile n'est jamais remplacée par un chiffre.
# #   Il vous **faut alors interrompre** votre kernel ; pour cela utilisez le menu *Kernel* qui a des options pour interrompre ou redémarrer le kernel courant ; les raccourcis clavier `i i` et `0 0` permettent aussi d'interrompre et redémarrer le noyau.

# %%
from corrections.gen_primes import exo_primes
exo_primes.example()

# %%


# à vous de jouer
from itertools import count
def primes():
    smaller_primes = []
    for n in count(2):
        prime = True
        for k in smaller_primes:
            if n%k == 0:
                prime = False
                break
            if k>n**(1/2):
                break
        if prime:
            smaller_primes.append(n)
            yield n
        


# %%


# pour corriger votre code
exo_primes.correction(primes)


# ##### zone de debug

# %%


# à toutes fins utiles

MAX = 10

iterator = primes()

for index, prime in enumerate(itertools.islice(iterator, MAX)):
    print(f"{index} -> {prime}")


# ***
# ***
# ***

# ## 2. Les carrés des nombres premiers

# On veut à présent énumérer les carrés des nombres premiers
# 
# **NOTE** il y a au moins deux façons triviales de parvenir au résultat.

# %%


from corrections.gen_primes import exo_prime_squares
exo_prime_squares.example()


# %%


# à vous

def prime_squares():
    return (x**2 for x in primes())
#   for x in primes():
#       yield x**2


# %%


exo_prime_squares.correction(prime_squares)


# ***
# ***
# ***

# ## 3. Combinaisons d'itérateurs

# On vous demande d'écrire un itérateur qui énumère des couples :
# 
# * en première position, on veut trouver les nombres premiers, mais avec un décalage :  
#   les **cinq premiers tuples** contiennent `1`, puis le sixième contient 2, et à partir de là les nombres premiers ;
# * en deuxième position, les carrés des nombres premiers, sans décalage :

# **NOTE**  
# Il peut être tentant de créer deux instances de l'itérateur `primes()` ; toutefois c'est cet objet qui demande le plus de temps de calcul, aussi on vous suggère de réfléchir, en option, à une solution qui ne crée qu'un seul exemplaire de cet itérateur.

# %%


from corrections.gen_primes import exo_prime_legos
exo_prime_legos.example()


# %%


# à vous de jouer
from itertools import chain, repeat
def prime_legos():
    return zip(chain(repeat(1,5), primes()), prime_squares())


# %%


exo_prime_legos.correction(prime_legos)


# ##### zone de benchmarking
# 
# un ordre de grandeur: pour le code suivant, ma solution prend environ 60ms  
# la cellule, qui fait le calcul 5 * 5 fois, prend environ 2s à afficher le résultat

# %%


get_ipython().run_cell_magic('timeit', '-n 5 -r 5', '\nN = 10_000\n\nP = prime_legos()\nfor x in range(N): next(P)\n')


# ***
# ***
# ***

# ## 4. Les $n$-ièmes nombres premiers, avec $n$ premier

# On vous demande d'implémenter un itérateur qui renvoie les $n$-ièmes nombres premiers, mais seulement pour $n$ premier.
# 
# Ainsi comme `primes()` retourne la suite
# 
# | indice | premier |
# |--------|---------|
# | 0 | 2 |
# | 1 | 3 |
# | 2 | 5 |
# | 3 | 7 |
# | 4 | 11|
# | 5 | 13|
# | 6 | 17|
# | 7 | 19|
# 
# on veut que `prime_th_primes` retourne la suite
# 
# | indice | premier |
# |--------|---------|
# | 0 | 5 |
# | 1 | 7 |
# | 2 | 13|
# | 3 | 19|

# %%


# à vous de jouer
from itertools import count
def prime_th_primes():
    tmp = (0,2)
    smaller_primes = []
    for n in count(2):
        prime = True
        for k in smaller_primes:
            if n%k == 0:
                prime = False
                break
            if k>n**(1/2):
                break
        if prime:
            smaller_primes.append(n)
            if len(smaller_primes)==tmp[1]+1:
                tmp = (tmp[0]+1, smaller_primes[tmp[0]+1])
                yield n


# %%


# pour corriger votre code
exo_prime_th_primes.correction(prime_th_primes)


# ##### zone de benchmarking
# 
# un ordre de grandeur: pour le code suivant, ma solution prend environ 150ms  
# la cellule, qui fait le calcul 3 * 3 fois, prend environ 1.5s à afficher le résultat

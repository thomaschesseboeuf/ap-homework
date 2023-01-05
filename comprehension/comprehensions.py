#!/usr/bin/env python
# coding: utf-8

# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# <span><img src="media/both-logos-small-alpha.png" /></span>
# </div>

# # Compréhensions

# ## Exercice - niveau basique
# 
# Il vous est demandé d'écrire une fonction `aplatir` qui prend *un unique* argument `l_conteneurs` qui est une liste (ou plus généralement un itérable) de conteneurs (ou plus généralement d'itérables), et qui retourne la liste de tous les éléments de tous les conteneurs.

# In[ ]:


# par exemple
from corrections.exo_aplatir import exo_aplatir
exo_aplatir.example()


# In[ ]:


def aplatir(conteneurs):
    return [x for iterable in conteneurs for x in iterable ]


# In[ ]:


# vérifier votre code
exo_aplatir.correction(aplatir)


# ## Exercice - niveau intermédiaire
# 
# À présent, on passe en argument deux conteneurs (deux itérables) `c1` et `c2` de même taille à la fonction `alternat`, qui doit construire une liste contenant les éléments pris alternativement dans `c1` et dans `c2`.

# In[ ]:


# exemple
from corrections.exo_alternat import exo_alternat
exo_alternat.example()


# **Indice** pour cet exercice il peut être pertinent de recourir à la fonction *built-in* `zip`.

# In[ ]:


def alternat(c1, c2):
    return aplatir(zip(c1, c2))     


# In[ ]:


# pour vérifier votre code
exo_alternat.correction(alternat)


# ## Exercice - niveau intermédiaire

# On se donne deux ensembles A et B de tuples de la forme
# 
# ```python
# (entier, valeur)
# ```
# 
# On vous demande d'écrire une fonction `intersect` qui retourne l'ensemble des objets `valeur` associés (dans A ou dans B) à un entier qui soit présent dans (un tuple de) A *et* dans (un tuple de) B.

# In[ ]:


# un exemple
from corrections.exo_intersect import exo_intersect
exo_intersect.example()


# In[ ]:


def intersect(A, B):
    dA, dB = dict(A), dict(B)
    I = set(dA.keys()) & set(dB.keys())
    return {d[x] for d in (dA,dB) for x in I}


# In[ ]:


# pour vérifier votre code
exo_intersect.correction(intersect)


# In[ ]:





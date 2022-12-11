#!/usr/bin/env python
# coding: utf-8
# %%
import numpy as np
def f(x,y):
        return x+y
g = np.vectorize(f)

def translate(x):
    if isinstance(x, (complex,int,float)):
        r, i = x.real, x.imag
        return Quaternion(r,i,0,0)
    return x
    

# %%


# votre code

class Quaternion:
    
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.coef = np.array([a,b,c,d])
    
    #def __init__(self, z):
        #self.a = z.real
        #self.b = z.imag
        #self.c = 0
        #self.d = 0
        #self.coef = np.array([a,b,c,d])
        # pour definir un quaternion à partir d'un complexe
    
    
    def __repr__(self):
        t = np.array(['','i','j','k'])
        m = g(np.vectorize(str)(self.coef),t)
        res = ''
        for x in m:
            if x[0] != '0':
                res += x
                if x != m[-1]:
                    res += '+'
        if res[-1] == '+':
            res = res[:-1]
        return res
    
    def __add__(self, other):
        self,other = translate(self), translate(other)
        a = g(self.coef, other.coef)
        return Quaternion(*tuple(a))
    
    def __eq__(self,other):
        self,other = translate(self), translate(other)
        return np.all(self.coef==other.coef)
    
    def __mul__(self, other):
        self,other = translate(self), translate(other)
        res = [0,0,0,0]
        s = {1,2,3}
        
        for a_pos,a in enumerate(self.coef):
            for b_pos, b in enumerate(other.coef):
                if 0 in [a_pos, b_pos]:
                    res[a_pos + b_pos] += a*b
                elif b_pos == a_pos:
                    res[0] += -a*b
                    
                elif b_pos-a_pos in [1,-2]:
                    x = s - {a_pos, b_pos}
                    res[x.pop()] += a*b
                    
                elif b_pos-a_pos in [-1,2]:
                    x = s - {a_pos, b_pos}
                    res[x.pop()] += -a*b
        return Quaternion(*res)
    

# %%
I = Quaternion(0,1,0,0)
J = Quaternion(0,0,1,0)
K = Quaternion(0,0,0,1)


# %%
I + 1

# %%
(I*J).coef == K.coef


# %%
I*J==K

# %%


J*K == I


# %%


K*I == J


# %%


I*I == J*J == K*K == -1


# %%


J*K == 1j


# %%


K*J == -1j


# %%


Quaternion(1, 2, 3, 4) == (1+2j) + J * Quaternion(3-4j)


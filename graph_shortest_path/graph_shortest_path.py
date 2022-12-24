import pandas as pd
import numpy as np
from collections import defaultdict


def parse_graph(filename):
    d={}
    with open(filename) as f:
        for line in f:
            edge = line.strip().split(sep=',')
            start_vertice, end_vertice, weight = edge
            if start_vertice in d.keys():
                (d[start_vertice])[end_vertice] = int(weight)
            else:
                (d[start_vertice]) = {end_vertice : int(weight)}
    return d


g = parse_graph('graph.csv')
reach = parse_graph('reach.csv')
g


def number_vertices(graph):
    L=[]
    for k,v in graph.items():
        L.append(k)
        for x in v.keys():
            L.append( x )
    S = set(L)
    return len(S)


def no_path():
    return {}


def where_can_I_go(graph, vertice):
    d = defaultdict(no_path)
    d.update(graph)
    return list(d[vertice].keys())


# +
def reachable(graph, vertice):
    # on initialise les sommets atteignables par ceux qui le sont directement 
    reachable_vertices = where_can_I_go(graph, vertice) 
    for v in reachable_vertices:
        #on ajoute les sommets atteignables qui ne sont pas encore présents dans la liste, que l'on va ensuite parcourir
        w = np.array( where_can_I_go(graph, v) )
        mask = [x not in reachable_vertices for x in w] 
        reachable_vertices.extend(w[mask])
    return reachable_vertices

# vous écrivez dans le tp : 
#'sans transition, mais c’est sans doute le bon moment pour signaler une limitation de Python, 
#qui est qu’on ne peut pas modifier un objet sur lequel on est en train de faire une boucle'
#Pourtant je pense que c'est ce que je fais...
        


# -
def list_of_reachable(graph):
    t = graph.copy()
    for s in t:
        print(f"en partant de {s} → {reachable(graph, s)}")


list_of_reachable(g)


def shortest_distance(graph, v1, v2):
    not_visited = reachable(graph,v1)
    if v2 not in not_visited:
        return None
    
    d = defaultdict(no_path) #pour ne pas avoir de problème si d'un sommet on ne peut aller nulle part
    d.update(graph)
    
    visited_to_not_visited = {} # dictionnaire qui à un tuple représentant une arête associe son poids, de manière à pouvoir itérer sur les arêtes directement
    for x in graph[v1] :
        visited_to_not_visited[(v1, x)] = graph[v1][x]
    visited = {v1 : 0}
    
    while v2 not in visited:
        easier_edge = min(visited_to_not_visited, key = lambda x : visited_to_not_visited[x] + visited[x[0]])
        source, destination = easier_edge
        visited[destination] = visited[source] + visited_to_not_visited[easier_edge]
        
        del visited_to_not_visited[easier_edge]
        for edge in visited_to_not_visited.copy():
            if edge[1] == destination:
                del visited_to_not_visited[edge]
        
        reachable_but_not_visited = set(d[destination].keys()) - set(visited.keys())
        for x in reachable_but_not_visited:
            visited_to_not_visited[(destination, x)] = graph[destination][x]
    
    return visited[v2]      


shortest_distance(g,'a','f')

g2 = parse_graph('graph2.csv')
print(shortest_distance(g, 'a', 'f') == 23,shortest_distance(g, 'a', 'e') == 20,shortest_distance(g, 'c', 'b') is None,shortest_distance(g2, 'v1', 'v6'))


def shortest_path(graph,v1,v2):
    not_visited = reachable(graph,v1)
    if v2 not in not_visited:
        return None
    
    d = defaultdict(no_path) #pour ne pas avoir de problème si d'un sommet on ne peut aller nulle part
    d.update(graph)
    
    visited_to_not_visited = {} # dictionnaire qui à un tuple représentant une arête associe son poids, de manière à pouvoir itérer sur les arêtes directement
    for x in graph[v1] :
        visited_to_not_visited[(v1, x)] = graph[v1][x]
    visited = {v1 : 0}
    
    while v2 not in visited:
        easier_path = min(visited_to_not_visited, key = lambda x : visited_to_not_visited[x] + visited[x[-2]])
        source, destination = easier_path[-2:]
        if destination == v2:
            shortest_path = easier_path
        visited[destination] = visited[source] + visited_to_not_visited[easier_path]
        del visited_to_not_visited[easier_path]
        for path in visited_to_not_visited.copy():
            if path[-1] == destination:
                del visited_to_not_visited[path]
        
        reachable_but_not_visited = set(d[destination].keys()) - set(visited.keys())
        for x in reachable_but_not_visited:
            visited_to_not_visited[(*easier_path,x)] = graph[destination][x]        
    
    return (f'The shortest path is {shortest_path}. It weighs {visited[v2]}.')      


shortest_path(g,'a','f')

import requests
thrones_url = "https://raw.githubusercontent.com/pupimvictor/NetworkOfThrones/master/stormofswords.csv"
get_request = requests.get(thrones_url)
text_data = get_request.text
with open('thrones.csv', 'w') as output:
    tmp =  text_data.split()[1:]
    for line in tmp:
        edge = line.strip().split(sep=',')
        if len(edge) == 3: #pb avec des lignes avec 1 seul élément
            print(line, file=output)

thrones = parse_graph("thrones.csv")


def how_many_vertices(graph):
    L=[]
    for k in graph:
        L.extend(reachable(graph,k))
    S = set(L)
    print(len(S))


how_many_vertices(thrones)


def neighbors(t,n):
    i,j =t
    L=[(i+1,j),(i,j+1),(i-1,j),(i,j-1)]
    mat=[]
    for x in L:
        mat.append(np.array(x)) #vectorisé np.array()?
    for x in mat:
        if ((np.any(x < 1)) or (np.any(x > n))):
            L.remove(tuple(x))
    return L


neighbors((2,1),4)


def planar(n):
    d = {}
    for i in range(1,n+1):
        for j in range(1,n+1):
            d[(i,j)] = {}
            for x in neighbors((i,j), n):  
                d[(i,j)][x]=1
    return d


planar(4)

L=[0,1,2,3]
mat = np.array(L)
for x in mat:
    del x

N=20
P=planar(N)


# +
def reachable_for_planar(graph, vertice):
    # on initialise les sommets atteignables par ceux qui le sont directement 
    reachable_vertices = where_can_I_go(graph, vertice) 
    for v in reachable_vertices:
        #on ajoute les sommets atteignables qui ne sont pas encore présents dans la liste, que l'on va ensuite parcourir
        w = np.array( where_can_I_go(graph, v) )
        mask = [tuple(x) not in reachable_vertices for x in w] 
        for x in w[mask]:
            reachable_vertices.append(tuple(x))
    return reachable_vertices

def shortest_path_for_planar(graph,v1,v2):
    not_visited = reachable_for_planar(graph,v1)
    if v2 not in not_visited:
        return None
    
    d = defaultdict(no_path) #pour ne pas avoir de problème si d'un sommet on ne peut aller nulle part
    d.update(graph)
    
    visited_to_not_visited = {} # dictionnaire qui à un tuple représentant une arête associe son poids, de manière à pouvoir itérer sur les arêtes directement
    for x in graph[v1] :
        visited_to_not_visited[(v1, x)] = graph[v1][x]
    visited = {v1 : 0}
        
    while v2 not in visited:
        easier_path = min(visited_to_not_visited, key = lambda x : visited_to_not_visited[x] + visited[x[-2]])
        source, destination = easier_path[-2:]
        if destination == v2:
            shortest_path = easier_path
        visited[destination] = visited[source] + visited_to_not_visited[easier_path]
        del visited_to_not_visited[easier_path]
        for path in visited_to_not_visited.copy():
            if path[-1] == destination:
                del visited_to_not_visited[path]
        
        reachable_but_not_visited = set(d[destination].keys()) - set(visited.keys())
        for x in reachable_but_not_visited:
            visited_to_not_visited[(*easier_path,x)] = graph[destination][x]        
    
    return (f'The shortest path is {shortest_path}. It weighs {visited[v2]}.')      


# -

# %timeit shortest_path_for_planar(P,(1,1),(N,N))

with open('slow.py','w') as f:
    print('from graph_shortest_path.py import *', file =f)
    print('N = 30', file = f)
    print('P = planar1(N)', file = f)
    print('print(shortest_path1(P, (1, 1), (N, N)))', file = f)

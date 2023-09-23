import networkx as nx
import random

def convert_to_g(V, E):
    return {i: [j for j in V if j!=i and (i, j) in E or (j, i) in E] for i in V}

class my_no_connected_components_class:
    def __init__(self, g):
        self.g = g
        self.visited = {}
        self.V = g.keys()
        self.ncc = 0
        for k in self.V:
            self.visited[k] = self.visited.get(k, False)

    def find(self):
        for k in self.V:
            if self.visited[k] == False:
                self.dfs(k)
                self.ncc+=1
        return self.ncc

    def dfs(self, k):
        self.visited[k] = True
        for p in self.g[k]:
            if self.visited[p] == False:
                self.dfs(p)

def my_no_connected_components(V, E):
    g = convert_to_g(V, E)
    instance = my_no_connected_components_class(g)
    no_cc = instance.find()
    return no_cc

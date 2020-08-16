"""
Minimize the maximum degree of a spanning tree of a graph.
approach:
    - start with assignment model
    - add cuts until there are no more disconnected components
    - two cutting plane possibilities (called inside "solve_tsp"):
        - addcut: limit the number of edges in a connected component S to |S|-1
        - addcut2: require the number of edges between two connected component to be >= 1
Copyright (c) by Joao Pedro PEDROSO and Mikio KUBO, 2012
"""
import math
import random
import networkx
from countries_adjacency import EurasianVertices, EurasianEdges
from pyscipopt import Model, quicksum
from  SquaredEdges import squared_edges

def solve_min_deg_spanning_tree(V, E):
    """solve_min_deg_spanning_tree -- solve the minimum degree spanning tree problem
       - start with assignment model
       - add cuts until there are no disconnected components
    Parameters:
        - E: set/list of edges in the graph
    Returns the optimum objective value and the list of edges used.
    """
    def addcut(cut_edges):
        G = networkx.Graph()
        G.add_edges_from(cut_edges)
        Components = list(networkx.connected_components(G))
        if len(Components) == 1:
            return False
        model.freeTransform()
        for S in Components:
            model.addCons(quicksum(x[i,j] for i, j in E if (i in S and j in S)) <= len(S)-1)
        return True


    def addcut2(cut_edges):
        G = networkx.Graph()
        G.add_edges_from(cut_edges)
        Components = list(networkx.connected_components(G))

        if len(Components) == 1:
            return False
        model.freeTransform()
        for S in Components:
            T = set(V) - set(S)
            # print("S:",S)
            # print("T:",T)
            model.addCons(quicksum(x[i,j] for (i, j) in E if (i in S and j in T) or (j in S and i in T)) >= 1)
        return True

    # main part of the solution process:
    model = Model("spanning_tree")

    model.hideOutput() # silent/verbose mode
    x = {}
    for e in E:
        x[e] = model.addVar(lb = 0, ub=1, name="x{}".format(e))

    # leaf[v] is an indicator for v being a leaf.
    leaf = {}
    model.addCons(quicksum(x[e] for e in E) == 133, "Edge number")
    for v in V:
        print(v)
        leaf[v] = model.addVar(lb = 0, ub=1, name="leaf{}".format(v))
        # If v is a leaf, then deg(v) = 1, so leaf[v] will also be 1. Otherwise, we can let leaf[v] = 0.
        model.addCons(quicksum(x[e] for e in E if v in e) + leaf[v] >= 2, "Leaf{}".format(str(v)))
        # Need to make sure the deg of each vertex is at least 1
        model.addCons(quicksum(x[e] for e in E if v in e) >= 1, "Incident{}".format(str(v)))

    model.setObjective(quicksum(leaf[v] for v in V), "minimize")

    EPS = 1.e-6
    isMIP = False
    while True:
        model.optimize()
        edges = []
        for (i,j) in E:
            if model.getVal(x[i,j]) > EPS:
                edges.append( (i,j) )
        print(edges)

        addcut2(edges)
        if not addcut(edges):
            if isMIP:     # integer variables, components connected: solution found
                break
            model.freeTransform()
            print("Switching to mip")
            for (i,j) in x:     # all components connected, switch to integer model
                model.chgVarType(x[i,j], "B")
            for v in V:
                model.chgVarType(leaf[v], "B")
            isMIP = True

    return model.getObjVal(),edges


if __name__ == "__main__":
    print(len(EurasianVertices))
    print(len(EurasianEdges))
    obj,edges = solve_min_deg_spanning_tree(EurasianVertices, squared_edges)
    print("Optimal cost:",obj)

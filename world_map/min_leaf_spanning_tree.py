from countries_adjacency import * 
import networkx
import matplotlib.pyplot as plt
import pydot
tree = {('India', 'Bangladesh'), ('Gaza Strip', 'Egypt'), ('Somalia', 'Djibouti'), ('Senegal', 'Gambia'), ('Myanmar', 'Laos'), ('Namibia', 'Botswana'), ('Saudi Arabia', 'Kuwait'), ('Papua New Guinea', 'Indonesia'), ('Guinea-Bissau', 'Guinea'), ('Eritrea', 'Djibouti'), ('South Africa', 'Lesotho'), ('Liberia', 'Ivory Coast'), ('Morocco', 'Algeria'), ('Mozambique', 'Eswatini'), ('Russia', 'Mongolia'), ('Netherlands', 'Germany'), ('Saudi Arabia', 'Qatar'), ('Togo', 'Ghana'), ('Germany', 'Denmark'), ('Chad', 'Central African Republic'), ('Russia', 'Norway'), ('Yemen', 'Oman'), ('Luxembourg', 'Belgium'), ('Central African Republic', 'Cameroon'), ('West Bank', 'Israel'), ('Mongolia', 'China'), ('Sierra Leone', 'Liberia'), ('Vatican City', 'Italy'), ('Uganda', 'Kenya'), ('Nepal', 'India'), ('Zimbabwe', 'Botswana'), ('Monaco', 'France'), ('Ukraine', 'Slovakia'), ('Sudan', 'Egypt'), ('Senegal', 'Guinea-Bissau'), ('Israel', 'Gaza Strip'), ('Niger', 'Mali'), ('West Bank', 'Jordan'), ('Thailand', 'Malaysia'), ('Turkmenistan', 'Kazakhstan'), ('Nigeria', 'Niger'), ('San Marino', 'Italy'), ('Namibia', 'Angola'), ('Jordan', 'Iraq'), ('Slovakia', 'Poland'), ('Lithuania', 'Belarus'), ('Malaysia', 'Brunei'), ('Somalia', 'Kenya'), ('Republic of the Congo', 'Angola'), ('Ukraine', 'Moldova'), ('Turkey', 'Georgia'), ('South Korea', 'North Korea'), ('Uzbekistan', 'Kyrgyzstan'), ('Thailand', 'Cambodia'), ('Western Sahara', 'Mauritania'), ('Latvia', 'Estonia'), ('Turkey', 'Syria'), ('Kuwait', 'Iraq'), ('Georgia', 'Azerbaijan'), ('Slovenia', 'Hungary'), ('Syria', 'Lebanon'), ('Nigeria', 'Benin'), ('Indonesia', 'East Timor'), ('Malaysia', 'Indonesia'), ('Yemen', 'Saudi Arabia'), ('Sierra Leone', 'Guinea'), ('India', 'Bhutan'), ('Tajikistan', 'Kyrgyzstan'), ('Tajikistan', 'China'), ('Russia', 'North Korea'), ('Lebanon', 'Israel'), ('China', 'Bhutan'), ('Mozambique', 'Malawi'), ('Tanzania', 'Malawi'), ('Latvia', 'Belarus'), ('Pakistan', 'Afghanistan'), ('Togo', 'Benin'), ('Sweden', 'Norway'), ('Azerbaijan', 'Armenia'), ('Libya', 'Chad'), ('Sweden', 'Finland'), ('Equatorial Guinea', 'Cameroon'), ('Uzbekistan', 'Kazakhstan'), ('Spain', 'Portugal'), ('Democratic Republic of the Congo', 'Burundi'), ('Spain', 'Andorra'), ('Gabon', 'Equatorial Guinea'), ('Poland', 'Czech Republic'), ('Liechtenstein', 'Austria'), ('Turkmenistan', 'Afghanistan'), ('Netherlands', 'Belgium'), ('Kosovo', 'Albania'), ('Tunisia', 'Algeria'), ('Serbia', 'Bulgaria'), ('Tanzania', 'Burundi'), ('Montenegro', 'Bosnia and Herzegovina'), ('Switzerland', 'Germany'), ('Croatia', 'Bosnia and Herzegovina'), ('North Macedonia', 'Greece'), ('Tunisia', 'Libya'), ('Zambia', 'Tanzania'), ('Greece', 'Albania'), ('South Sudan', 'Ethiopia'), ('Pakistan', 'Iran'), ('Mauritania', 'Mali'), ('Russia', 'Estonia'), ('Poland', 'Lithuania'), ('Zimbabwe', 'Zambia'), ('United Arab Emirates', 'Oman'), ('Western Sahara', 'Morocco'), ('Spain', 'Gibraltar'), ('Vietnam', 'Cambodia'), ('Sudan', 'South Sudan'), ('Montenegro', 'Kosovo'), ('Ethiopia', 'Eritrea'), ('France', 'Andorra'), ('Czech Republic', 'Austria'), ('Myanmar', 'Bangladesh'), ('Romania', 'Bulgaria'), ('Uganda', 'Rwanda'), ('Switzerland', 'Liechtenstein'), ('Ghana', 'Burkina Faso'), ('Ivory Coast', 'Burkina Faso'), ('Republic of the Congo', 'Gabon'), ('Romania', 'Moldova'), ('Hungary', 'Croatia'), ('Slovenia', 'Italy'), ('Luxembourg', 'France'), ('Serbia', 'North Macedonia'), ('South Africa', 'Eswatini'), ('Iran', 'Armenia'), ('Vietnam', 'Laos'), ('Rwanda', 'Democratic Republic of the Congo')}
def make_branches(tree):
    G = networkx.Graph()
    G.add_edges_from(tree)

    branches = dict()
    for vertex in G:
        neighbors = list(G.neighbors(vertex))
        if len(neighbors) == 1: # Found a leaf
            branches[vertex] = [vertex] # Only vertex found so far is vertex
            neighbor = neighbors[0] # Get the only neighbor of vertex
            branches[vertex].append(neighbor) # Add the neighbor of vertex to the branch
            prev_vertex = vertex
            next_neighbors = list(G.neighbors(neighbor))
            # Keep going along the branch until we get to a vertex that has degree
            # more than 2.
            while len(next_neighbors) == 2:
                # Find the neighbor that isn't the previous vertex.
                next_neighbor = (set(next_neighbors) - {prev_vertex}).pop()
                branches[vertex].append(next_neighbor)
                prev_vertex = neighbor
                neighbor = next_neighbor
                next_neighbors = list(G.neighbors(next_neighbor))
    return branches

G = networkx.Graph()
G.add_edges_from(tree)
pos = networkx.kamada_kawai_layout(G)
networkx.draw(G, pos=pos)
g_pydot = networkx.drawing.nx_pydot.to_pydot(G)

svg = g_pydot.write("graph.svg", prog='neato', format='svg') 
# def get_options(graph, branches):
#     replacement = dict()
#     for leaf in branches:
#         replacement[leaf] = set(graph.neighbors(leaf)) - set(branches[leaf])
#     print(replacement)
#     return replacement
# 
# BigG = networkx.Graph()
# BigG.add_edges_from(EurasianEdges)
#     
# def improve(tree):
#     branches = make_branches(tree)
# 
#     options = get_options(BigG, branches)
#     for leaf, option_set in options.items():
#         if len(option_set) == 0:
#             continue
#         replacement = option_set.pop() 
#         node = branches[leaf][-1]
#         next_node = branches[leaf][-2]
#         return (tree - {(node, next_node), (next_node, node)}).union({(leaf, replacement)})
#     return tree
#     
# G = networkx.Graph()
# G.add_edges_from(tree)
# print(len([0 for x in G if len(list(G.neighbors(x))) == 3]))
# for i in range(11):
#     tree = improve(tree)
#     G = networkx.Graph()
#     G.add_edges_from(tree)
#     print(len([0 for x in G if len(list(G.neighbors(x))) == 3]))
# 
# G = networkx.Graph()
# G.add_edges_from(tree)
# print(len([0 for x in G if len(list(G.neighbors(x))) == 3]))
# 
# print(tree)

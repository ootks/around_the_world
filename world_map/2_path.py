from countries_adjacency import * 
import networkx
path = [('San Marino', 'Slovenia'), ('Hungary', 'Moldova'), ('Romania', 'Ukraine'), ('North Korea', 'Tajikistan'), ('China', 'Latvia'), ('Latvia', 'Lithuania'), ('Hungary', 'Liechtenstein'), ('Democratic Republic of the Congo', 'Zimbabwe'), ('Moldova', 'Ukraine'), ('Estonia', 'Georgia'), ('Botswana', 'Namibia'), ('Austria', 'Serbia'), ('Benin', 'Togo'), ('Finland', 'Poland'), ('Jordan', 'Syria'), ('Albania', 'Montenegro'), ('Djibouti', 'Ethiopia'), ('Kosovo', 'North Macedonia'), ('Laos', 'Russia'), ('Kuwait', 'Qatar'), ('Norway', 'Sweden'), ('Brunei', 'Malaysia'), ('Ghana', 'Liberia'), ('Gambia', 'Guinea-Bissau'), ('San Marino', 'Vatican City'), ('Afghanistan', 'Myanmar'), ('East Timor', 'Indonesia'), ('Democratic Republic of the Congo', 'Malawi'), ('Chad', 'Sudan'), ('Burkina Faso', 'Mali'), ('Guinea-Bissau', 'Mauritania'), ('Angola', 'Zimbabwe'), ('Croatia', 'Kosovo'), ('Iran', 'Saudi Arabia'), ('Czech Republic', 'Italy'), ('Czech Republic', 'Liechtenstein'), ('Central African Republic', 'Kenya'), ('Bangladesh', 'Pakistan'), ('Angola', 'Cameroon'), ('Egypt', 'Ethiopia'), ('Cambodia', 'Thailand'), ('Ivory Coast', 'Sierra Leone'), ('Portugal', 'Spain'), ('Germany', 'Netherlands'), ('Burundi', 'Zambia'), ('Lithuania', 'Mongolia'), ('Azerbaijan', 'Bulgaria'), ('Kazakhstan', 'Uzbekistan'), ('Eritrea', 'Kenya'), ('Republic of the Congo', 'Uganda'), ('Botswana', 'Eswatini'), ('Benin', 'Mali'), ('Russia', 'Uzbekistan'), ('Burundi', 'Mozambique'), ('Croatia', 'Serbia'), ('Burkina Faso', 'Chad'), ('Laos', 'Myanmar'), ('Central African Republic', 'Gabon'), ('Egypt', 'Lebanon'), ('Lesotho', 'South Africa'), ('Ghana', 'Togo'), ('Gambia', 'Guinea'), ('Eswatini', 'Zambia'), ('Malaysia', 'Papua New Guinea'), ('Belarus', 'Mongolia'), ('Austria', 'Italy'), ('Djibouti', 'Somalia'), ('South Africa', 'Tanzania'), ('Gaza Strip', 'Syria'), ('Albania', 'Turkey'), ('Kyrgyzstan', 'Turkmenistan'), ('Liberia', 'Sierra Leone'), ('Belgium', 'Monaco'), ('Armenia', 'Iran'), ('Oman', 'United Arab Emirates'), ('Lesotho', 'Mozambique'), ('Tunisia', 'Western Sahara'), ('Bosnia and Herzegovina', 'Romania'), ('China', 'Turkmenistan'), ('Bosnia and Herzegovina', 'Montenegro'), ('Rwanda', 'Uganda'), ('Israel', 'West Bank'), ('Indonesia', 'Thailand'), ('Morocco', 'Portugal'), ('Poland', 'Slovakia'), ('Switzerland', 'Vatican City'), ('Andorra', 'Gibraltar'), ('Denmark', 'Switzerland'), ('Malawi', 'Tanzania'), ('Jordan', 'Oman'), ('Iraq', 'Kuwait'), ('Ivory Coast', 'Mauritania'), ('Rwanda', 'South Sudan'), ('Guinea', 'Senegal'), ('Cambodia', 'Vietnam'), ('Bangladesh', 'Bhutan'), ('Azerbaijan', 'Estonia'), ('Kazakhstan', 'Kyrgyzstan'), ('Iraq', 'Lebanon'), ('Finland', 'Sweden'), ('East Timor', 'Papua New Guinea'), ('United Arab Emirates', 'Yemen'), ('Niger', 'Western Sahara'), ('Greece', 'North Macedonia'), ('Qatar', 'Yemen'), ('Afghanistan', 'India'), ('Cameroon', 'Equatorial Guinea'), ('Belgium', 'Luxembourg'), ('Eritrea', 'Somalia'), ('Georgia', 'Greece'), ('Pakistan', 'Turkey'), ('Nepal', 'Tajikistan'), ('Algeria', 'Niger'), ('Algeria', 'Senegal'), ('Bhutan', 'Vietnam'), ('France', 'Gibraltar'), ('Belarus', 'Norway'), ('France', 'Netherlands'), ('North Korea', 'South Korea'), ('Libya', 'Tunisia'), ('Libya', 'Morocco'), ('India', 'Nepal'), ('Israel', 'Saudi Arabia'), ('Slovakia', 'Slovenia'), ('South Sudan', 'Sudan'), ('Armenia', 'Bulgaria'), ('Namibia', 'Republic of the Congo'), ('Equatorial Guinea', 'Nigeria'), ('Luxembourg', 'Spain'), ('Gabon', 'Nigeria'), ('Gaza Strip', 'West Bank'), ('Andorra', 'Monaco'), ('Denmark', 'Germany')]
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
print(make_branches(path))

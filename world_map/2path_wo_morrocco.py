from countries_adjacency import * 
import networkx
path = [('Oman', 'Yemen'), ('Afghanistan', 'Laos'), ('Bulgaria', 'Moldova'), ('Austria', 'Liechtenstein'), ('Angola', 'Mozambique'), ('Guinea-Bissau', 'Mauritania'), ('Bhutan', 'Mongolia'), ('South Africa', 'Zimbabwe'), ('Bhutan', 'Tajikistan'), ('Gabon', 'Republic of the Congo'), ('North Macedonia', 'Turkey'), ('Libya', 'Tunisia'), ('Egypt', 'Gaza Strip'), ('Azerbaijan', 'Kazakhstan'), ('Moldova', 'Romania'), ('Ghana', 'Liberia'), ('Botswana', 'Namibia'), ('Hungary', 'Slovakia'), ('Burkina Faso', 'Mauritania'), ('Italy', 'Slovenia'), ('Turkmenistan', 'Uzbekistan'), ('Gabon', 'Nigeria'), ('Kazakhstan', 'Pakistan'), ('Germany', 'Monaco'), ('Poland', 'Ukraine'), ('Malaysia', 'Thailand'), ('Djibouti', 'Sudan'), ('Malawi', 'Zimbabwe'), ('China', 'South Korea'), ('Albania', 'Turkey'), ('Georgia', 'Poland'), ('Malaysia', 'Papua New Guinea'), ('Andorra', 'Spain'), ('India', 'Pakistan'), ('Latvia', 'Norway'), ('Kenya', 'Uganda'), ('Luxembourg', 'Spain'), ('Algeria', 'Morocco'), ('Kyrgyzstan', 'Turkmenistan'), ('Czech Republic', 'Germany'), ('Ivory Coast', 'Mali'), ('Iraq', 'Israel'), ('Azerbaijan', 'Lithuania'), ('Oman', 'Qatar'), ('Greece', 'Serbia'), ('Croatia', 'Slovakia'), ('Luxembourg', 'Monaco'), ('Latvia', 'North Korea'), ('Mongolia', 'Vietnam'), ('United Arab Emirates', 'Yemen'), ('Cameroon', 'Nigeria'), ('Mozambique', 'Zambia'), ('North Korea', 'Tajikistan'), ('Hungary', 'Kosovo'), ('Central African Republic', 'Sudan'), ('Bangladesh', 'Nepal'), ('Republic of the Congo', 'Rwanda'), ('Burundi', 'Malawi'), ('Myanmar', 'Vietnam'), ('Egypt', 'South Sudan'), ('China', 'Finland'), ('Armenia', 'Greece'), ('Belarus', 'Georgia'), ('Iran', 'Kuwait'), ('Italy', 'San Marino'), ('Guinea', 'Sierra Leone'), ('Netherlands', 'Switzerland'), ('Jordan', 'West Bank'), ('Senegal', 'Sierra Leone'), ('Botswana', 'Eswatini'), ('Djibouti', 'Kenya'), ('Bangladesh', 'Thailand'), ('Benin', 'Libya'), ('San Marino', 'Vatican City'), ('Albania', 'Croatia'), ('Saudi Arabia', 'United Arab Emirates'), ('Iraq', 'Kuwait'), ('Mali', 'Niger'), ('Lesotho', 'Eswatini'), ('Russia', 'South Korea'), ('Armenia', 'Iran'), ('Belarus', 'Estonia'), ('Belgium', 'France'), ('Belgium', 'Denmark'), ('Somalia', 'Uganda'), ('Morocco', 'Western Sahara'), ('India', 'Kyrgyzstan'), ('East Timor', 'Indonesia'), ('Estonia', 'Lithuania'), ('Jordan', 'Qatar'), ('Syria', 'West Bank'), ('Benin', 'Chad'), ('Cambodia', 'Myanmar'), ('Austria', 'Vatican City'), ('Democratic Republic of the Congo', 'Tanzania'), ('East Timor', 'Papua New Guinea'), ('Lesotho', 'South Africa'), ('Cambodia', 'Laos'), ('Ethiopia', 'South Sudan'), ('Liechtenstein', 'Switzerland'), ('Burundi', 'Central African Republic'), ('Finland', 'Sweden'), ('Afghanistan', 'Nepal'), ('Brunei', 'Indonesia'), ('Russia', 'Uzbekistan'), ('Gambia', 'Guinea-Bissau'), ('Lebanon', 'Syria'), ('Eritrea', 'Somalia'), ('Norway', 'Sweden'), ('Bosnia and Herzegovina', 'Montenegro'), ('Czech Republic', 'Ukraine'), ('North Macedonia', 'Montenegro'), ('Gaza Strip', 'Lebanon'), ('Angola', 'Democratic Republic of the Congo'), ('Denmark', 'Netherlands'), ('Chad', 'Equatorial Guinea'), ('Eritrea', 'Ethiopia'), ('Tunisia', 'Western Sahara'), ('Andorra', 'Gibraltar'), ('Bulgaria', 'Kosovo'), ('Israel', 'Saudi Arabia'), ('France', 'Portugal'), ('Bosnia and Herzegovina', 'Serbia'), ('Algeria', 'Senegal'), ('Namibia', 'Tanzania'), ('Burkina Faso', 'Togo'), ('Ghana', 'Ivory Coast'), ('Romania', 'Slovenia'), ('Guinea', 'Liberia'), ('Niger', 'Togo'), ('Cameroon', 'Equatorial Guinea'), ('Rwanda', 'Zambia'), ('Gibraltar', 'Portugal')]

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

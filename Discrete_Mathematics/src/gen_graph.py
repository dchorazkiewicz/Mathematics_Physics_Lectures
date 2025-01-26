import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def analyze_graph(adjacency_list, directed=False, node1=None, node2=None):
    # Creating a graph from an adjacency list (Tworzenie grafu z listy sąsiedztwa)
    if directed:
        G = nx.DiGraph()
    else:
        G = nx.Graph()

    for node, neighbors in adjacency_list.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    # Generating different representations (Generowanie różnych reprezentacji)
    adjacency_matrix = nx.adjacency_matrix(G).todense()
    incidence_matrix = nx.incidence_matrix(G, oriented=directed).astype(int).todense()

    print("=== Graph Representations (Reprezentacje grafu) ===")
    print("Adjacency list (Lista sąsiedztwa):")
    for node, neighbors in adjacency_list.items():
        print(f"{node}: {neighbors}")
    print("Adjacency matrix (Macierz sąsiedztwa):")
    print(adjacency_matrix)
    print("Incidence matrix (Macierz incydencji):")
    print(incidence_matrix)

    # Graph statistics (Statystyki grafu)
    print("\n=== Graph Statistics (Statystyki grafu) ===")
    print(f"Number of nodes (Liczba wierzchołków): {G.number_of_nodes()}")
    print(f"Number of edges (Liczba krawędzi): {G.number_of_edges()}")
    print(f"Node degrees (Stopnie wierzchołków): {dict(G.degree())}")

    if nx.is_connected(G) if not directed else nx.is_strongly_connected(G):
        print("The graph is connected (Graf jest spójny).")
        diameter = nx.diameter(G) if not directed else nx.diameter(nx.to_undirected(G))
        print(f"Graph diameter (Średnica grafu): {diameter}")
        radius = nx.radius(G) if not directed else nx.radius(nx.to_undirected(G))
        print(f"Graph radius (Promień grafu): {radius}")
        center = nx.center(G) if not directed else nx.center(nx.to_undirected(G))
        print(f"Graph center (Centrum grafu): {center}")
    else:
        print("The graph is not connected (Graf nie jest spójny).")

    if nx.is_eulerian(G):
        print("The graph is Eulerian (Graf jest eulerowski).")
    else:
        print("The graph is not Eulerian (Graf nie jest eulerowski).")

    if nx.is_tree(G):
        print("The graph is a tree (Graf jest drzewem).")
    else:
        print("The graph is not a tree (Graf nie jest drzewem).")

    print(f"Graph density (Gęstość grafu): {nx.density(G)}")

    try:
        cycle_basis = list(nx.find_cycle(G))
        print(f"Graph circumference (Obwód grafu): {len(cycle_basis)}")
    except nx.NetworkXNoCycle:
        print("The graph does not contain a cycle (Graf nie zawiera cyklu).")

    # Shortest path between two nodes (Najkrótsza ścieżka między dwoma wierzchołkami)
    if node1 is not None and node2 is not None:
        try:
            shortest_path = nx.shortest_path(G, source=node1, target=node2)
            shortest_path_length = nx.shortest_path_length(G, source=node1, target=node2)
            print(f"\nShortest path between {node1} and {node2} (Najkrótsza ścieżka między {node1} a {node2}): {shortest_path}")
            print(f"Length of the shortest path (Długość najkrótszej ścieżki): {shortest_path_length}")
        except nx.NetworkXNoPath:
            print(f"No path between {node1} and {node2} (Brak ścieżki między {node1} a {node2}).")


    # Drawing the graph (Rysowanie grafu)
    print("\n=== Graph Visualization (Wizualizacja grafu) ===")
    plt.figure(figsize=(10, 7))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray', font_size=15)
    plt.show()

# Example usage (Przykład użycia)
adj_list = {
    1: [3],
    2: [1,4],
    3: [1,4,5],
    4: [6,7],
    5: [6,2],
    6: [4,5],
    7: [8],
    8: [7]
}

analyze_graph(adj_list, directed=True, node1=5, node2=8)

def build_curriculum():
    import networkx as nx
    G = nx.DiGraph()
    G.add_edges_from([
        ("CS101", "CS102"),
        ("CS102", "AI201"),
        ("CS102", "ML201"),
        ("Math101", "ML201"),
        ("Math101", "DS201"),
        ("DS201", "Capstone")
    ])
    return G

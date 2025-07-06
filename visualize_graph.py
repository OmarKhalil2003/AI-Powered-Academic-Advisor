import matplotlib.pyplot as plt
import networkx as nx
from curriculum_graph import build_curriculum

G = build_curriculum()
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_size=1500, node_color="lightblue", font_size=10)
plt.savefig("results/curriculum_graph.png")

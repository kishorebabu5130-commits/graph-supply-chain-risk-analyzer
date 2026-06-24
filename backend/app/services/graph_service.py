import networkx as nx

from sqlalchemy.orm import Session

from app.models.supplier import Supplier
from app.models.dependency import Dependency


#Graph Builder

def build_graph(db: Session):

    G = nx.DiGraph()

    suppliers = db.query(
        Supplier
    ).all()

    dependencies = db.query(
        Dependency
    ).all()

    for supplier in suppliers:
        G.add_node(
            supplier.id,
            name=supplier.supplier_name
        )

    for dependency in dependencies:
        G.add_edge(
            dependency.supplier_id,
            dependency.depends_on_supplier_id,
            weight=dependency.dependency_weight
        )

    print("GRAPH NODES")
    print(list(G.nodes(data=True)))

    print("GRAPH EDGES")
    print(list(G.edges(data=True)))

    return G


#Graph Endpoint Data

def get_graph_data(db: Session):

    G = build_graph(db)

    nodes = []

    for node in G.nodes(data=True):
        nodes.append({
            "id": node[0],
            "name": node[1].get("name", f"Supplier-{node[0]}")
        })

    edges = []

    for edge in G.edges(data=True):
        edges.append({
            "source": edge[0],
            "target": edge[1],
            "weight": edge[2]["weight"]
        })

    return {
        "nodes": nodes,
        "edges": edges,
        "metadata": {
            "node_count": G.number_of_nodes(),
            "edge_count": G.number_of_edges()
        }
    }



#Centrality Metrics 

def get_centrality_metrics(
    db: Session
):
    G = build_graph(db)

    return {
        "degree_centrality":
            nx.degree_centrality(G),

        "betweenness_centrality":
            nx.betweenness_centrality(G),

        "pagerank":
            nx.pagerank(G)
    }



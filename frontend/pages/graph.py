import streamlit as st
import networkx as nx
import plotly.graph_objects as go

from services.api_client import (
    get_graph,
    get_centrality
)

st.title("Supply Chain Network")

graph_data = get_graph()

nodes = graph_data["nodes"]
edges = graph_data["edges"]

G = nx.DiGraph()

for node in nodes:
    G.add_node(
        node["id"],
        name=node["name"]
    )

for edge in edges:
    G.add_edge(
        edge["source"],
        edge["target"]
    )

pos = nx.spring_layout(G)

edge_x = []
edge_y = []

for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]

    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])

edge_trace = go.Scatter(
    x=edge_x,
    y=edge_y,
    mode="lines"
)

node_x = []
node_y = []
node_text = []

for node in G.nodes():
    x, y = pos[node]

    node_x.append(x)
    node_y.append(y)

    node_text.append(
        G.nodes[node]["name"]
    )

node_trace = go.Scatter(
    x=node_x,
    y=node_y,
    mode="markers+text",
    text=node_text,
    textposition="top center"
)

fig = go.Figure(
    data=[
        edge_trace,
        node_trace
    ]
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader("Centrality Metrics")

centrality = get_centrality()

st.json(centrality)
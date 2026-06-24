from pydantic import BaseModel
from typing import List, Dict


class GraphNode(BaseModel):
    id: int
    name: str


class GraphEdge(BaseModel):
    source: int
    target: int
    weight: float


class GraphResponse(BaseModel):
    nodes: List[GraphNode]
    edges: List[GraphEdge]
    metadata: Dict
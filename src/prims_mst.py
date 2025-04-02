import heapq
from typing import List, Tuple, Dict

def prims_algorithm(graph: Dict[int, List[Tuple[int, int]]]) -> List[Tuple[int, int, int]]:
    """
    Implement Prim's algorithm to find the Minimum Spanning Tree (MST) of a graph.
    
    Args:
        graph (Dict[int, List[Tuple[int, int]]]): An adjacency list representation of the graph.
                Each key is a vertex, and the value is a list of (neighbor, weight) tuples.
    
    Returns:
        List[Tuple[int, int, int]]: A list of edges in the Minimum Spanning Tree,
                represented as (source, destination, weight) tuples.
    
    Raises:
        ValueError: If the graph is empty or not connected.
    
    Time Complexity: O((V + E) log V), where V is the number of vertices and E is the number of edges.
    Space Complexity: O(V + E)
    """
    # Validate input
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    # Choose an arbitrary starting vertex
    start_vertex = list(graph.keys())[0]
    
    # Track visited vertices and the minimum spanning tree
    visited = set([start_vertex])
    mst_edges = []
    
    # Priority queue to store edges to explore
    # Format: (weight, source, destination)
    pq = []
    
    # Add initial edges from the start vertex
    for neighbor, weight in graph[start_vertex]:
        heapq.heappush(pq, (weight, start_vertex, neighbor))
    
    # Continue until all vertices are visited
    while pq:
        weight, source, dest = heapq.heappop(pq)
        
        # Skip if destination already visited
        if dest in visited:
            continue
        
        # Add the edge to MST
        mst_edges.append((source, dest, weight))
        visited.add(dest)
        
        # Explore edges from the newly added vertex
        for neighbor, edge_weight in graph[dest]:
            if neighbor not in visited:
                heapq.heappush(pq, (edge_weight, dest, neighbor))
    
    # Check if all vertices were visited (graph is connected)
    if len(visited) != len(graph):
        raise ValueError("Graph is not connected. Cannot form a spanning tree.")
    
    return mst_edges
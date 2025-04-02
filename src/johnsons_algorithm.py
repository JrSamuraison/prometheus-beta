import heapq
import math
from typing import List, Dict, Tuple, Optional

def johnsons_algorithm(graph: Dict[int, Dict[int, int]]) -> Optional[Dict[int, Dict[int, int]]]:
    """
    Implement Johnson's algorithm for finding shortest paths between all pairs of vertices.
    
    Johnson's algorithm combines the Bellman-Ford algorithm to reweight edges 
    and Dijkstra's algorithm to find shortest paths efficiently.
    
    Args:
        graph (Dict[int, Dict[int, int]]): Adjacency list representation of the graph.
                                           Keys are source vertices, values are dictionaries 
                                           of destination vertices and their edge weights.
    
    Returns:
        Optional[Dict[int, Dict[int, int]]]: Dictionary of shortest paths between all vertex pairs.
                                             None if a negative cycle is detected.
    
    Raises:
        ValueError: If the graph is empty or contains invalid inputs.
    """
    # Validate input
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    # Add a new vertex with zero-weight edges to all other vertices
    vertices = list(graph.keys())
    dummy_vertex = max(vertices) + 1 if vertices else 0
    graph[dummy_vertex] = {v: 0 for v in vertices}
    
    # Step 1: Run Bellman-Ford to detect negative cycles and reweight edges
    h = bellman_ford(graph, dummy_vertex)
    if h is None:
        return None  # Negative cycle detected
    
    # Remove the dummy vertex
    del graph[dummy_vertex]
    
    # Step 2: Reweight the edges
    reweighted_graph = {}
    for u in graph:
        reweighted_graph[u] = {}
        for v, weight in graph[u].items():
            reweighted_graph[u][v] = weight + h[u] - h[v]
    
    # Step 3: Run Dijkstra for each vertex
    shortest_paths = {}
    for u in graph:
        shortest_paths[u] = dijkstra(reweighted_graph, u)
        
        # Correct the distances back to original weights
        for v in shortest_paths[u]:
            if shortest_paths[u][v] is not None:
                shortest_paths[u][v] += h[v] - h[u]
    
    return shortest_paths

def bellman_ford(graph: Dict[int, Dict[int, int]], source: int) -> Optional[Dict[int, int]]:
    """
    Bellman-Ford algorithm to detect negative cycles and compute vertex potentials.
    
    Args:
        graph (Dict[int, Dict[int, int]]): Graph represented as adjacency list
        source (int): Source vertex for computing distances
    
    Returns:
        Optional[Dict[int, int]]: Dictionary of vertex potentials, or None if negative cycle exists
    """
    # Initialize distances
    vertices = list(graph.keys())
    dist = {v: math.inf for v in vertices}
    dist[source] = 0
    
    # Relax edges |V| - 1 times
    for _ in range(len(vertices) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if dist[u] != math.inf and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
    
    # Check for negative cycles
    for u in graph:
        for v, weight in graph[u].items():
            if dist[u] != math.inf and dist[u] + weight < dist[v]:
                return None  # Negative cycle detected
    
    return dist

def dijkstra(graph: Dict[int, Dict[int, int]], source: int) -> Dict[int, Optional[int]]:
    """
    Dijkstra's algorithm for finding shortest paths from a source vertex.
    
    Args:
        graph (Dict[int, Dict[int, int]]): Graph represented as adjacency list
        source (int): Source vertex for computing distances
    
    Returns:
        Dict[int, Optional[int]]: Dictionary of shortest distances to each vertex
    """
    # Initialize distances and priority queue
    dist = {v: None for v in graph}
    dist[source] = 0
    pq = [(0, source)]
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        # If we've found a longer path to u, skip
        if current_dist > dist[u]:
            continue
        
        # Check all neighbors
        for v, weight in graph[u].items():
            distance = current_dist + weight
            
            # Update distance if shorter path found
            if dist[v] is None or distance < dist[v]:
                dist[v] = distance
                heapq.heappush(pq, (distance, v))
    
    return dist
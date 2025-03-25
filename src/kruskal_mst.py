from typing import List, Tuple

class DisjointSet:
    """
    Disjoint Set (Union-Find) data structure to detect cycles in a graph.
    
    This helper class is used in Kruskal's algorithm to efficiently 
    determine if adding an edge creates a cycle in the minimum spanning tree.
    """
    def __init__(self, vertices: int):
        """
        Initialize the DisjointSet with each vertex in its own set.
        
        Args:
            vertices (int): Number of vertices in the graph
        """
        self.parent = list(range(vertices))
        self.rank = [0] * vertices
    
    def find(self, item: int) -> int:
        """
        Find the root (representative) of a set with path compression.
        
        Args:
            item (int): Vertex to find the root for
        
        Returns:
            int: Root of the set containing the vertex
        """
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    
    def union(self, x: int, y: int) -> bool:
        """
        Merge two sets by rank, preventing cycles.
        
        Args:
            x (int): First vertex
            y (int): Second vertex
        
        Returns:
            bool: True if union was successful (no cycle), False otherwise
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        # If roots are same, it would create a cycle
        if root_x == root_y:
            return False
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        
        self.parent[root_y] = root_x
        
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        
        return True

def kruskal_mst(vertices: int, edges: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
    """
    Implement Kruskal's algorithm to find the Minimum Spanning Tree (MST).
    
    Args:
        vertices (int): Number of vertices in the graph
        edges (List[Tuple[int, int, int]]): List of edges, where each edge is 
                                            (source, destination, weight)
    
    Returns:
        List[Tuple[int, int, int]]: List of edges in the Minimum Spanning Tree
    
    Raises:
        ValueError: If input is invalid (no vertices or no edges)
    """
    # Input validation
    if vertices <= 0:
        raise ValueError("Number of vertices must be positive")
    
    if not edges:
        raise ValueError("Graph must have at least one edge")
    
    # Sort edges by weight in ascending order
    edges.sort(key=lambda x: x[2])
    
    # Initialize Disjoint Set
    disjoint_set = DisjointSet(vertices)
    
    # List to store MST edges
    mst_edges = []
    
    # Process edges
    for edge in edges:
        src, dest, weight = edge
        
        # Check if adding this edge creates a cycle
        if disjoint_set.union(src, dest):
            mst_edges.append(edge)
        
        # Stop when MST is complete (vertices - 1 edges)
        if len(mst_edges) == vertices - 1:
            break
    
    return mst_edges
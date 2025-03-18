class DisjointSet:
    """
    Disjoint Set (Union-Find) data structure to help with Kruskal's algorithm.
    
    This class provides efficient operations for detecting cycles and 
    connecting components in a graph.
    """
    def __init__(self, vertices):
        """
        Initialize the Disjoint Set data structure.
        
        :param vertices: Number of vertices in the graph
        """
        # Parent array to track the parent of each vertex
        self.parent = list(range(vertices))
        
        # Rank array to optimize union by rank
        self.rank = [0] * vertices

    def find(self, item):
        """
        Find the root (representative) of a set with path compression.
        
        :param item: Vertex to find the root for
        :return: Root of the set containing the vertex
        """
        # Path compression: make each node point directly to the root
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        """
        Union two sets by rank.
        
        :param x: First vertex
        :param y: Second vertex
        :return: True if union was successful (no cycle), False otherwise
        """
        # Find roots of both sets
        root_x = self.find(x)
        root_y = self.find(y)

        # If roots are same, a cycle is detected
        if root_x == root_y:
            return False

        # Union by rank to keep the tree balanced
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x

        # Update rank if needed
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        return True

def kruskal_mst(graph):
    """
    Implement Kruskal's algorithm to find the Minimum Spanning Tree.
    
    :param graph: List of edges, where each edge is (weight, u, v)
    :return: List of edges in the Minimum Spanning Tree
    :raises ValueError: If graph is None or empty
    """
    # Input validation
    if graph is None:
        raise ValueError("Graph cannot be None")
    
    if not graph:
        return []

    # Sort edges by weight in ascending order
    edges = sorted(graph, key=lambda x: x[0])
    
    # Number of vertices is the max vertex index + 1
    vertices = max(max(edge[1], edge[2]) for edge in graph) + 1
    
    # Initialize Disjoint Set
    ds = DisjointSet(vertices)
    
    # Minimum Spanning Tree storage
    mst = []
    
    # Kruskal's algorithm
    for edge in edges:
        weight, u, v = edge
        
        # If including this edge doesn't create a cycle, add it to MST
        if ds.union(u, v):
            mst.append(edge)
        
        # Stop when MST is complete (vertices - 1 edges)
        if len(mst) == vertices - 1:
            break
    
    return mst
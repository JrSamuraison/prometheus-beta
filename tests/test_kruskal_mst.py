import pytest
from src.kruskal_mst import kruskal_mst, DisjointSet

def test_disjoint_set():
    """Test the DisjointSet data structure."""
    ds = DisjointSet(5)
    
    # Test initial state
    assert ds.find(0) != ds.find(1)
    assert ds.find(2) != ds.find(3)
    
    # Test union
    assert ds.union(0, 1) is True
    assert ds.find(0) == ds.find(1)
    
    # Attempting to union already connected vertices should return False
    assert ds.union(0, 1) is False

def test_kruskal_mst_basic():
    """Test basic Kruskal's algorithm scenario."""
    # Simple graph: 4 vertices, 5 edges
    vertices = 4
    edges = [
        (0, 1, 10),   # weight 10
        (0, 2, 6),    # weight 6
        (0, 3, 5),    # weight 5
        (1, 3, 15),   # weight 15
        (2, 3, 4)     # weight 4
    ]
    
    mst = kruskal_mst(vertices, edges)
    
    # Expected MST edges (sorted by weight)
    expected_mst = [
        (2, 3, 4),    # lowest weight
        (0, 3, 5),    # next lowest
        (0, 1, 10)    # connects remaining vertices
    ]
    
    # Verify MST contains expected edges
    assert len(mst) == 3  # MST always has (vertices - 1) edges
    assert sorted(mst) == sorted(expected_mst)

def test_kruskal_mst_total_weight():
    """Test total weight of the minimum spanning tree."""
    vertices = 4
    edges = [
        (0, 1, 10),   # weight 10
        (0, 2, 6),    # weight 6
        (0, 3, 5),    # weight 5
        (1, 3, 15),   # weight 15
        (2, 3, 4)     # weight 4
    ]
    
    mst = kruskal_mst(vertices, edges)
    
    # Calculate total MST weight
    total_weight = sum(edge[2] for edge in mst)
    
    assert total_weight == 19  # 4 + 5 + 10

def test_kruskal_mst_error_handling():
    """Test error handling for invalid inputs."""
    # Test zero vertices
    with pytest.raises(ValueError, match="Number of vertices must be positive"):
        kruskal_mst(0, [(0, 1, 5)])
    
    # Test no edges
    with pytest.raises(ValueError, match="Graph must have at least one edge"):
        kruskal_mst(3, [])

def test_kruskal_mst_disconnected_graph():
    """Test scenario where graph might have disconnected components."""
    vertices = 5
    edges = [
        (0, 1, 1),    # Component 1
        (2, 3, 2),    # Component 2
        (0, 2, 3)     # Connects components
    ]
    
    mst = kruskal_mst(vertices, edges)
    
    # Ensure MST connects all vertices
    assert len(mst) == 4  # For 5 vertices
    
    # Check total weight
    total_weight = sum(edge[2] for edge in mst)
    assert total_weight == 6  # 1 + 2 + 3

def test_kruskal_mst_all_same_weight():
    """Test scenario where all edges have the same weight."""
    vertices = 4
    edges = [
        (0, 1, 5),
        (0, 2, 5),
        (0, 3, 5),
        (1, 2, 5),
        (1, 3, 5),
        (2, 3, 5)
    ]
    
    mst = kruskal_mst(vertices, edges)
    
    # Ensure MST has correct number of edges
    assert len(mst) == 3  # (vertices - 1) edges
    
    # Total weight should be consistent
    total_weight = sum(edge[2] for edge in mst)
    assert total_weight == 15  # 5 * 3
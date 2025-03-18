import pytest
from src.kruskal_mst import kruskal_mst, DisjointSet

def test_disjoint_set():
    """Test DisjointSet basic operations"""
    ds = DisjointSet(5)
    
    # Initially, each vertex is in its own set
    assert ds.find(0) != ds.find(1)
    
    # Union of sets
    ds.union(0, 1)
    assert ds.find(0) == ds.find(1)
    
    # Repeated union should not change state
    assert ds.union(0, 1) == False

def test_kruskal_basic():
    """Test basic Kruskal's algorithm with a simple graph"""
    # Graph: [(weight, vertex1, vertex2), ...]
    graph = [
        (1, 0, 1),
        (4, 1, 2),
        (3, 0, 2),
        (2, 1, 3),
        (5, 2, 3)
    ]
    
    mst = kruskal_mst(graph)
    
    # Expected total edges in MST is vertices - 1
    assert len(mst) == 3
    
    # Verify total weight is minimal
    total_weight = sum(edge[0] for edge in mst)
    assert total_weight == 6  # 1 + 2 + 3

def test_kruskal_disconnected():
    """Test Kruskal's algorithm with a disconnected graph"""
    graph = [
        (1, 0, 1),
        (5, 2, 3),
        (7, 4, 5)
    ]
    
    mst = kruskal_mst(graph)
    
    # Should return a subset of edges that connect accessible vertices
    assert len(mst) == 1
    assert mst[0] == (1, 0, 1)

def test_kruskal_edge_cases():
    """Test edge cases for Kruskal's algorithm"""
    # Empty graph
    assert kruskal_mst([]) == []
    
    # Single edge graph
    single_edge_graph = [(10, 0, 1)]
    assert kruskal_mst(single_edge_graph) == single_edge_graph

def test_kruskal_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError):
        kruskal_mst(None)

def test_kruskal_complex_graph():
    """Test Kruskal's algorithm with a more complex graph"""
    graph = [
        (2, 0, 1),
        (3, 1, 2),
        (1, 0, 2),
        (4, 1, 3),
        (5, 2, 3),
        (6, 3, 4),
        (7, 0, 4)
    ]
    
    mst = kruskal_mst(graph)
    
    # Expected total edges in MST is vertices - 1
    assert len(mst) == 4
    
    # Verify MST includes the cheapest edges
    expected_edges = {(1, 0, 2), (2, 0, 1), (3, 1, 2), (4, 1, 3)}
    assert set(mst) == expected_edges
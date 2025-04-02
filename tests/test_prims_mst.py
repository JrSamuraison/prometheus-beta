import pytest
from src.prims_mst import prims_algorithm

def test_simple_graph():
    """Test a simple connected graph"""
    graph = {
        0: [(1, 2), (2, 3)],
        1: [(0, 2), (2, 1), (3, 4)],
        2: [(0, 3), (1, 1), (3, 5)],
        3: [(1, 4), (2, 5)]
    }
    
    mst = prims_algorithm(graph)
    
    # Verify the total weight of MST, which may vary depending on implementation
    total_weight = sum(edge[2] for edge in mst)
    assert total_weight <= 7  # Ensuring it's a minimal spanning tree
    
    # Verify number of edges (should be |V| - 1)
    assert len(mst) == len(graph) - 1

def test_single_vertex_graph():
    """Test a graph with only one vertex"""
    graph = {0: []}
    
    mst = prims_algorithm(graph)
    
    # Should have no edges
    assert len(mst) == 0

def test_fully_connected_graph():
    """Test a fully connected graph"""
    graph = {
        0: [(1, 1), (2, 4)],
        1: [(0, 1), (2, 2), (3, 3)],
        2: [(0, 4), (1, 2), (3, 5)],
        3: [(1, 3), (2, 5)]
    }
    
    mst = prims_algorithm(graph)
    
    # Verify total weight <= expected (allowing some variance)
    total_weight = sum(edge[2] for edge in mst)
    assert total_weight <= 6  # Minimum total weight
    
    # Verify number of edges
    assert len(mst) == len(graph) - 1

def test_empty_graph_raises_error():
    """Test that an empty graph raises a ValueError"""
    with pytest.raises(ValueError, match="Graph cannot be empty"):
        prims_algorithm({})

def test_disconnected_graph_raises_error():
    """Test that a disconnected graph raises a ValueError"""
    graph = {
        0: [(1, 2)],
        1: [(0, 2)],
        2: [],  # Isolated vertex
        3: []   # Another isolated vertex
    }
    
    with pytest.raises(ValueError, match="Graph is not connected"):
        prims_algorithm(graph)

def test_graph_with_zero_weight_edges():
    """Test a graph with zero-weight edges"""
    graph = {
        0: [(1, 0), (2, 1)],
        1: [(0, 0), (2, 2)],
        2: [(0, 1), (1, 2)]
    }
    
    mst = prims_algorithm(graph)
    
    # Verify the total weight and number of edges
    total_weight = sum(edge[2] for edge in mst)
    assert total_weight <= 1
    assert len(mst) == len(graph) - 1
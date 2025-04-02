import pytest
import math
from src.johnsons_algorithm import johnsons_algorithm, bellman_ford, dijkstra

def test_johnsons_algorithm_basic_graph():
    """Test Johnson's algorithm with a simple weighted graph."""
    graph = {
        0: {1: 3, 2: 6},
        1: {2: 4, 3: 4},
        2: {3: 2},
        3: {}
    }
    result = johnsons_algorithm(graph)
    
    # Expected shortest paths
    assert result is not None
    assert result[0][3] == 7  # 0 -> 1 -> 3 with total weight 7
    assert result[1][3] == 4  # 1 -> 3 direct path
    assert result[2][3] == 2  # 2 -> 3 direct path

def test_johnsons_algorithm_disconnected_vertex():
    """Test a graph with a vertex not connected to others."""
    graph = {
        0: {1: 3},
        1: {2: 4},
        2: {},
        3: {}
    }
    result = johnsons_algorithm(graph)
    
    assert result is not None
    assert result[0][1] == 3
    assert result[0][2] == 7
    assert result[0][3] is None

def test_johnsons_algorithm_negative_weights():
    """Test Johnson's algorithm with negative edge weights."""
    graph = {
        0: {1: -1, 2: 4},
        1: {2: 3, 3: 2},
        2: {3: 5},
        3: {}
    }
    result = johnsons_algorithm(graph)
    
    assert result is not None
    assert result[0][3] == 1  # 0 -> 1 -> 3 with total weight 1

def test_johnsons_algorithm_negative_cycle():
    """Test Johnson's algorithm with a negative cycle."""
    graph = {
        0: {1: 1},
        1: {2: -3},
        2: {0: -2}
    }
    result = johnsons_algorithm(graph)
    
    assert result is None

def test_johnsons_algorithm_empty_graph():
    """Test Johnson's algorithm with an empty graph."""
    with pytest.raises(ValueError):
        johnsons_algorithm({})

def test_bellman_ford_basic():
    """Test Bellman-Ford algorithm for distance computation."""
    graph = {
        0: {1: 3, 2: 6},
        1: {2: 4, 3: 4},
        2: {3: 2},
        3: {}
    }
    result = bellman_ford(graph, 0)
    
    assert result is not None
    assert result[0] == 0
    assert result[1] == 3
    assert result[2] == 6
    assert result[3] == 7

def test_dijkstra_basic():
    """Test Dijkstra's algorithm for shortest paths."""
    graph = {
        0: {1: 3, 2: 6},
        1: {2: 4, 3: 4},
        2: {3: 2},
        3: {}
    }
    result = dijkstra(graph, 0)
    
    assert result[0] == 0
    assert result[1] == 3
    assert result[2] == 6
    assert result[3] == 7
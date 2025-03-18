import pytest
from src.astar_search import astar_search

def manhattan_distance(a, b):
    """Manhattan distance heuristic."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def test_simple_grid_path():
    """Test a simple grid path finding."""
    def get_neighbors(node):
        x, y = node
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    
    start = (0, 0)
    goal = (3, 3)
    
    path = astar_search(start, goal, get_neighbors, manhattan_distance)
    
    assert path is not None
    assert path[0] == start
    assert path[-1] == goal
    assert len(path) <= manhattan_distance(start, goal) + 1

def test_blocked_path():
    """Test path finding with obstacles."""
    blocked = {(1, 1), (1, 2), (1, 3)}
    
    def get_neighbors(node):
        x, y = node
        possible = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        return [n for n in possible if n not in blocked]
    
    start = (0, 0)
    goal = (3, 3)
    
    path = astar_search(start, goal, get_neighbors, manhattan_distance)
    
    assert path is not None
    assert path[0] == start
    assert path[-1] == goal
    assert all((1, y) not in path for y in range(1, 4))

def test_impossible_path():
    """Test when no path exists."""
    def get_neighbors(node):
        return []  # No neighbors possible
    
    start = (0, 0)
    goal = (3, 3)
    
    path = astar_search(start, goal, get_neighbors, manhattan_distance)
    
    assert path is None

def test_same_start_goal():
    """Test when start and goal are the same."""
    def get_neighbors(node):
        return []
    
    start = (2, 2)
    goal = (2, 2)
    
    path = astar_search(start, goal, get_neighbors, manhattan_distance)
    
    assert path == [(2, 2)]

def test_invalid_input():
    """Test handling of invalid inputs."""
    def get_neighbors(node):
        return []
    
    with pytest.raises(ValueError):
        astar_search(None, (3, 3), get_neighbors, manhattan_distance)
    
    with pytest.raises(ValueError):
        astar_search((0, 0), None, get_neighbors, manhattan_distance)
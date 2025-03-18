from typing import List, Tuple, Callable, Optional
import heapq

def astar_search(
    start: Tuple[int, int], 
    goal: Tuple[int, int], 
    get_neighbors: Callable[[Tuple[int, int]], List[Tuple[int, int]]], 
    heuristic: Callable[[Tuple[int, int], Tuple[int, int]], float], 
    cost_fn: Callable[[Tuple[int, int], Tuple[int, int]], float] = lambda a, b: 1
) -> Optional[List[Tuple[int, int]]]:
    """
    Implement A* search algorithm to find the optimal path between start and goal.
    
    Args:
        start (Tuple[int, int]): Starting coordinates
        goal (Tuple[int, int]): Target coordinates
        get_neighbors (Callable): Function to get valid neighboring nodes
        heuristic (Callable): Heuristic function estimating distance to goal
        cost_fn (Callable, optional): Function to calculate movement cost. Defaults to unit cost.
    
    Returns:
        Optional[List[Tuple[int, int]]]: Optimal path from start to goal, or None if no path exists
    
    Raises:
        ValueError: If start or goal is None
    """
    # Validate inputs
    if start is None or goal is None:
        raise ValueError("Start and goal must be valid coordinates")
    
    # Priority queue to store nodes to explore
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    # Tracking paths and costs
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    
    while open_set:
        # Get the node with lowest f_score
        current_f, current = heapq.heappop(open_set)
        
        # Check if reached goal
        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return list(reversed(path))
        
        # Explore neighbors
        for neighbor in get_neighbors(current):
            # Calculate tentative g_score
            tentative_g = g_score.get(current, float('inf')) + cost_fn(current, neighbor)
            
            # If this path is better than previous known path
            if tentative_g < g_score.get(neighbor, float('inf')):
                # Update tracking
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                
                # Add to open set if not already present
                if neighbor not in [n[1] for n in open_set]:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    # No path found
    return None
"""
A* Search Algorithm Implementation
"""
import heapq
from typing import Dict, List, Tuple, Optional, Callable
from .grid_world import GridWorld
def a_star(
    world: GridWorld,
    start: Tuple[int, int],
    goal: Tuple[int, int],
    heuristic: Callable,
    use_optimization: bool = True,
    verbose: bool = False
) -> Tuple[Optional[List[Tuple[int, int]]], int, float]:
    """
    A* search algorithm with optional closed set optimization.
    
    Args:
        world: GridWorld instance
        start: Starting position (x,y)
        goal: Goal position (x,y)
        heuristic: Heuristic function h(n)
        use_optimization: If True, use closed set (requires consistent heuristic)
        verbose: Print progress information
    
    Returns:
        Tuple of (path, expansions, cost)
        - path: List of positions from start to goal (None if not found)
        - expansions: Number of nodes expanded
        - cost: Total path cost (inf if not found)
    """
    
    # Priority queue: (f_score, g_score, node)
    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), 0, start))
    
    # Best known cost from start to each node
    g_score: Dict[Tuple[int, int], float] = {start: 0}
 
    # Parent pointers for path reconstruction
    parent: Dict[Tuple[int, int], Optional[Tuple[int, int]]] = {start: None}
    
    # Counter for node expansions
    expansions = 0
    
    # Closed set optimization
    closed_set = set() if use_optimization else None
    
    if verbose:
        print(f"Starting A* with {heuristic.__name__} (optimization={use_optimization})")
 
    while open_set:
        f, g, current = heapq.heappop(open_set)
 
        # Goal test
        if current == goal:
            if verbose:
                print(f"✓ Goal reached! Expanded {expansions} nodes")
    
            # Reconstruct path
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path, expansions, g_score[goal]
    
        # Closed set optimization
        if use_optimization:
            if current in closed_set:
                continue
            closed_set.add(current)
 
        expansions += 1
 
        # Explore neighbors
        for neighbor in world.neighbors(current):
            tentative_g = g_score[current] + 1 # Step cost = 1
    
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, tentative_g, neighbor))
                parent[neighbor] = current
 
    # No path found
    if verbose:
        print("✗ No path found!")
    return None, expansions, float('inf')
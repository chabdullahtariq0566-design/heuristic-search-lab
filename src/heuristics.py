"""
Heuristic Functions for A* Search
"""
import math
from typing import Tuple
def heuristic_zero(node: Tuple[int, int], goal: Tuple[int, int]) -> float:
    """
    Zero heuristic - turns A* into Dijkstra's algorithm.
 
    Args:
        node: Current position (x,y)
        goal: Goal position (x,y)
 
    Returns:
        0 (uninformed)
    """
    return 0.0
def heuristic_manhattan(node: Tuple[int, int], goal: Tuple[int, int]) -> float:
    """
    Manhattan distance heuristic for grid movement.
 
    Args:
        node: Current position (x,y)
        goal: Goal position (x,y)
    
    Returns:
        Manhattan distance: |x1-x2| + |y1-y2|
    """
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])
    
def heuristic_euclidean(node: Tuple[int, int], goal: Tuple[int, int]) -> float:
    """
    Euclidean distance heuristic.
    
    Args:
        node: Current position (x,y)
        goal: Goal position (x,y)
 
    Returns:
        Euclidean distance: sqrt((x1-x2)² + (y1-y2)²)
    """
    return math.hypot(node[0] - goal[0], node[1] - goal[1])
def heuristic_chebyshev(node: Tuple[int, int], goal: Tuple[int, int]) -> float:
    """
    Chebyshev distance (for 8-directional movement).
    
    Args:
        node: Current position (x,y)
        goal: Goal position (x,y)
    
    Returns:
        Chebyshev distance: max(|x1-x2|, |y1-y2|)
    """
    return max(abs(node[0] - goal[0]), abs(node[1] - goal[1]))

# Dictionary for easy lookup
HEURISTICS = {
    'zero': heuristic_zero,
    'manhattan': heuristic_manhattan,
    'euclidean': heuristic_euclidean,
    'chebyshev': heuristic_chebyshev
}
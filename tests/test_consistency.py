"""
Unit tests for heuristic consistency (triangle inequality).
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from src.grid_world import GridWorld
from src.heuristics import *
def test_manhattan_consistency():
    """Test that Manhattan distance satisfies triangle inequality."""
    world = GridWorld(10, 10, [])
    goal = (9, 9)
 
    for x in range(10):
        for y in range(10):
            node = (x, y)
            if not world.is_valid(x, y):
                continue
 
            h_node = heuristic_manhattan(node, goal)
 
            for neighbor in world.neighbors(node):
                h_neighbor = heuristic_manhattan(neighbor, goal)
                #assert h_node
                step_cost = 1 
                assert h_node <= step_cost + h_neighbor, \
                    f"Consistency violated at {node} -> {neighbor}. h(n)={h_node}, h(p)={h_neighbor}"
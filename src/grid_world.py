"""
Grid World Environment for Pathfinding
"""
import numpy as np
from typing import List, Tuple, Set, Optional
class GridWorld:
    """
    2D grid environment with obstacles for pathfinding experiments.
 
    Attributes:
        width (int): Number of columns
        height (int): Number of rows 
        obstacles (Set[Tuple[int, int]]): Set of blocked positions
    """
 
    def __init__(self, width: int, height: int, obstacles: Optional[List[Tuple[int, int]]] = None):
        """
        Initialize the grid world.
 
        Args:
            width: Grid width (x-axis)
            height: Grid height (y-axis)
            obstacles: List of (x,y) obstacle positions
        """
        self.width = width
        self.height = height
        self.obstacles = set(obstacles) if obstacles else set()
 
    def is_valid(self, x: int, y: int) -> bool:
        """Check if a position is within bounds and not an obstacle."""
        return (0 <= x < self.width and
        0 <= y < self.height and
        (x, y) not in self.obstacles)
    
    def neighbors(self, node: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
        Get all valid neighboring positions (4-directional).
    
        Args:
            node: Current position (x,y)
    
        Returns:
            List of valid neighbor positions
        """
        x, y = node
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        neighbors = []
    
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny):
                neighbors.append((nx, ny))
    
        return neighbors
 
    @classmethod
    def create_maze(cls, maze_type: str = "default", size: int = 10) -> 'GridWorld':
        """
        Factory method to create predefined maze configurations.
    
        Args:
            maze_type: Type of maze ('empty', 'sparse', 'dense', 'spiral', 'default')
            size: Size of the grid (size x size)

        Returns:
            Configured GridWorld instance
        """
        if maze_type == "empty":
            return cls(size, size, [])

        elif maze_type == "sparse":
            obstacles = [(i, size//2) for i in range(size//3, 2*size//3)]
            return cls(size, size, obstacles)
 
        elif maze_type == "dense":
            obstacles = []
            for i in range(size//4, 3*size//4, size//8):
                obstacles.extend([(i, j) for j in range(size)])
            return cls(size, size, obstacles)
 
        elif maze_type == "spiral":
            obstacles = []
            for i in range(2, size-2):
                obstacles.extend([(i, 2), (i, size-3), (2, i), (size-3, i)])
            return cls(size, size, obstacles)
 
        else: # default maze
            obstacles = [
                (3, i) for i in range(size)
                ] + [
                (i, size//2) for i in range(size//2, size)
                ] + [
                (1, 2), (2, 2), (size-3, size-3), (size-2, size-3)
            ]
            return cls(size, size, obstacles)
 
    def visualize(self, path=None, start=None, goal=None, title="Grid World"):
        """
        Visualize the grid world with obstacles, path, start, and goal.
        """
        import matplotlib.pyplot as plt
        from matplotlib.patches import Rectangle, Circle
    
        fig, ax = plt.subplots(1, 1, figsize=(10, 10))
 
        # Draw grid cells
        for x in range(self.width):
            for y in range(self.height):
                if (x, y) in self.obstacles:
                    rect = Rectangle((x, y), 1, 1, facecolor='black', edgecolor='gray')
                    ax.add_patch(rect)
                else:
                    rect = Rectangle((x, y), 1, 1, facecolor='white', edgecolor='lightgray')
                    ax.add_patch(rect)
 
        # Draw path if provided
        if path:
            path_x = [p[0] + 0.5 for p in path]
            path_y = [p[1] + 0.5 for p in path]
            ax.plot(path_x, path_y, 'b-', linewidth=3, alpha=0.7, label='Path')
            ax.scatter(path_x, path_y, c='blue', s=50, alpha=0.7)
    
        # Draw start
        if start:
            circle = Circle((start[0] + 0.5, start[1] + 0.5), 0.3,
            facecolor='green', edgecolor='darkgreen', linewidth=2)
            ax.add_patch(circle)
            ax.text(start[0] + 0.5, start[1] + 0.5, 'S',
            ha='center', va='center', fontweight='bold', color='white')
    
        # Draw goal
        if goal:
            circle = Circle((goal[0] + 0.5, goal[1] + 0.5), 0.3,
            facecolor='red', edgecolor='darkred', linewidth=2)
            ax.add_patch(circle)
            ax.text(goal[0] + 0.5, goal[1] + 0.5, 'G',
            ha='center', va='center', fontweight='bold', color='white')
    
        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)
        ax.set_xticks(range(self.width + 1))
        ax.set_yticks(range(self.height + 1))
        ax.grid(True, linestyle='--', alpha=0.5)
        ax.set_aspect('equal')
        ax.set_title(title, fontsize=14, fontweight='bold')
        ax.legend(loc='upper right')
 
        plt.tight_layout()
        plt.show()
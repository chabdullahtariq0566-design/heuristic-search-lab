import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.grid_world import GridWorld
from src.evaluator import HeuristicEvaluator
from src.heuristics import HEURISTICS

def test_admissibility():
    print("\n--- Running Admissibility Tests ---")
    world = GridWorld.create_maze("empty", size=10)
    evaluator = HeuristicEvaluator(world, (0,0), (9,9))
    
    for name, func in HEURISTICS.items():
        is_adm, opt, h_val = evaluator.test_admissibility(func)
        status = "✅" if is_adm else "❌"
        print(f"{status} {name:10} | Optimal: {opt} | Heuristic: {h_val}")

if __name__ == "__main__":
    test_admissibility()
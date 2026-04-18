Heuristic Search & Empirical Evaluation Lab 🚀
Author: Abdullah

Affiliation: Riphah School of Computing & Innovation (RSCI), Lahore

Domain: Artificial Intelligence / Pathfinding & Optimization

📌 Project Overview
This repository contains a comprehensive framework for implementing, testing, and evaluating Heuristic Search Algorithms. The core focus is the A Search Algorithm* and an empirical analysis of how different heuristic functions—Manhattan, Euclidean, and Chebyshev—affect search efficiency, computational cost, and path optimality in 2D grid environments.

🏗️ Project Structure
The project follows a modular and scalable Python package structure:
heuristic-search-lab/
├── README.md # Project overview and instructions
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore file
├── setup.py # Package setup
├── LICENSE # MIT License
│
├── src/ # Source code
│ ├── __init__.py
│ ├── grid_world.py # Grid environment
│ ├── heuristics.py # Heuristic functions
│ ├── a_star.py # A* implementation
│ ├── evaluator.py # Evaluation metrics
│ └── visualizer.py # Visualization tools
│
├── notebooks/ # Jupyter notebooks
│ ├── 01_Introduction.ipynb
│ ├── 02_Heuristics_Visualized.ipynb
│ ├── 03_A_Star_Implementation.ipynb
│ ├── 04_Empirical_Evaluation.ipynb
│ └── 05_Final_Project.ipynb
│
├── experiments/ # Experiment scripts
│ ├── run_all_experiments.py
│ ├── compare_heuristics.py
│ ├── test_admissibility.py
│ └── benchmark_mazes.py
│
├── tests/ # Unit tests
│ ├── __init__.py
│ ├── test_grid_world.py
│ ├── test_heuristics.py
│ ├── test_a_star.py
│ └── test_consistency.py
│
├── results/ # Output directory (gitignored)
│ ├── figures/
│ ├── data/
│ └── logs/
│
├── docs/ # Documentation
│ ├── tutorial.md
│ ├── api_reference.md
│ └── experiments_guide.md
│
└── scripts/ # Utility scripts
 ├── setup_environment.sh
 ├── run_tests.sh
 └── clean_results.sh

🚀 Getting Started

1. Installation

# Clone the repository
git clone https://github.com/yourusername/heuristic-search-lab.git
cd heuristic-search-lab

# Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -e .

2. Running Experiments
To run the full suite of evaluations and generate performance graphs:

PowerShell
python experiments/run_all_experiments.py

Efficiency Analysis
Performance is measured by comparing Node Expansions vs. Path Optimality. We analyze how uninformed searches (Dijkstra/Zero Heuristic) compare against informed searches (A* with Manhattan).

🛠️ Tech Stack
Language: Python 3.13+

Libraries: NumPy, Pandas, Matplotlib, Seaborn

Testing: Pytest

📝 License
This project is licensed under the MIT License.
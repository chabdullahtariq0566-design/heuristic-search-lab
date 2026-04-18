from setuptools import setup, find_packages
setup( 
    name="heuristic-search-lab",
    version="1.0.0",
    author="Abdullah",
    description="A comprehensive lab for learning heuristic search and A* algorithm",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
    line.strip() for line in open("requirements.txt").readlines()
    ],
)
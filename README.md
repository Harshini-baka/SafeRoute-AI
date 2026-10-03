# SafeRoute AI

A dynamic emergency evacuation route planning system that finds safer paths through a building while accounting for changing fire and smoke hazards.

## Overview

SafeRoute AI simulates an emergency evacuation scenario inside a building.

The system represents a building as a grid containing walls, an evacuee, an exit, fire, and smoke. It uses hazard-aware Dijkstra pathfinding to calculate a safer evacuation route while the environment changes dynamically.

As fire and smoke spread, the system updates the building and recalculates the route.

The simulation is visualized using Pygame.

## Problem Statement

During an emergency such as a building fire, the shortest path to an exit may not always be the safest path.

A route that is initially available may become dangerous as fire and smoke spread.

SafeRoute AI addresses this problem by combining:

- Grid-based building representation
- Dynamic fire propagation
- Dynamic smoke propagation
- Hazard-aware pathfinding
- Continuous route recalculation
- Real-time visualization

## Objectives

- Represent a building as a 2D grid.
- Model walls, exits, people, fire, and smoke.
- Simulate dynamic fire and smoke propagation.
- Find evacuation routes using pathfinding algorithms.
- Assign higher traversal costs to hazardous areas.
- Recalculate routes as environmental conditions change.
- Detect when no safe route is available.
- Provide a visual simulation using Pygame.
- Maintain automated tests for the core components.

## Features

### Dynamic Hazard Simulation

Fire and smoke change the environment during the simulation.

### Hazard-Aware Pathfinding

Dijkstra's algorithm considers the cost of entering different cell types.

Current cost model:

| Cell | Cost |
|------|------|
| Empty | 1 |
| Smoke | 5 |
| Fire | Impassable |
| Wall | Impassable |

### Dynamic Route Recalculation

The evacuation route is recalculated as the environment changes.

### No Safe Route Detection

If the destination cannot be reached through available safe cells, the system reports that no safe route is currently available.

### Visualization

Pygame displays:

- Walls
- Person
- Exit
- Smoke
- Fire
- Calculated route
- Route status

## Algorithms

### BFS

Breadth-First Search is used as a baseline pathfinding algorithm.

BFS finds a path based on the number of steps and does not consider hazard costs.

### Dijkstra's Algorithm

Dijkstra's algorithm is used for hazard-aware routing.

Unlike BFS, Dijkstra can assign different costs to different cells.

Therefore, it can prefer a slightly longer route through safe cells over a shorter route through smoke.

## System Architecture

```text
                Building Environment
                         |
             +-----------+-----------+
             |                       |
             v                       v
       Hazard Simulator         Pathfinding
             |                       |
       +-----+------+           +----+----+
       |            |           |         |
     Fire         Smoke        BFS    Dijkstra
       |            |                     |
       +-----+------+                     |
             |                            |
             v                            |
      Updated Environment                 |
             |                            |
             +------------+---------------+
                          |
                          v
                  Route Recalculation
                          |
                          v
                   Pygame Visualization

## Project Structure

SafeRoute-AI/
│
├── src/
│   ├── environment/
│   │   ├── building.py
│   │   ├── grid.py
│   │   └── hazard.py
│   │
│   └── pathfinding/
│       ├── bfs.py
│       └── dijkstra.py
│
├── tests/
│   ├── test_bfs.py
│   ├── test_building.py
│   ├── test_dijkstra.py
│   ├── test_hazard.py
│   └── test_pathfinding_comparison.py
│
├── .gitignore
├── requirements.txt
└── README.md

## Technologies used

Python
Pygame
Pytest
Git
GitHub

## Installation

Clone the repository:

git clone https://github.com/Harshini-baka/SafeRoute-AI.git
cd SafeRoute-AI

Create a virtual environment:

python -m venv .venv

Activate it on Windows:

.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

## Running the Simulation

python -m src.environment.grid

## Running Tests

python -m pytest -v

The project currently contains automated tests covering:

Building representation
BFS pathfinding
Dijkstra pathfinding
BFS/Dijkstra comparison
Fire propagation
Smoke propagation
Hazard updates

## Current Limitations

The current version is a simulation prototype.

Some aspects are simplified:

The building is represented as a 2D grid.
Fire and smoke propagation use simplified rules.
Hazard spread is probabilistic.
Only a single evacuee and exit are currently modeled.
The environment does not represent a physically accurate building.
The system does not use real sensor data.

## Future Improvements

Possible future improvements include:

Multiple evacuees
Multiple exits
More realistic fire and smoke models
Different smoke density levels
Dynamic hazard costs
Real-world building map support
Multiple evacuation strategies
Performance optimization for larger buildings
Machine-learning-based hazard prediction
Sensor or IoT integration
More advanced visualization

## Testing Status

The current implementation includes an automated test suite for the major components of the system.

9 tests passing
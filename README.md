# EVRP_TW


This repository implements the **Electric Vehicle Routing Problem with Time Windows (EVRP_TW)**, aimed at optimizing routing and charging schedules for electric vehicles.

## Folder Structure
```
.
├── EVRP_Graph.py # Contains the Graph_EVRP_TW class for representing the EVRP-TW graph structure
├── EVRP_Solver.py # Implements the EVPR_TW_Solver class
├── README.mdevrptw_instances # Data instances
├── data_parser.py # A utility for parsing input data files into the necessary format for the solver.
└── README.md
```

## Prerequisites

- **Python 3.x**
- **IBM ILOG CPLEX Optimization Studio**: Ensure CPLEX is installed and accessible. You can check this by running:
  ```bash
  python -c "import cplex"

## How to Use (For an instance)
python main.py --file_path your_instance_path
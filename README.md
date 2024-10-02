# EVRP_TW


This repository implements the **Electric Vehicle Routing Problem with Time Windows (EVRP_TW)**, aimed at optimizing routing and charging schedules for electric vehicles.

## Folder Structure

EVRP_TW/ 
├── EVRP_Graph.py 
├── EVRP_Solver.py 
├── data_parser.py  
├── main.py 
├── utility.py 
├── evrptw_instances/ 
└── README.md

## Prerequisites

- **Python 3.x**
- **IBM ILOG CPLEX Optimization Studio**: Ensure CPLEX is installed and accessible. You can check this by running:
  ```bash
  python -c "import cplex"

## How to Use (For an instance)
python main.py --file_path your_instance_path
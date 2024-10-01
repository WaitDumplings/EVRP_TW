from data_parser import parse_file
from EVRP_Graph import Graph_EVRP_TW
from EVRP_Solver import EVPR_TW_Solver
import argparse

def main(file_path):
    """
    Main function to run the EVRP-TW solver.
    
    :param file_path: Path to the input file containing the node data.
    """
    # Parse the input file to get depot, customer, RS nodes, and parameters
    Depot_nodes, Customer_nodes, RS_nodes, parameters = parse_file(file_path)
    
    # Create a graph instance for the EVRP-TW
    Graph = Graph_EVRP_TW(Depot_nodes, Customer_nodes, RS_nodes, parameters)
    
    # Create a solver instance and solve the problem
    Solver = EVPR_TW_Solver(Graph)
    Solver.solver()
    
    # Print the results of the solver
    Solver.print_results(Optimal_Value=True, DV_Info=False, Routes=True)

if __name__ == "__main__":
    # Setup argument parser
    parser = argparse.ArgumentParser(description="Run EVRP-TW solver with the provided input file.")
    
    # Define the file path argument
    parser.add_argument('--file_path', type=str, help="Path to the input text file.")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Call the main function with the provided file path
    main(args.file_path)


    
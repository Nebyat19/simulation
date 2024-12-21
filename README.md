# User Manual for Simulation of Load Balancing Algorithms

## Overview

This simulation tool demonstrates various load balancing algorithms using a discrete event simulation framework. It simulates request arrivals, processes them across multiple servers, and analyzes their performance.

## Features

- Implements three load balancing algorithms:
  - **Round Robin**
  - **Least Loaded**
  - **Random Selection**
- Simulates request arrivals based on a Poisson distribution.
- Processes requests with a normal distribution for processing times.
- Visualizes server utilizations and average response times.

## Requirements

- Python 3.x
- Required libraries:
  - `simpy`
  - `numpy`
  - `matplotlib`

## Installation

1. Ensure Python 3.x is installed on your system.
2. Install the required libraries using pip:

   ```bash
   pip install simpy numpy matplotlib
   ```

3. Download the `simulate.py` file.

## Usage

1. **Run the Simulation**:
   Execute the script from the command line:

   ```bash
   python simulate.py
   ```

2. **Experiment Configuration**:
   The main experiment loop runs simulations with different configurations:
   - **Algorithms**: Round Robin, Least Loaded, Random Selection
   - **Arrival Rates**: 0.5, 1, 2 requests per time unit
   - **Server Counts**: 2, 4, 6 servers

3. **Viewing Results**:
   After each simulation, results are displayed in the terminal:
   - Total Requests handled
   - Server Utilizations for each server
   - Average Response Times for each server

   Additionally, visualizations are generated for server utilization and average response time.

## Understanding the Algorithms

- **Round Robin**: Cycles through the servers in order.
- **Least Loaded**: Selects the server with the least current load.
- **Random Selection**: Chooses a server at random.

## Customization

To modify the parameters of the simulation:

- Change the `arrival_rates` or `server_counts` lists in the `experiment()` function.
- Adjust the processing time distribution in the `process_request` function.

## Troubleshooting

- Ensure all dependencies are installed.
- If you encounter any errors, check the Python version and library compatibility.

## Conclusion

This simulation provides insights into how different load balancing algorithms perform under varying conditions. Use it to understand server load dynamics and optimize your own systems.
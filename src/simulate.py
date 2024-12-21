import simpy
import numpy as np
import random
import matplotlib.pyplot as plt

# Load balancing algorithms
def round_robin(servers, request_id):
    server = servers[request_id % len(servers)]  # Cyclic selection
    return server

def least_loaded(servers, request_id):
    # Choose the server with the least load
    server = min(servers, key=lambda x: x['load'])
    return server

def random_selection(servers, request_id):
    # Random server selection
    return random.choice(servers)

# Request arrival process
def request_arrival(env, servers, algorithm, request_times, processing_times):
    request_id = 0
    while True:
        inter_arrival_time = np.random.exponential(1)  # Poisson distribution
        yield env.timeout(inter_arrival_time)

        # Select server based on the chosen algorithm
        server = algorithm(servers, request_id)

        # Simulate the request processing
        processing_time = np.random.normal(5, 1)  # Normal distribution for processing time
        request_times.append(env.now)  # Log the request arrival time
        processing_times.append(processing_time)  # Log the processing time
        server['load'] += 1  # Increment server load

        # Process the request
        env.process(process_request(env, server, processing_time, request_id))
        request_id += 1

# Request processing (server simulation)
def process_request(env, server, processing_time, request_id):
    yield env.timeout(processing_time)
    server['load'] -= 1  # Decrease load after processing
    server['processing_times'].append(processing_time)

# Run the simulation
def run_simulation(algorithm, num_servers=4, arrival_rate=1, runtime=1000):
    # Create environment and servers
    env = simpy.Environment()
    servers = [{'id': i, 'load': 0, 'processing_times': []} for i in range(num_servers)]
    
    # Logs for analysis
    request_times = []
    processing_times = []

    # Start the request arrival process
    env.process(request_arrival(env, servers, algorithm, request_times, processing_times))
    
    # Run the simulation
    env.run(until=runtime)

    # Collect statistics
    server_utilizations = [sum(server['processing_times']) / runtime for server in servers]
    avg_response_times = [np.mean(server['processing_times']) for server in servers]
    total_requests = len(request_times)

    return server_utilizations, avg_response_times, total_requests, request_times, processing_times

# Visualization function
def visualize_results(server_utilizations, avg_response_times, request_times, processing_times):
    # Plot server utilization
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.bar(range(len(server_utilizations)), server_utilizations)
    plt.title('Server Utilization')
    plt.xlabel('Server ID')
    plt.ylabel('Utilization')

    # Plot average response time
    plt.subplot(1, 2, 2)
    plt.bar(range(len(avg_response_times)), avg_response_times)
    plt.title('Average Response Time')
    plt.xlabel('Server ID')
    plt.ylabel('Response Time (s)')
    
    plt.tight_layout()
    plt.show()

# Main experiment loop
def experiment():
    algorithms = [round_robin, least_loaded, random_selection]
    arrival_rates = [0.5, 1, 2]  # Different traffic intensities
    server_counts = [2, 4, 6]  # Different numbers of servers

    for algorithm in algorithms:
        for arrival_rate in arrival_rates:
            for server_count in server_counts:
                print(f"Running simulation with {algorithm.__name__}, Arrival Rate: {arrival_rate}, Servers: {server_count}")
                server_utilizations, avg_response_times, total_requests, request_times, processing_times = run_simulation(algorithm, num_servers=server_count, arrival_rate=arrival_rate)

                # Display results
                print(f"Total Requests: {total_requests}")
                print(f"Server Utilizations: {server_utilizations}")
                print(f"Average Response Times: {avg_response_times}")
                print("-" * 50)

                # Visualize the results
                visualize_results(server_utilizations, avg_response_times, request_times, processing_times)

# Run the experiment
if __name__ == '__main__':
    experiment()

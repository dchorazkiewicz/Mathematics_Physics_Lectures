import numpy as np
import matplotlib.pyplot as plt

# Define the logistic map function, which calculates the next population value
# given the current population (x) and the growth rate (r).
def logistic_map(r, x):
    return r * x * (1 - x)  # Core equation of the logistic map

# Function to generate and plot the bifurcation diagram
def bifurcation_diagram(r_min=2.5, r_max=4.0, steps=10000, discard=1000, plot_points=200):
    # Generate a range of r values between r_min and r_max.
    r_values = np.linspace(r_min, r_max, steps)

    # Initialize the population values with an array of 0.5 (arbitrary starting value).
    x = 0.5 * np.ones(steps)

    # Set up the figure for plotting.
    plt.figure(figsize=(10, 7))

    # Iterate to discard transient dynamics, ensuring we only analyze steady-state behavior.
    for _ in range(discard):
        x = logistic_map(r_values, x)

    # After discarding transients, iterate again to collect data points for the diagram.
    for _ in range(plot_points):
        x = logistic_map(r_values, x)
        # Plot the r values against the current population values (x).
        plt.plot(r_values, x, ',k', alpha=0.25)  # ',' creates small dots for a dense diagram

    # Add plot titles and labels for clarity.
    plt.title("Bifurcation Diagram of the Logistic Map")
    plt.xlabel("Growth Rate (r)")
    plt.ylabel("Population (x)")
    plt.grid(True, alpha=0.5)  # Optional grid for better readability
    plt.savefig("docs/Mechanics/pic/bifurcation_diagram.png")  # Save the plot as an image file
    #plot has been saved to the file bifurcation_diagram.png

# Entry point to execute the bifurcation diagram plot.
if __name__ == "__main__":
    bifurcation_diagram()  # Call the function with default parameters
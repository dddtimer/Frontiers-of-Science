"""
Lesson 1, Screen 5: Histogram of Readiness Potential (RP) Times (Subject 1)

This script generates Figure 4 from Lesson 1, Screen 5 in the Argos platform:
- A histogram of Subject 1's Readiness Potential (RP) times from the Libet experiment.

The dataset represents Subject 1's measured RP times (in milliseconds), showing how often
different RP times occur.

Instructions:
- By default, the histogram uses Subject 1's data.
- Bin edges are set from -700 ms to 0 ms, with 50 ms intervals.
- The final figure is saved as a PNG file following the naming convention for Lesson 1, Screen 5, Figure 4.

Output:
- A static histogram image: 'L1_S5_Fig4-RP_histogram_subject1.png'
"""

import numpy as np
import matplotlib.pyplot as plt

# Data for Subject 1 of the Libet experiment (RP times in ms)
data = [
    -310.8, -267.0, -683.6, -249.1, -85.5, -318.4, -225.0, -261.5, -111.0, -228.3,
    -471.3, -120.9, -119.7, -35.0, -417.7, -82.6, -227.9, -366.0, -433.9, -398.0,
    -220.1, -256.4, -116.8, -71.6, -96.0, -138.9, -415.2, -130.8, -217.1, -164.2,
    -190.0, -273.5, -256.1, -154.2, -307.6, -145.0, -475.5, -248.8, -67.6, -489.8
]

# Calculate fixed bin edges (from -700 ms to 0 ms, with 50 ms intervals)
min_val, max_val = -700, 0
bin_edges = np.arange(min_val, max_val + 50, 50)  # 50 ms wide bins

# Calculate the mean value of the RP times (for potential future use)
mean_value = np.mean(data)

# Create the figure and axis for the histogram
fig, ax = plt.subplots(figsize=(12, 6))  # Set figure size to 12x6 inches

# Plot the histogram for the RP times
n, _, patches = ax.hist(data, bins=bin_edges, color='steelblue', edgecolor='black')

# Set x-axis ticks and labels (rotated for clarity)
ax.set_xticks(bin_edges)
ax.set_xticklabels(bin_edges, rotation=45, ha='right')

# Label the x-axis and y-axis
ax.set_xlabel('Measured RP time (ms)', fontsize=14)
ax.set_ylabel('Number of observations', fontsize=14)

# Fix the y-axis limit to improve visualization
ax.set_ylim(0, 10)  # Maximum 10 observations per bin
ax.set_xlim(min_val, max_val)  # X-axis range is -700 ms to 0 ms

# Adjust tick label size for both axes
ax.tick_params(axis='both', which='major', labelsize=14)

# Optionally, add a vertical line for the mean value (commented out by default)
# ax.axvline(x=mean_value, color='black', linestyle='--', linewidth=2, label=f'Mean: {mean_value:.2f} ms')

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the figure as a PNG file following the new naming convention
plt.savefig('L1_S5_Fig4-RP_histogram_subject1.png', dpi=300, bbox_inches='tight')

# Display the plot
plt.show()

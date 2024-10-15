"""
Lesson 1, Screen 6: Histogram of Wish Times (W Times) for Subject 2

This script generates Figure 1 from Lesson 1, Screen 6 in the Argos platform:
- A histogram of Subject 2's Wish Times (W Times) from the Libet experiment.

The data for Subject 2 has been generated to have the same mean as Subject 1's W times,
but with a smaller standard deviation, meaning that Subject 2's responses are more
tightly clustered around the mean.

Instructions:
- The histogram uses Subject 2's data by default.
- Bin edges are set from -200 ms to 50 ms, with 10 ms intervals.
- The final figure is saved as a PNG file following the naming convention for Lesson 1, Screen 6, Figure 1.

Output:
- A static histogram image: 'L1_S6_Fig1-W_histogram_subject2.png'

Optional:
- Uncomment the code to include a vertical line for the mean W time.

Author: [Your Name]
Date: [Today's Date]
"""

import numpy as np
import matplotlib.pyplot as plt

# Data for Subject 2 (Wish Times in ms)
# This dataset has the same mean as Subject 1 but a smaller standard deviation.
data = [-68.3, -132.3, -113.3, -53.7, -86.7, -82.5, -85.7, -110.3, -45.4, -87.4, 
        -127.3, -63.8, -92.8, -142.6, -86.0, -56.4, -89.6, -116.8, -87.9, -88.9, 
        -73.3, -80.3, -69.6, -91.0, -73.0, -52.3, -68.4, -76.1, -125.7, -79.6, 
        -54.4, -76.7, -56.6, -106.4, -50.3, -37.0, -84.4, -102.3, -47.9, -73.6]

# Define bin edges for the histogram (from -200 ms to 50 ms, in 10 ms intervals)
min_val, max_val = -200, 50
bin_edges = np.arange(min_val, max_val + 10, 10)  # Ensures bins are in steps of 10 ms

# Calculate the mean value of the W times (for potential use later)
mean_value = np.mean(data)

# Create the figure and axis for the histogram
fig, ax = plt.subplots(figsize=(12, 6))  # Set figure size to 12x6 inches

# Plot the histogram for the W times
n, _, patches = ax.hist(data, bins=bin_edges, color='steelblue', edgecolor='black')

# Set x-axis ticks and labels (rotated for clarity)
ax.set_xticks(bin_edges)
ax.set_xticklabels(bin_edges, rotation=45, ha='right')

# Label the x-axis and y-axis
ax.set_xlabel('Reported W time (ms)', fontsize=14)
ax.set_ylabel('Number of responses', fontsize=14)

# Fix the y-axis limit to improve visualization
ax.set_ylim(0, 12)  # Maximum 12 responses per bin
ax.set_xlim(min_val, max_val)  # X-axis range from -200 ms to 50 ms

# Adjust tick label size for both axes
ax.tick_params(axis='both', which='major', labelsize=14)

# Optionally, add a vertical line for the mean value (currently commented out)
# ax.axvline(x=mean_value, color='black', linestyle='--', linewidth=2, label=f'Mean: {mean_value:.2f} ms')

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the figure as a PNG file following the new naming convention
plt.savefig('L1_S6_Fig1-W_histogram_subject2.png', dpi=300, bbox_inches='tight')

# Display the plot
plt.show()

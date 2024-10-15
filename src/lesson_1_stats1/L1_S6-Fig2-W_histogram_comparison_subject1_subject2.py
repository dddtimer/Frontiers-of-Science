"""
Lesson 1, Screen 6: Side-by-Side Comparison of Wish Times (W Times) for Subjects 1 and 2

This script generates Figure 2 from Lesson 1, Screen 6 in the Argos platform:
- A side-by-side comparison of the Wish Times (W Times) for Subject 1 and Subject 2 from the Libet experiment.

Key Information:
- Subject 1 and Subject 2 have the same mean Wish Time, but Subject 2's responses have a smaller standard deviation, meaning that Subject 2's data is more tightly clustered around the mean.
- The two histograms are displayed side-by-side for easy comparison.

Instructions:
- The data for both Subject 1 and Subject 2 are plotted.
- Vertical lines show the mean Wish Time for each subject.
- Bin edges are set from -200 ms to 50 ms, with 10 ms intervals.
- The final figure is saved as a PNG file following the naming convention for Lesson 1, Screen 6, Figure 2.

Output:
- A static side-by-side histogram image: 'L1_S6_Fig2-W_histogram_comparison_subject1_subject2.png'

Author: [Your Name]
Date: [Today's Date]
"""

import numpy as np
import matplotlib.pyplot as plt

# Data for Subject 1 and Subject 2 (Wish Times in ms)
data1 = [-85.4, -85.4, -170.8, -99.6, -56.9, -142.3, -85.4, -142.3, -56.9, -85.4, 
         -170.8, -128.1, -56.9, -71.2, -85.4, -56.9, -142.3, 42.7, 0.0, -85.4, 
         -142.3, -85.4, -56.9, -99.6, -56.9, -142.3, -85.4, -56.9, -99.6, -170.8, 
         -113.9, -56.9, 42.7, -85.4, 0.0, -85.4, -170.8, -85.4, 0.0, 0.0]

data2 = [-68.3, -132.3, -113.3, -53.7, -86.7, -82.5, -85.7, -110.3, -45.4, -87.4, 
         -127.3, -63.8, -92.8, -142.6, -86.0, -56.4, -89.6, -116.8, -87.9, -88.9, 
         -73.3, -80.3, -69.6, -91.0, -73.0, -52.3, -68.4, -76.1, -125.7, -79.6, 
         -54.4, -76.7, -56.6, -106.4, -50.3, -37.0, -84.4, -102.3, -47.9, -73.6]

# Define bin edges for the histogram (from -200 ms to 50 ms, in 10 ms intervals)
min_val, max_val = -200, 50
bin_edges = np.arange(min_val, max_val + 10, 10)

# Calculate mean values for both subjects
mean1 = np.mean(data1)
mean2 = np.mean(data2)

# Create the figure with two subplots (side-by-side)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6), sharey=True)  # Share y-axis between plots

# Plot the histogram for Subject 1
n1, _, patches1 = ax1.hist(data1, bins=bin_edges, color='steelblue', edgecolor='black')
ax1.axvline(x=mean1, color='black', linestyle='--', linewidth=2, label=f'Mean: {mean1:.2f} ms')
ax1.set_title('Subject 1', fontsize=16)
ax1.set_xlabel('Reported W time (ms)', fontsize=14)
ax1.set_ylabel('Number of responses', fontsize=14)
ax1.set_ylim(0, 12)  # Maximum 12 responses per bin
ax1.set_xlim(min_val, max_val)  # X-axis range from -200 ms to 50 ms
ax1.set_xticks(np.arange(min_val, max_val + 20, 20))  # X-axis ticks every 20 ms
ax1.tick_params(axis='both', which='major', labelsize=14, rotation=45)

# Plot the histogram for Subject 2
n2, _, patches2 = ax2.hist(data2, bins=bin_edges, color='steelblue', edgecolor='black')
ax2.axvline(x=mean2, color='black', linestyle='--', linewidth=2, label=f'Mean: {mean2:.2f} ms')
ax2.set_title('Subject 2', fontsize=16)
ax2.set_xlabel('Reported W time (ms)', fontsize=14)
ax2.set_ylim(0, 12)  # Maximum 12 responses per bin
ax2.set_xlim(min_val, max_val)  # X-axis range from -200 ms to 50 ms
ax2.set_xticks(np.arange(min_val, max_val + 20, 20))  # X-axis ticks every 20 ms
ax2.tick_params(axis='both', which='major', labelsize=14, rotation=45)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the figure as a PNG file following the new naming convention
plt.savefig('L1_S6_Fig2-W_histogram_comparison_subject1_subject2.png', dpi=300, bbox_inches='tight')

# Display the plot
plt.show()

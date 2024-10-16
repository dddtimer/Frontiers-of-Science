"""
Lesson 2, Screen 4: Bar Plot of Gray Matter Volume Across Different Music Experience Levels

This script generates Figure 1 from Lesson 2, Screen 4 in the Argos platform:
- It displays a bar plot comparing the percentage of gray matter volume among non-musicians, amateurs, and professionals.

Key Concepts:
- **Gray Matter Volume**: The percentage of gray matter volume is plotted for three groups: non-musicians, amateurs, and professionals.
- **Error Bars**: The plot includes error bars showing the range for each group (e.g., for non-musicians, gray matter volume ranges from -4.5 to -0.5%).

Instructions:
- Categories: Non-musicians, Amateurs, and Professionals.
- Each category is associated with a mean value and an error range.
- The bars are color-coded to represent each group.

Output:
- The figure is saved as 'L2_S4_Fig1-gray_matter_volume_barplot.png'.

Author: David Timerman
"""

import matplotlib.pyplot as plt
import numpy as np

# Data for the categories and their corresponding means and error ranges
categories = ['Non-musicians', 'Amateurs', 'Professionals']
means = [-2.5, 2.5, 3]  # Mean gray matter volume (%)
errors = [
    [2, 2],  # Non-musicians: -4.5 to -0.5
    [2.5, 2.5],  # Amateurs: 0 to 5
    [3, 3]  # Professionals: 0 to 6
]
colors = ['#87CEEB', '#808080', '#90EE90']  # Colors for the bars

# Create the figure and axes
fig, ax = plt.subplots(figsize=(10, 6))  # Set figure size to 10x6 inches

# Plot the bar chart
x = np.arange(len(categories))  # X positions for the bars
bar_width = 0.5  # Width of the bars
bars = ax.bar(x, means, bar_width, color=colors, alpha=0.8)  # Plot the bars

# Add error bars to each bar
for i, bar in enumerate(bars):
    ax.errorbar(bar.get_x() + bar.get_width()/2, means[i],
                yerr=np.array(errors[i]).reshape(2, 1),  # Error bars
                fmt='none', color='black', capsize=5)

# Customize the plot
ax.set_ylabel('% Gray matter volume', fontsize=16)
ax.set_title('PreCG: Gray Matter Volume by Music Experience', fontsize=16)  # Updated title for clarity
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=14)
ax.set_ylim(-8, 8)  # Set y-axis limits
ax.set_yticks(range(-8, 9, 2))  # Set y-axis ticks every 2 units
ax.tick_params(axis='y', labelsize=14)  # Adjust y-axis tick label size

# Add grid lines for better visualization
ax.grid(True, linestyle='--', alpha=0.7)

# Add borders to the bars
for bar in bars:
    bar.set_edgecolor('black')
    bar.set_linewidth(1)

# Add a dashed horizontal line at y=0 for reference
ax.axhline(y=0, color='black', linewidth=1.5, linestyle='--', alpha=0.7)

# Save the figure using the new naming convention
plt.savefig('L2_S4_Fig1-gray_matter_volume_barplot.png', dpi=300, bbox_inches='tight')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()

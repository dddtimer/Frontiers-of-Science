"""
Lesson 1, Screen 6: Normal Distribution with Incremental Shading and SD Markers

This script generates Figures 3, 5, 6, 8, and 10 from Lesson 1, Screen 6 in the Argos platform:
- It displays a normal distribution (bell curve) and progressively adds features across the figures:
    - Figure 3: Histogram with the normal distribution curve (bell curve) superimposed. Only the mean is labeled on the x-axis.
    - Figure 5: Adds labels for -3SD, -2SD, -1SD, mean, 1SD, 2SD, and 3SD. Vertical dashed lines are added at these points, extending from the x-axis up to the height of the curve at each SD value.
    - Figure 6: Fills the area under the curve between -1SD and 1SD with a darker blue shade.
    - Figure 8: Adds shaded areas between -2SD and -1SD, and between 1SD and 2SD with a medium blue shade.
    - Figure 10: Completes the graph by shading the areas between -3SD and -2SD, and between 2SD and 3SD with a lighter blue shade.

Key Features:
- **Histogram and Normal Distribution Curve**: A histogram of randomly generated data (from a normal distribution with mean = 0 and standard deviation = 1) is plotted in all figures, with the bell curve superimposed.
- **Vertical Dashed Lines**: Starting from Figure 5, vertical dashed lines are drawn at the -3SD to 3SD positions, but these lines only extend up to the curve's height at each SD value (not across the entire plot).
- **Incremental Shading**: Starting from Figure 6, progressively more areas under the curve are shaded with different shades of blue:
    - **Dark Blue** for the area between -1SD and 1SD.
    - **Medium Blue** for the areas between -2SD and -1SD, and between 1SD and 2SD.
    - **Light Blue** for the areas between -3SD and -2SD, and between 2SD and 3SD.

Instructions:
- To generate all figures, simply run the script. Each figure will be saved as a PNG file with the following naming convention:
    - `L1_S6_Fig3_normal_distribution.png`
    - `L1_S6_Fig5_normal_distribution.png`
    - `L1_S6_Fig6_normal_distribution.png`
    - `L1_S6_Fig8_normal_distribution.png`
    - `L1_S6_Fig10_normal_distribution.png`
    
- The figures are displayed one by one and saved in the working directory.
- The top, right, and left spines (borders) are hidden, leaving only the bottom x-axis visible.

Customization:
- You can modify the standard deviation ranges to shade different areas or change the shades of blue used by altering the `fill_sd_ranges` argument passed to the `plot_normal_distribution_figure()` function.
- If you want to remove or adjust the labels and vertical dashed lines, modify the relevant sections in the `plot_normal_distribution_figure()` function.

Author: David Timerman
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Set font sizes
title_fontsize = 18
label_fontsize = 16
tick_fontsize = 16


# Generate normal distribution plot for each figure
def plot_normal_distribution_figure(figure_number, fill_sd_ranges=[]):
    """
    Generates a normal distribution plot based on the figure number and SD ranges to fill.

    Parameters:
    - figure_number: The figure number (3, 5, 6, 8, 10)
    - fill_sd_ranges: A list of tuples, each tuple contains the start and end SD values to fill (e.g., [(-1, 1)])
    """

    # Set up the plot
    fig, ax = plt.subplots(figsize=(12, 8))

    # Generate sample data
    np.random.seed(42)  # for reproducibility
    sample_data = np.random.normal(loc=0, scale=1, size=10000)

    # Plot histogram with larger bins and black edges
    n, bins, patches = ax.hist(sample_data, bins=15, density=True, alpha=0.9, color='white', edgecolor='black')

    # Create x values for the normal distribution curve
    x = np.linspace(-4, 4, 1000)

    # Calculate the normal distribution
    y = norm.pdf(x, 0, 1)

    # Plot the curve
    ax.plot(x, y, 'k', linewidth=1)

    # Define shades of blue for different SD ranges
    color_1 = '#4DB8FF'  # Darker blue for -1SD to 1SD
    color_2 = '#99CCFF'  # Medium blue for -2SD to -1SD and 1SD to 2SD
    color_3 = '#CCE5FF'  # Lighter blue for -3SD to -2SD and 2SD to 3SD

    # Fill areas under the curve progressively
    if figure_number >= 6:  # Start filling from -1SD to 1SD for Figure 6
        ax.fill_between(x, y, where=(x >= -1) & (x <= 1), color=color_1, alpha=0.5)

    if figure_number >= 8:  # Add filling from -2SD to -1SD and 1SD to 2SD for Figure 8
        ax.fill_between(x, y, where=(x >= -2) & (x <= -1), color=color_2, alpha=0.5)
        ax.fill_between(x, y, where=(x >= 1) & (x <= 2), color=color_2, alpha=0.5)

    if figure_number >= 10:  # Add filling from -3SD to -2SD and 2SD to 3SD for Figure 10
        ax.fill_between(x, y, where=(x >= -3) & (x <= -2), color=color_3, alpha=0.5)
        ax.fill_between(x, y, where=(x >= 2) & (x <= 3), color=color_3, alpha=0.5)

    # Add vertical dashed lines extending up to the bell curve at SD values (starting from Figure 5)
    if figure_number >= 5:  # Add SD lines from -3SD to 3SD
        for i in range(-3, 4):
            if i != 0:
                # Find the height of the curve at this SD value (y corresponding to x=i)
                y_value_at_sd = norm.pdf(i, 0, 1)
                # Draw a vertical dashed line up to the bell curve at this SD value
                ax.plot([i, i], [0, y_value_at_sd], color='black', linestyle='--', alpha=1, linewidth=1.5)

    # Add x-axis labels
    if figure_number >= 5:  # Add SD labels starting from Figure 5
        labels = ["-3SD", "-2SD", "-1SD", "mean", "1SD", "2SD", "3SD"]
        ax.set_xticks(range(-3, 4))
        ax.set_xticklabels(labels, rotation=0, ha='center', fontsize=tick_fontsize)
    else:  # Only show the mean label for Figure 3
        ax.set_xticks([0])
        ax.set_xticklabels(['mean'], rotation=0, ha='center', fontsize=tick_fontsize)

    # Remove y-axis
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks([])
    ax.yaxis.set_ticklabels([])

    # Set y-axis to start at 0 and end at 0.45
    ax.set_ylim(0, 0.45)

    # Adjust layout
    plt.tight_layout()

    # Save the figure using the new naming convention
    filename = f'L1_S6_Fig{figure_number}_normal_distribution.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')

    # Display the plot
    plt.show()


# Generate each figure

# Figure 3: Histogram with bell curve, only mean labeled
plot_normal_distribution_figure(3)

# Figure 5: Adds SD labels and vertical dashed lines extending up to the curve
plot_normal_distribution_figure(5)

# Figure 6: Adds filled area between -1SD and 1SD (dark blue)
plot_normal_distribution_figure(6, fill_sd_ranges=[(-1, 1)])

# Figure 8: Adds filled areas between -2SD and -1SD, and between 1SD and 2SD (medium blue)
plot_normal_distribution_figure(8, fill_sd_ranges=[(-1, 1), (-2, -1), (1, 2)])

# Figure 10: Adds filled areas between -3SD and -2SD, and between 2SD and 3SD (light blue)
plot_normal_distribution_figure(10, fill_sd_ranges=[(-1, 1), (-2, -1), (1, 2), (-3, -2), (2, 3)])

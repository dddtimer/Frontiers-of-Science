"""
Lesson 1, Screen 7: Histograms of Readiness Potential (RP) Times for Two Subjects

This script generates Figure 2 from Lesson 1, Screen 7 in the Argos platform:
- It displays two histograms side-by-side, showing the distribution of RP times for two subjects.

Key Concepts:
- **Readiness Potential (RP) Times**: A measure of brain activity preceding voluntary movement.
- Two subjects' RP times are shown as histograms, displaying how frequently certain RP times occurred.
- The second plot, created later in the lesson, includes additional lines to indicate the mean and percentiles (2.5% and 97.5%) for each subject.

Instructions:
- The first plot contains the basic histograms for both subjects.
- A subsequent plot (which you can add to this script if needed) would display the mean and percentile values as vertical lines and shaded areas.

Output:
- The initial figure is saved as 'L1_S7_Fig2-RP_histogram_comparison_of_two_subjects.png'.

Optional:
- Additional percentile lines and shaded areas can be added using the `plot_histogram_full()` function.

Author: [Your Name]
Date: [Today's Date]
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# Data for Subject 1 and Subject 2 (RP times and frequency)
data1 = {
    'Onset of RP (ms)': [-1200, -1100, -1000, -900, -800, -700, -600, -500, -400, -300, -200, -100, 0, 100],
    'Frequency': [0, 0, 0, 1, 1, 5, 6, 8, 7, 7, 2, 5, 1, 0]
}

data2 = {
    'Onset of RP (ms)': [-1200, -1100, -1000, -900, -800, -700, -600, -500, -400, -300, -200, -100, 0, 100],
    'Frequency': [3, 3, 2, 7, 2, 0, 0, 4, 5, 10, 2, 2, 1, 0]
}


def find_percentile_location(data, percentile):
    """
    Calculate the RP time corresponding to a given percentile.
    
    Parameters:
    - data: A dictionary containing 'Onset of RP (ms)' and 'Frequency' for a subject.
    - percentile: The target percentile (e.g., 2.5, 97.5).
    
    Returns:
    - The RP time at the specified percentile.
    """
    onset = data['Onset of RP (ms)']
    freq = data['Frequency']
    total = sum(freq)
    target_count = (percentile / 100) * total

    cumulative = 0
    for i, f in enumerate(freq):
        prev_cumulative = cumulative
        cumulative += f
        if cumulative >= target_count:
            bin_start = onset[i]
            bin_end = onset[i + 1] if i + 1 < len(onset) else onset[i] + 100  # Assuming 100ms bins
            fraction = (target_count - prev_cumulative) / f
            return bin_start + fraction * 100  # 100ms bin width

    return None


def integer_formatter(x, pos):
    """
    Custom formatter to ensure that y-axis labels are integers.
    
    Parameters:
    - x: The x value to format.
    - pos: The tick position (not used here).
    
    Returns:
    - Formatted integer string.
    """
    return f'{int(x)}'


def plot_histogram_basic(ax, data, title):
    """
    Plot a basic histogram of RP times for a subject.
    
    Parameters:
    - ax: The axis on which to plot.
    - data: The RP data for a subject (onset and frequency).
    - title: The title for the histogram.
    """
    onset = data['Onset of RP (ms)']
    freq = data['Frequency']

    ax.bar(onset, freq, width=100, align='edge', color='steelblue', edgecolor='black')
    ax.set_xlabel('Measured RP time (ms)', fontsize=14)
    ax.set_ylabel('Number of measurements', fontsize=14)
    ax.set_title(title, fontsize=14)
    ax.tick_params(axis='both', which='major', labelsize=14)
    ax.set_xlim(-1200, 100)
    ax.set_xticks(onset)
    ax.set_xticklabels(onset, rotation=45, ha='right')
    ax.set_ylim(0, 20)
    ax.yaxis.set_major_formatter(FuncFormatter(integer_formatter))
    ax.set_yticks(range(0, 21, 2))


# Plot basic histograms for both subjects (side by side)
fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Plotting basic histograms
plot_histogram_basic(ax1, data1, 'Subject 1')
plot_histogram_basic(ax2, data2, 'Subject 2')

# Save the figure with the appropriate naming convention
plt.tight_layout()
plt.savefig('L1_S7_Fig2-RP_histogram_comparison_of_two_subjects.png', dpi=300, bbox_inches='tight')
plt.show()
plt.close(fig1)

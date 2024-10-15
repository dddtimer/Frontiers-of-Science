"""
Lesson 1, Screen 4: Histogram of Wish Times (Subject 1)

This script generates Figures 1 and 2 from Lesson 1, Screen 4.

This script generates two figures for Lesson 1, Screen 4 in the Argos platform:
1. An animated histogram of Subject 1's "Wish Times" from the Libet experiment.
2. A static final frame from the histogram, saved as a PNG file.

Both figures visualize the reported "Wish Times" (W) for Subject 1, where each wish time is the 
moment when the subject reported being aware of their intention to act (in milliseconds).

The script includes:
- An animated GIF for visualizing how the "Wish Times" accumulate over time.
- A static image of the final histogram frame for display.

Instructions:
- Subject 1's data is plotted by default. Subject 2's data is provided but commented out.
- To switch to Subject 2's data, uncomment the `subject2_data` section and comment out `subject1_data`.
- The output files are saved as:
  - 'lesson1_screen4_figure1_animated_histogram_subject1.gif' (animated GIF)
  - 'lesson1_screen4_figure2_final_frame_subject1.png' (static final frame)
- Adjust bin ranges, titles, and file names as needed if you work with new datasets or subjects.

Dependencies:
- numpy
- matplotlib
- matplotlib.animation (for creating the animated GIF)
- PillowWriter (for saving the GIF)

Author: [Your Name]
Date: [Today's Date]
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib.animation import PillowWriter

# Data for Subject 1 of the Libet experiment (Wish Times in ms)
subject1_data = [
    -310.8, -267.0, -683.6, -249.1, -85.5, -318.4, -225.0, -261.5, -111.0, -228.3,
    -471.3, -120.9, -119.7, -35.0, -417.7, -82.6, -227.9, -366.0, -433.9, -398.0,
    -220.1, -256.4, -116.8, -71.6, -96.0, -138.9, -415.2, -130.8, -217.1, -164.2,
    -190.0, -273.5, -256.1, -154.2, -307.6, -145.0, -475.5, -248.8, -67.6, -489.8
]

# Data for Subject 2 (Wish Times in ms) [Currently not used, but available for future use]
# subject2_data = [
#     -85.4, -85.4, -170.8, -99.6, -56.9, -142.3, -85.4, -142.3, -56.9, -85.4,
#     -170.8, -128.1, -56.9, -71.2, -85.4, -56.9, -142.3, 42.7, 0.0, -85.4,
#     -142.3, -85.4, -56.9, -99.6, -56.9, -142.3, -85.4, -56.9, -99.6, -170.8,
#     -113.9, -56.9, 42.7, -85.4, 0.0, -85.4, -170.8, -85.4, 0.0, 0.0
# ]

# Set the dataset to be plotted (subject1_data for now)
data = subject1_data
total_data_points = len(data)

# Define bin edges for the histogram (from -200ms to 50ms, in steps of 10ms)
min_val, max_val = -200, 50
bin_edges = np.arange(min_val, max_val + 10, 10)  # Ensure bins are divisible by 10

# Set font sizes for consistency across plots
plt.rcParams.update({'font.size': 14})

# Function to update the histogram for each frame in the animation
def update_hist(num):
    """
    Updates the histogram for each frame in the animation.
    :param num: Current frame number (corresponds to the number of data points plotted)
    """
    plt.cla()  # Clear the current axes to update the histogram
    n, _, patches = plt.hist(data[:num], bins=bin_edges, color='steelblue', edgecolor='black')

    # Set x-axis ticks and labels for bin edges
    plt.xticks(bin_edges, rotation=45, ha='right')

    # Label axes
    plt.xlabel('Reported RP time (ms)', fontsize=14)
    plt.ylabel('Number of responses', fontsize=14)

    # Fix y-axis and x-axis limits for consistent visualization
    plt.ylim(0, 12)
    plt.xlim(min_val, max_val)

    # Add vertical lines to indicate bin edges
    for edge in bin_edges:
        plt.axvline(x=edge, color='#404040', linestyle='-', linewidth=0.5)

    # Display trial number and the most recent data point in the title
    if num > 0:
        plt.title(f'Trial {num}: {data[num - 1]} ms', loc='left', pad=10, fontsize=14)

    # Add data labels above each bar in the histogram
    for rect in patches:
        height = rect.get_height()
        if height > 0:
            plt.text(rect.get_x() + rect.get_width() / 2, height, f'{int(height)}',
                     ha='center', va='bottom', fontsize=14)

    # Adjust layout to prevent x-axis labels from being cut off
    plt.tight_layout()

# Create a figure for the histogram
fig = plt.figure(figsize=(12, 7), dpi=300)  # Increased height for better aspect ratio

# Calculate the interval between frames to make the animation last 30 seconds
interval = 30000 // total_data_points  # Duration of 30 seconds divided by total data points

# Create the animation object
animation = ani.FuncAnimation(fig, update_hist, frames=total_data_points + 1,
                              interval=interval, blit=False, repeat=False)

# Save the animated histogram as a GIF
writer = PillowWriter(fps=1)
animation.save('L1_S4_Fig1-animated_histogram_subject1.gif', writer=writer, dpi=300)

# Save the final frame of the animation as a static image
update_hist(total_data_points)
plt.savefig('L1_S4_Fig2-final_frame_subject1.png', dpi=300, bbox_inches='tight')

# Show the plot (final frame)
plt.show()

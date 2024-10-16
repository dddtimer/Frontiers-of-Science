"""
Lesson 2, Figures 1 and 2: Motor Cortex Response for Left Pinky (D5)

This script generates Figures 1 and 2 from Lesson 2:
- Figure 1 shows the motor cortex response with error bars representing standard deviation (SD).
- Figure 2 shows the same motor cortex response with error bars representing 95% confidence intervals (CI).

Key Concepts:
- **Motor Cortex Response**: The strength of the magnetic resonance (MR) signal (nA m) is measured in musicians and non-musicians.
- **Figure 1**: Error bars represent the standard deviation (SD).
- **Figure 2**: Error bars represent the 95% confidence intervals (CI).

Instructions:
- Both figures compare musicians and non-musicians in terms of MR signal strength.
- Figure 1 uses standard deviation as error bars.
- Figure 2 uses 95% confidence intervals as error bars.

Output:
- Figure 1: 'L2_Fig1-MotorCortex_SD.png'
- Figure 2: 'L2_Fig2-MotorCortex_CI.png'

Author: David Timerman
"""

import matplotlib.pyplot as plt
import numpy as np

# Data for both figures
categories = ['Musicians', 'Non-musicians']
means = [20, 8]  # Mean values for the MR signal (nA m)
std_devs = [5, 2]  # Standard deviations for the MR signal

# 95% confidence intervals
ci_lower = [16.7, 6.4]
ci_upper = [23.3, 9.6]

colors = ['#90EE90', '#87CEEB']  # Colors for the bars


def plot_motor_cortex_response(error_type='SD'):
    """
    Plot the motor cortex response for musicians and non-musicians with error bars.

    Parameters:
    - error_type: 'SD' for standard deviation error bars or 'CI' for 95% confidence intervals.
    """
    # Create the figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the bar chart
    x = np.arange(len(categories))  # X positions for the bars
    bar_width = 0.5  # Width of the bars
    bars = ax.bar(x, means, bar_width, color=colors, alpha=0.8)  # Plot the bars

    # Add error bars depending on the error type
    if error_type == 'SD':
        # Standard deviation error bars (Figure 1)
        for i, bar in enumerate(bars):
            ax.errorbar(bar.get_x() + bar.get_width() / 2, means[i],
                        yerr=std_devs[i], fmt='none', color='black', capsize=5)
        # Set filename for Figure 1
        filename = 'L2_Fig1-MotorCortex_SD.png'
    elif error_type == 'CI':
        # 95% confidence interval error bars (Figure 2)
        for i, bar in enumerate(bars):
            ax.errorbar(bar.get_x() + bar.get_width() / 2, means[i],
                        yerr=[[means[i] - ci_lower[i]], [ci_upper[i] - means[i]]],
                        fmt='none', color='black', capsize=5)
        # Set filename for Figure 2
        filename = 'L2_Fig2-MotorCortex_CI.png'

    # Customize the plot
    ax.set_ylabel('Strength of MR Signal (nA m)', fontsize=16)
    ax.set_title('Motor Cortex Response for Left Pinky (D5)', fontsize=16)
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=14)
    ax.tick_params(axis='y', labelsize=14)

    # Add grid lines for better visualization
    ax.grid(True, linestyle='--', alpha=0.7)

    # Add borders to the bars
    for bar in bars:
        bar.set_edgecolor('black')
        bar.set_linewidth(1)

    # Add a dashed horizontal line at y=0 for reference
    ax.axhline(y=0, color='black', linewidth=1.5, linestyle='--', alpha=0.7)

    # Set y-axis limits and ticks to accommodate error bars
    y_max = max(means) + max(std_devs) + 5
    ax.set_ylim(0, y_max)
    ax.set_yticks(range(0, int(y_max), 5))

    # Save the figure
    plt.savefig(filename, dpi=300, bbox_inches='tight')

    # Adjust layout and display the plot
    plt.tight_layout()
    plt.show()


# Generate Figure 1 (Standard Deviation)
plot_motor_cortex_response(error_type='SD')

# Generate Figure 2 (95% Confidence Intervals)
plot_motor_cortex_response(error_type='CI')

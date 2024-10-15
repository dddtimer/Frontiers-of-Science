"""
Lesson 1, Screen 7: Histograms of Random and Systematic Error in Fruit Weighing

This script generates Figure 1 from Lesson 1, Screen 7 in the Argos platform:
- It displays two histograms side-by-side that compare random and systematic error in fruit weighing.

Key Concepts:
- **Random Error**: Natural variations in measurements, typically due to slight changes in how the fruit is placed on the scale.
- **Systematic Error**: A consistent bias in measurements caused by a miscalibrated scale (in this case, the scale consistently weighs 10 grams too high).

Instructions:
- The random error data is generated based on a true fruit weight of 100 grams with a random normal error (mean = 0, SD = 5).
- The systematic error introduces a consistent 10-gram bias on top of the random error.
- Two histograms are plotted side by side:
    - The first subplot shows the random error in the fruit's weight.
    - The second subplot shows the systematic error (random error + consistent bias).

Output:
- The plots show both the true weight and the mean of the measurements for comparison.

Author: David Timerman
"""

import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Generate data
true_weight = 100  # True weight of fruit in grams
num_measurements = 500

# Random error (natural variations in placement on the scale)
random_error = np.random.normal(loc=true_weight, scale=5, size=num_measurements)

# Systematic error (scale not properly zeroed, consistently weighing 10g too high)
systematic_shift = 10
systematic_error = random_error + systematic_shift

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))  # Two subplots side by side

# Plot random error histogram
ax1.hist(random_error, bins=20, edgecolor='black')
ax1.axvline(x=true_weight, color='r', linestyle='-', linewidth=5, label='True Weight')
ax1.axvline(x=np.mean(random_error), color='black', linestyle=':', linewidth=5, label='Mean')
ax1.set_xlabel('Measured Weight (g)', fontsize=14)
ax1.set_ylabel('Number of measurements', fontsize=14)
ax1.legend()
ax1.tick_params(axis='both', which='major', labelsize=12)
ax1.set_ylim(0, 80)  # Adjust y-axis to ensure consistent scaling

# Plot systematic error histogram
ax2.hist(systematic_error, bins=20, edgecolor='black')
ax2.axvline(x=true_weight, color='r', linestyle='--', linewidth=5, label='True Weight')
ax2.axvline(x=np.mean(systematic_error), color='black', linestyle=':', linewidth=5, label='Mean')
ax2.set_xlabel('Measured Weight (g)', fontsize=14)
ax2.set_ylabel('Number of measurements', fontsize=14)
ax2.legend()
ax2.tick_params(axis='both', which='major', labelsize=12)
ax2.set_ylim(0, 80)  # Same y-axis limit as the first plot for consistency

# Adjust layout and display the plots
plt.tight_layout()
plt.show()

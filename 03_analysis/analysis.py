"""
Scientific Inquiry Project - Analysis Script Template

Replace this script with your own data analysis code.
You may use Python, R, Julia, or any other language; adjust the file name accordingly.

This template provides a basic structure for loading data, performing exploratory
analysis, statistical tests, and generating plots.

Instructions:
1. Replace the placeholder code with your actual analysis.
2. Ensure all file paths are relative to the repository root.
3. Add comments to explain each step.
4. Run the script to produce outputs in the ../04_results/ directory.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import os

# Set random seed for reproducibility
np.random.seed(42)

# --------------------------------------------------------------------
# 1. LOAD DATA
# --------------------------------------------------------------------
# Adjust the path to your cleaned data file (stored in ../02_data/ or ../03_analysis/)
data_path = '../02_data/cleaned_data.csv'  # Example; change as needed

if os.path.exists(data_path):
    df = pd.read_csv(data_path)
    print(f"Data loaded successfully. Shape: {df.shape}")
    print(df.head())
else:
    print(f"Warning: {data_path} not found. Please ensure your data file exists.")
    # Create a dummy dataset for demonstration purposes only
    print("Creating a dummy dataset for illustration.")
    df = pd.DataFrame({
        'treatment': np.repeat(['control', 'experimental'], 20),
        'measurement': np.concatenate([
            np.random.normal(10, 2, 20),
            np.random.normal(12, 2, 20)
        ])
    })

# --------------------------------------------------------------------
# 2. EXPLORATORY ANALYSIS
# --------------------------------------------------------------------
print("\n=== EXPLORATORY ANALYSIS ===")
print("Summary statistics:")
print(df.describe())

print("\nGroup means:")
print(df.groupby('treatment').mean())

# Basic visualization
plt.figure(figsize=(8, 5))
sns.boxplot(x='treatment', y='measurement', data=df)
plt.title('Measurement by Treatment Group (Example)')
plt.ylabel('Measurement (units)')
plt.xlabel('Treatment')
plt.tight_layout()
plt.savefig('../04_results/exploratory_boxplot.png', dpi=300)
plt.close()
print("Saved exploratory boxplot to ../04_results/exploratory_boxplot.png")

# --------------------------------------------------------------------
# 3. STATISTICAL TESTING
# --------------------------------------------------------------------
print("\n=== STATISTICAL TEST ===")
# Example: independent t-test between two groups
if 'treatment' in df.columns and 'measurement' in df.columns:
    groups = df['treatment'].unique()
    if len(groups) == 2:
        group_a = df[df['treatment'] == groups[0]]['measurement']
        group_b = df[df['treatment'] == groups[1]]['measurement']
        t_stat, p_val = stats.ttest_ind(group_a, group_b, equal_var=False)
        print(f"Welch's t-test: t = {t_stat:.3f}, p = {p_val:.3f}")
        if p_val < 0.05:
            print("Result suggests a statistically significant difference (p < 0.05).")
        else:
            print("Result does not suggest a statistically significant difference (p ≥ 0.05).")
    else:
        print(f"Expected 2 treatment groups, found {len(groups)}. Adjust the test accordingly.")
else:
    print("Required columns 'treatment' and 'measurement' not found. Modify the test.")

# --------------------------------------------------------------------
# 4. ADDITIONAL ANALYSIS (customize as needed)
# --------------------------------------------------------------------
# Add your own analysis steps here: regression, ANOVA, time-series, etc.

# --------------------------------------------------------------------
# 5. SAVE PROCESSED DATA (optional)
# --------------------------------------------------------------------
# If you create a cleaned/transformed dataset, save it for later use
processed_path = 'processed_data.csv'
df.to_csv(processed_path, index=False)
print(f"\nProcessed data saved to {processed_path}")

# --------------------------------------------------------------------
# 6. FINAL PLOTS FOR REPORT
# --------------------------------------------------------------------
print("\n=== GENERATING FINAL PLOTS ===")
# Example scatter plot (if you have two numeric variables)
if 'x_var' in df.columns and 'y_var' in df.columns:
    plt.figure(figsize=(7, 5))
    sns.scatterplot(x='x_var', y='y_var', hue='treatment', data=df)
    plt.title('Relationship Between X and Y')
    plt.savefig('../04_results/scatter_xy.png', dpi=300)
    plt.close()
    print("Saved scatter plot to ../04_results/scatter_xy.png")

# --------------------------------------------------------------------
print("\n=== ANALYSIS COMPLETE ===")
print("Check the ../04_results/ directory for generated figures.")
print("Remember to document your analysis steps in the README or in comments.")
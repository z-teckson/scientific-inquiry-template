# Analysis Phase

This directory contains your data cleaning, processing, and statistical analysis code. The goal is to transform raw data into meaningful results that answer your research question.

## Structure

- `analysis.py` – A placeholder Python script. Replace it with your own analysis code (Python, R, Julia, etc.) or delete it if you prefer a different language.
- (Optional) `notebooks/` – You may create a sub‑directory for Jupyter or RMarkdown notebooks if you prefer interactive analysis.
- (Optional) `scripts/` – For helper scripts (e.g., functions, plotting utilities).
- (Optional) `output/` – For intermediate files generated during analysis (cleaned data, transformed datasets). **Do not commit large files**; use `.gitignore` to exclude them.

## Workflow

1. **Data Cleaning**
   - Load the raw data from `../02_data/`.
   - Check for missing values, outliers, and inconsistencies.
   - Convert units, rename columns, and create derived variables as needed.
   - Save a cleaned version of the dataset (e.g., `cleaned_data.csv`) in this directory or a sub‑folder.

2. **Exploratory Analysis**
   - Generate summary statistics (mean, median, standard deviation, etc.).
   - Create preliminary visualizations (histograms, scatter plots, box plots) to understand the data distribution and relationships.

3. **Statistical Testing / Modeling**
   - Perform the statistical tests or models specified in your proposal (t‑tests, ANOVA, regression, etc.).
   - Document the assumptions of each test and verify them where possible.

4. **Generate Final Results**
   - Produce the figures and tables that will go into your final report.
   - Save them in the `../04_results/` directory with descriptive names.

## Reproducibility Checklist

- [ ] Your analysis script(s) can be run from start to finish without manual intervention.
- [ ] All file paths are relative (e.g., `../02_data/raw_data.csv`), not absolute.
- [ ] You have listed all required packages and their versions (e.g., in a `requirements.txt` or `environment.yml` file).
- [ ] You have added comments explaining non‑obvious steps.
- [ ] The script outputs the same results when run on a different machine (if possible, test this).

## Example `analysis.py` Outline

The included `analysis.py` file shows a basic skeleton. Adapt it to your own project.

```python
"""
Analysis script for [Your Project Name]
Author: [Your Name]
Date: [Date]

This script loads the cleaned data, performs statistical tests, and generates plots.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# 1. Load data
data = pd.read_csv('../02_data/cleaned_data.csv')

# 2. Exploratory analysis
print(data.describe())
print(data.groupby('treatment').mean())

# 3. Statistical test (example: t‑test between two groups)
group1 = data[data['treatment'] == 'control']['measurement']
group2 = data[data['treatment'] == 'experimental']['measurement']
t_stat, p_value = stats.ttest_ind(group1, group2)
print(f'T‑test: t = {t_stat:.3f}, p = {p_value:.3f}')

# 4. Create a figure
plt.figure(figsize=(8, 5))
sns.boxplot(x='treatment', y='measurement', data=data)
plt.title('Measurement by Treatment Group')
plt.savefig('../04_results/boxplot_treatment.png', dpi=300)
plt.close()
```

## Language Flexibility

You are not required to use Python. Feel free to replace `analysis.py` with:

- An R script (`analysis.R`)
- A Julia script (`analysis.jl`)
- A Jupyter notebook (`analysis.ipynb`)
- A Markdown file with embedded code (RMarkdown, Quarto)

Whatever language you choose, make sure your code is well‑documented and reproducible.

## Next Steps

Once your analysis is complete and you have generated the required outputs, move to the `04_results` directory to organize your figures and tables. Open a Pull Request linking to the “Complete Data Analysis Script” issue.
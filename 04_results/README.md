# Results Directory

Store all final figures, tables, and other outputs from your analysis here. This directory is meant for the **final versions** of visuals that you will include in your report.

## Guidelines

1. **File Naming**
   - Use descriptive names that indicate what the figure/table shows.
   - Include the figure number if you have a sequence (e.g., `fig1_growth_vs_time.png`, `table2_statistics.csv`).
   - Avoid spaces; use underscores or hyphens.

2. **Formats**
   - **Images:** `.png` (recommended for plots), `.svg` (scalable vector graphics), `.jpg` (for photographs).
   - **Tables:** `.csv` (comma‑separated values) or `.tsv` (tab‑separated) for data tables; `.md` (Markdown) for formatted tables.
   - **Other:** `.pdf` for multi‑page documents, `.txt` for plain‑text summaries.

3. **Organization**
   - You may create sub‑folders if needed (e.g., `figures/`, `tables/`, `supplementary/`).
   - Keep the directory tidy—remove intermediate or unused files.

4. **Version Control**
   - Large binary files (e.g., high‑resolution images) can be tracked with Git LFS if necessary, but for this project standard Git is fine.
   - If a file is very large (>10 MB), consider compressing it or storing it elsewhere (e.g., a cloud drive) and linking to it in a README.

## What to Include

- **Figures:** Graphs, charts, diagrams, maps, photographs of experimental setups.
- **Tables:** Summary statistics, model coefficients, raw data summaries.
- **Supplementary Material:** Additional analyses, sensitivity tests, extended data.

## Example Structure

```
04_results/
├── README.md
├── fig1_growth_curves.png
├── fig2_correlation_scatter.png
├── table1_descriptive_stats.csv
├── table2_anova_results.md
└── supplementary/
    └── extra_analysis_plot.pdf
```

## Linking to Your Report

In your final report (`../05_final_report/final_report.md`), reference each figure and table by its file name, e.g.:

```markdown
![Growth curves over time](fig1_growth_curves.png)

Table 1: Descriptive statistics ([download](table1_descriptive_stats.csv))
```

## Quality Checklist

- [ ] All figures have clear axis labels, units, and a legend where appropriate.
- [ ] Color choices are accessible (visible in grayscale, consider color‑blind viewers).
- [ ] Tables are formatted consistently and include necessary captions.
- [ ] Each file is referenced in the final report.
- [ ] The resolution of images is sufficient for printing or screen viewing (≥300 DPI for print, ≥96 DPI for screen).

## Next Steps

Once your results are ready, proceed to the `05_final_report` directory to write up your findings. Open a Pull Request linking to the “Draft Final Report” issue when your report is complete.
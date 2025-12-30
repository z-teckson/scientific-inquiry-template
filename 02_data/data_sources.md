# Data Sources & Documentation

This directory is for documenting the raw data you collect or obtain for your project. Good documentation ensures your work is reproducible and transparent.

## Instructions

1. **Store raw data files** in this directory (or in a sub‑folder, e.g., `raw/`).
2. **Never edit raw data files directly.** If you need to clean or transform the data, do so in the `03_analysis` directory and keep the original raw files unchanged.
3. **Document each data source** using the template below.

## Data Source Template

Copy and fill out this template for each distinct dataset you use.

### Dataset 1: [Short descriptive name]

- **Origin:** Where did the data come from? (e.g., your own experiment, a public repository, a survey)
- **Collection method:** How were the data collected? (e.g., manual measurement, automated sensor, downloaded from [source])
- **Date range:** When were the data collected?
- **File format:** `.csv`, `.xlsx`, `.txt`, etc.
- **File name(s):** `raw_data_experiment1.csv`
- **Variables recorded:** List the columns or measurements included.
- **Units:** Specify the units for each numeric variable.
- **Notes:** Any issues, limitations, or special considerations (e.g., missing values, calibration details).

### Dataset 2: [Short descriptive name]

*(Repeat the same structure as above.)*

## Ethical & Licensing Considerations

- If you collected data from human participants, describe how you obtained informed consent and maintained confidentiality.
- If you are using data from another source, provide the proper citation and verify that you are allowed to use it under its license.
- If your data are sensitive (e.g., location data of endangered species), explain how you are protecting them.

## Data Quality Checklist

Before proceeding to analysis, verify the following:

- [ ] Files are named consistently and descriptively.
- [ ] Metadata (units, collection dates, etc.) is recorded.
- [ ] Missing or anomalous values are flagged.
- [ ] Data are backed up in at least one other location (e.g., cloud storage, external drive).
- [ ] You have permission to use and share the data (if applicable).

## Next Steps

Once your raw data are documented and stored, move to the `03_analysis` directory to begin cleaning and analyzing them. Create a Pull Request linking to the “Gather and Document Raw Data” issue when this step is complete.
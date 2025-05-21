# ALDA-Project

## Overview

ALDA-Project is a data analysis and visualization toolkit focused on healthcare datasets, particularly patient records. It provides robust tools for parsing, analyzing, and visualizing medical data, enabling users to extract insights about patient demographics, chronic conditions, and other health indicators.

## Features

- **Data Parsing:** Automatic normalization and cleaning of CSV files with Spanish medical data.
- **Analysis Tools:** Functions for frequency counts, group statistics, and custom filtering.
- **Visualization:** Generation of publication-quality plots for key health metrics (e.g., BMI, blood pressure, age/weight by gender).
- **Jupyter Notebooks:** Example notebooks for data exploration and reproducibility.
- **Testing:** Comprehensive test suite for all core modules.

## Project Structure

```
data/                # Raw and sample datasets (CSV, ZIP)
notebooks/           # Jupyter Notebooks for EDA and data parsing
plots/               # Output visualizations (PNG)
src/
  analyzer.py        # Analysis functions (counts, means, filters)
  parser.py          # CSV parsing and normalization
  visualizer.py      # Plotting utilities
  run_visualizer.py  # Script to generate all plots
tests/               # Unit tests for all modules
requirements.txt     # Python dependencies
```

## Getting Started

### Prerequisites

- Python 3.8+
- Recommended: Create a virtual environment

### Installation

1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd Data-Analysis
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Usage

#### Data Parsing

Use the parser to load and normalize CSV files:
```python
from src.parser import parse_csv
df = parse_csv("data/data014_small.csv")
```

#### Analysis

Example: Count patients by gender
```python
from src.analyzer import count_by_column
counts = count_by_column(df, "género")
```

#### Visualization

Generate all plots:
```sh
python src/run_visualizer.py
```
Plots will be saved in the `plots/` directory.

#### Jupyter Notebooks

Explore the `notebooks/` folder for step-by-step data exploration and analysis.

### Testing

Run all tests with:
```sh
.\Scripts\coverage.bat 
```

## 📊 Analysis and Insights

The following visualizations were generated to explore the clinical dataset:

### 1. **Weight vs Age by Gender**

The scatterplot revealed a positive trend between age and weight. Male patients tend to weigh more than female patients across all ages. However, the weight distribution appears relatively stable after age 40, and a number of outliers were observed at both extremes, suggesting potential data anomalies or exceptional health conditions.

### 2. **BMI vs Chronic Conditions**

The violin plot comparing BMI distributions shows that individuals with chronic diseases (e.g., hypertension, diabetes) tend to have higher BMIs on average. The distribution is notably shifted toward higher values for those with chronic conditions, suggesting a clear association between elevated BMI and chronic illness prevalence.

### 3. **Systolic Blood Pressure vs Socioeconomic Level**

Boxplots showed consistent systolic pressure distributions across the "Low", "Medium", and "High" socioeconomic groups. Medians were close to 120 mmHg in all categories, with no substantial differences in spread, indicating that socioeconomic level may not strongly influence systolic blood pressure in this dataset.

### 4. **Weight vs Height**

This scatterplot confirmed the expected linear correlation between height and weight. Male patients generally appear taller and heavier than female patients. The clustering patterns reflect standard physiological differences and suggest that both variables are good mutual predictors.

### 5. **Weight vs Age by Gender and Chronic Condition**

Using a faceted plot, we analyzed weight and age jointly by gender and the presence of chronic conditions. The panels show that patients with chronic conditions tend to have slightly higher weight values at similar ages, particularly among males. This supports the notion that chronic illnesses may co-occur with higher body mass, especially in aging populations.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

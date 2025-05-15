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
pytest
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

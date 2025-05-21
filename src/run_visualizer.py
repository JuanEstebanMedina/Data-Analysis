from src.parser import parse_csv
import os
from src.visualizer import (
    plot_weight_age_by_gender,
    plot_imc_by_chronic_condition,
    plot_pressure_by_socioeconomic_level,
    plot_weight_vs_height,
    plot_weight_age_by_gender_and_condition,
)

# DATA = "data014_big.csv"
DATA = "data014_small.csv"

csv_path = os.path.join(os.path.dirname(__file__), "..", "data", DATA)
df = parse_csv(csv_path)

plot_weight_age_by_gender(df)
plot_imc_by_chronic_condition(df)
plot_pressure_by_socioeconomic_level(df)
plot_weight_vs_height(df)
plot_weight_age_by_gender_and_condition(df)

print("Gráficos generados satisfactoriamente.")

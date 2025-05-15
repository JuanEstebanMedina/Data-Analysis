from src.parser import parse_csv
import os
from src.visualizer import (
    plot_weight_age_by_gender,
    plot_imc_by_chronic_condition,
    plot_pressure_by_socioeconomic_level
)

csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "data014_small.csv")
df = parse_csv(csv_path)

plot_weight_age_by_gender(df)
plot_imc_by_chronic_condition(df)
plot_pressure_by_socioeconomic_level(df)

print("Gráficos generados satisfactoriamente.")

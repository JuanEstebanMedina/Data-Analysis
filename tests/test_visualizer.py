import pytest
import pandas as pd
import os
from src.visualizer import (
    plot_imc_by_chronic_condition,
    plot_weight_age_by_gender,
    plot_pressure_by_socioeconomic_level,
)


def test_plot_weight_age_by_gender_creates_file():
    data = {
        "edad": [25, 30, 45, 50],
        "peso": [60, 75, 70, 80],
        "género": ["F", "M", "F", "M"],
    }
    df = pd.DataFrame(data)
    file_path = "tests/test_plots/test_edad_peso_por_genero.png"

    plot_weight_age_by_gender(df, save_path=file_path)

    assert os.path.exists(file_path)

    os.remove(file_path)


def test_plot_weight_age_by_gender_without_a_column():
    data = {
        "edad": [25, 30, 45, 50],
        "peso": [60, 75, 70, 80],
        # 'género' missing
    }
    df = pd.DataFrame(data)
    file_path = "tests/test_plots/test_edad_peso_por_genero.png"

    with pytest.raises(ValueError):
        plot_weight_age_by_gender(df, save_path=file_path)


def test_plot_imc_by_chronic_condition_creates_file():
    data = {
        "imc": [22.5, 27.3, 30.1, 24.2],
        "enfermedades_crónicas": [
            "Ninguna",
            "Hipertensión",
            "Diabetes tipo 2",
            "Ninguna",
        ],
    }
    df = pd.DataFrame(data)
    file_path = "tests/test_plots/test_imc_enfermedades_cronicas.png"

    plot_imc_by_chronic_condition(df, save_path=file_path)

    assert os.path.exists(file_path)
    os.remove(file_path)


def test_plot_imc_by_chronic_condition_without_a_column():
    data = {
        "imc": [22.5, 27.3, 30.1, 24.2],
        # 'enfermedades_crónicas' missing
    }
    df = pd.DataFrame(data)
    file_path = "tests/test_plots/test_imc_enfermedades_cronicas.png"

    with pytest.raises(ValueError):
        plot_imc_by_chronic_condition(df, save_path=file_path)


def test_plot_pressure_by_socioeconomic_level_creates_file():
    data = {
        "presión_arterial": [
            "120/80 mmHg",
            "130/85 mmHg",
            "125/82 mmHg",
            "110/70 mmHg",
        ],
        "nivel_socioeconómico": ["1", "2", "3", "2"],
    }
    df = pd.DataFrame(data)
    file_path = "tests/test_plots/test_presion_vs_nivel.png"

    plot_pressure_by_socioeconomic_level(df, save_path=file_path)

    assert os.path.exists(file_path)
    os.remove(file_path)


def test_plot_pressure_by_socioeconomic_level_without_column():
    data = {
        "presión_arterial": ["120/80 mmHg", "130/85 mmHg"],
        # 'nivel_socioeconómico' missing
    }
    df = pd.DataFrame(data)
    file_path = "tests/test_plots/test_presion_vs_nivel.png"

    with pytest.raises(ValueError):
        plot_pressure_by_socioeconomic_level(df, save_path=file_path)


def test_extract_systolic_handles_invalid_input():
    data = {
        "presión_arterial": ["abs", "hola mundo", "", None],
        "nivel_socioeconómico": ["1", "2", "3", "2"],
    }
    df = pd.DataFrame(data)
    file_path = "tests/test_plots/test_presion_vs_nivel.png"

    plot_pressure_by_socioeconomic_level(df, save_path=file_path)

    assert os.path.exists(file_path)
    os.remove(file_path)

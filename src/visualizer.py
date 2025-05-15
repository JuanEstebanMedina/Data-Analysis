import seaborn as sns
import matplotlib.pyplot as plt
import os


def plot_weight_age_by_gender(df, save_path="plots/edad_peso_por_genero.png"):
    """
    Plot the relationship between age and weight, colored by gender.
    Saves the plot to the specified path.
    """
    if (
        "edad" not in df.columns
        or "peso" not in df.columns
        or "género" not in df.columns
    ):
        raise ValueError(
            "Las columnas necesarias ('edad', 'peso', 'género') no están presentes en el DataFrame."
        )

    filtered_df = df[["edad", "peso", "género"]].dropna()

    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=filtered_df, x="edad", y="peso", hue="género", palette="Set2")
    plt.title("Relación entre Edad y Peso por Género")
    plt.xlabel("Edad")
    plt.ylabel("Peso")
    plt.legend(title="Género")
    plt.tight_layout()

    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Save the plot
    plt.savefig(save_path)
    plt.close()


def plot_imc_by_chronic_condition(df, save_path="plots/imc_enfermedades_cronicas.png"):
    """
    Plot distribution of BMI (IMC) based on presence of chronic diseases.
    Assumes 'imc' and 'enfermedades_crónicas' columns exist.
    """
    if "imc" not in df.columns or "enfermedades_crónicas" not in df.columns:
        raise ValueError("Las columnas 'imc' y 'enfermedades_crónicas' son necesarias.")

    # Clean and standardize chronic disease status
    filtered_df = df[["imc", "enfermedades_crónicas"]].dropna()

    filtered_df["condición"] = filtered_df["enfermedades_crónicas"].apply(
        lambda x: (
            "Ninguna"
            if str(x).strip().lower() == "ninguna"
            else "Con enfermedad crónica"
        )
    )

    plt.figure(figsize=(8, 6))
    sns.violinplot(
        data=filtered_df,
        x="condición",
        y="imc",
        hue="condición",
        legend=False,
        palette="pastel",
    )

    plt.title("Relación entre IMC y Enfermedades Crónicas")
    plt.xlabel("Condición Crónica")
    plt.ylabel("Índice de Masa Corporal (IMC)")
    plt.tight_layout()

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path)
    plt.close()


def plot_pressure_by_socioeconomic_level(
    df, save_path="plots/presion_vs_nivel_socioeconomico.png"
):
    if "presión_arterial" not in df.columns or "nivel_socioeconómico" not in df.columns:
        raise ValueError(
            "Las columnas 'presión_arterial' y 'nivel_socioeconómico' son necesarias."
        )

    def extract_systolic(value):
        try:
            return int(str(value).split("/")[0])
        except Exception:
            return None

    df["presión_sistólica"] = df["presión_arterial"].apply(extract_systolic)
    df = df.dropna(subset=["presión_sistólica", "nivel_socioeconómico"])

    plt.figure(figsize=(8, 6))
    sns.boxplot(
        data=df,
        x="nivel_socioeconómico",
        y="presión_sistólica",
        hue="nivel_socioeconómico",
        legend=False,
        palette="Blues",
        orientation="vertical",
    )
    plt.title("Presión Sistólica por Nivel Socioeconómico")
    plt.xlabel("Nivel Socioeconómico")
    plt.ylabel("Presión Sistólica (mmHg)")
    plt.tight_layout()

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path)
    plt.close()

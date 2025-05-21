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


def plot_weight_vs_height(df, save_path="plots/peso_vs_estatura.png"):
    """
    Plot the relationship between weight and height.
    Optional: colored by gender if column exists.
    """
    if "peso" not in df.columns or "altura" not in df.columns:
        raise ValueError("Las columnas 'peso' y 'altura' son necesarias.")

    filtered_df = df[["peso", "altura"]].copy()
    if "género" in df.columns:
        filtered_df["género"] = df["género"]

    filtered_df = filtered_df.dropna()

    plt.figure(figsize=(8, 6))
    if "género" in filtered_df.columns:
        sns.scatterplot(
            data=filtered_df, x="altura", y="peso", hue="género", palette="Set2"
        )
    else:
        sns.scatterplot(data=filtered_df, x="altura", y="peso", color="steelblue")

    plt.title("Relación entre Peso y Estatura")
    plt.xlabel("Estatura (cm)")
    plt.ylabel("Peso (kg)")
    plt.tight_layout()

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path)
    plt.close()


def plot_weight_age_by_gender_and_condition(
    df, save_path="plots/peso_edad_genero_enfermedades.png"
):
    """
    Plot weight vs age, colored by gender, separated by chronic condition status.
    """
    required_cols = ["edad", "peso", "género", "enfermedades_crónicas"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"La columna '{col}' es requerida para este gráfico.")

    filtered_df = df[required_cols].dropna()

    # Categorizar enfermedades
    filtered_df["condición"] = filtered_df["enfermedades_crónicas"].apply(
        lambda x: (
            "Ninguna"
            if str(x).strip().lower() == "ninguna"
            else "Con enfermedad crónica"
        )
    )

    # Crear el grid
    g = sns.FacetGrid(
        filtered_df, col="condición", hue="género", palette="Set2", height=5, aspect=1.2
    )
    g.map_dataframe(sns.scatterplot, x="edad", y="peso")
    g.set_axis_labels("Edad", "Peso (kg)")
    g.add_legend()
    g.fig.subplots_adjust(top=0.85)
    g.fig.suptitle("Relación entre Peso, Edad, Género y Condición Crónica")

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    g.savefig(save_path)
    plt.close()

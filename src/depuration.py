# src/depuration.py
# Contiene funciones para la sección de depuración del notebook 01_Preprocessing.ipynb
import matplotlib.pyplot as plt
import numpy as np

# Función para visualizar la distribución de una variable numérica con boxplot e histograma
def visualizar_variable(df, variable, transformar=None):
    fig, ax = plt.subplots(2, figsize=(10, 6))
    plt.style.use('seaborn-v0_8-whitegrid')
    if transformar == 'log':
        x = np.log1p(df[variable]) # se usa log1p() para evitar errores con ceros
        variable = variable + '_log'
    elif transformar == 'sqrt':
        x = np.sqrt(df[variable])
        variable = variable + '_sqrt'
    else:
        x = df[variable]
    # Gráfico superior: boxplot
    ax[0].boxplot(x.dropna(), vert=False)
    ax[0].set_title(f'Boxplot e histograma de {variable}')

    # Gráfico inferior: histograma con binning de variables continuas
    ax[1].hist(x.dropna(), bins=30)
    ax[1].set_xlabel(variable)
    ax[1].set_ylabel('Frecuencia')

    plt.tight_layout()
    plt.show()

def separar_numericas(df, numericas):
    simetricas = []
    asimetricas = []

    # Evaluamos la asimetría de cada columna
    for col in numericas:
        sesgo = df[col].skew()
        if abs(sesgo) > 3:
            asimetricas.append(col)
        else:
            simetricas.append(col)
    return simetricas, asimetricas
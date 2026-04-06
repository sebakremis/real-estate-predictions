# Real Estate Predictions 🏡📊

Este repositorio contiene mi solución para la competencia de Kaggle: [House Prices - Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques).

El objetivo principal de este proyecto es predecir con precisión el precio de venta de propiedades en Ames, Iowa, mediante la implementación de técnicas avanzadas de regresión en Machine Learning. Se utilizan un total de 79 variables explicativas (características de las casas) para construir el modelo.

## 🚀 Estructura del Proyecto

* `data/raw`: Contiene los archivos de datos originales provistos por Kaggle (`train.csv`, `test.csv`, `data_description.txt`).
* `data/submission.csv`: Archivo de salida para subir las predicciones a la plataforma de Kaggle.
* `src/`: Carpeta con scripts modulares en Python.
  * `functions.py`: Funciones customizadas para la visualización y limpieza de la base de datos (e.g. histogramas, boxplots).
* `01_Preprocessing.ipynb`: Jupyter notebook enfocado en la exploración inicial (EDA), limpieza de datos, manejo de valores nulos y creación de nuevas variables (Feature Engineering).
* `02_Modeling.ipynb`: Jupyter notebook donde se entrenan modelos de ML y se evalúan los resultados.


## 🛠️ Instalación y Requisitos

Para replicar y ejecutar el código de este proyecto de manera local, primero clona este repositorio y luego instala las dependencias utilizando el archivo `requirements.txt`. Asegúrate de tener instalado Python 3.8+:

```bash
git clone https://github.com/sebakremis/real-estate-predictions.git
cd real-estate-predictions
pip install -r requirements.txt
```

Ejecuta el notebook desde Jupyter o un entorno compatible. Ejemplo:
```bash
jupyter notebook 01_Preprocessing.ipynb
```

🧠 Metodología
Análisis Exploratorio de Datos (EDA): Visualización y descubrimiento de la distribución de SalePrice y su relación con variables clave.

Data Cleaning & Preprocessing.

Concatenación de datos de entrenamiento y test para un procesamiento uniforme.

Manejo avanzado de valores faltantes (NaNs interpretados según el dominio del problema).

Conversión inteligente de variables categóricas vs. numéricas.

Feature Engineering: Creación de métricas de dominio específicas, como `AvgRoomSize`, `HasGarage` y `GarageAge`.

👨‍💻 Autor
[Sebastian Kremis] * [LinkedIn](https://www.linkedin.com/in/sebastian-kremis)

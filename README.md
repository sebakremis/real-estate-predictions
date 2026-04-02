# Real Estate Predictions 🏡📊

Este repositorio contiene mi solución para la competencia de Kaggle: [House Prices - Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques).

El objetivo principal de este proyecto es predecir con precisión el precio de venta de propiedades en Ames, Iowa, mediante la implementación de técnicas avanzadas de regresión en Machine Learning. Se utilizan un total de 79 variables explicativas (características de las casas) para construir el modelo.

## 🚀 Estructura del Proyecto

* `data/`: Contiene los archivos de datos originales provistos por Kaggle (`train.csv`, `test.csv`, `data_description.txt`).
* `src/`: Carpeta con scripts modulares en Python.
  * `depuration.py`: Funciones customizadas para la visualización y limpieza de la base de datos (e.g. histogramas, boxplots).
* `01_Preprocessing.ipynb`: Jupyter notebook enfocado en la exploración inicial (EDA), limpieza de datos, manejo de valores nulos y creación de nuevas variables (Feature Engineering).
* `sample_submission.csv`: Archivo de ejemplo para los resultados enviados a la plataforma.

## 🛠️ Instalación y Requisitos

Para replicar y ejecutar el código de este proyecto de manera local, asegúrate de tener instalado Python 3.8+ y las siguientes librerías:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
git clone [https://github.com/TU_USUARIO/real-estate-predictions.git](https://github.com/TU_USUARIO/real-estate-predictions.git)

```

Ejecuta el notebook desde Jupyter o un entorno compatible. Ejemplo:
```bash
jupyter notebook 01_Preprocessing.ipynb
```

🧠 Metodología
Análisis Exploratorio de Datos (EDA): Visualización y descubrimiento de la distribución de SalePrice y su relación con variables clave.

Data Cleaning & Preprocessing:

Concatenación de datos de entrenamiento y test para un procesamiento uniforme.

Manejo avanzado de valores faltantes (NaNs interpretados según el dominio del problema).

Conversión inteligente de variables categóricas vs. numéricas.

Feature Engineering: Creación de métricas de dominio específicas, como AvgRoomSize, HasGarage y GarageAge.

📈 Próximos Pasos (To-Do)
[ ] Transformación Box-Cox / Logarítmica para características sesgadas y target.

[ ] Codificación Ordinal (Ordinal Encoding) para features de calidad de los inmuebles.

[ ] Entrenar y optimizar modelos Baseline (Lasso, Ridge Regression).

[ ] Implementar modelos basados en árboles (XGBoost, LightGBM, CatBoost).

[ ] Ensamblado de modelos (Stacking) para optimizar el Root Mean Squared Logarithmic Error (RMSLE).

🏆 Resultados
(A completar: Añade aquí tu métrica de Score final de Kaggle RMSLE y la posición una vez que hagas la sumisión final).

👨‍💻 Autor
[Sebastian Kremis] * [LinkedIn](www.linkedin.com/in/sebastian-kremis)

[Kaggle](https://www.kaggle.com/sebastiankremis)
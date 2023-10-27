#1. Se pide cargar el archivo como dataframe de Airbnb-Milan.csv

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("airbnb_Milan.csv", sep=";")
df.head()

#2. Se pide crear un nuevo dataframe que contenga únicamente las siguientes columnas:     “host_is_superhost”, “host_identity_verified", “bathrooms”, “bedrooms”, “daily_price”, “security deposit”, “minimum_nights”, “number_of_reviews”, “review_scores_rating”

df2 = df[["host_is_superhost", "host_identity_verified", "bathrooms", "bedrooms", "daily_price", "security_deposit", "minimum_nights", "number_of_reviews", "review_scores_rating"]]
df2.head()

#3. Se pide cambiar los factores de la variable “host_is_superhost” de 0, 1 a: “SI” y, "NO”.(investigar la función recode).





#4. Se pide cambiar los factores de la variable “host_identity_verified" de 0, 1 a: “VERIFICA” y "NO VERIFICA”.

df2["host_is_superhost"] = df2["host_is_superhost"].replace({0: "NO", 1: "SI"})
df2["host_identity_verified"] = df2["host_identity_verified"].replace({0: "NO VERIFICA", 1: "VERIFICA"})
df2.head()






1.4 Mostrar un resumen estadístico de los datos

1.5 Filtrar el dataset por apartamentos cuyo mínimo de noches sea igual o menor que siete.

1.6 ¿Cuál es el precio medio por día de una habitación en función de si el anfitrión tiene verificado o no su perfil?

1.7 Quien tiene un mayor numero de reseñas un super host o un super no host

1.8 Sobre la estadística anterior ¿quién tiene la puntuación media más alta?

1.9Crea un vector categórico llamado “CATEGORÍA”, en función de que, si para la puntuación de las reseñas tiene de 0 a 49, sea "NO ACONSEJABLE"; de 50 a 75 sea “ESTÁNDAR”; y de 76 a 100 sea “TOP”.

1.10 Mostrar las frecuencias de la variable categoría

1.11 Obtener el histograma del precio por día
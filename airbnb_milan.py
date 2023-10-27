import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Se pide cargar el archivo como dataframe de airbnb_milan.csv
df = pd.read_csv("airbnb_milan.csv", sep=";")
df.head()
print(df.shape)

# 2. Se pide crear un nuevo dataframe que contenga únicamente las siguientes columnas:“host_is_superhost”“host identity verified",“bathrooms”,“bedrooms”,“daily_price”,“security deposit”,“minimum_nights”,“number_of_reviews”“review_scores_rating”

# Seleccionar las columnas de interés
cols = ["host_is_superhost", "host_identity_verified", "bathrooms", "bedrooms", "daily_price",
        "security_deposit", "minimum_nights", "number_of_reviews", "review_scores_rating"]
df2 = df[cols]

# Mostrar información sobre el subconjunto de datos
df2.info()
print(df2.shape)

# Mostrar un resumen estadístico de los datos
print(df2.describe())

# 3.Se pide cambiar los factores de la variable “host_is_superhost” de 0, 1 a: “SI” y, "NO”.(investigar la función recode).

df["host_is_superhost"] = df["host_is_superhost"].replace({0: "NO", 1: "SI"})
print(df["host_is_superhost"].head())

# 4.Se pide cambiar los factores de la variable “host_identity_verified" de 0, 1 a: “VERIFICA” y "NO VERIFICA”.

df2["host_is_superhost"] = df2["host_is_superhost"].replace({0: "NO", 1: "SI"})
df2["host_identity_verified"] = df2["host_identity_verified"].replace(
    {0: "NO VERIFICA", 1: "VERIFICA"})
df2.head()
print(df2.shape)

# 5. Se pide cambiar los factores de la variable “security_deposit” de 0, 1 a: “NO” y, "SI”.

df2["security_deposit"] = df2["security_deposit"].replace({0: "NO", 1: "SI"})
df2.head()
print(df2.shape)

# 6. Se pide cambiar los factores de la variable “review_scores_rating” de 0, 1 a: “NO” y, "SI”.
df2["review_scores_rating"] = df2["review_scores_rating"].replace({
                                                                  0: "NO", 1: "SI"})
df2.head()
print(df2.shape)

# 7.Mostrar un resumen estadístico de los datos
print(df2.describe())

# 8.Filtrar el dataset por apartamentos cuyo mínimo de noches sea igual o menor que siete.
df_filtered = df2[df2["minimum_nights"] <= 7]
print(df_filtered.shape)

# 11. ¿Cuál es el precio medio por día de una habitación en función de si el anfitrión tiene verificado o no su perfil?
df2.groupby("host_identity_verified")["daily_price"].mean()
print(df2.groupby("host_identity_verified")["daily_price"].mean())

# 10. Quien tiene un mayor numero de reseñas un super host o un super no host
df2.groupby("host_is_superhost")["number_of_reviews"].sum()
print(df2.groupby("host_is_superhost")["number_of_reviews"].sum())

# 11. Sobre la estadística anterior ¿quién tiene la puntuación media más alta?
df2.groupby("host_is_superhost")["review_scores_rating"].mean()
print(df2.groupby("host_is_superhost")["review_scores_rating"].mean())


# 12 Crea un vector categórico llamado “CATEGORÍA”, en función de que, si para la puntuación de las reseñas tiene de 0 a 49, sea "NO ACONSEJABLE"; de 50 a 75 sea “ESTÁNDAR”; y de 76 a 100 sea “TOP”.
df2["CATEGORÍA"] = pd.cut(df2["review_scores_rating"], bins=[
                          0, 49, 75, 100], labels=["NO ACONSEJABLE", "ESTÁNDAR", "TOP"])
df2.head()
print(df2.shape)


# 13 Mostrar las frecuencias de la variable categoría
df2["CATEGORÍA"].value_counts()
print(df2["CATEGORÍA"].value_counts())


# 14 Obtener el histograma del precio por día
df2["daily_price"].hist()


# 15 Obtener el histograma del precio por día, pero con 20 intervalos
df2["daily_price"].hist(bins=20)

# 16 Obtener el histograma del precio por día, pero con 20 intervalos y en color verde
df2["daily_price"].hist(bins=20, color="green")

# 17 Obtener el histograma del precio por día, pero con 20 intervalos, en color verde y con un título
df2["daily_price"].hist(bins=20, color="green")
plt.title("Precio por día")
plt.xlabel("Precio")
plt.ylabel("Frecuencia")
plt.show()

# 18 Obtener el histograma del precio por día, pero con 20 intervalos, en color verde, con un título y con una línea vertical en la media
df2["daily_price"].hist(bins=20, color="green")
plt.title("Precio por día")
plt.xlabel("Precio")
plt.ylabel("Frecuencia")
plt.axvline(df2["daily_price"].mean(), color="red")
plt.show()

# 19 Obtener el histograma del precio por día, pero con 20 intervalos, en color verde, con un título y con una línea vertical en la media y otra en la mediana usando seaborn
sns.distplot(df2["daily_price"], bins=20, color="green")
plt.title("Precio por día")
plt.xlabel("Precio")
plt.ylabel("Frecuencia")
plt.axvline(df2["daily_price"].mean(), color="red")
plt.axvline(df2["daily_price"].median(), color="blue")
plt.show()

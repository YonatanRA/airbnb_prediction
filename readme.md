# Airbnb Price Prediction


## 1 - Descripción

Los datos provienen del proyecto [Inside Airbnb](http://insideairbnb.com/about.html) y describen el uso de la pltaforma de alquileres temporarios Airbnb en la ciudad de Madrid. Están compuestos de 7 archivos:

Archivo | Descripción
--------|------------
[listings.csv.gz](http://data.insideairbnb.com/spain/comunidad-de-madrid/madrid/2020-01-10/data/listings.csv.gz) | Detalle de las publicaciones
[calendar.csv.gz](http://data.insideairbnb.com/spain/comunidad-de-madrid/madrid/2020-01-10/data/calendar.csv.gz) | Datos detallados del calendario para las publicaciones
[reviews.csv.gz](http://data.insideairbnb.com/spain/comunidad-de-madrid/madrid/2020-01-10/data/reviews.csv.gz) | Datos detallados de las reseñas
[listings.csv](http://data.insideairbnb.com/spain/comunidad-de-madrid/madrid/2020-01-10/visualisations/listings.csv) | Resumen de información y métricas para las publicaciones
[reviews.csv](http://data.insideairbnb.com/spain/comunidad-de-madrid/madrid/2020-01-10/visualisations/reviews.csv) | Resumen de reseñas 
[neighbourhoods.csv](http://data.insideairbnb.com/spain/comunidad-de-madrid/madrid/2020-01-10/visualisations/neighbourhoods.csv) | Lista de barrios. Procedente de archivos GIS de código abierto o de la ciudad
[neighbourhoods.geojson](http://data.insideairbnb.com/spain/comunidad-de-madrid/madrid/2020-01-10/visualisations/neighbourhoods.geojson) | Archivo GeoJSON de barrios de la ciudad

Se plantea un escenario hipotético en el que un cliente posee propiedades disponibles para su alquiler, distribuidas en diferentes barrios de la ciudad. Además de un análsis detallado de la situación, el cliente quiere poder predecir el precio final al que podría alquilar cada propiedad. 

## 2 - Objetivos específicos 

### 2.1 - Analisis exploratorio

*  2.1.1 - Describir la situación del mercado de alquileres temporales en Airbnb en la ciudad de Madrid a nivel general. Se valorarán las descripciones visuales y la explotación de la riqueza de los datos. Por ejemplo, haciendo uso de los datos geoespaciales y/o del lenguaje natural.

*  2.1.2 - Analizar los precios de las propiedades publicadas.

### 2.2 - Predicción

* 2.2.1 - Entrenar un modelo capaz de predecir el precio de alquiler diario de una propiedad en Airbnb. Además de las métricas obtenidas, se valorará la justificación del proceso de construcción del modelo (por ejemplo: variables utilizadas/descartadas, métrica/s de evaluación, selección de modelo/s, etc.), la creatividad en la construcción de nuevas variables (utilizando los datos de geolocalización y/o texto no estructurado) y el uso de diferentes técnicas predictivas.


### 3 - Proceso

El proceso a seguir para este problema será el siguiente:
    
+ 1) Limpieza de los datos. Comprobación de valores nulos, duplicados y tipo de dato.
+ 2) Transformación de datos. Normalización, codificación de variables categóricas, etc..
+ 3) Punto de referencia. Con los datos transformados tal cual vienen, se entrena un modelo sencillo y se mide su rendimiento.
+ 4) Exploración y selección de características. Se prueban varios métodos de selección.
+ 5) Entrenamiento del modelo de predicción. Se prueban varios modelos.
+ 6) Extracción de word embeddings con transformers (BERT, DistilBert..) para creación de variables basadas en las reviews. Prueba de modelo multimodal.
+ 7) Análisis completo por barrios. Visualización de mapas y análisis de la dinámica de precios según demanda.
+ 8) Dashboard.


### 4 - Uso

**Todo el proceso paso a paso esta en la carpeta notebooks, cada uno de ellos tiene algunas explicaciones en su interior.**

Para la correcta ejecución de todo el código, es conveniente instalar el entorno virtual de este repositorio ejecutando `conda env create -f entorno.yml` por terminal.


### 5 - Comentarios y Conclusiones

En primer lugar, existen alojamientos con precios extremos, de hasta 10000€. He restringido mi análisis, y también el entrenamiento del modelo predictivo, a precios por debajo de 200€ la noche. Aunque para el estudio de dinámica de precios he dejado todos los datos extremos, puesto que hacen crecer mucho la media y genera diferencias significativas.

En total, existen en Madrid 20372 distintos alojamientos de Airbnb, con un precio medio por noche de 73€. Analizando por barrios, voy primero a los extremos. El barrio con el precio medio por noche más barato es Horcajo en Moratalaz, mientras que el barrio con el precio más alto por noche es Recoletos es Salamanca. En cuanto al número de alojamientos, el barrio con menos airbnbs es El Pardo en Fuencarral y el barrio con más airbnbs es Embajadores en el Centro de Madrid.








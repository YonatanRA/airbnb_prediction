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

## 3 - Entregables

* Código (\*)
* Documentación
* Informe (y/o presentación) con los resultados del análisis y la interpretación de las métricas de predicción obtenidas. Se valorarán positivamente las recomendaciones de negocio.
* Propuesta de despliegue y/o productivización de la solución (\*\*)

<font size="1.9">  \* *Puedes utilizar R y/o Python* </font>

<font size="1.9"> \*\* *Opcional* </font>


### 4 - Extras

Si quieres/puedes hacer algún otro tipo de demostración de habilidades técnicas, aprovechando la riqueza de los datos, anímate! Lo tendremos en cuenta en la evaluación.




# Proceso

El proceso a seguir para este problema será el siguiente:
    
+ 1) Limpieza de los datos. Comprobación de valores nulos, duplicados y tipo de dato.
+ 2) Transformación de datos. Normalización, codificación de variables categóricas, etc..
+ 3) Punto de referencia. Con los datos transformados tal cual vienen, se entrena un modelo sencillo y se mide su rendimiento.
+ 4) Exploración y selección de características. Se prueban varios métodos de selección.
+ 5) Entrenamiento del modelo de predicción. Se prueban varios modelos.
+ 6) Extracción de word embeddings con transformers (BERT, DistillBert..) para creación de variables basadas en las reviews. Prueba de modelo multimodal.
+ 7) Análisis completo por barrios. Visualización de mapas y análisis de la dinámica de precios según demanda.
+ 8) Dashboard.
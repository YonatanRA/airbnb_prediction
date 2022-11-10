![airbnb](https://images.squarespace-cdn.com/content/v1/503bd485e4b0411ce5b1b9f3/1405972951923-A2PGOA76S0M88LAD27ZR/Airbnb_Belo_argumentacion_nuevo_logo.gif?format=1000w)

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

Se puede ver un dashboard en el siguiente link: http://yonrod.pythonanywhere.com/


### 5 - Comentarios y Conclusiones

En primer lugar, existen alojamientos con precios extremos, de hasta 10000€. He restringido mi análisis, y también el entrenamiento del modelo predictivo, a precios por debajo de 200€ la noche. Aunque para el estudio de dinámica de precios he dejado todos los datos extremos, puesto que hacen crecer mucho la media y genera diferencias significativas.


En total, existen en Madrid 20372 distintos alojamientos de Airbnb, con un precio medio por noche de 73€. Analizando por barrios, voy primero a los extremos. El barrio con el precio medio por noche más barato es Horcajo en Moratalaz, mientras que el barrio con el precio más alto por noche es Recoletos es Salamanca. En cuanto al número de alojamientos, el barrio con menos airbnbs es El Pardo en Fuencarral y el barrio con más airbnbs es Embajadores en el Centro de Madrid. Tanto la mayor cantidad de airbnbs y de precio más alto, por supuesto, están en el centro de Madrid, salvo barrios como Mirasierra y Valdefuentes, ambos con precios medios superiores a 90€.


En cuanto al modelo predictivo, explicaré primero la selección de variables. Primero he borrado todas esas columnas constantes y las que no son informativas. Luego he probado varios métodos distintos para realizar la última selección. Las variables más explicativas y con las que finalmente he entrenado han sido:

```python
['accommodates', 'air_conditioning', 'availability_30', 'availability_365', 'availability_60', 'availability_90',
'bathrooms', 'bedrooms', 'beds', 'calculated_host_listings_count', 'calculated_host_listings_count_entire_homes',
'calculated_host_listings_count_private_rooms', 'calculated_host_listings_count_shared_rooms', 'cleaning_fee',
'dishwasher', 'extra_people', 'guests_included','latitude', 'longitude', 'maximum_nights', 'minimum_nights', 
'number_of_reviews', 'number_of_reviews_ltm', 'room_type_private_room', 'room_type_shared_room', 'security_deposit',
'price']
```


Con estas variables y con precios entre 20€ y 196€ (esto me deja con el 85% de los datos), he entrenado un modelo de regresión [Catboost](https://catboost.ai/en/docs/concepts/python-reference_catboostregressor). Después de comprobar el sobreajuste por el ajuste de hiperparámetros he decido dejar los parámetros por defecto del modelo. LLegado a este punto, se realiza la evaluación del modelo. He usado tres métricas: RMSE, MAE y R2. Tanto el primero como el segundo miden errores medios, el tercero es en realidad una razón entre error y varianza. El resultado de la evaluación en la fase de testeo ha sido: `RMSE: 20.89, MAE: 14.44, R2: 0.71`. De realizar el entrenamiento con todos los valores extremos del dataset, el resultado de la evaluación es `RMSE: 256.92, MAE: 69.52, R2: 0.52`. En este último caso, la diferencia entre MAE y RMSE nos da el indicio de que efectivamente ahí están los outliers(se puede ver en la distribución del precio).



Después de esto he entrenado un AutoML de [h2o](https://docs.h2o.ai/h2o/latest-stable/h2o-py/docs/intro.html), he intentado aplicar el análisis de sentimiento para generar nuevas variables, he intentado TFIDF con [spacy](https://spacy.io/) y también un [modelo multimodal](https://github.com/georgian-io/Multimodal-Toolkit) estacando un modelo BERT con un perceptrón de 2 capas como regresor. Estas aproximaciones necesitan más tiempo de análisis y de entrenamiento.



Los datos agrupados por barrios están representados en mapas realizados con [keplergl](https://kepler.gl/). Estos mapas son completamente interactivos, mostrando la información que le usuario necesita.



El estudio de la dinámica de precios me ha dado un par de cosas. Hay barrios cuyo mercado se comporta de una manera completamente saturada, permitiendo un alza en los precios para nuestro hipotético cliente de tener propiedades es ese barrio. Por otro lado, hay barrios cuyo mercado es casi constante. Se requiere más tiempo para un análisis pormenorizado barrio a barrio, aunque idealmente este estudio ha de ser realizado por producto, es decir, para cada alojamiento de airbnb.



Finalmente, he realizado una aproximación al estudio de la serie temporal. La estacionalidad en Madrid es muy acusada, generando picos de ocupación en navidad y en semana santa, pero siendo muy constante durante el resto del año. Por supuesto, existen eventos en ciertos barrios. Además, el precio aumenta de media un 10% los fines de semana con los precios entre semana. Esta es otra estrategia para nuestro posible cliente. 


LLegados a este punto, precisamente los que necesitamos es definir correctamente a nuestro cliente. ¿Cuál es su propósito?¿Alquilar una única casa a las afueras?¿En el centro?¿Es un estudiante que necesita rentabilizar su casa?¿Quizás es un inversor que desea tener en cuenta el precio del suelo y el potencial futuro del barrio? 

La previsión a futuro realizada indica que el precio del airbnb en Madrid subirá.


Esto es un primer paso en el estudio de Aibnb en Madrid.



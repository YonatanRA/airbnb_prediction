from datetime import date, timedelta, datetime

import pandas as pd
import geopandas as gpd
from keplergl import KeplerGl
from flask import Flask, render_template, request

from tools.plots import treemap

import pickle


app = Flask(__name__)

data = gpd.read_file('data/total.geojson')

modelo = pickle.load(open('model/catboost_airbnb.pk', 'rb'))

mapa_config={'version': 'v1',
                 'config': {'visState': {'filters': [],
                   'layers': [{'id': '3m64kx8',
                     'type': 'geojson',
                     'config': {'dataId': 'Madrid',
                      'label': 'Madrid',
                      'color': [202, 242, 244],
                      'highlightColor': [252, 242, 26, 255],
                      'columns': {'geojson': 'geometry'},
                      'isVisible': True,
                      'visConfig': {'opacity': 0.8,
                       'strokeOpacity': 0.8,
                       'thickness': 0.5,
                       'strokeColor': [18, 92, 119],
                       'colorRange': {'name': 'Pink Wine 6',
                        'type': 'sequential',
                        'category': 'Uber',
                        'colors': ['#2C1E3D',
                         '#573660',
                         '#83537C',
                         '#A6758E',
                         '#C99DA4',
                         '#EDD1CA']},
                       'strokeColorRange': {'name': 'Global Warming',
                        'type': 'sequential',
                        'category': 'Uber',
                        'colors': ['#5A1846',
                         '#900C3F',
                         '#C70039',
                         '#E3611C',
                         '#F1920E',
                         '#FFC300']},
                       'radius': 10,
                       'sizeRange': [0, 10],
                       'radiusRange': [0, 50],
                       'heightRange': [0, 500],
                       'elevationScale': 17.4,
                       'enableElevationZoomFactor': True,
                       'stroked': True,
                       'filled': True,
                       'enable3d': True,
                       'wireframe': False},
                      'hidden': False,
                      'textLabel': [{'field': None,
                        'color': [255, 255, 255],
                        'size': 18,
                        'offset': [0, 0],
                        'anchor': 'start',
                        'alignment': 'center'}]},
                     'visualChannels': {'colorField': {'name': 'avg_price', 'type': 'real'},
                      'colorScale': 'quantile',
                      'strokeColorField': None,
                      'strokeColorScale': 'quantile',
                      'sizeField': None,
                      'sizeScale': 'linear',
                      'heightField': {'name': 'avg_price', 'type': 'real'},
                      'heightScale': 'linear',
                      'radiusField': None,
                      'radiusScale': 'linear'}}],
                   'interactionConfig': {'tooltip': {'fieldsToShow': {'Madrid': [{'name': 'neighbourhood',
                        'format': None},
                       {'name': 'avg_price', 'format': None},
                       {'name': 'count_', 'format': None}]},
                     'compareMode': False,
                     'compareType': 'absolute',
                     'enabled': True},
                    'brush': {'size': 0.5, 'enabled': False},
                    'geocoder': {'enabled': False},
                    'coordinate': {'enabled': False}},
                   'layerBlending': 'normal',
                   'splitMaps': [],
                   'animationConfig': {'currentTime': None, 'speed': 1}},
                  'mapState': {'bearing': 3.2660550458715605,
                   'dragRotate': True,
                   'latitude': 40.418132280553976,
                   'longitude': -3.6675547392865,
                   'pitch': 52.053764006523224,
                   'zoom': 10.524764239108396,
                   'isSplit': False},
                  'mapStyle': {'styleType': 'satellite',
                   'topLayerGroups': {},
                   'visibleLayerGroups': {},
                   'threeDBuildingColor': [3.7245996603793508,
                    6.518049405663864,
                    13.036098811327728],
                   'mapStyles': {}}}}
                


@app.route('/', methods=['POST', 'GET'])
def dashboard():

    cuantos = int(data.count_.sum())  # airbnbs en madrid
    precio = round(data.avg_price.mean(), 2)  # precio medio
    camas = int(data.beds.sum())  # plazas medias por airbnb
    hosts = int(data.superhosts.sum())   # total de superhost en madrid

    graph = treemap(data)

    return render_template('dashboard.html',
                           n_companies=cuantos,
                           average_daily_jobs=camas,
                           salaries=precio,
                           hosts = hosts,
                           graphJSON=graph)


@app.route('/prediccion/', methods=['POST', 'GET'])
def prediccion():

    row_data = {'accommodates': 2.0,
                'air_conditioning': 0.0,
                'availability_30': 22.0,
                'availability_365': 82.0,
                'availability_60': 52.0,
                'availability_90': 82.0,
                'bathrooms': 1.0,
                'bedrooms': 1.0,
                'beds': 0.0,
                'calculated_host_listings_count': 1.0,
                'calculated_host_listings_count_entire_homes': 0.0,
                'calculated_host_listings_count_private_rooms': 1.0,
                'calculated_host_listings_count_shared_rooms': 0.0,
                'cleaning_fee': 5.0,
                'dishwasher': 0.0,
                'extra_people': 15.0,
                'guests_included': 2.0,
                'latitude': 40.45627975463867,
                'longitude': -3.6776299476623535,
                'maximum_nights': 365.0,
                'minimum_nights': 1.0,
                'number_of_reviews': 73.0,
                'number_of_reviews_ltm': 14.0,
                'room_type_private_room': 0.0,
                'room_type_shared_room': 0.0,
                'security_deposit': 0.0}


    if request.method == 'POST':

        camas = request.form['camas']
        habitas = request.form['habitas']
        deposito = request.form['deposito']

        row_data['beds'] = int(camas)
        row_data['bedrooms'] = int(habitas)
        row_data['security_deposit'] = float(deposito)

        y_pred = modelo.predict(list(row_data.values()))

        return render_template('prediccion.html', camas=camas, habitas=habitas, deposito=deposito, precio=round(y_pred, 2))

    else:

        return render_template('prediccion.html', camas=1, habitas=1, deposito=20, precio=0)


@app.route('/market_info/', methods=['POST', 'GET'])
def market_info():


    mapa=KeplerGl(height=600, width=800, config=mapa_config)  

    mapa.add_data(data.copy(), 'Madrid')  

    mapa.save_to_html(file_name='static/mapa/mapa.html')  

    
    
    return render_template('market.html')



if __name__ == '__main__':
    app.run(debug=True)

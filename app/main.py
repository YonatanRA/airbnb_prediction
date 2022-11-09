import geopandas as gpd
from keplergl import KeplerGl
from flask import Flask, render_template, request

from tools.plots import treemap
from tools.config import mapa_config

import pickle
import os

app = Flask(__name__)


PATH=os.path.dirname(os.path.abspath(__file__))


data = gpd.read_file(PATH + '/data/total.geojson')
modelo = pickle.load(open(PATH + '/model/catboost_airbnb.pk', 'rb'))


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

    mapa.save_to_html(file_name=PATH + '/static/mapa/mapa.html')

    return render_template('market.html')



if __name__ == '__main__':
    app.run(debug=True)

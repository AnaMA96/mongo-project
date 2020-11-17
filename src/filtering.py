import json, requests, os, math, folium
from geopy.distance import geodesic

def sum_funding(funding_rounds):
    '''
    Esta función recibe como parámetro los datos de la columna funding_rounds y obtiene
    el total de dinero intertido en financiación en USD.
    '''
    currency_dict = {"USD":1, "EUR":1.09, "GBP":1.29, "CAD":0.75, "SEK":0.1, "JPY":0.0091}
    result = []
    for e in funding_rounds:
        result.append(sum([0 if k["raised_amount"] == None else k["raised_amount"]*currency_dict[k["raised_currency_code"]] for k in e if "raised_amount" in k.keys() and "raised_currency_code" in k.keys()]))
    return result

def toGeoJson(lat,lng):
    '''
    Esta función recibe la latitud y la longitud de cada oficina, comprueba que no haya NaN y las devuelve en un 
    diccionario de tipo Point para poder trabajar desde MongoDB.
    '''
    lat = float(lat)
    lng = float(lng)
    if not math.isnan(lat) and not math.isnan(lng):
        return {
            "type":"Point",
            "coordinates":[lng,lat]
            }

def meters_between_coordinates(first_lat, first_lon, second_lat, second_lon):
    return geodesic((first_lat, first_lon), (second_lat, second_lon)).meters
from dotenv import load_dotenv
load_dotenv()
import os
apik = os.getenv('google')
import requests
import src.filtering as fl

apiKey = os.getenv("google")

def latlong(office):
    '''
    Obtiene la latitud y la longitud para poder usar la API de Google. Recibe como parámetro cada oficina.
    '''
    return str(office['location']['coordinates'][::-1]).replace(' ', '')[1:-1]

def get_google(latlong, radius,typ, apiKey, keyw=None):
    '''
    Realiza la request a la API de Google places con los parámetros que se le indiquen: latitud y longitud obtenidas
    a través de la función anterior "latlong" y el typ, apikey y una keyword que ayuda a complementar
    la búsqueda para que sea más precisa.
    '''
    keyword= '&keyword='+keyw if keyw else ''
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latlong}&radius={radius}&type={typ}{keyword}&key={apiKey}'
    res = requests.get(url)
    return res.json()['results']

def fill_nearest_places(offices_list):
    '''
    Esta función realiza llamadas a la API de google para obtener de cada una de las oficinas recogidas en la lista que
    se le pasa como parámetro los servicios más cercanos indicados en cada llamada, con el radio que se especifica.
    Posteriormente mide la longitud de la lista obtenida de modo que refleja, por cada oficina la cantidad de servicios especificados
    que hay dentro del radio marcado.
    '''
    for office in offices_list:
        airports_nearby = get_google(latlong(office), radius=2000, typ='airport', apiKey=apiKey, keyw='international')
        office["airports_2km"] = len(airports_nearby)
        
        primary_schools_nearby = get_google(latlong(office), radius=1000, typ='primary_school', apiKey=apiKey)
        office["primary_schools_1km"] = len(primary_schools_nearby)
        
        night_clubs_nearby = get_google(latlong(office), radius=1000, typ='night_club', apiKey=apiKey)
        office["night_clubs_1km"] = len(night_clubs_nearby)
        
        starbucks_nearby = get_google(latlong(office), radius=500, typ='cafe', apiKey=apiKey, keyw='starbucks')
        office["starbucks_500m"] = len(starbucks_nearby)
    
    return offices_list
        
def nearest_place(longitude, latitude, pet_services):
    '''
    Esta función recibe como parámetros la latitud y la longitud de una oficina, la lista con los locales
    de servicios para mascotas y sus localizaciones y obtiene el local más cercano a cada oficina.
    '''

    min_distance = None
    nearest_pet_service = None
    for pet_service in pet_services:
        coordinates = pet_service["location"]["coordinates"]
        distance_in_meters = fl.meters_between_coordinates(latitude, longitude, coordinates[1], coordinates[0])
        if not min_distance:
            min_distance = distance_in_meters
            nearest_pet_service = pet_service
        elif distance_in_meters < min_distance:
            min_distance = distance_in_meters
            nearest_pet_service = pet_service
    
    if nearest_pet_service:
        return {"name": nearest_pet_service["nombre"], 
        "location": nearest_pet_service["location"]["coordinates"], 
        "meters_to_office": min_distance}
    else:
        return {}


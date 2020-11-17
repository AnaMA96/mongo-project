def obtain_geoquery(coordinates, maxDistance=2000,minDistance=0):
    """
    Esta función realiza una geoquery a partir de las coordenadas que se le pasen como argumento
    con un radio por defecto de 2000 metros y una distancia mínima de 0 metros.

    """
    print(coordinates)
    my_location = {"type": "Point", "coordinates": coordinates}
    return {
        "location": {
         "$near": {
           "$geometry": my_location,
           "$maxDistance": maxDistance,
           "$minDistance": minDistance
         }
       }
    }
  
def find_pet_services(db, coordinates):
    '''
    Esta función encuentra los locales de servicios para mascotas más cercanos a las coordenadas que se le pasen.
    '''
    geo_query = obtain_geoquery(coordinates, maxDistance=4000)
    print(geo_query)
    return list(db['pet_services'].find(geo_query))
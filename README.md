# 🗺 ¿Dónde pongo mi oficina?🏢

![](https://elefantesenbicicleta.com/wp-content/uploads/2018/01/tintin_mundo.jpg)

Como empresa recién llegada a la industria de los videojuegos, necesitamos decidir dónde ponemos nuestra oficina.

## ¿Qué stack de teconologías voy a utilizar?

En este proyecto utilizo una base de datos llamada "Companies" formada por oficinas de las cuales encontramos información como: nombre, latitud, longitud, ciudad, país...etc. De esta bbdd obtengo información acerca de dichas oficinas mediante queries y geoqueries que complemento con las APIs de [Google Places](https://cloud.google.com/maps-platform/places/?hl=es&utm_source=google&utm_medium=cpc&utm_campaign=FY18-Q2-global-demandgen-paidsearchonnetworkhouseads-cs-maps_contactsal_saf&utm_content=text-ad-none-none-DEV_c-CRE_436338821277-ADGP_Hybrid%20%7C%20AW%20SEM%20%7C%20BKWS%20~%20Places%20%7C%20EXA%20%7C%20Google%20Maps%20Places%20API-KWID_43700051585713668-aud-599078372864%3Akwd-22859391737-userloc_1005493&utm_term=KW_google%20places%20api-ST_google%20places%20api&gclid=Cj0KCQiA48j9BRC-ARIsAMQu3WQaf_bwuj-2dxUFXixCeaM7ycBwiBgY0p3dqrqg4zpg2povN-h0cK0aAlDZEALw_wcB) y [FourSquare](https://developer.foursquare.com) que, mediante llamadas me permiten obtener más información acerca de las localizaciones de los lugares que nos interesan para situar nuestra oficina.

Además, trabajo con GeoDataFrames y utilizo la librería [Folium](https://python-visualization.github.io/folium/) para visualizar las conclusiones obtenidas en un mapa.

## ¿Qué conclusiones?¿Con qué nos hemos ido guiando?
Bien, a la hora de ver dónde situar la oficina de la empresa había que atender una serie de una requisitos, o parte de ellos, para que la plantilla se sintiese a gusto. El listado requisitos es el siguiente (destacando en negrita los elegidos para el desarrollo del proyecto):

- A los diseñadores les gusta ir a charlas de diseño y compartir conocimientos. Debe haber algunas empresas cercanas que también diseñen.

- **El 30% del personal de la empresa tiene al menos 1 hijo.**

- A los desarrolladores les gusta estar cerca de nuevas empresas tecnológicas exitosas que hayan recaudado al menos 1 millón de dólares.

- **A los ejecutivos les gusta mucho Starbucks. Asegúrese de que haya un Starbucks no muy lejos.**

- **Los gerentes de cuentas necesitan viajar mucho, por lo que necesitan un eropuerto cerca**

- **Todos en la empresa tienen entre 25 y 40 años, dales un lugar para ir de fiesta.**

- El CEO es vegano.

- Si quieres hacer feliz al encargado de mantenimiento, un estadio de baloncesto debe estar a unos 10 km.

- **El perro de la oficina: "Pepe" necesita un peluquero todos los meses. Asegúrese de que haya uno no demasiado lejos.**


## Por favor, para poder ver bien el mapa final y el trabajo realizado con la librería Folium, abre el .ipynb correspondiente "4.  Folium" desde aquí:
**[Ver Jupyter Notebook: "4. Folium"](https://nbviewer.jupyter.org/github/AnaMA96/mongo-project/blob/main/4.%20%20%20Folium.ipynb)**
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geolocator = Nominatim(user_agent="DRY7122App")

def calcular_distancia(ciudad_origen, ciudad_destino):
    try:
        origen = geolocator.geocode(ciudad_origen + ", Chile")
        destino = geolocator.geocode(ciudad_destino + ", Argentina")
        if not origen or not destino:
            print("No se pudo encontrar una o ambas ciudades.")
            return

        coord_origen = (origen.latitude, origen.longitude)
        coord_destino = (destino.latitude, destino.longitude)

        distancia_km = geodesic(coord_origen, coord_destino).km
        distancia_millas = geodesic(coord_origen, coord_destino).miles
        duracion_horas = distancia_km / 80  # Asumiendo 80 km/h promedio

        print("\n----- Resultado del viaje -----")
        print(f"Desde: {ciudad_origen} (Chile)")
        print(f"Hasta: {ciudad_destino} (Argentina)")
        print(f"Distancia: {distancia_km:.2f} km | {distancia_millas:.2f} millas")
        print(f"Duración estimada: {duracion_horas:.2f} horas a 80 km/h")
        print(f"Narrativa: El viaje comienza en {ciudad_origen}, cruzando la cordillera hacia {ciudad_destino}.\n")
    except Exception as e:
        print(f"Error al calcular distancia: {e}")

while True:
    print("Ingrese 's' en cualquier momento para salir.\n")
    origen = input("Ciudad de Origen (Chile): ")
    if origen.lower() == "s":
        break
    destino = input("Ciudad de Destino (Argentina): ")
    if destino.lower() == "s":
        break

    print("Seleccione medio de transporte:")
    print("1) Auto\n2) Bus\n3) Avión")
    transporte = input("Opción (1/2/3): ")
    if transporte.lower() == "s":
        break

    medios = {"1": "Auto", "2": "Bus", "3": "Avión"}
    medio = medios.get(transporte, "Desconocido")

    print(f"\nMedio de transporte seleccionado: {medio}")
    calcular_distancia(origen, destino)

import time

from geopy.geocoders import Nominatim
from geopy import distance

app = Nominatim(user_agent="location_chauffeur")


def trouver_adresse_depuis_coordonnees(latitude, longitude, langue="fr"):
    """fonction permettant de trouver l'adresse d'un lieu à partir
    de la latitude et la longitude"""
    coord = f"{latitude}, {longitude}"
    time.sleep(1)
    try:
        return app.reverse(coord, language=langue).raw
    except AttributeError:
        return trouver_adresse_depuis_coordonnees(latitude, longitude)


def trouver_coordonnees_depuis_adresse(adresse):
    """fonction permettant de trouver la latitude et la longitude d'un
         lieu ou d'une adresse"""
    time.sleep(1)
    try:
        return app.geocode(adresse).raw
    except AttributeError:
        print("Error")
        return trouver_coordonnees_depuis_adresse(adresse)


def calculer_distance(point_a, point_b):
    """fonction permettant de calculer la distance séparant deux lieux"""
    time.sleep(1)
    try:
        return distance.distance(point_a, point_b)
    except AttributeError:
        return calculer_distance(point_a, point_b)


def distance_la_plus_courte(point_a, conducteurs):
    """fonction qui renvoie un tableau trié de distances séparant un lieu
    d'ensemble d'autres lieux différents."""
    distances = []
    for conducteur in conducteurs:
        point_b = (
            conducteur["localisation"]["latitude"],
            conducteur["localisation"]["longitude"]
        )
        distance_ = calculer_distance(point_a, point_b)
        objet = {
            "id": conducteur["id_conducteur"],
            "distance": distance_
        }
        distances.append(objet)
    distances.sort(key=lambda x: x['distance'])
    return distances

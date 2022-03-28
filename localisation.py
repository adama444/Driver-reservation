import time

from geopy.geocoders import Nominatim
from geopy import distance

app = Nominatim(user_agent="location_chauffeur")


def trouver_adresse_depuis_coordonnees(latitude, longitude, langue="fr"):
    coord = f"{latitude}, {longitude}"
    time.sleep(1)
    try:
        return app.reverse(coord, language=langue).raw
    except:
        return trouver_adresse_depuis_coordonnees(latitude, longitude)


def trouver_coordonnees_depuis_adresse(adresse):
    time.sleep(1)
    try:
        return app.geocode(adresse).raw
    except:
        return trouver_coordonnees_depuis_adresse(adresse)


def calculer_distance(point_a, point_b):
    time.sleep(1)
    try:
        return distance.distance(point_a, point_b)
    except:
        return calculer_distance(point_a, point_b)


def distance_la_plus_courte(point_a, conducteurs):
    distances = []
    for conducteur in conducteurs:
        point_b = (conducteur["localisation"]["latitude"],
                   conducteur["localisation"]["longitude"])
        distance_ = calculer_distance(point_a, point_b)
        objet = {"id": conducteur["id"], "distance": distance_}
        distances.append(objet)
    distances.sort()
    return distances

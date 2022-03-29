import json

import conducteur
import localisation
import mail
from utilisateur import Utilisateur


class Client(Utilisateur):
    def __init__(self,
                 id_client, prenom, nom, sexe,
                 numero_telephone, mail, mot_de_passe, age,
                 profession, localisation, est_marie, nombre_enfants=0):
        super().__init__(
            id_client, prenom, nom,
            sexe, numero_telephone, mail, mot_de_passe, age, profession, localisation)
        self.est_marie = est_marie
        self.nombre_enfants = nombre_enfants

    def dict(self):
        dictionaire = {
            "id_client": self.id_utilisateur,
            "prenom": self.prenom,
            "nom": self.nom,
            "sexe": self.sexe,
            "numero_telephone": self.numero_telephone,
            "mail": self.mail,
            "mot_de_passe": self.mot_de_passe,
            "age": self.age,
            "profession": self.profession,
            "localisation": {
                "latitude": self.localisation[0],
                "longitude": self.localisation[1]
            },
            "est_marie": self.est_marie,
            "nombre_enfants": self.nombre_enfants
        }
        return dictionaire


def ajouter_client(client):
    with open('database.json', 'r+') as file:
        base_de_donnees = json.load(file)
        non_vide = len(base_de_donnees['clients']) == 1
        if client.id_utilisateur is None and non_vide:
            client.id_utilisateur = int(base_de_donnees['clients'][-1]["id_client"]) + 1
        else:
            client.id_utilisateur = 1
        base_de_donnees['clients'].append(client.dict())
        file.seek(0)
        json.dump(base_de_donnees, file)
    return True


def trouver_client(mail, mot_de_passe):
    existe = False
    with open('database.json', 'r') as file:
        base_de_donnees = json.load(file)
        for user in base_de_donnees['clients']:
            if user["mail"] == mail and user['mot_de_passe'] == mot_de_passe:
                print('connecter avec succès')
                existe = True
    return existe


def liste_clients():
    clients = []
    with open('database.json', 'r') as file:
        base_de_donnees = json.load(file)
        for client in base_de_donnees['clients']:
            clients.append(client)
    return clients


def donner_client(id_client):
    with open('database.json', 'r') as file:
        base_de_donnees = json.load(file)
        client = None
        for user in base_de_donnees['clients']:
            if user["id_client"] == id_client:
                client = user
    return client


def rechercher_conducteur(client):
    liste_conducteurs = conducteur.liste_conducteurs()
    point_a = (client["localisation"]['latitude'], client["localisation"]['longitude'])
    liste_distances = localisation.distance_la_plus_courte(point_a, liste_conducteurs)
    liste_conducteurs_proches = []
    for conducteur_ in liste_conducteurs:
        if conducteur_["id_conducteur"] == liste_distances[0]["id"]:
            liste_conducteurs_proches.append(conducteur_)
    conducteur_selectionne = liste_conducteurs_proches[0]
    mail.envoyer_mail("as91404togo@gmail.com", conducteur_selectionne)

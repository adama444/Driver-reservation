import json

from utilisateur import Utilisateur


class Conducteur(Utilisateur):
    def __init__(self,
                 id_conducteur, prenom, nom, sexe,
                 numero_telephone, mail, mot_de_passe,
                 age, profession, localisation, numero_permis,
                 annee_experience, disponibilite,
                 categorie_permis):
        super().__init__(
            id_conducteur, prenom,
            nom, sexe,
            numero_telephone, mail,
            mot_de_passe, age, profession, localisation)
        self.numero_permis = numero_permis
        self.annee_experience = annee_experience
        self.disponibilite = disponibilite
        self.categorie_permis = categorie_permis

    def dict(self):
        dictionaire = {
            "id_conducteur": self.id_utilisateur,
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
            "numero_permis": self.numero_permis,
            "annee_experience": self.annee_experience,
            "disponibilite": {
                "de": self.disponibilite[0],
                "a": self.disponibilite[1]
            },
            "categorie_permis": self.categorie_permis
        }
        return dictionaire


def ajouter_conducteur(conducteur):
    """ fonction pour l'ajout d'un nouveau conducteur dans la base de données JSON """
    with open('database.json', 'r+') as file:
        base_de_donnees = json.load(file)
        non_vide = len(base_de_donnees['conducteurs']) == 1
        if conducteur.id_utilisateur is None and non_vide:
            conducteur.id_utilisateur = int(base_de_donnees['conducteurs'][-1]["id_conducteur"]) + 1
        else:
            conducteur.id_utilisateur = 1
        base_de_donnees['conducteurs'].append(conducteur.dict())
        file.seek(0)
        json.dump(base_de_donnees, file)
    return True


def trouver_conducteur(mail, mot_de_passe):
    """ fonction qui cherche un conducteur ayant un mail et un mot de passe """
    existe = False
    with open('database.json', 'r') as file:
        base_de_donnees = json.load(file)
        for user in base_de_donnees['conducteurs']:
            if user["mail"] == mail and user['mot_de_passe'] == mot_de_passe:
                print('connecter avec succès')
                existe = True
    return existe


def liste_conducteurs():
    conducteurs = []
    with open('database.json', 'r') as file:
        base_de_donnees = json.load(file)
        for conducteur in base_de_donnees['conducteurs']:
            conducteurs.append(conducteur)
    return conducteurs


def donner_conducteur(id_conducteur):
    with open('database.json', 'r') as file:
        base_de_donnees = json.load(file)
        client = base_de_donnees['conducteurs'][id_conducteur]
    return client

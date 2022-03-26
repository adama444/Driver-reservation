import json

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
            "localisation": self.localisation,
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

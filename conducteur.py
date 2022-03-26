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
            "localisation": self.localisation,
            "numero_permis": self.numero_permis,
            "annee_experience": self.annee_experience,
            "disponibilite": self.disponibilite,
            "categorie_permis": self.categorie_permis
        }
        return dictionaire


def ajouter_conducteur(conducteur):
    with open('database.json', 'r+') as file:
        base_de_donnees = json.load(file)
        non_vide = len(base_de_donnees['conducteurs']) == 1 and \
                   base_de_donnees['conducteurs'][-1]["id_utilisateur"] >= 1
        if conducteur.id_utilisateur is None and non_vide:
            conducteur.id_utilisateur += base_de_donnees['conducteurs'][-1]["id_utilisateur"]
        else:
            conducteur.id_utilisateur = 1
        base_de_donnees['conducteurs'].append(conducteur.dict())
        file.seek(0)
        json.dump(base_de_donnees, file)
    return True

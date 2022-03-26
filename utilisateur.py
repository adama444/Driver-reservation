class Utilisateur:
    def __init__(self,
                 id_utilisateur, prenom, nom,
                 sexe, numero_telephone,
                 mail, mot_de_passe, age,
                 profession, localisation):
        self.id_utilisateur = id_utilisateur
        self.prenom = prenom
        self.nom = nom
        self.sexe = sexe
        self.mot_de_passe = mot_de_passe
        self.numero_telephone = numero_telephone
        self.mail = mail
        self.age = age
        self.profession = profession
        self.localisation = localisation

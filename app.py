import json

import client
import conducteur
import localisation
import mail

""" programme principal """
print("initialisation ...")


def connecter():
    """ fonction pour la connexion d'un utilisateur """
    print('Connexion ...')
    mail = input("mail: ")
    mot_de_passe = input("mot de passe: ")
    if client.trouver_client(mail, mot_de_passe) or \
            conducteur.trouver_conducteur(mail, mot_de_passe):
        print("connecter avec succès !")
        return True
    else:
        print("informations incorrectes !")
        return False


def creer_compte():
    """ fonction pour la création d'un compte """
    print("Création d'un nouveau compte ...")
    creer_client = input("Client ? (O/n)\n")
    if creer_client == 'O':
        prenom = input("prenom: ")
        nom = input("nom: ")
        mot_de_passe = input("mot de passe: ")
        sexe = input("sexe: ")
        numero_telephone = input("numero de telephone: ")
        mail = input("mail: ")
        age = input("age: ")
        profession = input("profession: ")
        localisation = (
            input("localisation [latitude]: "),
            input("localisation [longitude]: ")
        )
        est_marie = input("Etes vous marié ? (O/n)\n")
        nombre_enfants = 0
        if est_marie == 'O':
            nombre_enfants = input("nombre d'enfants: ")
        nouveau_client = client.Client(None,
                                       prenom,
                                       nom,
                                       sexe,
                                       numero_telephone,
                                       mail,
                                       mot_de_passe,
                                       age,
                                       profession,
                                       localisation,
                                       est_marie,
                                       nombre_enfants)
        client.ajouter_client(nouveau_client)
        print("client crée avec succès !")
    else:
        prenom = input("prenom: ")
        nom = input("nom: ")
        mot_de_passe = input("mot de passe: ")
        sexe = input("sexe: ")
        numero_telephone = input("numero de telephone: ")
        mail = input("mail: ")
        age = input("age: ")
        profession = input("profession: ")
        localisation = (
            input("localisation [latitude]: "),
            input("localisation [longitude]: ")
        )

        numero_permis = input("numéro du permis: ")
        annee_experience = input("année d'expériences: ")
        disponibilite = (
            input("disponibilité [de]: "),
            input("disponibilité [a]: ")
        )
        categorie_permis = input("catégorie de permis: ")
        nouveau_conducteur = conducteur.Conducteur(None,
                                                   prenom,
                                                   nom,
                                                   sexe,
                                                   numero_telephone,
                                                   mail,
                                                   mot_de_passe,
                                                   age,
                                                   profession,
                                                   localisation,
                                                   numero_permis,
                                                   annee_experience,
                                                   disponibilite,
                                                   categorie_permis)
        conducteur.ajouter_conducteur(nouveau_conducteur)
        print("conducteur crée avec succès !")


# fil d'exécution principale
autoriser = False
if str.lower(input("se connecter ? (O/n)\n")) == 'n':
    creer_compte()
else:
    autoriser = connecter()

if autoriser:
    client.rechercher_conducteur(client.donner_client(1))
    # print(localisation.trouver_coordonnees_depuis_adresse("UCAO-UUT"))
    # print(localisation.trouver_adresse_depuis_coordonnees(6.2308526, 1.1015976053714729))
    # print(mail.envoyer_mail("as91404togo@gmail.com", "ultime test"))




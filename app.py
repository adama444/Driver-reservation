import json

import client
import conducteur

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
        localisation = input("localisation: ")
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
        localisation = input("localisation: ")
        numero_permis = input("numéro du permis: ")
        annee_experience = input("année d'expériences: ")
        disponibilite = input("disponibilité: ")
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


def afficher_menu():
    print("1 - afficher la liste des conducteurs")
    print("2 - afficher la liste des clients")
    print("3 - réserver un conducteur")
    print("4 - se déconnecter")


# fil d'exécution principale
autoriser = False
if str.lower(input("se connecter ? (O/n)\n")) == 'n':
    creer_compte()
else:
    autoriser = connecter()

if autoriser:
    afficher_menu()

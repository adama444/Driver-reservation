import json

import client
import conducteur

print("initialisation ...")


def connecter():
    print('Connexion ...')
    mail = input("mail: ")
    mot_de_passe = input("mot de passe: ")

    with open('database.json', 'r') as file:
        base_de_donnees = json.load(file)
        valider_mail = mail in base_de_donnees['clients'].items() or \
                       mail in base_de_donnees['clients'].items()
        valider_mot_de_passe = mot_de_passe in base_de_donnees['clients'].items() or \
                       mot_de_passe in base_de_donnees['clients'].items()
        if valider_mail and valider_mot_de_passe:
            print('connecter avec succès')



def creer_compte():
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


if input("se connecter ? (O/n)\n") == 'O':
    connecter()
else:
    creer_compte()

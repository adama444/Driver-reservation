import smtplib

serveur = smtplib.SMTP_SSL('smtp.gmail.com', 465)
serveur_mail = "technopova2002@gmail.com"
serveur_mot_de_passe = "AStechnopova2002@gmail.com"


def envoyer_mail(mail_destinataire, conducteur_):
    """cette manière d'envoyer un mail n'est pas du tout conseiller.
    Mais dans un contexte pédagogique nous nous le permettons"""
    serveur.login(serveur_mail, serveur_mot_de_passe)
    est_envoye = False
    try:
        serveur.sendmail(serveur_mail, mail_destinataire, produire_message(conducteur_).encode("UTF-8"))
        est_envoye = True
    except ConnectionError:
        print("error")
    serveur.quit()
    return est_envoye


def produire_message(conducteur_):
    """fonction qui formate le mail avant l'envoi"""
    message_final = "Subject: API Reservation conducteur.\n\n"
    message_final += "Nous avons trouver pour vous un conducteur qui est " \
                     "le plus proche de votre position. Voici ces coordonnées.\n\n"
    message_final += "Conducteur: "
    message_final += conducteur_["nom"] + " " + conducteur_["prenom"]
    message_final += "\n Mail: " + conducteur_["mail"]
    message_final += "\n Numéro de téléphone: " + conducteur_["numero_telephone"]
    return message_final

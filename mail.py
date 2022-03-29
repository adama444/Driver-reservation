import smtplib

serveur = smtplib.SMTP_SSL('smtp.gmail.com', 465)
serveur_mail = "technopova2002@gmail.com"
serveur_mot_de_passe = "AStechnopova2002@gmail.com"


def envoyer_mail(mail_destinataire, message):
    """cette manière d'envoyer un mail n'est pas du tout conseiller.
    Mais dans un contexte pédagogique nous nous le permettons"""
    serveur.login(serveur_mail, serveur_mot_de_passe)
    est_envoye = False
    try:
        serveur.sendmail(serveur_mail, mail_destinataire, produire_message(message))
        est_envoye = True
    except ConnectionError:
        print("error")
    serveur.quit()
    return est_envoye


def produire_message(message):
    """fonction qui formate le mail avant l'envoi"""
    message_final = "Subject: API Reservation conducteur.\n\n"
    message_final += message
    return message_final

import smtplib

serveur = smtplib.SMTP_SSL('smtp.gmail.com', 465)
serveur_mail = "technopova2002@gmail.com"
serveur_mot_de_passe = ""
serveur.login(serveur_mail, serveur_mot_de_passe)


def envoyer_mail(mail_destinataire, message):
    est_envoye = False
    if serveur.sendmail(serveur_mail, mail_destinataire, message):
        est_envoye = True
    serveur.quit()
    return est_envoye


def produire_message():
    message = ""
    return message
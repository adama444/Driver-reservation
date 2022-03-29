# Location-de-conducteur
## Description
Le but du projet est de concevoir une api en python permettant de trouver pour un client en fonction de sa position le conducteur le plus proche pour qu'il puisse effectuer ses courses.

## Prerequis

- Installer *Python 3.10+*
- Installer *geopy*

## Fonctionnalités

- Création de compte Client et Conducteur dont les informations seront stockées dans un fichier JSON nommé *database.json*
- Recherche d'un conducteur en fonction de la distance qui lui sépare du client
- Envoi d'un mail au client dès qu'un conducteur est trouvé

## Fonctionnalités futures

- Filtrer la recherche en fonction de la disponibilité du conducteur et celui du client qui effectue la recherche
- Permettre aux conducteurs de définir leur préférence quant aux voitures qu'ils aiment conduire  

## Comment utiliser le projet

- Le module *mail.py* gère la gestion de l'envoi des emails aux clients
- Le module *client.py* contient la classe Client et les différents cas d'utilisations d'un client
- Le module *app.py* est le module où les tests ont été effectuer. C'est la porte d'entrée principale du projet

## Contributeurs

Nous remercions tous ceux grâce à qui ce projet a su se developer pour leurs contributions et leurs efforts :
- [@Sena APEKE](apekekodjo@gmail.com)
- [@Jean-Gael AMEGANVI](willialfred24@gmail.com)
- [@Jean-Pierre MINLEKIBE](jpminlekibe@gmail.com)
- [@Junior GBODJO](juniorgbodjo@gmail.com)

## Remerciements

Merci aux initiateurs, auteurs du projets pour leurs idées et leur collaboration :
- [@Adama SAMAKE](adama.samake.work@gmail.com)
- [@Ghaffar KORIKO](korikoghaffar@gmail.com)

Description :
Ce projet contient un script Python simple qui permet de récupérer l'en-tête ETag d'une ressource web en effectuant une requête HTTP GET. L'en-tête ETag est souvent utilisé pour gérer la mise en cache des ressources côté client (dans le navigateur) et côté serveur (sur le serveur web). Ce script peut être utile pour suivre des ressources spécifiques sur un serveur web et déterminer si elles ont été modifiées depuis la dernière requête.

Fonctionnalités :

Effectue une requête HTTP GET à une URL spécifiée.
Valide le code d'état de la réponse pour s'assurer que la requête a réussi.
Récupère l'en-tête ETag de la réponse, s'il est présent.
Affiche l'ETag ou indique qu'aucun en-tête ETag n'a été trouvé.
Utilisation :
Pour utiliser ce script, vous devez spécifier l'URL de la ressource que vous souhaitez interroger en modifiant la variable url dans le script. Après avoir configuré l'URL, exécutez le script, et il vous affichera l'ETag de la ressource, s'il est disponible.

Avertissement :
L'utilisation de ce script peut entraîner des requêtes HTTP non sécurisées si la vérification du certificat SSL est désactivée. Veillez à utiliser ce script de manière responsable et à respecter les règles et politiques du serveur que vous interrogez.

N'hésitez pas à personnaliser cette description en fonction de votre projet et de ses objectifs spécifiques. Assurez-vous également de fournir des informations complémentaires, telles que des exemples d'utilisation, des captures d'écran, des instructions d'installation, etc., pour rendre votre projet plus accessible aux utilisateurs potentiels sur GitHub.

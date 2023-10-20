#!/usr/bin/env python3

import requests

url = "https://stelycube.fr/p/les-packs"  # Remplacez l'URL par celle de la ressource que vous souhaitez interroger.

# Effectuer une requête HTTP GET pour obtenir la ressource et ses en-têtes
response = requests.get(url, verify=False)


# Vérifier si la requête a réussi
if response.status_code == 200:
    # L'en-tête ETag est accessible via le dictionnaire des en-têtes de la réponse
    etag = response.headers.get("ETag")
    if etag:
        print(f"ETag de la ressource : {etag}")
    else:
        print("Aucun en-tête ETag trouvé.")
else:
    print(f"La requête a échoué avec le code d'état {response.status_code}")

import requests

def envoyer_pub_vers_sites(lien_youtube, sites_pub):
    """
    Envoie un lien publicitaire vers plusieurs sites web via leurs formulaires ou API.
    
    Args:
    - lien_youtube (str): Lien vers votre chaîne YouTube ou vidéo.
    - sites (dict): Un dictionnaire où les clés sont les noms des sites et les valeurs sont les URLs des formulaires ou API.
    
    Returns:
    - dict: Un dictionnaire avec les résultats des requêtes pour chaque site.
    """
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; Python script)',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    # Résultat pour chaque site
    resultats = {}
    
    for site, url in sites_pub.items():
        try:
            # Les données peuvent varier selon les sites
            data = {
                'message': f"Découvrez ma chaîne YouTube ici: {lien_youtube}"
            }
            
            response = requests.post(url, data=data, headers=headers)
            
            if response.status_code == 200:
                resultats[site] = "Lien envoyé avec succès"
            else:
                resultats[site] = f"Erreur {response.status_code}"
        
        except Exception as e:
            resultats[site] = f"Erreur: {str(e)}"
    
    return resultats

# Utilisation
sites_pub = {
    'Reddit': 'https://www.reddit.com/api/submit_post',  # Exemple fictif
    'Twitter': 'https://api.twitter.com/2/tweets',       # Exemple fictif
    'Facebook': 'https://www.facebook.com/post_api'      # Exemple fictif
}

lien_youtube = 'https://www.youtube.com/@foleykant01'
resultats = envoyer_pub_vers_sites(lien_youtube, sites_pub)


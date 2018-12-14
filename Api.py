###########
# IMPORTS #
###########

import requests

# url va me servir de changer de page dans la boucle while
url = "https://swapi.co/api/people/"

# Quand il n'y a plus de "page suivante", la page "next" sera egale a None
# Donc, je boucle sur url tant qu'elle n'est egale a None :)
while url is not None:
	print("")

	############################
	# RÉCUPÉRATION DES DONNÉES #
	############################

	# Je fais la requête sur la page en cours, et je recupere la data
	r = requests.get(url)
	data = r.json() 

	# C'est ici que je change l'url pour avoir la page d'apres :)
	url = data["next"]
	# Ce tableau est la liste de tous les personnages
	persosTab = data["results"]

	###########################
	# UTILISATION DES DONNÉES #
	###########################

	# Je fais ensuite une boucle qui parcourt tous les personnages
	# et qui affiche leur nom !
	for perso in persosTab:
		print(perso["name"])
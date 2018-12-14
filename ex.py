###########
# IMPORTS #
###########

import requests

# url va me servir à changer de page dans la boucle while
url = "https://swapi.co/api/people/"

print("Welcome to the Useless Star Wars Facts !")

# Quand il n'y a plus de "page suivante", la page "next" sera égale à None
# Donc, je boucle sur url tant qu'elle n'est pas égale à None :)
while url is not None:

	############################
	# RÉCUPÉRATION DES DONNÉES #
	############################

	print("")
	# Je fais la requête sur la page en cours, et je récupère la data
	r = requests.get(url)
	data = r.json() 

	# C'est ici que je change l'url pour avoir la page d'après :)
	url = data["next"]
	# Ce tableau est la liste de tous les personnages
	persosTab = data["results"]

	###########################
	# UTILISATION DES DONNÉES #
	###########################

	# Je fais ensuite une boucle qui parcourt tous les personnages
	# et qui affiche plein d'infos sur eux :)
	for perso in persosTab:
	    # Pour la planète natale, je récupère le lien fourni par l'API
	    # et je fais une requête dessus pour récupérer son nom ;)
	    homeworld = requests.get(perso["homeworld"])
	    homeworldName = homeworld.json()["name"]
		
	    # Et ici je fais un méga print qui affiche tout !
	    print(perso["name"] + " is a " + perso["eye_color"] + " eyed " + perso["gender"] 
	    	+ ", he has " + perso["hair_color"] + " hair and weighs " + perso["mass"] 
		+ ". He is from planet " + homeworldName + " ! 😘\n")
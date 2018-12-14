###########
# IMPORTS #
###########

import requests

# url va me servir à changer de page dans la boucle while
url = "https://swapi.co/api/people/"

print("Welcome to the Useless Star Wars Facts !")

# Ce tableau contient les noms de certains personnages importants de Star Wars
# qui n'apparaissent pas dans au moins 3 films, mais dont j'ai quand même envie
# d'avoir les informations
namesWeWant = ["Dooku", "Darth Maul", "Jar Jar Binks",
"Grievous", "Jango Fett", "Qui-Gon Jinn", "Lando Calrissian",
"Ackbar", "Greedo",]

# Quand il n'y a plus de "page suivante", la page "next" sera égale à None
# Donc, je boucle sur url tant qu'elle n'est pas égale à None :)
while url is not None:

	############################
	# RÉCUPÉRATION DES DONNÉES #
	############################

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
		name = perso["name"]
		
		# Si le perso en cours n'est pas un des persos du tableau namesWeWant
		# et n'apparaît pas dans au moins 3 films, on le passe et on continue
		if name not in namesWeWant:
			if len(perso["films"]) < 3:
				continue

		print("")

		# Petite condition pour Jar Jar Binks, notre Dieu à tous
		if name == "Jar Jar Binks":
			name = "The Great and Mighty Jar Jar Binks, Emperor of the World"

		# Condition spéciale qui ajoute une option au cas où cette info est inconnue
		eyes = perso["eye_color"]
		if eyes == "unknown" or eyes == "n/a":
			eyes = "no-eyed"

		# Ici, je récupère le lien de la race du perso en cours, et je fais une requête dessus
		# Si le perso en cours n'a pas de race précisée, je lui donne la race "thing"
		if len(perso["species"]) == 1:
			speciesURL = perso["species"][0]
			rSpecies = requests.get(speciesURL)
			species = rSpecies.json()["name"]
		else:
			species = "thing"

		# Petite condition spéciale pour Yoda, le plus grand des maîtres Jedi
		if species == "Yoda's species":
			species = "Jedi Master"

		# Ici, je récupere le genre du perso en cours, et lui attribue son pronom
		# Pour un homme, "He", pour une femme "she"
		# Et pour les inconnus et les hermaphrodites (comme Jabba, no fake), "It"
		gender = perso["gender"]
		if gender == "unknown" or gender == "n/a":
			gender = "It"
		elif gender == "male":
			gender = "He"
		elif gender == "female":
			gender = "She"
		elif gender == "hermaphrodite":
			gender = "It"

		# Ici, je récupère la couleur des cheveux
		hair = perso["hair_color"]
		if hair == "unknown" or hair == "n/a" or hair == "none":
			hair = "bald"
		# Petite condition spéciale pour Darth Vader, brûlé au 66e degré
		if name == "Darth Vader":
			hair = "burnt"

		# Ici, je récupère la taille en cm
		height = perso["height"]

		# Ici, je récupère le poids en kg
		mass = perso["mass"]
		if mass == "unknown":
			mass = "0"

		# Ici, je récupère la planète d'origine
		homeworld = requests.get(perso["homeworld"])
		homeworldName = homeworld.json()["name"]
		if homeworldName == "unknown":
			homeworldName = "an unknown planet"

		# Et enfin, je fais mon méga print avec toutes les infos ! :)
		print(name + " is a " + eyes + " eyed " + species + ". " 
			+ gender + " is " + height + "cm tall, weighs " + mass
			+ "kg, and has " + hair + " hair. " + gender + " comes from " + homeworldName + " ! :)")

print("")
import requests


url = "htpps://swap.co/api/people/"

print("bienvenue  dans notre exemple")


while url is not None:

	print("")

	r = requests.get(url)

	data = r.json()

	url = data["next"]

	persosTab = data["results"]

	for perso in persosTab:

		homeworld = requests.get(perso["homeworld"])
		homeworldName = homeworld.json()["name"]


		print(perso["name"] + "is a " + perso["la_couleur_des_yeux"] +  "les_yeux" + perso["genre"]
		    + ", ils sont " + perso["la_couleur_des_cheveux "] + "cheveux_et_poids" + perso["mass"]
		    + ", il_vient_de_la_planete" + homeworldName + " ! 😘\n")
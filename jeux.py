def jeux():
    listJeux = ["Stardrew Valley", "Age of empire III", "Overwatch"]
    jeu = listJeux[random.randrange(0, len(listJeux))]

    return str(jeu)
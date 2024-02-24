﻿# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define lockedin = Character('The Lock In Avatar', color="#999898")
define mc = Character("[playername]",color="#0084ff")
define eliza = Character("Elizabeth",color="#034888")

# Le jeu commence ici
label start:
    scene lock_realm

    show lock_avatar
    lockedin "Quel est ton nom inconnu au bataillon?"

    $ playername = renpy.input("Quel est ton nom compatriote?")

    if playername == "Elizabeth":
        eliza "nuh uh you're not me"
        $ playername = "Elizabeth Wannabe"

    lockedin "Bienvenu dans le locked in realm, [playername]"

    lockedin "Le lock in sont les raisons par lequelles le {b}grind se revele."

    lockedin "Seuls ceux qui sont locked in, peuvent achever leur lock in."

    lockedin "Atteindre son grind exige beaucoup de grind et une energie de sigma a toute epreuve."

    menu:
        lockedin "es-tu un hunter?"

        "oui":
            mc "Oui monsieur je suis bel et bien un hunter."
            lockedin "Que ton grind soit rempli de grind."
        "non":
            mc "Qu'est-ce un hunter? je me sens tres faible."
            lockedin "Ta sentence est d'etre la plus grande des merguez, tu me decois beaucoup futur hunter."



    return

from combat import *
import random

def ajouter_pokemon(nom, niveau, type):
    types = {'Normal': Normal, 'Feu': Feu, 'Eau': Eau, 'Terre': Terre}
    if type in types:
        p = types[type](nom, niveau)
    info = p.info()
    
    try:
        with open("pokemon.json", "r") as f:
            pokemon = json.load(f)
    except FileNotFoundError:
        pokemon = {}
    except json.decoder.JSONDecodeError:
        pokemon = {}

    if nom in pokemon:
        if info['Niveau'] >= pokemon[nom]['Niveau']:
            pokemon[nom] = info
    else:
        pokemon[nom] = info

    print('')
    print("Vous avez ajouté un nouveau pokemon : \n{} : {}".format(nom, info))
    print('')

    with open("pokemon.json", "w") as f:
        json.dump(pokemon, f)

def main():
    types = {'Normal': Normal, 'Feu': Feu, 'Eau': Eau, 'Terre': Terre}
    choix = input("Tapez \n1 pour lancer une partie,\n2 pour ajouter un pokemon,\n3 pour accéder à votre pokedex\nVotre choix : ")
    print('')
    if choix == 'q':
        print('Fermeture du jeu')
        return 'This is the end'
    
    elif choix == '1':
        print('La partie commence...')
        print('')

        try:
            with open("pokemon.json", "r") as f:
                pokemon = json.load(f)
        except FileNotFoundError:
            pokemon = {}
        except json.decoder.JSONDecodeError:
            pokemon = {}

        p1 = random.choice(list(pokemon.keys()))
        p2 = random.choice(list(pokemon.keys()))
        p2 = types[pokemon[p2]['Type']](p2, pokemon[p2]['Niveau'])

        try:
            with open('pokedex.json', 'r') as f:
                pokedex = json.load(f)
            test = True
            if pokedex == {}:
                test = False
                print('Votre pokedex est vide')
        except json.decoder.JSONDecodeError:
            test = False
            print('Votre pokedex est vide')
            print('')


        if test == False:
            print('Votre pokemon par default est {}\nVoici ces info : {}'.format(p1, pokemon[p1]))
            p1 = types[pokemon[p1]['Type']](p1, pokemon[p1]['Niveau'])
            
            info = p1.info()

            try:
                with open("pokedex.json", "r") as f:
                    pokemon = json.load(f)
            except FileNotFoundError:
                pokemon = {}
            except json.decoder.JSONDecodeError:
                pokemon = {}

            if p1.get_nom() in pokemon:
                if p1.niveau >= pokemon[nom]['Niveau']:
                    pokemon[p1.get_nom()] = info
            else:
                pokemon[p1.get_nom()] = info

            with open("pokedex.json", "w") as f:
                json.dump(pokemon, f)
            
            print('')
            print('Battez de nouveaux pokemon pour les débloquer')
            print('')
            a = input("Voulez-vous combattre avec ce pokemon ou retourner au menu principal ?\n'c' pour combattre et 'm' pour menu : ")
            print('')
            if a == 'm':
                main()
        else:
            with open('pokedex.json', 'r') as f:
                pokedex = json.load(f)

            print('Votre pokedex :')
            for i in pokedex:
                print("  {} : {}".format(i,pokedex[i]))

            p1 = input("Entrez le nom du pokemon choisi : ")
            print("{} : {}".format(p1,pokedex[p1]))
            p1 = types[pokedex[p1]['Type']](p1, pokedex[p1]['Niveau'])
        
        combat = Combat(p1,p2)
        combat.combat(p1,p2)
        main()

    elif choix == '2':
        nom = input("Entrez le nom du pokemon : ")
        niveau = input("Entrez le niveau du pokemon : ")
        type = input('Entrez le type du pokemon : ')

        if type in types:
            pokemon = types[type](nom, niveau)
        info = pokemon.info()
        ajouter_pokemon(nom, niveau, type)
        print('')
        main()
    
    elif choix == '3':
        try:
            with open('pokedex.json', 'r') as f:
                data = json.load(f)
            print("Il y a {} pokemon dans votre pokedex".format(len(data)))
            for i in data:
                print("{} : {}".format(i,data[i]))
            print('')
            main()
        except json.decoder.JSONDecodeError:
            print('Votre Pokédex est vide')
            print('')
            main()

ajouter_pokemon('Pikachu', 1, 'Normal')
ajouter_pokemon('Sandslash', 1, 'Terre')
ajouter_pokemon('Magmar', 1, 'Feu')
ajouter_pokemon('Magikarp', 1, 'Eau')

main()
from normal import Normal
from terre import Terre
from eau import Eau
from feu import Feu
from random import randint
import time
import json

class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.p1 = pokemon1
        self.p2 = pokemon2

    def verifie(self, pokemon):
        self.pokemon = pokemon
        if self.pokemon.get_pv() < 1:
            return False
        else:
            return True
        
    def win(self, vainqueur):
        return 'Le vainqueur est {}'.format(vainqueur.get_nom())

    def lose(self, perdant):
        return 'Le perdant est {}'.format(perdant.get_nom())
    
    def fail_ou_pas(self):
        a = randint(0,1)
        if a == 1:
            return True
        else:
            return False
        
    def attaque(self, attaquant, defenseur):
        if type(attaquant) == Normal:
            if type(defenseur) == Feu:
                return attaquant.attaque * 0.75
            elif type(defenseur) == Terre:
                return attaquant.attaque * 0.75
            else:
                return attaquant.attaque
        
        elif type(attaquant) == Eau:
            if type(defenseur) == Feu:
                return attaquant.attaque * 2
            elif type(defenseur) == Terre:
                return attaquant.attaque * 0.5
            else:
                return attaquant.attaque

        elif type(attaquant) == Feu:
            if type(defenseur) == Terre:
                return attaquant.attaque * 2
            elif type(defenseur) == Eau:
                return attaquant.attaque * 0.5
            else:
                return attaquant.attaque

        elif type(attaquant) == Terre:
            if type(defenseur) == Feu:
                return attaquant.attaque * 0.5
            elif type(defenseur) == Eau:
                return attaquant.attaque * 2
            else:
                return attaquant.attaque
            
    def enlever_point(self, defenseur, degat):
        if defenseur == self.p1:
            pv = self.p1.get_pv() - degat
            self.p1.set_pv(pv)
        elif defenseur == self.p2:
            pv = self.p2.get_pv() - degat
            self.p2.set_pv(pv)
    

    def enregistrer_pokedex(self, nom, niveau, type):
        types = {'Normal': Normal, 'Feu': Feu, 'Eau': Eau, 'Terre': Terre}
        if type in types:
            p = types[type](nom, niveau)
        info = p.info()
        
        try:
            with open("pokedex.json", "r") as f:
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

        with open("pokedex.json", "w") as f:
            json.dump(pokemon, f)

    def combat(self, p1, p2):
        Round = 1
        if not self.verifie(p1):
            print('{} est mort'.format(self.p1.get_nom()))
            self.verifie(p1)
            print(self.win(p2))
            print(self.lose(p1))
        elif not self.verifie(p2):
            print('{} est mort'.format(self.p2.get_nom()))
            self.verifie(p2)
            print(self.win(p1))
            print(self.lose(p2))
            self.enregistrer_pokedex(self.p2.get_nom(), self.p2.niveau, self.p2.__class__.__name__)
        
        self.p1.afficher_info()
        self.p2.afficher_info()

        while self.verifie(p1) and self.verifie(p2):

            if Round == 1:
                if self.fail_ou_pas():
                    print("Le combat commence...")
                    degat = self.attaque(p1,p2)
                    self.enlever_point(p2, degat)
                    print("\nNom : {}\nPV : {}\n ".format(self.p2.get_nom(), self.p2.get_pv()))
                    if not self.verifie(p2):
                        print('{} est mort'.format(self.p2.get_nom()))
                        self.verifie(p2)
                        print(self.win(p1))
                        print(self.lose(p2))
                        self.enregistrer_pokedex(self.p2.get_nom(), self.p2.niveau, self.p2.__class__.__name__)
                        if self.p1.niveau < 4:
                            self.p1.niveau += 1
                        print('')
                    Round += 1
                else:
                    Round += 1
                    print('{} a raté son attaque'.format(self.p1.get_nom()))
            elif(Round % 2 == 0):
                if self.fail_ou_pas():
                    degat = self.attaque(p2,p1)
                    self.enlever_point(p1, degat)
                    print("\nNom : {}\nPV : {}\n ".format(self.p1.get_nom(), self.p1.get_pv()))
                    if not self.verifie(p1):
                        print('{} est mort'.format(self.p1.get_nom()))
                        self.verifie(p1)
                        print(self.win(p2))
                        print(self.lose(p1))
                        self.enregistrer_pokedex(self.p1.get_nom(), self.p1.niveau, self.p1.__class__.__name__)
                        print('')
                    Round += 1
                else:
                    Round += 1
                    print('{} a raté son attaque'.format(self.p1.get_nom()))
            elif(Round % 2 != 0):
                if self.fail_ou_pas():
                    degat = self.attaque(p1,p2)
                    self.enlever_point(p2, degat)
                    print("\nNom : {}\nPV : {}\n ".format(self.p2.get_nom(), self.p2.get_pv()))
                    if not self.verifie(p2):
                        print('{} est mort'.format(self.p2.get_nom()))
                        self.verifie(p2)
                        print(self.win(p1))
                        print(self.lose(p2))
                        self.enregistrer_pokedex(self.p2.get_nom(), self.p2.niveau, self.p2.__class__.__name__)
                        if self.p1.niveau < 4:
                            self.p1.niveau += 1
                        print('')
                    Round += 1
                else:
                    Round += 1
                    print('{} a raté son attaque'.format(self.p2.get_nom()))

            time.sleep(0.5)
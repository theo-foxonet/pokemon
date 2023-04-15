from pokemon import Pokemon

class Feu(Pokemon):
    def __init__(self, nom, niveau, attaque = 25, defense = 5, pv = 90):
        if niveau == 2:
            attaque += 3
            defense += 2
            pv += 5
        elif niveau == 3:
            attaque += 6
            defense += 4
            pv += 10
        elif niveau == 4:
            attaque += 12
            defense += 8
            pv += 20
        super().__init__(nom, niveau, attaque, defense, pv)

    def afficher_info(self):
        print("\nNom : {}\nPV : {}\nNiveau : {}\nAttaque : {}\nDéfense : {}\n ".format(self.get_nom(), self.get_pv(), self.niveau, self.attaque, self.defense))

    def info(self):
        return {"Type": self.__class__.__name__, "Niveau": self.niveau, "PV": self.get_pv(), "Attaque": self.attaque, "Defense": self.defense}
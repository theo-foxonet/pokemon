class Pokemon:
    def __init__(self, nom , niveau, attaque, defense = 0, pv = 100):
        self.__nom = nom
        self.__pv = pv
        self.niveau = niveau
        self.attaque = attaque
        self.defense = defense

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    def get_pv(self):
        return self.__pv

    def set_pv(self, pv):
        self.__pv = pv
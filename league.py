import interface
import ranking
import random

class uefa(interface.Section):
    """
    Toto je jedna nasa implementovana europska liga
    Musi dedit od Section
    a zmenit si meno nastavit tabulky a vracanie tych co postupili
    """
    def __init__(self):
        """
        Nastavy tabulky
        """
        super(uefa,self).__init__()
        self.name = "UEFA"
        for a in range(ord('A'),ord('I')+1):
            self.tables[chr(a)] = list()
        
        names = ranking.getAllShortNames()
        #rozdelenie temov nahodne
        random.shuffle(names)
        groups = list(self.tables.keys())
        temp = 0
        for name in names:
            team = interface.Team(name)
            self.tables[groups[temp]].append(team)
            temp = (temp + 1) % len(groups)
        


    def getPromoted(self):
        """
        vrati list, koty postupili ak sa odohrali vsetky zapasi inak vrati None
        """
        out = super(uefa,self).getPromoted()

        if out is None:
            return None

        ret = []
        for gr in self.tables:
            group = self.tables[gr]
            ret.append(max(group)) # tu postupuje len prvy
            
        return ret

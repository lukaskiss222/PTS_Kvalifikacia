import sim
class Team(object):
    """
    Klasa ktora obaluje tym v tabulke a podporuje porovnavanie medzi temami
    """
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.goal_get = 0
        self.goal_shoot = 0
        self.ranking = 0
    def __str__(self):
        return "" + self.name + ": " + str(self.points) + ", " + str(self.goal_shoot) + ", "  +  str(self.goal_get)  
    def __repr__(self):
        return self.__str__() + "\n"
    def __gt__(self,team):
        if self.points > team.points:
            return True
        if self.points < team.points:
            return False
        # teraz sa body rovnaju rozhodne pocet strelenych golov
        if self.goal_shoot > team.goal_shoot:
            return True
        if self.goal_shoot < team.goal_shoot:
            return False
        # ak aj to sa rovna rozhdone pocet dostanych golov
        if self.goal_get < team.goal_get:
            return True
        else:
            return False # ak sa vetko rovna tak vratime False

    def __lt__(self, team):
        if not self.__eq__(team):
            return not self.__gt__(team)
    def __eq__(self, team):
        if (team.points == self.points) and (team.goal_shoot == self.goal_shoot) and (
                team.goal_get == self.goal_get):
            return True 

class Section(object):
    """
    Klasa ktora robi interface medzi ligami,
    kazda liga musi toto dedit
    """
    def __init__(self):
        self.tables = {} 
        self.days = []
        self.actualDay = 0
        self.played_macthes = []
        self.name = "Interface"
    
    def hasNextDay(self):
        """
        Este su niake dni na hranie ?
        """
        return self.actualDay < len(self.days)

    def nextDay(self):
        """
        odsimuluje zapasi pre nasledujuci den
        """
        day = self.days[self.actualDay]
        for match in day:
            ret = sim.match(match[0].name, match[1].name)
            if ret[0] == ret[1]:
                match[0].points += 1
                match[1].points += 1
            
            if ret[0] > ret[1]:
                match[0].points += 3
            
            if ret[1] > ret[0]:
                match[1].points += 3

            match[0].goal_get += ret[1]
            match[0].goal_shoot += ret[0]

            match[1].goal_get += ret[0]
            match[1].goal_shoot += ret[1]

            self.played_macthes.append((match[0],match[1],ret[0],ret[1]))
        self.actualDay += 1 #dalsi den

    def getPromoted(self):
        """
        Vrati list ktory postupuju ak sa odohrali vsetky zapasi inak vrati None
        Kazda liga si tot musi implementovat sama
        """
        if self.hasNextDay():
            return None
        return []

    def createPlan(self):
        """
        Tu sa vytvori rozpis zapasou
        pre tuto ligu
        """
        temp = []
        for gr in self.tables:
            for i in range(len(self.tables[gr])):
                for j in range(i +1,len(self.tables[gr])):
                    temp.append((self.tables[gr][i],self.tables[gr][j]))
        # teraz roztriedime zapasy na dni
        # Chceme max 3 zapasy na den
        count_days = (len(temp) //2) 
        for a in range(count_days):
            self.days.append([])

        i = 0
        while len(temp) >0:
            pom = temp.pop()
            self.days[i].append(pom)
            i += 1

            if i >= count_days:
                i = 0
    
    def printPlayed(self):
        """
        Vypise odohrane zapasi
        """
        for match in self.played_macthes:
            print("%s:%d\t%s:%d" % (match[0].name ,match[2], match[1].name, match[3]))
    
    def printTable(self, index):
        """
        Vypise tabulku s indexom index
        """
        print("..................... GROUP-" + str(index) + " ......................")
        group = self.tables[index]
        group.sort(reverse = True)
        for team in group:
            print(team)
    
    def printTables(self):
        """
        Vypise vsetky tabulky
        """
        for gr in self.tables:
            self.printTable(gr)

import league
import cmd
import sys

def printPlayed(leagues):
    """
    Vypise doteraz odohrane zapasi pre kazdu ligu
    """
    for lg in leagues:
        print("########################### " + lg.name + " ###############################")
        lg.printPlayed()

def NextDay(leagues):
    """
    Prekazdu ligu odsimuluje jeden den
    a ked uz ziadna liga nemoze hrat dalsi den tak vrati False
    """
    ne = False
    for lg in leagues:
        if lg.hasNextDay():
            lg.nextDay()
            ne = True
    return ne

def printTables(leagues):
    """
    Vypise vsetky tabulky pre kazdu ligu.
    Ligy dostane ako parameter list
    """
    for lg in leagues:
        print("########################### " + lg.name + " ###############################")
        print("B - points, S - goals shoot, G - goals get")
        print("     B  S  G")
        lg.printTables()

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))


class FootBallShell(cmd.Cmd):
    """
    Klasa na obalovanie Command navrhoveho vzoru
    """
    intro = "Welcome to simulator of FIFA 2018"
    promt = ":>"
    
    def __init__(self):
        super(FootBallShell,self).__init__()
        self.leagues = [league.uefa()]

        for a in self.leagues:
            a.createPlan()

    def do_next(self, arg):
        if not NextDay(self.leagues):
            print("All matches played")

    def do_played(self, arg):
        printPlayed(self.leagues)
    
    def do_tables(self, arg):
        printTables(self.leagues)

    def do_exit(self, arg):
        print("Bey")
        sys.exit(0)
    
    def do_playAll(self, arg):
        while NextDay(self.leagues):
            pass

if __name__ == "__main__":
    FootBallShell().cmdloop()

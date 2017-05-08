
filename = 'ranking.csv'


def iterator(function):
    """
    iteruje cez prvky v subore a oplikuje nanu funkciu function
    ak vrati True tak vrati aj tato fukcia
    Tato fukcia je iterator cez prvky v subore
    """
    f = open(filename,'r')
    for line in f:
        values = line.split(',')
        if function(values):
            yield values

    f.close()


def getAllShortNames():
    """
    Vrati vsetky skratky statov
    """
    def f(v):
        return True
    ret = []
    for values in iterator(f):
        ret.append(values[2])
    return ret

def shortToLong(name):
    """
    Skonvertuje kratke na dlhe
    """
    def f(v):
        if v[2] == name:
            return True
    for val in iterator(f):
        return val[1]

def getPoints(list_names):
    """
    Ziska Rank z tabulky a vrati to cislo pre kazdy stat v liste
    """
    def f(v):
        if v[2] in list_names:
            return True
    ret = {}
    for val in iterator(f):
        ret[val[2]] = int(val[3].split("(")[0])
    return ret

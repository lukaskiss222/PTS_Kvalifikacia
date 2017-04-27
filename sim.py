from ranking import getPoints
import random
import numpy as np


def mutate_dict(f,d):
    for k, v in d.items():
        d[k] = f(v)

def non_linearRandomFloat(const = 1/2):
    return 1 - np.power(1 - random.random(), const)


def non_linearRandomInt(to, const = 1/2):
    return int(np.floor(non_linearRandomFloat(const)*to))



def match(name1, name2):
    points = getPoints([name1,name2])
    su = points[name1] + points[name2]

    mutate_dict(lambda x: (x/su)/4, points)
    score1 = non_linearRandomInt(10, points[name1])# + non_linearRandomInt(3,1/4)
    score2 = non_linearRandomInt(10, points[name2])
    
    return [score1,score2]
    



if __name__ == "__main__":
    import time
    while True:
        print(match("GER","CZE"))
        time.sleep(0.2)

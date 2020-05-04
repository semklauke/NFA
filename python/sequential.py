import time

class NFA:
    def __init__(self, states):
        self.states = states
        self.transistions = { state:[] for state in self.states }
        
    def addTransition(self, state1, symbol, state2):
        self.transistions[state1].append((symbol, state2))
        
    def simulate(self, start, word):
        active = set()
        active.add(start)
        for w in word:
            new_active = set()
            for state in active:
                for (symbol, target) in self.transistions[state]:
                    if symbol == w:
                        new_active.add(target)
            if len(new_active) == 0:
                return active
            else:
                active = new_active
        return active

automata = NFA([i for i in range(1,35)])
with open('../transitions') as f:
    for line in f:
        t = line.split(" ")
        automata.addTransition(int(t[0]), t[1], int(t[2]))

#s = 0
with open('../input') as f:
    for index, line in enumerate(f):
        #start = time.time()
        res = automata.simulate(7, line)
        #end = time.time()
        #diff = end-start
        #s += diff
        print("{}. Wort:\n{}".format(index+1, res))
        
#print("Laufzeit: {}sec".format(round(s, 2)))

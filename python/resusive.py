import time

class NFA:
    def __init__(self, states):
        self.states = states
        self.transistions = { state:[] for state in self.states }
        
    def addTransition(self, state1, symbol, state2):
        self.transistions[state1].append((symbol, state2))
        
    def simulate(self, state, word):
        if len(word) == 0:
            return set()
        w = word[0]
        new_word = word[1:]
        delta = set()
        delta.add(state)
        for (symbol, target) in self.transistions[state]:
            if symbol == w:
                delta.add(target)
                delta = delta.union(self.simulate(target, new_word))
        return delta
        
automata = NFA([i for i in range(1,35)])
with open('../transitions') as f:
    for line in f:
        t = line.split(" ")
        automata.addTransition(int(t[0]), t[1], int(t[2]))

res = automata.simulate(7, "abababbaa")
print("δ(7,abababbaa): \n{}".format(res))

# Not stack not big enought
#
#s = 0
#with open('input') as f:
#    for index, line in enumerate(f):
#        start = time.time()
#        res = automata.simulate(7, line)
#        end = time.time()
#        diff = end-start
#        s += diff
#        print("{}. Wort ({}sec):\n{}".format(index+1, (round(diff, 2), res)))
#        
#print("Laufzeit: {}sec".format(round(s, 2)))

import itertools

MAXI=6

def gen(length):
    if length == 1:
        return [[x] for x in range(1, MAXI+1)]
    return [[i] + j for i in xrange(MAXI) for j in gen(length-1)]

def count_hits(l1, l2, armor):
    res = 0
    l1.sort(reverse=True)
    l2.sort(reverse=True)
    for (a,b) in itertools.izip_longest(l1,l2):
        res += (not b or a > b) and a > armor
    return res

def fight(a_dices, d_dices, armor):
    hits = [0.0]*(MAXI+1)
    attacks = gen(a_dices)
    defenses = gen(d_dices)
    all = len(attacks) * len(defenses)
    for attack in attacks:
        for defense in defenses:
            hits[count_hits(attack, defense, armor)] += 1
    return [hit/all for hit in hits]

print fight(1,1,0)

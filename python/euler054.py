from collections import Counter

cardvalues = {
    '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
}

cardcolors = {'H': 1, 'S': 2, 'C': 3, 'D': 4}

combs = {
    'RF': 9, 'FK': 8, 'FH': 7, 'Flush': 6, 'Str': 5,
    'TK': 4, 'TP': 3, 'Pair': 2
}


class Card:

    def __init__(self, cardstr):
        self.value = cardvalues[cardstr[0]]
        self.color = cardcolors[cardstr[1]]


class Hand:

    def __init__(self, handarr):
        self.values = [cardvalues[cardstr[0]] for cardstr in handarr]
        self.values.sort()
        self.colors = [cardcolors[cardstr[1]] for cardstr in handarr]

    def score(self):
        result = 4 * [0]
        result[3] = max(self.values)
        print self.values

        flagthree = False
        flagtwo = False
        argtwo = 0

        counts = Counter(self.values)
        for k in counts.iterkeys():
            if counts[k] == 4:
                result[0] = combs['FK']
                result[1] = k
                return result
            if counts[k] == 3:
                flagthree = True
                result[1] = k
            if counts[k] == 2:
                if flagtwo:
                    result[0] = combs['TP']
                    result[1] = max(k, argtwo)
                    result[2] = min(k, argtwo)
                    return result
                flagtwo = True
                argtwo = k
        if flagthree and flagtwo:
            result[0] = combs['FH']
            result[1] = argtwo
            return result
        if flagthree:
            result[0] = combs['TK']
            return result
        if flagtwo:
            result[0] = combs['Pair']
            result[1] = argtwo
            return result

        flush = len(set(self.colors)) == 1
        straight = self.values[4] - self.values[0] == 4
        if straight and flush:
            result[0] = combs['RF']
            result[1] = self.values[4]
            return result
        if flush:
            result[0] = combs['Flush']
            result[1] = self.values[0]
            return result
        if straight:
            result[0] = combs['Str']
            result[1] = self.values[4]
            return result
        return result


count = 0

file = open('../fixtures/euler054')
for line in file:
    hands = line.rstrip().split(' ')
    if Hand(hands[:5]).score() > Hand(hands[5:]).score():
        count += 1

print count

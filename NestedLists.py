n = int(input())
scores1 = []
dane = []
wyniki = []
for i in range(n):
    name = input()
    score = float(input())
    dane.append(name)
    dane.append(score)
    scores1.append(dane)
    dane = []

scores1 = sorted(scores1, key = lambda x: x[1]) #sorts the list by the second element
najgorsze = scores1[0][1]
scores1.pop(0) #removes the lowest element


porownanie = scores1[0][1]

for i in range(len(scores1)):
    if scores1[i][1] == porownanie:
        wyniki.append(scores1[i][0])

wyniki = sorted(wyniki)
print(*wyniki, sep="\n")

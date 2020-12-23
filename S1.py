task = list(input())
clubs = []
diamonds = []
hearts = []
spades = []

def makeString(seq):
    string = " "
    for i in seq:
        string += str(i) + " "
    string = string[:-1]
    return string
here = task.index("D")
clubs = task[1:here]
now = task.index("H")
diamonds = task[here + 1 : now]
here = task.index("S")
hearts = task[now + 1:here]
spades = task[here + 1:]

'''print(clubs)
print(diamonds)
print(hearts)
print(spades)'''

clubsum = clubs.count("A") * 4 + clubs.count("K") * 3 + clubs.count("Q") * 2 + clubs.count("J")
diasum = diamonds.count("A") * 4 + diamonds.count("K") * 3 + diamonds.count("Q") * 2 + diamonds.count("J")
heartsum = hearts.count("A") * 4 + hearts.count("K") * 3 + hearts.count("Q") * 2 + hearts.count("J")
spadsum = spades.count("A") * 4 + spades.count("K") * 3 + spades.count("Q") * 2 + spades.count("J")

for i in range(3):
    if len(clubs) == i:
        clubsum += (i - 3) * -1
    if len(diamonds) == i:
        diasum += (i - 3) * -1
    if len(hearts) == i:
        heartsum += (i - 3) * -1
    if len(spades) == i:
        spadsum += (i - 3) * -1

print("Cards Dealt          Points")
hold = makeString(clubs)
print("Clubs" + hold + "             " + str(clubsum))

hold = makeString(diamonds)
print("Diamonds" + hold + "             " + str(diasum))

hold = makeString(hearts)
print("Hearts" + hold + "             " + str(heartsum))

hold = makeString(spades)
print("Spades" + hold + "             " + str(spadsum))


total = clubsum + diasum + heartsum + spadsum
print("Total " + str(total))
all = []
total = []
while True:
    task = input()
    if task == "**":
        break
    all.append(task)

#print(all)

'''for i in range(len(all)):
    all[i] = sorted(all[i])

print(all)'''

start = ["A"]

def count(value):
    times = 0
    save = []
    for i in all:
        if value in i:
            times +=1
            save.append(i[i.index(value)-1])

    return [times, save]

def duplications(seq):
    inital = ""
    for i in seq:
        inital += i
#    print(inital)
    current = []
    result = count(inital[-1])
    for i in range(result[0]):
        insert = inital + result[1][i]
        current.append(insert)

    return [current, result[1]]

def removethem(seq):
    final = []
    for i in all:
        if i not in seq:
            final.append(i)
    return final



first = duplications(start)
all = removethem(first)
#print(all)
#print(first)
watch = 0
while True:
    if watch == 3:
        break
    watch +=1
    amount = len(first)
    for i in range(amount):
#        print(first[i])
        hold = duplications(first[i])
#        print(hold)
        first.append(hold[0])
        all = removethem(hold[1])
    del first[:amount]
    print(first)
#    print(all)
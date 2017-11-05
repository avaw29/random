fname = "TheVictors.txt"
f = open(fname, "r")
reading = f.read()
words = reading.split()
word_count = {}
for x in words:
    if x not in word_count:
        word_count[x] = 1
    else:
        word_count[x] += 1
count_tup = []
for a in word_count:
    tup = (a, word_count[a])
    count_tup.append(tup)
alpha = sorted(count_tup, reverse = True)
srtd = sorted(alpha, reverse = True, key = lambda k: k[1])

for (y, z) in srtd[:15]:
    print (y, z)

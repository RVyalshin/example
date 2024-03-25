lis = []
max_sum = -1000000000
maxi = 0
for i in range(270012, 270823 + 1):
    k = 0
    lis_del = []
    for j in range(1, i + 1):
        if i % j == 0:
            k += 1
            lis_del.append(j)
    if k >= 5:
        max_sum = max(max_sum, sum(lis_del))
        lis.append([i, sum(lis_del), len(lis_del)])

for i in lis:
    if i[1] == max_sum:
        print(i[1], i[2])
for i in range(100715, 100742 + 1):
    k = 0
    lis_del = []
    for j in range(2, i):
        if i % j == 0:
            k += 1
            lis_del.append(j)
        if k > 2:
            break
    if k == 2:
        print(lis_del[1], lis_del[0])
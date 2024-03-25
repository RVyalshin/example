lis_gl = []
for i in range(8812000, 8812310 + 1):
    k = 0
    lis = []
    for j in range(2, i):
        if i % j == 0:
            k += 1
            lis.append(j)
        if k > 4:
            break
    if k == 4:
        lis = lis[-2:]
        lis_gl.append(lis)

lis_pro = []

for i in lis_gl:
    lis_pro.append(i[0] * i[1])

slovar_lis = {}

for i in range(len(lis_gl)):
    slovar_lis[lis_pro[i]] = lis_gl[i]

lis_pro = sorted(lis_pro)

for i in lis_pro:
    print(slovar_lis[i])
from itertools import *

lis = permutations("АБВГДЕЖЗ", 8)
k = 0

for i in lis:
    word = ""
    for j in i:
        word += j
    if not("АГ" in word) and not("ГА" in word):
        k += 1
print(k)
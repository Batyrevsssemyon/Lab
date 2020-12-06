A = 185311
B = 185330
count = 2
k = []
for i in range (A, B + 1):
    for j in range (2, i // 2 + 1):
        if i % j == 0:
            count += 1
            k.append(j)
    if count == 4:
        print(1, *k, i)
    k = []
    count = 2
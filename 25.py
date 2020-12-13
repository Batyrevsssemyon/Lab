for i in range (185311, 185331):
    k = [1]
    for j in range (2, i // 2 + 1):
        if i % j == 0:
            k.append(j)
    k.append(i)
    if len(k) == 4:
        print(*k)
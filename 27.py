f = open("27B.txt")  # файл A(B)
a0 = [] # массив, в котором записываются все значения файла A(B)
a1 = [] # массив, в котором записываются первые числа из пар чисел, удовлетворяющих условию задачи
a2 = [] # массив, в котором записываются вторые числа из пар чисел, удовлетворяющих условию задачи
k = 0 # количество пар чисел, удовлетворяющих условию задачи
M = 0 # значение максимальной суммы чисел среди пар чисел, удовлетворяющих условию задачи
for lines in f:
    a0.append(int(lines))
n = a0.pop(0)
for i in range(0, n):
    if a0[i] % 17 == 0:
        for j in range(0, n):
            if (a0[i] - a0[j]) % 2 == 0 and j < i:
                a1.append(a0[i])
                a2.append(a0[j])
                k += 1
            elif (a0[i] - a0[j]) % 2 == 0 and j > i and a0[j] % 17 != 0:
                a1.append(a0[i])
                a2.append(a0[j])
                k += 1
for i in range(0, k):
        if a1[i] + a2[i] > M:
            M = a1[i] + a2[i]
            M1 = a1[i]
            M2 = a2[i]
f.close()
print(M1, M2)
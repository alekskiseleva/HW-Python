from random import randint

K = int(input("Введите количество операций итерирования: "))
n = int(input("Введите количество элементов массива: "))

B = []
k = 0
i = 0

A = [randint(1, 100) for j in range(n)]
S = sum(A)

while k < K:

    for a in A:
        a = S - a
        B.append(a)

    S = sum(B)

    while i < len(A):
        A[i] = B[i]
        i += 1

    G = B.copy()
    B.clear()

    k += 1

print('Конечный массив', G)
diff = max(G) - min(G)
print(max(G), min(G))
print(diff)
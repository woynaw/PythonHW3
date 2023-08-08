print("Введите a1")
a1 = int(input())
print("Введите d")
d = int(input())
print("Введите n")
n = int(input())
list = []
for i in range(n):
    list.append(a1 + i * d)
print(*list)

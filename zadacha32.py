print("Введите массив")
list = []
list = input().split()
print(*list)
print("Введите min")
d = []
d.append(int(input()))
print("Введите max")
d.append(int(input()))
print(d)
res = []
for i in range(len(list)):
    if (int(list[i]) >= d[0])&(int(list[i]) <= d[1]):
        res.append(i)
print(*res)


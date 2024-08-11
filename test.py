list = []

for  i in range(2,101):
    checkSNT = True
    for j in range(2, i):
        if i % j == 0:
            checkSNT = False
    if checkSNT:
        list.append(i)

for i in list:
    print(i, end=" - ")
print()
print("Tong cua list tren la", sum(list))

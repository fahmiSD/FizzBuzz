def apaBole(n):
    arr = []
    for i in range(1, n+1):
        if i % 3 == 0:
            if i % 5 == 0:
                arr.append("ApaBole")
            else:
                arr.append("Apa")
        elif i % 5 == 0:
            arr.append("Bole")
        else:
            arr.append(i)
    return arr


print(apaBole(100))

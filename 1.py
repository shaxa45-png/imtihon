def musbat(sonlar):
    hisob = 0
    for x in sonlar:
        if x > 0:
            hisob += x
    return hisob


print(musbat([1, -2, 3, -4, 5]))
def kopaytma(sonlar):
    natija = 1
    for son in sonlar:
        natija = natija * son
    return natija


print(kopaytma([1, 2, 3, 4]))       

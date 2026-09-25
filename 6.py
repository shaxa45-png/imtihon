def qiymatlar_yigindisi(lugat):
    yigindi = 0
    for x, y  in lugat.items():
        yigindi += y[x]
    return yigindi
 
print(qiymatlar_yigindisi({"a": 1, "b": 2, "c": 3}))  
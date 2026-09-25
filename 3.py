def raqamlar_soni(matn):
    hisob = 0
    for x in matn:
        if x.isdigit():
            hisob = hisob + 1
    return hisob


print(raqamlar_soni("asbc123")) 

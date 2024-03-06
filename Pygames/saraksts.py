saraksts = [1,2,5,7]
saraksts2 = [6,7,8,9,4,5,7]

def saskaitit(sar):
    s=0
    for sk in sar:
        s+=sk
    return s
print("Summa ir ", saskaitit(saraksts))
print("Summa ir ", saskaitit(saraksts2))

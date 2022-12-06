josmalo = True
ovoisto = []
while josmalo:
    ovoisto.append(float(input("Broj??? ")))
    if ovoisto[-1] < 0:
        ovoisto.pop()
        break
print(f"Aritmeticka sredina brojeva je: {sum(ovoisto)/len(ovoisto)}")
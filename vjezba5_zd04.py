rijec = input("Rijec: ")
rijec = [i for i in rijec]
for c in rijec:
    if "A" < c.capitalize() < "Z":
        print(c)
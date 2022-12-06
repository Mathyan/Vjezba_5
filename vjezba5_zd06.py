toliko = int(input("Upisite broj ocjena: "))
ocj = []
ocjtest = 0
koliko = 0
while koliko < toliko:
    ocjtest = int(input("Unesite ocjenu od 1 do 5: "))
    if ocjtest < 1 or ocjtest > 5:
        print("Unijeli ste pogresnu ocjenu.")
        continue
    ocj.append(ocjtest)
    koliko += 1
if 1 in ocj:
    print("Nedovoljan.")
    exit()
print(sum(ocj)/len(ocj))
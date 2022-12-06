broj = int(input("Upisite broj: "))
skup_djel = []
for i in range(1,broj +1):
    if not(broj % i):
        skup_djel.append(i)
if len(skup_djel) == 2:
    print(f"Broj {broj} je prosti")
else:
    print(f"Broj {broj} je slozežen te ima djelitelji su mu {skup_djel}")
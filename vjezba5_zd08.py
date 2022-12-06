fefta = int(input("Broj: "))
fefta = str(fefta)
if set([int(i) for i in fefta]) & set([int(i) for i in "56789"]):
    print("Broj nije feftalni!!!")
dec = 0
fefta = [int(j) for j in fefta]
for i in range(len(fefta)):
    dec+=(fefta[i]*(5**(len(fefta)-i-1)))
print(dec)
broj= int(input("Broj: "))
if broj < 10 or broj > 99:
    print("Krivi unos!!!!!")
    exit()
for i in range(10,broj):
    if (i//10%2 == 1) and (i%10%2 == 1):
        print(i)
m = int(input("Upisite prvi broj: "))
n = int(input("Upisite drugi broj: "))
for i in range(m+1,n):
    if (i//10+i%10) == 10:
        print(i)
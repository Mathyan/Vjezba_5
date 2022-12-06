n = int(input("Upisi broj: "))
for i in range(n+1,1,-1):
    if i == int(str(i)[::-1]):
        print(i)
        break
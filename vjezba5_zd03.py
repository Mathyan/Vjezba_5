m = int(input("Upisite prvi broj: "))
n = int(input("Upisite drugi broj: "))
while n:
    m , n = n , m%n
print(m)
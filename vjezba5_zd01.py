broj = int(input("Upisite broj: "))
for i in range(1,broj + 1):
    print(i,end=" ")
print()
for i in range(0,broj + 1):
    print(i*2+1,end=" ")
print()
fakt = 1
for i in range(1,broj+1):
    fakt*=i
print(f"Faktorjela broje je {fakt}")
if broj % 2 :
    for i in range(1,broj + 1,2):
        print(i)
else: 
    for i in range(2,broj + 1,2):
        print(i)
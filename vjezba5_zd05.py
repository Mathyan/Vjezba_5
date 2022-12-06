rijec = input("Rijec: ")
rijec = [i for i in rijec]
flag = False
for i in range(len (rijec)):
    if i < len(rijec):
        if rijec[i].capitalize() in "LN" and rijec[i + 1].capitalize() == "J":
            print("".join(rijec[i:i+2]))
            flag = True
            continue
        elif rijec[i].capitalize() in "D" and rijec[i + 1].capitalize() == "Ž":
            print("".join(rijec[i:i+2]))
            flag = True
            continue
    if flag: 
        flag = False
        continue
    elif rijec[i].isalpha():
        print(rijec[i])

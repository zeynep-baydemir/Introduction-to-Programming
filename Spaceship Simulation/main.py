
x = int(input())
y = int(input())
g = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
if x==0:
    print("YOU WON!")
    olist=[]
    for i in range(g):
        mylist = list(y*" ")
        olist.insert(i,mylist)
        for t in range(y):
            print(olist[i][t],end="")
        print()
    shiplist = []
    if y % 2 == 1:
        o = int((y - 1) / 2)
    else:
        o = int(y / 2 - 1)
    for t in range(y):
        if t == o:
            shiplist.insert(t, "@")
        else:
            shiplist.append(" ")
        print(shiplist[t], end="")
    print()
    print(72 * "-")
    print("YOUR SCORE: 0")
    my_bool=False
    mama=0
else:
    starlist=[]
    for a in range(x):
        firstlist = list(y*"*")
        starlist.insert(a, firstlist)
        for k in range(y):
            print(starlist[a][k], end="")
        print()
    bosluklist = []
    for a in range(g):
        secondlist = list(y*" ")
        bosluklist.insert(a, secondlist)
        for i in range(y):
            print(bosluklist[a][i], end="")
        print()
    shiplist = []
    if y % 2 == 1:
        o = int((y-1)/2)
    else:
        o = int(y/2-1)
    for t in range(y):
        if t == o:
            shiplist.insert(t, "@")
        else:
            shiplist.append(" ")
        print(shiplist[t], end="")
    print()
    print(72*"-")
    totallist = starlist + bosluklist
    my_bool = True
    mama=1
bitis=True
aman=1
while my_bool==True:
    for time in range(5):
        action = input("Choose your action!\n")
        action = action.lower()
        if action == "left":
            if time==4:
                if "*" in totallist[-1]:
                    print("GAME OVER")
                    if shiplist[0] == "@":
                        for a in range(x + g):
                            for k in range(y):
                                print(totallist[a][k], end="")
                            print()
                        for t in range(y):
                            print(shiplist[t], end="")
                        print()
                        print(72 * "-")
                        my_bool = False
                        break
                    else:
                        for a in range(x + g):
                            for k in range(y):
                                print(totallist[a][k], end="")
                            print()
                        shipindex = shiplist.index("@")
                        shiplist[shipindex] = " "
                        shiplist[shipindex - 1] = "@"
                        for t in range(y):
                            print(shiplist[t], end="")
                        print()
                        print(72 * "-")
                    my_bool = False
                    break
                else:
                    newlist = []
                    for i in range(y):
                        newlist.append(" ")
                    totallist.insert(0, newlist)
                    totallist.pop(-1)
                    if shiplist[0] == "@":
                        for a in range(x + g):
                            for k in range(y):
                                print(totallist[a][k], end="")
                            print()
                        for t in range(y):
                            print(shiplist[t], end="")
                        print()
                        print(72 * "-")

                    else:
                        for a in range(x+g):
                            for k in range(y):
                                print(totallist[a][k], end="")
                            print()
                        shipindex = shiplist.index("@")
                        shiplist[shipindex] = " "
                        shiplist[shipindex - 1] = "@"
                        for t in range(y):
                            print(shiplist[t], end="")
                        print()
                        print(72 * "-")
            else:
                if shiplist[0]=="@":
                    for a in range(x+g):
                        for k in range(y):
                            print(totallist[a][k], end="")
                        print()
                    for t in range(y):
                        print(shiplist[t], end="")
                    print()
                    print(72 * "-")
                else:
                    for a in range(x+g):
                        for k in range(y):
                            print(totallist[a][k], end="")
                        print()
                    shipindex = shiplist.index("@")
                    shiplist[shipindex] = " "
                    shiplist[shipindex - 1] = "@"
                    for t in range(y):
                        print(shiplist[t], end="")
                    print()
                    print(72 * "-")
        elif action == "right":
            if time==4:
                if "*" in totallist[-1]:
                    print("GAME OVER")
                    if shiplist[-1] == "@":
                        for a in range(x + g):
                            for k in range(y):
                                print(totallist[a][k], end="")
                            print()
                        for t in range(y):
                            print(shiplist[t], end="")
                        print()
                        print(72 * "-")
                        my_bool = False
                        break
                    else:
                        for a in range(x + g):
                            for k in range(y):
                                print(totallist[a][k], end="")
                            print()
                        shipindex = shiplist.index("@")
                        shiplist[shipindex] = " "
                        shiplist[shipindex + 1] = "@"
                        for t in range(y):
                            print(shiplist[t], end="")
                        print()
                        print(72 * "-")
                    my_bool = False
                    break
                else:
                    newlist = []
                    for i in range(y):
                        newlist.append(" ")
                    totallist.insert(0, newlist)
                    totallist.pop(-1)
                    if shiplist[-1] == "@":
                        for a in range(x + g):
                            for k in range(y):
                                print(totallist[a][k], end="")
                            print()
                        for t in range(y):
                            print(shiplist[t], end="")
                        print()
                        print(72 * "-")
                    else:
                        for a in range(x + g):
                            for k in range(y):
                                print(totallist[a][k], end="")
                            print()
                        shipindex = shiplist.index("@")
                        shiplist[shipindex] = " "
                        shiplist[shipindex + 1] = "@"
                        for t in range(y):
                            print(shiplist[t], end="")
                        print()
                        print(72 * "-")
            else:
                if shiplist[-1] == "@":
                    for a in range(x + g):
                        for k in range(y):
                            print(totallist[a][k], end="")
                        print()
                    for t in range(y):
                        print(shiplist[t], end="")
                    print()
                    print(72 * "-")
                else:
                    for a in range(x + g):
                        for k in range(y):
                            print(totallist[a][k], end="")
                        print()
                    shipindex = shiplist.index("@")
                    shiplist[shipindex] = " "
                    shiplist[shipindex + 1] = "@"
                    for t in range(y):
                        print(shiplist[t], end="")
                    print()
                    print(72 * "-")
        elif action == "fire":
            shipindex = shiplist.index("@")
            if time != 4:
                for sayi in range(len(totallist)):
                    if totallist[len(totallist) - sayi - 1][shipindex] == "*":
                        totallist[len(totallist) - sayi - 1][shipindex] = " "
                        wincontrol = 0
                        for i in range(len(totallist)):
                            if "*" in totallist[i]:
                                wincontrol += 1
                            else:
                                continue
                        if wincontrol == 0:
                            print("YOU WON!")
                            for a in range(len(totallist)):
                                for k in range(y):
                                    print(totallist[a][k], end="")
                                print()
                            for t in range(y):
                                print(shiplist[t], end="")
                            print()
                            print(72 * "-")
                            my_bool = False
                            bitis = False
                            break

                        for a in range(x + g):
                            for k in range(y):
                                print(totallist[a][k], end="")
                            print()
                        for t in range(y):
                            print(shiplist[t], end="")
                        print()
                        print(72 * "-")
                        break
                    else:
                        if sayi == len(totallist) - 1:
                            totallist[len(totallist) - sayi - 1][shipindex] = "|"
                            for a in range(x + g):
                                for k in range(y):
                                    print(totallist[a][k], end="")
                                print()
                            for t in range(y):
                                print(shiplist[t], end="")
                            print()
                            print(72 * "-")
                            totallist[len(totallist) - sayi - 1][shipindex] = " "
                            for a in range(x + g):
                                for k in range(y):
                                    print(totallist[a][k], end="")
                                print()
                            for t in range(y):
                                print(shiplist[t], end="")
                            print()
                            print(72 * "-")
                            totallist[len(totallist) - sayi - 1][shipindex] = " "
                        else:
                            totallist[len(totallist) - sayi - 1][shipindex] = "|"
                            for a in range(x + g):
                                for k in range(y):
                                    print(totallist[a][k], end="")
                                print()
                            for t in range(y):
                                print(shiplist[t], end="")
                            print()
                            print(72 * "-")
                            totallist[len(totallist) - sayi - 1][shipindex] = " "
            else:
                for sayi in range(len(totallist)):
                    if totallist[len(totallist) - sayi - 1][shipindex] == "*":
                        totallist[len(totallist) - sayi - 1][shipindex] = " "
                        wincontrol = 0
                        for i in range(len(totallist)):
                            if "*" in totallist[i]:
                                wincontrol += 1
                            else:
                                continue
                        if "*" in totallist[-1]:
                            print("GAME OVER")
                            for a in range(x + g):
                                for k in range(y):
                                    print(totallist[a][k], end="")
                                print()
                            for t in range(y):
                                print(shiplist[t], end="")
                            print()
                            print(72 * "-")
                            my_bool = False
                            bitis = False
                            break
                        elif not wincontrol==0 and not "*" in totallist[-1]:
                            newlist = []
                            for i in range(y):
                                newlist.append(" ")
                            totallist.insert(0, newlist)
                            totallist.pop(-1)
                            for a in range(x + g):
                                for k in range(y):
                                    print(totallist[a][k], end="")
                                print()
                            for t in range(y):
                                print(shiplist[t], end="")
                            print()
                            print(72 * "-")
                            break
                        if wincontrol == 0:
                            print("YOU WON!")
                            for a in range(len(totallist)):
                                for k in range(y):
                                    print(totallist[a][k], end="")
                                print()
                            for t in range(y):
                                print(shiplist[t], end="")
                            print()
                            print(72 * "-")
                            my_bool = False
                            bitis = False
                            break
                    else:
                        if sayi == len(totallist) - 1:
                            totallist[len(totallist) - sayi - 1][shipindex] = "|"
                            if "*" in totallist[-1]:
                                for a in range(x + g):
                                    for k in range(y):
                                        print(totallist[a][k], end="")
                                    print()
                                for t in range(y):
                                    print(shiplist[t], end="")
                                print()
                                print(72 * "-")
                                totallist[len(totallist) - sayi - 1][shipindex] = " "
                                print("GAME OVER")
                                for a in range(x + g):
                                    for k in range(y):
                                        print(totallist[a][k], end="")
                                    print()
                                for t in range(y):
                                    print(shiplist[t], end="")
                                print()
                                print(72 * "-")
                                my_bool = False
                                bitis = False
                                break
                            else:
                                for a in range(x + g):
                                    for k in range(y):
                                        print(totallist[a][k], end="")
                                    print()
                                for t in range(y):
                                    print(shiplist[t], end="")
                                print()
                                print(72 * "-")
                                totallist[len(totallist) - sayi - 1][shipindex] = " "
                                newlist = []
                                for i in range(y):
                                    newlist.append(" ")
                                totallist.insert(0, newlist)
                                totallist.pop(-1)
                                for a in range(x + g):
                                    for k in range(y):
                                        print(totallist[a][k], end="")
                                    print()
                                for t in range(y):
                                    print(shiplist[t], end="")
                                print()
                                print(72 * "-")
                                totallist[len(totallist) - sayi - 1][shipindex] = " "
                        else:
                            totallist[len(totallist) - sayi - 1][shipindex] = "|"
                            for a in range(x + g):
                                for k in range(y):
                                    print(totallist[a][k], end="")
                                print()
                            for t in range(y):
                                print(shiplist[t], end="")
                            print()
                            print(72 * "-")
                            totallist[len(totallist) - sayi - 1][shipindex] = " "
            if bitis == False:
                break
            else:
                continue
        elif action == "exit":
            my_bool = False
            for a in range(x + g):
                for k in range(y):
                    print(totallist[a][k], end="")
                print()
            for t in range(y):
                print(shiplist[t], end="")
            print()
            print(72 * "-")
            break
        else:
            if time == 4:
                if "*" in totallist[-1]:
                    print("GAME OVER")
                    if shiplist[-1] == "@":
                        for a in range(x + g):
                            for k in range(y):
                                print(totallist[a][k], end="")
                            print()
                        for t in range(y):
                            print(shiplist[t], end="")
                        print()
                        print(72 * "-")
                        my_bool = False
                        break
                else:
                    newlist = []
                    for i in range(y):
                        newlist.append(" ")
                    totallist.insert(0, newlist)
                    totallist.pop(-1)
                    for a in range(x + g):
                        for k in range(y):
                            print(totallist[a][k], end="")
                        print()
                    for t in range(y):
                        print(shiplist[t], end="")
                    print()
                    print(72 * "-")
            else:
                for a in range(x + g):
                    for k in range(y):
                        print(totallist[a][k], end="")
                    print()
                for t in range(y):
                    print(shiplist[t], end="")
                print()
                print(72 * "-")
if mama==0:
    pass
else:
    kalan = 0
    for i in range(x):
        kalan += starlist[i].count("*")
    score = x*y-kalan
    print("YOUR SCORE:", score)



# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE




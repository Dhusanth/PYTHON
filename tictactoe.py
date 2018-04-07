t = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3) :
    print(t[i])

print("USER 1 => 1\nUSER 2 => 2")

j = 1
for i in range(9) :
    if j == 1 :
        p = int(input("Enter the position User 1 "))
        x = p // 3
        y = p % 3
        t[x][y] = 1
    else:
        p = int(input("Enter the position User 2 "))
        x = p // 3
        y = p % 3
        t[x][y] = 2

    j = j * (-1)

    for a in range(0,3) :
        for b in range(0,3) :
            print(t[a][b] , end = " ")
        print("\n")

    for a in range(0,3) :
        if t[a][0] == t[a][1] == t[a][2] == 1 :
            print("User 1 wins !!")
            exit(0)
        if t[a][0] == t[a][1] == t[a][2] == 2 :
            print("User 2 wins !!")
            exit(0)

    for a in range(0,3) :
        if t[0][a] == t[1][a] == t[2][a] == 1 :
            print("User 1 wins !!")
            exit(0)
        if t[0][a] == t[1][a] == t[2][a] == 2 :
            print("User 2 wins !!")
            exit(0)

    if t[0][0] == t[1][1] == t[2][2] == 1 :
        print("User 1 wins !!")
        exit(0)
    elif t[0][0] == t[1][1] == t[2][2] == 2 :
        print("User 2 wins !!")
        exit(0)
    elif t[0][2] == t[1][1] == t[2][0] == 1 :
        print("User 1 wins !!")
        exit(0)
    elif t[0][2] == t[1][1] == t[2][0] == 2 :
        print("User 2 wins !!")
        exit(0)


print("Sorry No Winner !!")
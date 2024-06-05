ln = int(input("층수: "))

for i in range(ln) : 
    for j in range(ln-i) :
        print("*", end=" ")
    print()
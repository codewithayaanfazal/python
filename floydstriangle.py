u = int(input("Enter your number of rows: "))
n = 1
for i in range(1,u+1):
    for x in range(1,i+1):
        print(n,end=" ")
        n+=1
    print()
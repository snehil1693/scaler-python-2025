

balance = int(input()) #Initial balance

M = int(input()) #read the number of operations

for _ in range(M):
    operation_input = input().split()
    Type = int(operation_input[0])
    X = int(operation_input[1])

    if Type == 1:
        balance = balance + X
        print(balance)
    else:
        if X > balance:
            print("Insuffieient Funds")
        else:
            balance = balance - X
            print(balance)


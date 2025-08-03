
N = int(input())

for i in range(1, N+1):
    if i < N:
        print(i , end = " ")
    else:
        print(i)

for i in range(N,0, -1):
    if i >1:
        print(i, end = " ")
    else:
        print(i)

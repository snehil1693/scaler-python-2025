
A = int(input())

for i in range (1, A+1):
    if int(i ** 0.5) ** 2 == i:
        print(i , end = ' ')
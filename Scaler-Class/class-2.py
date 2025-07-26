N = int(input())

if N == 1:
    print("Not Prime")
elif N == 2:
    print("Prime")
else:
    i = 2
    while i < N:
        if N % i == 0:
            print("Not Prime")
            break
        i+=1
    else:
        print("Prime")
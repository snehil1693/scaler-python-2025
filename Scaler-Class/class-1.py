
# Check whether a number is prime or not

N = int(input())

flag = False

if N == 1:
    print("Not Prime")
elif N == 2:
    print("Prime")
else:
    for i in range(2,N):
        if N % i == 0:
            flag = True
            break
    if flag:
            print("Not Prime")
    else:
            print("Prime")

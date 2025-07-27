
#Read T numbers and for every number reverse the digits

T = int(input())

while T > 0:
    N = int(input())

    if N < 0:
        copy = N * -1 # to make it positive
    else:
        copy = N

    rev = 0

    while copy>0:
        d = copy % 10  # to get the last digit
        rev = rev * 10 + d # append the last digit
        copy = copy//10

    if N < 0:
        rev = rev * -1
    print(rev)
    T-=1

# reverse the difit of a number

N = int(input())

while N > 0:
    print(N % 10, end="") # print the last digit
    N = N //10 # removing the last digit

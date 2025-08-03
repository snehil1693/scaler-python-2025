
N = int(input())

rev = 0

while N > 0:
    d = N % 10
    rev = rev * 10 + d
    N = N //10

print(rev)
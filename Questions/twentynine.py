
N = int(input())

ans = 0
while N>0:
    ans += N % 10
    N=N//10
print(ans)
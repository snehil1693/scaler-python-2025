
A = int(input())

rev = 0

original = A

while (A>0):
    digit = A % 10
    rev = rev * 10 + digit
    A //= 10

if original == rev:
    print("Yes")
else:
    print("No")





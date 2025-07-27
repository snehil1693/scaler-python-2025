
# find the reverse of a given number

N = int(input())

if N < 0:
    copy = N * -1 # hack for negative number
else:
    copy = N
rev = 0

while copy>0:
    d = copy % 10 # last digit
    rev = rev * 10 + d # append the last digit
    copy = copy//10

if N < 0:
    rev = rev * -1
print(rev)

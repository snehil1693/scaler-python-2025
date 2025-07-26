
# i = 2
# if i ==2:
#     i +=1
# for j in range (i):
#     pass
#     break
#     i +=1
# print(i)

n = 8
while n>0:
    n -=2
    if n%2==0:
        continue
    print(n, end = " ")
else:
    print("Exec", end = " ")

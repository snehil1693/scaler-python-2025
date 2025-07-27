
N = int(input())

flag = False

if N == 1:
   print("NO")
elif N == 2:
   print("YES")

else:
  for i in range(2, N):
    if N % i == 0:
      flag = True
      break
  if flag == True:
      print("NO")
  else:
      print("YES")
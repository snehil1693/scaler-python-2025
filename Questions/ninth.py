# import category
#
# N = int(input())
#
# if (N>=2100):
#     print("grand master")
# elif (N>=1900 and N<2100):
#     print("candidate master")
# elif (N>=1600 and N<1900):
#     print("expert")
# elif (N>=1400 and N<1600):
#     print("pupil")
# else:
#     print("newbie")
#
# if N % 2 ==1:
#     print(category.lower())
# else:
#     print(category.upper())

# n = int(input())
# category = (
#     "grand master" if n >= 2100 else
#     "candidate master" if n >= 1900 else
#     "expert" if n >= 1600 else
#     "pupil" if n >= 1400 else
#     "newbie"
# )
# print(category.lower() if n % 2 else category.upper())

n = int(input())

if n >= 2100:
    category = "grand master"
elif n >= 1900:
    category = "candidate master"
elif n >= 1600:
    category = "expert"
elif n >= 1400:
    category = "pupil"
else:
    category = "newbie"

print(category.lower() if n % 2 == 1 else category.upper())

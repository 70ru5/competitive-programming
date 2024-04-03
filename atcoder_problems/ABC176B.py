N = input()
lst = [int(x) for x in list(N)]

sum = 0
for i in range(len(lst)):
  sum += lst[i]

if sum % 9 == 0:
  print("Yes")
  
else:
  print("No")

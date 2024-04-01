N, X, T = map(int, input().split())

count = 0
time = 0

if N%X == 0:
  count = N//X
else:
  count = N//X + 1
  
time = T * count
print(time)

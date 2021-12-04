x = int(input())
y = int(input())
n = int(input())

ans = (n / (x + y)) * 2
if (n % (x + y)) > y:
  ans += 2
elif (n % (x + y)) > 0:
  ans += 1

print(int(ans))
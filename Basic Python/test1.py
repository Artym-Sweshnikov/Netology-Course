m = int(input())
n = int(input())
while m != n:
    s = m * n
    if s // m == n and s // n == m:
        break
print(s)




a = int(input())
x1 = a // 1000
x2 = a // 100 % 10
x3 = a // 10 % 10
x4 = a % 10
print(int(x1 == x4 and x3 == x2))

x, n = map(int, input().split())
new_p = n - x * 100
x1 = new_p / 100
x2 = new_p // 100
if x1-x2 > 0:
    print(x2+1)
else:
    print(x2)
    

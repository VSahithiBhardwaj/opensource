x, y, z = map(int, input().split())

z_in_min = 24*60*z

if x * y <= z_in_min:
    print("YES")
else:
    print("NO")

x = int(input())

c1 = x * 0.9
c2 = x - 100
   
max_discount = min(c1, c2)
print(int(max_discount))

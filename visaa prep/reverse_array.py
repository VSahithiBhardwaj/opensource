n = int(input())
arr = list(map(int, input().split()))
reversed_arr = arr[::-1]
res = ' '.join([str(num) for num in reversed_arr])
print(res)

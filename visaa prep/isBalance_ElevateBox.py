N = int(input())
A = list(map(int, input().split()))
l = 0
r = 0
for i in range(N):
    if i != 0 or i != N:
        l += sum(A[0:i])
        r += sum(A[i+1:N+1])
        res = abs(l-r)
        print(res, end = " ")
        l, r = 0, 0
    elif i == 0:
        l = 0
        r += A[i+1:N+1]
        res = abs(l-r)
        print(res, end = " ")
    else:
        r = 0
        l += A[0:N]
        res = abs(l-r)
        print(res, end = " ")
print()

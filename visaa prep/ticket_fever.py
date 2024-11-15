t = int(input())
for i in range(0, t):
    N, M = map(int, input().split())
    if N >= M:
        print(N-M)
    else:
        print(0)
    

n = int(input())
n_str = str(n)
n_sum = 0
for i in n_str:
    n_sum += int(i)
if n_sum % 2 == 0:
    print("Vignesh")
else:
    print("Charan")

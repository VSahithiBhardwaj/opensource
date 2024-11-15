v, c = map(str, input().split())

if (v == "S" and c == "P") or (v == "P" and c == "R") or (v == "R" and c == "S"):
    print("Vignesh")
elif v == c:
    print("NULL")
else:
    print("Charan")

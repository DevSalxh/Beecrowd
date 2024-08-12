Value = list(map(int, input().split()))
Value2 = Value.copy()
Value.sort()
for x in range(len(Value)):
    print(Value[x])
print()
for x in range(len(Value2)):
    print(Value2[x])

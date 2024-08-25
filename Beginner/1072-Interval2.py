n = int(input())
inValue = 0
outValue = 0

for i in range(n):
    value = int(input())

    if 10 <= value <= 20:
        inValue += 1
    else:
        outValue += 1

print(f'{inValue} in')
print(f'{outValue} out')
count = 0
for i in range(5):
    Value = float(input())
    if Value % 2 == 0:
        count += 1
print(f'{count} valores pares')
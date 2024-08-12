PositiveQuotient = 0
Sum = 0
for i in range(6):
    Value = float(input())
    if Value >= 0:
        PositiveQuotient += 1
        Sum += Value

print(f'{PositiveQuotient} valores positivos')
Avg = Sum /PositiveQuotient
print('%0.1f'%Avg)
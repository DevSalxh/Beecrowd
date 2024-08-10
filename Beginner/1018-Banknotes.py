Value = int(input())
print(Value)
Currency = [100, 50, 20, 10, 5, 2, 1]
for X in Currency:
    Quotient = int((Value / X))
    print(f'{Quotient} nota(s) de R$ {X},00')
    Remaining = Value % X
    Value = Remaining
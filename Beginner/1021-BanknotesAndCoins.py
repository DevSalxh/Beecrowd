Value = float(input())
Currency = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
Coins = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
print('NOTAS:')
for x in Currency:
    Quotient = int((Value / x))
    print(f'{Quotient} nota(s) de R$ {x:.2f}')
    Remainding = Value % x
    Value = Remainding
print('MOEDAS:')
for y in Coins:
    Quotient = int(round(Value,2) / y)
    print(f'{Quotient} moeda(s) de R$ {y:.2f}')
    Remainding = round(Value,2) % y
    Value = Remainding
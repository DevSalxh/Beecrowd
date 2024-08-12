Salary = float(input())

if Salary > 4500:
    Tax1 = 1000 * 0.08
    Tax2 = 1500 * 0.18
    Tax3 = (Salary - 4500) * 0.28
    print('R$ %0.2f'%(Tax1 + Tax2 + Tax3))
elif 3000<Salary<=4500:
    Tax1 = 1000 * 0.08
    Tax2 = (Salary - 3000) * 0.18
    print('R$ %0.2f'%(Tax1+Tax2))
elif 2000<Salary<=3000:
    Tax = (Salary - 2000) * 0.08
    print('R$ %0.2f'%Tax)
else:
    print('Isento')
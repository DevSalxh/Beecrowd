#Reading the employee's salary
Salary = float(input())

if 0<Salary<=400.00:
    print("Novo salario: %.2f" %(Salary*1.15))
    print("Reajuste ganho: %.2f" %((Salary*1.15)-Salary))
    print("Em percentual: 15 %")
if 400.01<=Salary<=800.00:
    print("Novo salario: %.2f" %(Salary*1.12))
    print("Reajuste ganho: %.2f" %((Salary*1.12)-Salary))
    print("Em percentual: 12 %")
if 800.01<=Salary<=1200.00:
    print("Novo salario: %.2f" %(Salary*1.10))
    print("Reajuste ganho: %.2f" %((Salary*1.10)-Salary))
    print("Em percentual: 10 %")
if 1200.01<=Salary<=2000.00:
    print("Novo salario: %.2f" %(Salary*1.07))
    print("Reajuste ganho: %.2f" %((Salary*1.07)-Salary))
    print("Em percentual: 7 %")
if Salary>2000.00:
    print("Novo salario: %.2f" %(Salary*1.04))
    print("Reajuste ganho: %.2f" %((Salary*1.04)-Salary))
    print("Em percentual: 4 %")
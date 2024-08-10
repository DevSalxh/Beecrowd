AgeInDays = int(input())
Check = [365, 30, 1]
Solution = []
text = ['ano(s)', 'mes(es)', 'dia(s)']
for x in Check:
    Quotient = int(AgeInDays / x)
    Solution.append(Quotient)
    Remaining = AgeInDays % x
    AgeInDays = Remaining
for j in range(3):
    print(f'{Solution[j]} {text[j]}')
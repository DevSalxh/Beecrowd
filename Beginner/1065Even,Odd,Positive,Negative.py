Positives = 0
Negatives = 0
Odds = 0
Evens = 0
for i in range(5):
    Val = float(input())
    if Val > 0:
        Positives += 1
    if Val < 0 :
        Negatives += 1
    if Val % 2 == 0 :
        Evens += 1
    if Val % 2 != 0:
        Odds += 1
print(f'{Evens} valor(es) par(es)')
print(f'{Odds} valor(es) impar(es)')
print(f'{Positives} valor(es) positivo(s)')
print(f'{Negatives} valor(es) positivo(s)')
n = int(input())
evenSum = 0

for num in range(1, n+1):
    if num % 2 == 0:
        evenSum = num*num
        print("%d^2 = %d" %(num, evenSum))
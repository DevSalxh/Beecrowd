LedTable = [6,2,5,5,4,5,6,3,7,6]

n = int(input())
for i in range(n):
    Sum = 0
    Value = input()
    for num in Value:
        Sum += LedTable[int(num)]
    print(f'{Sum} leds')

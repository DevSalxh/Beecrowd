LedTable = [6,2,5,5,4,5,6,3,7,6]
Sum = 0
n = int(input())
for i in range(n):
    Value = input()
    for num in Value:
        Sum += LedTable[int(num)]
    print(f'{Sum} leds')
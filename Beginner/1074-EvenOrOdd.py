n = int(input())

for i in range(n):
    value = int(input())
    if value > 0:
        if value % 2 == 0:
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')
    elif value < 0:
        if value % 2 == 0:
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE') 
    else:
        print('NULL')  
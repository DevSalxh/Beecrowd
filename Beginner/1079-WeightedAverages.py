n = int(input())
result = 0.0
for i in range(n):
    x, y, z = map(float, input().split())
    result = (x*2+y*3+z*5)/10
    print('%0.1f'%result)
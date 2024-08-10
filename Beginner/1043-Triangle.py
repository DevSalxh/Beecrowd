A,B,C = map(float,input().split())
if A+B>C and A+C>B and B+C>A:
    Perimeter = A+B+C
    print(f'Perimetro = {Perimeter}')
else:
    Area = 0.5*(A+B)*C
    print(f'Area = {Area}')
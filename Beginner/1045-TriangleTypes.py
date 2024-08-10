A= float(input())
B = float(input())
C = float(input())
if A >= (B + C):
    print('NAO FORMA TRIANGULO')
if A*A == (B*B + C*C):
    print('TRIANGULO RETANGULO')
if   A*A > (B*B + C*C):
    print('TRIANGULO OBTUSANGULO')
if  A*A < (B*B + C*C):
    print('TRIANGULO ACUTANGULO')
if A == C and C== B:
    print('TRIANGULO EQUILATERO')
if A==C or C==B:
    print('TRIANGULO ISOSCELES')
ProdNum1 = input().split(" ")
ProdNum2 = input().split(" ")
C1, U1, P1 = ProdNum1
C2, U2, P2 = ProdNum2
Price = ( (int(U1) * float(P1)) + (int(U2) * float(P2)) )
print('VALOR A PAGAR: R$ %0.2f' %Price)
N1,N2,N3,N4 = list(map(float,input().split()))
Avg = ( (N1*2) + (N2*3) + (N3*4) + (N4*1) )/(1+2+3+4)
print("Media: %.1f"%Avg)
if Avg >=7:
    print('Aluno aprovado.')
elif Avg <5.0:
    print('Aluno reprovado.')
elif Avg >= 5.0 and Avg<6.9:
    print('Aluno em exame.')
    N5 = float(input())
    print('Nota do exame: %.1f'%N5)
    Avg5=(Avg+N5)/2
    if Avg5 >=5.0 :
        print('Aluno aprovado.')
    elif Avg5 <=4.9:
        print('Aluno reprovado.')
    print('Media final: %.1f'%Avg5)
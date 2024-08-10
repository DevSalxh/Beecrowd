x, y, w, z = map(int, input().split())
if ( y>w and  z>x and (w+z) > (x+y) and w>0 and z>0 and x%2==0):
    print ('Valores aceitos')
else:
    print('Valores nao aceitos')
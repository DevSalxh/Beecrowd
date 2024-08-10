a, b, c = input().split(" ")
ab = ( int(a) + int(b) + abs( int(a) - int(b) ) )/2
major_abc = ( int(ab) + int(c) + abs( int(ab) - int(c)) )/2
print("%d eh o maior" %major_abc)
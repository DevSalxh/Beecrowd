A, B, C = input().split(" ")
Triangle = 0.5 * float(A) * float(C)
Circle = 3.14159 * (float(C))**2
Trapezoid = 0.5 * ( float(A) + float(B) ) * float(C)
Square = (float(B))**2
Rectangle = float(A) * float(B)
print("TRIANGULO: %0.3f" %Triangle)
print("CIRCULO: %0.3f" %Circle)
print("TRAPEZIO: %0.3f" %Trapezoid)
print("QUADRADO: %0.3f" %Square)
print("RETANGULO: %0.3f" %Rectangle)
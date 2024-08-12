X = int(input())
Y = int(input())
Value1 = min(X,Y)+1
Value2 = max(X,Y)
if Value1 % 2 == 0:
    Value1 += 1

sum = 0
for i in range(Value1, Value2, 2):
    sum += i
print(sum)
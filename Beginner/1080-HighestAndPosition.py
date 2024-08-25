HighestValue = 0
Location = 0
for i in range(100):
    Value = int(input())
    if Value > HighestValue:
        HighestValue = Value
        Location = (i+1)
print(HighestValue)
print(Location)
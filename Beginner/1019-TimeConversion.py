Seconds = int(input())
CheckTime = [3600, 60, 1]
TheSolution = []
for time in CheckTime:
    Value = int(Seconds / time)
    TheSolution.append(Value)
    Remaining = Seconds % time
    Seconds = Remaining
print(f'{TheSolution[0]}:{TheSolution[1]}:{TheSolution[2]}')
Start,End = map(int, input().split())
if Start > End:
    Hours = 24 - (Start - End)
    print("O JOGO DUROU %d HORA(S)" %Hours)
elif End > Start:
    Hours = End - Start
    print("O JOGO DUROU %d HORA(S)" %Hours) 
elif Start == End:
    print("O JOGO DUROU 24 HORA(S)")

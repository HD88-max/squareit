start = int(input("What number do you want to start with?: "))#11
ge = int(input("And what number do you want to end with?: "))#12
evenlist = []
oddlist = []
while start < ge:#11<12
    for i in range(start,ge,1):
        rang = i * i
        if rang%2 == 0:
            evenlist.append(rang)
        else:
            oddlist.append(rang)
    start = start +1
print("Even list is:",evenlist)
print("Odd list is:",oddlist)
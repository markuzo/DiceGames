from datetime import datetime

def averageTime(times):
    if len(times) is 0:
        return 0
    return sum(times)/len(times)

def datetimeToSec(time):
    return time.seconds

def printAll(people, currentperson, bau):
    normcol = '\033[0m'

    basiccol = '\033[96m'
    for p in people:
        col = basiccol
        if p is currentperson:
            col = '\033[92m'

        print(col,p[0],"\t",averageTime(p[1]),"\t",p[1],normcol)

    print(basiccol,"zw","\t",averageTime(bau),"\t",bau,normcol)

def outputResults(people, bau):
    with open("timing-results.txt",'w') as f:
        msg = "person\taverage\ttimes\n"
        f.write(msg)
        for p in people:
            msg = p[0]+"\t"+str(averageTime(p[1]))+"\t"+str(p[1])+"\n"
            f.write(msg)

        msg = "ZB"+"\t"+str(averageTime(bau))+"\t"+str(bau)+"\n"
        f.write(msg)

persons = [('Guy',[]),('Mic',[]),('Mum',[]),('Mrkz',[]),('Mel',[])]
zwischenbau = []
zwischenbauPhase = False

person = 0
time1 = datetime.now()

paused = False
pausetimerstart = datetime.now()
pausetimerend   = datetime.now()
pausetime = 0

print("Press 's' to start.")
while input() != "s":
    print("Press 's' to start.")
    continue

printAll(persons,persons[person],zwischenbau)

run = True
while run:
    c = input()
    if c is "p":
        if not paused:
            paused = True
            pausetimerstart = datetime.now()
            print("Paused")

    if c is "r":
        if paused:
            paused = False
            pausetimerend = datetime.now()
            pausetime += datetimeToSec(pausetimerend - pausetimerstart)
            print("Resume")

    if paused == True:
        continue

    if c is "q":
        run = False
        continue
    
    if not c is "":
        continue

    if zwischenbauPhase:
        zwischenbauPhase = False
        zwischenbauTime = datetime.now()
        zwischenbau.append(datetimeToSec(zwischenbauTime - time1) - pausetime)
        time1 = zwischenbauTime
        pausetime = 0
        print("Timing...")
        continue

    time2 = datetime.now()

    persons[person][1].append(datetimeToSec(time2-time1)-pausetime)
    pausetime = 0

    time1 = time2

    person = (person+1)%len(persons)
    printAll(persons, persons[person], zwischenbau)
    zwischenbauPhase = True

    print("\nZwischenbau!")

outputResults(persons, zwischenbau)

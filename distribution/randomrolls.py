import random

totals = {}
for i in range(2,13):
    totals[str(i)] = 0

count = 100000

for i in range(1,count):
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    totals[str(d1+d2)] += 1

expectations = {}
expectations['2'] =  1/36.0
expectations['3'] =  2/36.0
expectations['4'] =  3/36.0
expectations['5'] =  4/36.0
expectations['6'] =  5/36.0
expectations['7'] =  6/36.0
expectations['8'] =  5/36.0
expectations['9'] =  4/36.0
expectations['10'] = 3/36.0
expectations['11'] = 2/36.0
expectations['12'] = 1/36.0

red = '\033[91m'
yel = '\033[93m'
gre = '\033[92m'
blu = '\033[94m'
ind = '\033[96m'
vio = '\033[95m'

colnorm = '\033[0m'

maxwidth = 480
for i in range(2,13):
    k = str(i)
    exp = expectations[k]
    act = (totals[k]/count)
    
    xbars = int(exp * maxwidth)
    ybars = int(act * maxwidth)

    spacing = ""
    if i < 10:
        spacing = " "

    print("-"*10, vio, spacing, k, colnorm, "-"*10, ind, "(", totals[k], ")")
    print(red, "E  ","#"*xbars, colnorm,exp)
    print(gre, "A  ","#"*ybars, colnorm,act)

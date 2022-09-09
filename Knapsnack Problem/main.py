import re

t = open("calc.in", "r")
file = str(t.read())
t.close()

def finish():
    f = open("calc.out", "w")
    f.write("Dont Let Me Down")
    f.close()
    import sys
    sys.exit()

if not "AnaDegiskenler" in file:    #anadegiskenler yoksa
    finish()
if not "YeniDegiskenler" in file:    #yenidegiskenler yoksa
    finish()
if not "Sonuc" in file:             #sonuc yoksa
    finish()
if not file.startswith("AnaDegiskenler"):           #anadegiskenlerden once bir sey geliyorsa
    for i in range(file.index("AnaDegiskenler")):       #gelen sey bosluk degilse
        if file[i] != "\n":
            if file[i]!=" ":
                finish()

if file.count("AnaDegiskenler") != 1 or file.count("YeniDegiskenler") != 1 or file.count("Sonuc") != 1:   #herhangi biri birden fazlaysa
    finish()

if not file.index("YeniDegiskenler") < file.index("Sonuc"):     #sonuc yenidegiskenlerden önce geldiyse
    finish()
keywords = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'sifir', 'bir', 'iki', 'uc', 'dort', 'bes', 'alti',
            'yedi', 'sekiz', 'dokuz', 'dogru', 'yanlis', '+', '-', '*', 'arti', 'eksi', 'carpi', 've', 'veya', '(', ')',
            'ac-parantez', 'kapa-parantez', 'AnaDegiskenler', 'YeniDegiskenler', 'Sonuc', 'degeri', 'olsun', 'nokta']
# General Structure Done#
whole = r"\s*([\s\S]*?)\n"
wholelines = re.findall(whole, file)

mydict = {}
init = r"AnaDegiskenler\s*([\s\S]*?)\s*YeniDegiskenler"         #initstatemnts bulma
initstatements = re.findall(init, file)

initvar = r"\s*(.*?)\s* degeri"
initvars = re.findall(initvar, initstatements[0])
initval = r"degeri\s* (.*?)\s* olsun"
initvalues = re.findall(initval, initstatements[0])

a = initstatements[0].count("degeri")
b = len(initvars)
if initstatements[0].count("degeri") != len(initvars):
    finish()
if initstatements[0].count("olsun") != len(initvars):
    finish()
x=initstatements[0].split("\n")
poplist=[]
for p in range(len(x)):
    if x[p]=='':
        poplist.append(p)
for a in range(len(poplist)):
    x.pop(poplist[a]-a)
for i in x:
    if not "olsun" in i:
        finish()
alphanumeric = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for name in initvars:
    if len(name) > 10:
        finish()
    if name in keywords:
        finish()
    for character in name:
        if not character in alphanumeric:
            finish()
            # initvariables rules done#

initval = r"degeri \s*(.*?)\s* olsun"
initvalues = re.findall(initval, initstatements[0])
mid = r"YeniDegiskenler\s*([\s\S]*)\s*Sonuc"
midstatements = re.findall(mid, file)

midvar = r"\s*(.*?)\s* degeri"
midvariables = re.findall(midvar, midstatements[0])

midval = r"degeri \s*(.*?)\s* olsun"
midvalues = re.findall(midval, midstatements[0])
c=midstatements[0].split("\n")
midpoplist=[]

for p in range(len(c)):
    if c[p]=='':
        midpoplist.append(p)
for a in range(len(midpoplist)):
    c.pop(midpoplist[a]-a)
for i in c:
    if not "olsun" in i:
        finish()

possiblevalues = ["dogru", "yanlis"]
tdigit = ["sifir", "bir", "iki", "uc", "dort", "bes", "alti", "yedi", "sekiz", "dokuz"]
digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
floatpoint=[]
for i in range(10):
    for k in range(10):
        floatpoint.append(str(float(str(i) + "." + str(k))))            #olasi floatpoint

i_term = ["dogru", "yanlis"]
for i in range(10):
    possiblevalues.append(str(i))
for i in range(10):
    for k in range(10):
        possiblevalues.append(str(float(str(i) + "." + str(k))))
for i in tdigit:
    possiblevalues.append(str(i))
    for k in tdigit:
        possiblevalues.append(str(str(i) + " nokta " + str(k)))  # possibleinitvaluesdone
for value in initvalues:
    if not value in possiblevalues:
        if "nokta" in value:
            a = value.index("nokta")
            u = value[0:a].rstrip()
            o= u.lstrip()
            v = value[a + 5:].lstrip()
            s=v.rstrip()
            if v and o in tdigit:
                w=initvalues.index(value)
                initvalues[w]=o+" "+"nokta"+" "+s
            else:
                finish()
        else:
            finish()
for name in initvars:
    if name in mydict:
        finish()
    else:
        a = initvars.index(name)
        mydict[name] = initvalues[a]


if midstatements[0].count("degeri") != len(midvariables):
    finish()
if midstatements[0].count("olsun") != len(midvariables):
    finish()
middict = {}
for name in midvariables:
    if name in mydict:
        finish()
    if name in middict:
        finish()
    else:
        middict[name] = 1
    if len(name) > 10:                                      #midvariable kontrol
        finish()
    if name in keywords:
        finish()
    for character in name:
        if not character in alphanumeric:
            finish()

mybool = True
cont = 0

newlist = []
for value in midvalues:
    a = value.split()
    newlist.append(a)

for i in range(len(newlist)):
    for j in range(len(newlist[i])):                    # yazilari ( + - * ya cevirme
        if newlist[i][j] == "ac-parantez":
            newlist[i][j] = "("
        elif newlist[i][j] == "kapa-parantez":
            newlist[i][j] = ")"
        elif newlist[i][j] == "arti":
            newlist[i][j] = "+"
        elif newlist[i][j] == "eksi":
            newlist[i][j] = "-"
        elif newlist[i][j] == "carpi":
            newlist[i][j] = "*"
    if newlist.count("(") != newlist.count(")"):
        finish()

aritop = ["+", "-", "*"]
logop = ["ve", "veya"]
logopposs = ["dogru", "yanlis", "(",]
logicalposs = ["ve", "veya", ")"]

aritcont = 0
logcont = 0
parantezospossible = ['(', ')','ve','veya','dogru', 'yanlis', '0', '1', '2', '3', '4', '5', '6', '7',
                      '8', '9', '0.0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0', '1.1',
                      '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '1.8', '1.9', '2.0', '2.1', '2.2', '2.3', '2.4', '2.5',
                      '2.6', '2.7', '2.8', '2.9', '3.0', '3.1', '3.2', '3.3', '3.4', '3.5', '3.6', '3.7', '3.8', '3.9',
                      '4.0', '4.1', '4.2', '4.3', '4.4', '4.5', '4.6', '4.7', '4.8', '4.9', '5.0', '5.1', '5.2', '5.3',
                      '5.4', '5.5', '5.6', '5.7', '5.8', '5.9', '6.0', '6.1', '6.2', '6.3', '6.4', '6.5', '6.6', '6.7',
                      '6.8', '6.9', '7.0', '7.1', '7.2', '7.3', '7.4', '7.5', '7.6', '7.7', '7.8', '7.9', '8.0', '8.1',
                      '8.2', '8.3', '8.4', '8.5', '8.6', '8.7', '8.8', '8.9', '9.0', '9.1', '9.2', '9.3', '9.4', '9.5',
                      '9.6', '9.7', '9.8', '9.9', 'sifir', 'sifir nokta sifir', 'sifir nokta bir', 'sifir nokta iki',
                      'sifir nokta uc', 'sifir nokta dort', 'sifir nokta bes', 'sifir nokta alti', 'sifir nokta yedi',
                      'sifir nokta sekiz', 'sifir nokta dokuz', 'bir', 'bir nokta sifir', 'bir nokta bir',
                      'bir nokta iki', 'bir nokta uc', 'bir nokta dort', 'bir nokta bes', 'bir nokta alti',
                      'bir nokta yedi', 'bir nokta sekiz', 'bir nokta dokuz', 'iki', 'iki nokta sifir', 'iki nokta bir',
                      'iki nokta iki', 'iki nokta uc', 'iki nokta dort', 'iki nokta bes', 'iki nokta alti',
                      'iki nokta yedi', 'iki nokta sekiz', 'iki nokta dokuz', 'uc', 'uc nokta sifir', 'uc nokta bir',
                      'uc nokta iki', 'uc nokta uc', 'uc nokta dort', 'uc nokta bes', 'uc nokta alti', 'uc nokta yedi',
                      'uc nokta sekiz', 'uc nokta dokuz', 'dort', 'dort nokta sifir', 'dort nokta bir',
                      'dort nokta iki', 'dort nokta uc', 'dort nokta dort', 'dort nokta bes', 'dort nokta alti',
                      'dort nokta yedi', 'dort nokta sekiz', 'dort nokta dokuz', 'bes', 'bes nokta sifir',
                      'bes nokta bir', 'bes nokta iki', 'bes nokta uc', 'bes nokta dort', 'bes nokta bes',
                      'bes nokta alti', 'bes nokta yedi', 'bes nokta sekiz', 'bes nokta dokuz', 'alti',
                      'alti nokta sifir', 'alti nokta bir', 'alti nokta iki', 'alti nokta uc', 'alti nokta dort',
                      'alti nokta bes', 'alti nokta alti', 'alti nokta yedi', 'alti nokta sekiz', 'alti nokta dokuz',
                      'yedi', 'yedi nokta sifir', 'yedi nokta bir', 'yedi nokta iki', 'yedi nokta uc',
                      'yedi nokta dort', 'yedi nokta bes', 'yedi nokta alti', 'yedi nokta yedi', 'yedi nokta sekiz',
                      'yedi nokta dokuz', 'sekiz', 'sekiz nokta sifir', 'sekiz nokta bir', 'sekiz nokta iki',
                      'sekiz nokta uc', 'sekiz nokta dort', 'sekiz nokta bes', 'sekiz nokta alti', 'sekiz nokta yedi',
                      'sekiz nokta sekiz', 'sekiz nokta dokuz', 'dokuz', 'dokuz nokta sifir', 'dokuz nokta bir',
                      'dokuz nokta iki', 'dokuz nokta uc', 'dokuz nokta dort', 'dokuz nokta bes', 'dokuz nokta alti',
                      'dokuz nokta yedi', 'dokuz nokta sekiz', 'dokuz nokta dokuz']

tdigitposs =["nokta", "+", "*", "-", ")"]
digitposs = [ "+", "*", "-", ")"]
arposs = []
for i in range(10):
    for k in range(10):
        arposs.append(str(float(str(i) + "." + str(k))))
ariopposs = digit + tdigit + arposs
parantez=["(",")"]
arioppossonce = ariopposs + ["("]

possvaluewithoutlogic = []
for i in range(10):
    possvaluewithoutlogic.append(str(i))
for i in range(10):
    for k in range(10):
        possvaluewithoutlogic.append(str(float(str(i) + "." + str(k))))
for i in tdigit:
    possvaluewithoutlogic.append(str(i))
    for k in tdigit:
        possvaluewithoutlogic.append(str(str(i) + " nokta " + str(k)))

arithmeticall = digit + tdigit + aritop
nokta=[".","nokta"]
arith=[]
for i in range(10):
    arith.append(str(i))
for i in range(10):
    for k in range(10):
        arith.append(str(float(str(i) + "." + str(k))))
for i in tdigit:
    arith.append(str(i))
    for k in tdigit:
        arith.append(str(str(i) + " nokta " + str(k)))
keylist=list(mydict.keys())
for i in range(len(newlist)):
    aritcont=0
    logcont=0
    if len(newlist[i]) == 1:                #ic liste tek elemanliysa
        if newlist[i][0] in possiblevalues:
            continue
        if not newlist[i][0] in possiblevalues:
            if newlist[i][0] in keylist:
                continue
            else:
                if newlist[i][0] in midvariables[0:i]:
                    continue
                else:
                    finish()
            finish()

    elif len(newlist[i]) > 1:  # ic liste 1 elemandan fazlaysa
        for t in range(len(newlist[i])):
            if newlist[i][t] in arithmeticall:  # arit ve log ayni elemanda varsa
                aritcont = 1
            if newlist[i][t] in logop:
                if aritcont == 1:
                    finish()
                logcont = 1
        if aritcont + logcont == 2:
            finish()
    for t in range(len(newlist[i])):
        acparsayisi = newlist[i][0:t + 1].count("(")
        kapaparsayisi = newlist[i][0:t + 1].count(")")
        if kapaparsayisi > acparsayisi:  # parantez uyumsuzlugu
            finish()
        if newlist[i][t] == "(":                                                    # ( ise
            if t == len(newlist[i]) - 1:
                finish()
            else:
                if not newlist[i][t + 1] in parantezospossible:
                    if not newlist[i][t + 1] in keylist:
                        if not newlist[i][t + 1] in midvariables[0:i]:
                            finish()
                if newlist[i][t+1]==")":
                    finish()
        elif newlist[i][t] == ")":                                                  # ) ise
            if t == 0:
                finish()
            elif t == len(newlist[i]) - 1:
                continue
            else:
                if not newlist[i][t + 1] in digitposs:
                    if not newlist[i][t + 1] in logop:
                        finish()
                if newlist[i][t - 1] == "(":
                    finish()
        else:
            if newlist[i][t] in tdigit:                                     #tdigitse
                if t == 0:
                    if not newlist[i][t + 1] in tdigitposs:
                        finish()
                    if (newlist[i][t + 1] == "(") or (newlist[i][t + 1] == ")"):
                        finish()
                    else:
                        continue
                elif t==len(newlist[i])-1:
                    continue
                else:
                    if not newlist[i][t + 1] in tdigitposs:
                        finish()
                if (newlist[i][t - 1] == ")") and (newlist[i][t + 1] == "("):
                    finish()
            elif newlist[i][t] in digit:                            #digit ise
                if t == 0:
                    if not newlist[i][t + 1] in digitposs:
                        finish()
                    if (newlist[i][t + 1] == "(") or (newlist[i][t + 1] == "("):
                        finish()
                elif t==len(newlist[i]) - 1:
                    continue
                else:
                    if not newlist[i][t + 1] in digitposs:
                        finish()
                if (newlist[i][t - 1] == ")") and (newlist[i][t + 1] == "("):
                    finish()
            elif newlist[i][t] in aritop:                       # arti carpi eksi ise
                if t == 0:
                    finish()
                elif t == len(newlist[i]) - 1:                  # son eleman +
                    finish()
                else:
                    if not newlist[i][t + 1] in arioppossonce:
                        if newlist[i][t + 1] in keylist:
                            if not mydict[newlist[i][t + 1]] in arith:
                                finish()
                        elif newlist[i][t + 1] in midvariables[0:i]:
                            k = midvariables.index(newlist[i][t + 1])
                            for word in newlist[k]:
                                if (word in logop) or (word in i_term):
                                    finish()
                        else:
                            finish()
                if (newlist[i][t - 1] == "(") and (newlist[i][t + 1] == ")"):  #####    (arti ise)
                    finish()
            elif newlist[i][t] in i_term:                                         #dogru veya yanlissa
                if t == 0:
                    if not newlist[i][t + 1] in logicalposs:
                        finish()
                elif t!=len(newlist[i])-1:
                    if not newlist[i][t + 1] in logicalposs:
                        finish()
                    if (newlist[i][t - 1] == ")") and (newlist[i][t + 1] == "("):
                        finish()
            elif newlist[i][t] in logop:
                if t == 0:
                    finish()
                elif t == len(newlist[i]) - 1:
                    finish()
                else:
                    if newlist[i][t + 1] not in logopposs:
                        if newlist[i][t + 1] in keylist:
                            if not mydict[newlist[i][t + 1]] in i_term:
                                finish()
                        elif newlist[i][t + 1] in midvariables[0:i]:
                            k = midvariables.index(newlist[i][t + 1])
                            for word in newlist[k]:
                                if (word in aritop) or (word in arithmeticall):
                                    finish()
                        else:
                            finish()
                    if (newlist[i][t - 1] == "(") and (newlist[i][t + 1] == ")"):
                        finish()
            elif newlist[i][t] == "nokta":
                if t == 0:
                    finish()
                elif t == len(newlist[i]) - 1:
                    finish()
                else:
                    if not newlist[i][t + 1] in tdigit:
                        finish()
                    if not newlist[i][t-1] in tdigit:
                        finish()
            elif newlist[i][t] == ".":
                if t == 0:
                    finish()
                elif t == len(newlist[i]) - 1:
                    finish()
                else:
                    if not newlist[i][t - 1] in digit:
                        finish()
                    if not newlist[i][t + 1] in digit:
                        finish()
            elif newlist[i][t] in keylist:  # anadaki degiskenlerden biriyse
                if aritcont == 1:
                    if not mydict[newlist[i][t]] in possvaluewithoutlogic:
                        finish()
                    if t == 0:
                        if not newlist[i][t + 1] in aritop:
                            finish()
                    elif t == len(newlist[i]) - 1:
                        if not newlist[i][t - 1] in aritop:
                            finish()
                    else:
                        if not newlist[i][t + 1] in aritop:
                            if not newlist[i][t + 1]==")":
                                finish()
                elif logcont == 1:
                    if not mydict[newlist[i][t]] in i_term:
                        finish()
                    if t == 0:
                        if not newlist[i][t + 1] in logop:
                            finish()
                    elif t == len(newlist[i]) - 1:
                        if not newlist[i][t - 1] in logop:
                            finish()
                    else:
                        if not newlist[i][t + 1] in logop:
                            if not newlist[i][t + 1]==")":
                                finish()
            else:
                if newlist[i][t] in midvariables[0:i]:
                    y = midvariables.index(newlist[i][t])
                    for p in range(len(newlist[y])):
                        if aritcont == 1:
                            if (newlist[y][p] in logop) or (newlist[y][p] in i_term) :
                                finish()
                            if t == 0:
                                if not newlist[i][t+1] in aritop:
                                    finish()
                            elif t == len(newlist[i]) - 1:
                                if not newlist[i][t-1] in aritop:
                                    finish()
                            else:
                                if not newlist[i][t+1] in aritop:
                                    if not newlist[i][t + 1] == ")":
                                        finish()
                        elif logcont == 1:
                            if (newlist[y][p] in arithmeticall) or (newlist[y][p] in aritop):
                                    finish()
                            if t == 0:
                                if not newlist[i][t + 1] in logop:
                                    finish()
                            elif t == len(newlist[i]) - 1:
                                if not newlist[i][t - 1] in logop:
                                    finish()
                            else:
                                if not newlist[i][t + 1] in logop:
                                    if not newlist[i][t + 1] == ")":
                                        finish()
                elif newlist[i][t] in floatpoint:
                    if t==0:
                        if newlist[i][t+1] not in aritop:
                            if not newlist[i][t+1] ==")":
                                finish()
                    elif t==len(newlist)-1:
                        if newlist[i][t-1] not in aritop:
                            if not newlist[i][t-1] =="(":
                                finish()
                    else:
                        if newlist[i][t+1] not in aritop:
                            if not newlist[i][t+1]==")":
                                finish()
                else:
                    finish()
    if acparsayisi!=kapaparsayisi:
        finish()

sonuc=r"Sonuc\s*([\s\S]*)\s*"
sonucexpres=re.findall(sonuc,file)
sonuce=sonucexpres[0].rstrip("\n")
sonucex=sonuce.lstrip("\n")
sonlist=sonucex.split()

for i in range(len(sonlist)):
    if sonlist[i]=="ac-parantez":        #yazilari ( + - * ya cevirme
        sonlist[i]="("
    elif sonlist[i]=="kapa-parantez":
        sonlist[i]=")"
    elif sonlist[i]=="arti":
        sonlist[i] = "+"
    elif sonlist[i]=="eksi":
        sonlist[i] = "-"
    elif sonlist[i] == "carpi":
        sonlist[i] = "*"
if sonlist.count("(")!=sonlist.count(")"):
        finish()

aritcont=0
logcont=0
if len(sonlist) == 1:                #ic liste tek elemanliysa
    if not sonlist[0] in possiblevalues:
        if not sonlist[0] in keylist:
            if not sonlist[0] in midvariables[0]:
                finish()
elif len(sonlist) > 1:  # ic liste 1 elemandan fazlaysa
    for t in range(len(sonlist)):
        if sonlist[t] in arithmeticall:  # arit ve log ayni elemanda varsa
            aritcont = 1
        if sonlist[t] in logop:
            if aritcont == 1:
                finish()
            logcont = 1
    if aritcont + logcont == 2:
            finish()
for t in range(len(sonlist)):
    acpar = sonlist[0:t + 1].count("(")
    kapapar = sonlist[0:t + 1].count(")")
    if kapapar > acpar:  # parantez uyumsuzlugu
        finish()
    if sonlist[t] == "(":                                                    # ( ise
        if t == len(sonlist) - 1:
            finish()
        else:
            if not sonlist[t + 1] in parantezospossible:
                if not sonlist[t + 1] in keylist:
                    if not sonlist[t + 1] in midvariables:
                        finish()
            if sonlist[t+1]==")":
                finish()
    elif sonlist[t] == ")":                                                  # ) ise
        if t == 0:
            finish()
        elif t == len(sonlist) - 1:
            continue
        else:
            if not sonlist[t + 1] in digitposs:
                if not sonlist[t + 1] in logop:
                    finish()
            if sonlist[t - 1] == "(":
                finish()
    else:
        if sonlist[t] in tdigit:                                     #tdigitse
            if t == 0:
                if not sonlist[t + 1] in tdigitposs:
                    finish()
                if (sonlist[t + 1] == "(") or (sonlist[t + 1] == ")"):
                    finish()
                else:
                    continue
            elif t==len(sonlist)-1:
                continue
            else:
                if not sonlist[t + 1] in tdigitposs:
                    finish()
            if (sonlist[t - 1] == ")") and (sonlist[t + 1] == "("):
                finish()
        elif sonlist[t] in digit:                            #digit ise
            if t == 0:
                if not sonlist[t + 1] in digitposs:
                    finish()
                if (sonlist[t + 1] == "(") or (sonlist[t + 1] == "("):
                    finish()
            elif t==len(sonlist) - 1:
                continue
            else:
                if not sonlist[t + 1] in digitposs:
                    finish()
            if (sonlist[t - 1] == ")") and (sonlist[t + 1] == "("):
                finish()
        elif sonlist[t] in aritop:                       # arti carpi eksi ise
            if t == 0:
                finish()
            elif t == len(sonlist) - 1:                  # son eleman +
                finish()
            else:
                if not sonlist[t + 1] in arioppossonce:
                    if sonlist[t + 1] in keylist:
                        if not mydict[sonlist[t + 1]] in arith:
                            finish()
                    elif sonlist[t + 1] in midvariables:
                        k = midvariables.index(sonlist[t + 1])
                        for word in newlist[k]:
                            if (word in logop) or (word in i_term):
                                finish()
                    else:
                        finish()
            if (sonlist[t - 1] == "(") and (sonlist[t + 1] == ")"):  #####    (arti ise)
                finish()
        elif sonlist[t] in i_term:                                         #dogru veya yanlissa
            if t == 0:
                if not sonlist[t + 1] in logicalposs:
                    finish()
                if  (sonlist[t + 1] == "("):
                    finish()
            elif t!=len(sonlist)-1:
                if not sonlist[t + 1] in logicalposs:
                    finish()
                if (sonlist[t - 1] == ")") and (sonlist[t + 1] == "("):
                    finish()
        elif sonlist[t] in logop:
            if t == 0:
                finish()
            elif t == len(sonlist) - 1:
                finish()
            else:
                if sonlist[t + 1] not in logopposs:
                    if sonlist[t + 1] in keylist:
                        if not mydict[sonlist[t + 1]] in i_term:
                            finish()
                    elif sonlist[t + 1] in midvariables:
                        k = midvariables.index(sonlist[t + 1])
                        for word in newlist[k]:
                            if (word in aritop) or (word in arithmeticall):
                                finish()
                    else:
                        finish()
        elif sonlist[t] == "nokta":
            if t == 0:
                finish()
            elif t == len(sonlist) - 1:
                finish()
            else:
                if not sonlist[t + 1] in tdigit:
                    finish()
                if not sonlist[t-1] in tdigit:
                    finish()
        elif sonlist[t] == ".":
            if t == 0:
                finish()
            elif t == len(sonlist) - 1:
                finish()
            else:
                if not sonlist[t - 1] in digit:
                    finish()
                if not sonlist[t + 1] in digit:
                    finish()
        elif sonlist[t] in keylist:  # anadaki degiskenlerden biriyse
            if aritcont == 1:
                if not mydict[sonlist[t]] in possvaluewithoutlogic:
                    finish()
                if t == 0:
                    if not sonlist[t + 1] in aritop:
                        finish()
                elif t == len(sonlist) - 1:
                    if not sonlist[t - 1] in aritop:
                        finish()
                else:
                    if not sonlist[t + 1] in aritop:
                        if not sonlist[t + 1]==")":
                            finish()
            elif logcont == 1:
                if not mydict[sonlist[t]] in i_term:
                    finish()
                if t == 0:
                    if not sonlist[t + 1] in logop:
                        finish()
                elif t == len(sonlist) - 1:
                    if not sonlist[t - 1] in logop:
                        finish()
                else:
                    if not sonlist[t + 1] in logop:
                        if not sonlist[t + 1]==")":
                            finish()
        elif sonlist[t] in midvariables:
            y = midvariables.index(sonlist[t])
            for p in range(len(newlist[y])):
                if aritcont == 1:
                    if (newlist[y][p] in logop) or (newlist[y][p] in i_term):
                        finish()
                    if t == 0:
                        if not sonlist[t+1] in aritop:
                            finish()
                    elif t == len(sonlist) - 1:
                        if not sonlist[t-1] in aritop:
                            finish()
                    else:
                        if not sonlist[t+1] in aritop:
                            if not sonlist[t + 1] == ")":
                                finish()
                elif logcont == 1:
                    if (newlist[y][p] in arithmeticall) or (newlist[y][p] in aritop):
                            finish()
                    if t == 0:
                        if not sonlist[t + 1] in logop:
                            finish()
                    elif t == len(sonlist) - 1:
                        if not sonlist[t - 1] in logop:
                            finish()
                    else:
                        if not sonlist[t + 1] in logop:
                            if not sonlist[t + 1] == ")":
                                finish()
        elif sonlist[t] in floatpoint:
            if t==0:
                if sonlist[t+1] not in aritop:
                    if not sonlist[t+1]==")":
                        finish()
            elif t==len(sonlist)-1:
                if sonlist[t-1] not in aritop:
                    finish()
            else:
                if not sonlist[t+1]  in aritop:
                    if not sonlist[t+1]==")":
                        finish()
        else:
            finish()
if len(sonlist)>1:
    if acpar!=kapapar:
        finish()

f = open("calc.out", "w")
f.write("Here Comes the Sun")
f.close()
import sys
sys.exit()


#!/usr/bin/env python
# coding: utf8

#Inhalt
#Diese Skript erzeugt skripte, aus denen das LaTeX Paket Tikz Zahlenstrahle erzeugen kann.

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())

def erzeugePythagorasBerechnen(seitenwahl='',mitBogen=True,mitText=True):
#Diese Funktion erzeugt eine Aufgabe, bei der 2 Seiten eines Rechtwinkligen Dreiecks vorgegeben sind.
#Es soll die fehlende Seite berechnet werden.
#Aufruf:
#     [afg,lsg,[seitenAfg]]=erzeugePythagorasBerechnen(seitenwahl,mitBogen,mitText)
#Seitenwahl: seitenwahl=0 --> a, seitenwahl=1 --> b, seitenwahl=2 --> c
#Die Seite c ist die Hypothenuse
    rechtWinkBei='gamma'  #-->a=kx,b=ky,c=hyp
    afg=(['\\pbox{\\linewidth}{']+['Berechne die fehlende Seite: \\\\']) if mitText else []
    einheit=random.choice(['mm','cm','dm','m','km'])
    seiten=['a','b','c']
    seitenAfg=list(seiten)
    seitenwahl=seitenwahl if seitenwahl in seiten else random.choice(seiten)
    seitenAfg.remove(seitenwahl)
    seitenOp=list(seitenAfg)
    if 'c' in seitenOp :
        seitenOp.remove('c')
    a,b=random.randint(20,50)/10.0,random.randint(20,50)/10.0
    c=(a**2+b**2)**0.5
    labelDic={'a':f'{strNW(a)} {einheit}','b':f'{strNW(b,True)} {einheit}','c':f'{strNW(c,True)} {einheit}'}
    label=[(labelDic[x] if x in seitenAfg else '')  for x in seiten]
    afg=afg+dreieckRechtw(k=[a*1.2,b*0.8],label=label,mitBogen=mitBogen)+(['}'] if mitText else [])
    setzePBox(afg)
    lsg=['$\\begin{aligned}']
    lsg.append(f'\\mbox{{geg: }} {seitenAfg[0]}&={strNW(eval(seitenAfg[0]),True)}~{einheit}& &\\\\')
    lsg.append(f' {seitenAfg[1]}&={strNW(eval(seitenAfg[1]),True)}~{einheit} & &\\\\')
#    lsg.append('\\\\')
    lsg.append(f'\\mbox{{ges: }} {seitenwahl}&=?& & \\\\')
#    lsg.append('\\\\')
    lsg.append(' & & & \\\\ ')
    lsg.append('c^2&=a^2+b^2 & & \\\\ ')
    lsg.append(f'c^2&=a^2+b^2 & & \\\\'.replace(seitenAfg[0],strNW(eval(seitenAfg[0]),True)).replace(seitenAfg[1],strNW(eval(seitenAfg[1]),True)))
    op="" if seitenwahl=='c' else f'\\mid~-{strNW(eval(seitenOp[0])**2,True)},~\\mbox{{umdrehen}}'
    lsg.append(f'c^2&=a^2+b^2 & & {op} \\\\'.replace(f'{seitenAfg[0]}^2',strNW(eval(seitenAfg[0])**2,True)).replace(f'{seitenAfg[1]}^2',strNW(eval(seitenAfg[1])**2,True)))
    lsg.append(f'{seitenwahl}^2&={strNW(eval(seitenwahl)**2,True)} & & \\mid~\\sqrt{{~}} \\\\')
    lsg.append(f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{{seitenwahl}~=~{strNW(eval(seitenwahl),True)}~{einheit}}}}}}}')
    lsg.append(f'{seitenwahl}&={strNW(eval(seitenwahl),True)}~{einheit}& & \\\\')
    lsg.append('\\end{aligned}$')
    return [afg,lsg,[seitenAfg]]

def erzeugePythagorasFormulieren(seitenBeshr=True,pktBeschr=False,gemischt=False,mitBogen=True,mitText=True):
#Diese Funktion erzeugt eine Aufgaben, mit der aus vorgegebenen Seiten und/oder Punkten
#der Pythagoras formuliert werden soll.
    afg=['Formuliere den Pythagoras:'] if mitText else ['']
    seiten=['']*3
    while not(len(set(seiten))==len(seiten)):
        seiten = [random.choice(buchstabenKlein) for i in range(3)]
    punkte=[seiten[1].upper(),seiten[2].upper(),seiten[0].upper()]
    sLsg=list(seiten)
    pLsg=list(punkte)
    if gemischt:
        auswahl = [''] * 3
        while not(len(set(auswahl))==len(auswahl)):
            auswahl = [random.randint(0,2) for i in range(random.randint(1,2))]
        for i in auswahl:
            punkte[i]=''
        for i in range(3):
            if i not in auswahl:
                seiten[i]=''
    else:
        seiten=['']*3 if not seitenBeshr else seiten
        punkte=['']*3 if not pktBeschr else punkte
    kx=random.randint(15,40)/10
    ky=random.randint(15,40)/10
    rotWinkel=random.randint(0,360)
    afg=['\\pbox{\\linewidth}{']+afg+['\\\\']
    afg=(afg if mitText else [])+dreieckRechtw(k=[kx,ky],label=seiten,punkte=punkte,mitBogen=mitBogen,dR=rotWinkel)
    #dreieckRechtwinklig(kx=kx,ky=ky,rotWinkel=rotWinkel,seiten=seiten,punkte=punkte,mitBogen=mitBogen,rechtWinkBei=winkel[winkelWahl])
    afg=afg+(['}'] if mitText else [])
    lsg=['\\pbox{\\linewidth}{']
    lsg=lsg+dreieckRechtw(k=[kx,ky],label=sLsg,punkte=pLsg,mitBogen=True,dR=rotWinkel)
    lsg=lsg+['\\\\']
    lsg=lsg+['$'+sLsg[2]+'^2='+sLsg[0]+'^2+'+sLsg[1]+'^2$']+['\\\\']
    lsg=lsg+['}']
    return [afg,lsg,[seiten,punkte]]


def erzeugeTrapezUmfangBerechnung(mitText=True):
    afg=(['\\pbox{\\linewidth}{']+['Berechne den Umfang: \\\\']) if mitText else ['']
    einheit=random.choice(['mm','cm','dm','m','km'])
    seitenBuchst=['a','b','d','c'] #[chr(i) for i in range(97,101)]
    seiten=[random.randint(30, 100)/10 for i in range(4)]
    while abs(seiten[0]-seiten[3])<0.5:
        seiten=[random.randint(30, 100)/10 for i in range(4)]
    seiten[1]=((seiten[0]-seiten[3])**2+seiten[2]**2)**0.5
    auswahl=random.randint(0,3)
    sAfg=[f'{strNW(x,True)} {einheit}' for i,x in enumerate(seiten)]
    sAfgLabel=[f'{seitenBuchst[i]}={strNW(x,True)} {einheit}' for i,x in enumerate(seiten)]
    sAfg[auswahl]=''
    sAfgLabel[auswahl]=f'{seitenBuchst[auswahl]}=?'
    afg=afg+trapezEinSeiteSenkrecht(a=seiten[0]/2,c=seiten[2]/2,d=seiten[3]/2,aStr=sAfgLabel[0],bStr=sAfgLabel[1],cStr=sAfgLabel[2],dStr=sAfgLabel[3])
    if mitText:
        afg.append('}')
    lsg=['\\pbox{\\linewidth}{']
    sAfgLabel[auswahl]=f'{seitenBuchst[auswahl]}={strNW(seiten[auswahl],True)} {einheit}'
    lsg=lsg+trapezEinSeiteSenkrecht(a=seiten[0]/2,c=seiten[2]/2,d=seiten[3]/2,aStr=sAfgLabel[0],bStr=sAfgLabel[1],cStr=sAfgLabel[2],dStr=sAfgLabel[3],zeichneX=True)
    lsg=lsg+['\\\\']
    lsg=lsg+['$\\begin{aligned}']
    for i,s in enumerate(sAfg):
        if len(s)>0:
            lsg.append(f'{"$$mbox{{geg: }}" if i==0 or (auswahl==0 and i==1) else ""} {seitenBuchst[i]}&={s} & &\\\\'.replace('$$','\\'))
    lsg.append(f'$$mbox{{ges: }} u&=? & &\\\\'.replace('$$','\\'))
    if auswahl==0 or auswahl==3:
        para=3 if auswahl==0 else 0
        op='+' if (auswahl==0 and seiten[0]>seiten[3]) or (auswahl==3 and seiten[3]>seiten[0]) else '-'
        maxAdStr=max(seiten[0],seiten[3])
        minAdStr=min(seiten[0],seiten[3])
        lsg.append(F'b^2&=d^2+x^2 & & \\\\')
        lsg.append(F'{strNW(seiten[1],True)}^2              &={strNW(seiten[2],True)}^2+x^2   & &\\\\')
        lsg.append(F'{strNW(seiten[1]**2,True)}             &={strNW(seiten[2]**2,True)}+x^2  & &\\mid -{strNW(seiten[2]**2,True)} \\\\')
        lsg.append(F'{strNW(seiten[1]**2-seiten[2]**2,True)}&=x^2                             & &\\mid \\sqrt{{~}},\\mbox{{ umdrehen}} \\\\')
        x=(seiten[1]**2-seiten[2]**2)**0.5
        erg=F'x&={strNW(x,True)}~{einheit}'
        lsg=lsg+['\\makebox[0pt][l]{\\uline{\phantom{'+erg.replace('&','')+'}}}']
        lsg=lsg+[erg+' &']+['\\\\']
        lsg=lsg+[F'{seitenBuchst[auswahl]}&={seitenBuchst[para]}{op}x& &']+['\\\\']
        lsg=lsg+[F'{seitenBuchst[auswahl]}&={strNW(seiten[para])}{op}{strNW(x,True)}& &']+['\\\\']
        aOderD=F'{seitenBuchst[auswahl]}&={strNW(eval(F"{seiten[para]}{op}{x}"),True)}~{einheit}'
        lsg=lsg+['\\makebox[0pt][l]{\\uline{\phantom{'+aOderD.replace('&','~~')+'}}}']
        lsg=lsg+[aOderD+'& &']+['\\\\']
    elif auswahl==1:
        maxAdStr=max(seiten[0],seiten[3])
        minAdStr=min(seiten[0],seiten[3])
        lsg.append(f'x&={"a-c" if seiten[0]>seiten[3] else "c-a"} & & \\\\')
        lsg.append(f'x&={strNW(maxAdStr)}-{strNW(minAdStr)} & & \\\\')
        lsg.append(f'\\makebox[0pt][l]{{\\uline{{\\phantom{{ x~=~{strNW(maxAdStr-minAdStr)} }} }} }} ')
        lsg.append(f'x&={strNW(maxAdStr-minAdStr)} & & \\\\')
        lsg=lsg+[F'b^2&=d^2+x^2 & &']+['\\\\']
        lsg=lsg+[F'b^2&={strNW(seiten[2])}^2+{strNW(maxAdStr-minAdStr)}^2 &']+['\\\\']
        lsg=lsg+[F'b^2&={strNW(seiten[2]**2)}+{strNW((maxAdStr-minAdStr)**2)} &']+['\\\\']
        lsg=lsg+[F'b^2&={strNW(seiten[2]**2+(maxAdStr-minAdStr)**2)} &\\mid \\sqrt{{~}}']+['\\\\']
        erg=F'b&={strNW((seiten[2]**2+(maxAdStr-minAdStr)**2)**0.5,True)}~{einheit}'
        lsg=lsg+['\\makebox[0pt][l]{\\uline{\phantom{'+erg.replace('&','')+'}}}']
        lsg=lsg+[erg+' &']+['\\\\']
    elif auswahl==2:
        maxAdStr=max(seiten[0],seiten[3])
        minAdStr=min(seiten[0],seiten[3])
        lsg.append(f'x&={"a-c" if seiten[0]>seiten[3] else "c-a"}  & & \\\\')
        lsg.append(f'x&={strNW(maxAdStr)}-{strNW(minAdStr)} & & \\\\')
        lsg.append(f'x&={strNW(maxAdStr-minAdStr,True)} & & \\\\')
        lsg=lsg+[F'b^2&=d^2+x^2 & &']+['\\\\']
        lsg=lsg+[F'{strNW(seiten[1],True)}^2&=d^2+{strNW(maxAdStr-minAdStr,True)}^2 & & ']+['\\\\']
        lsg=lsg+[F'{strNW(seiten[1]**2,True)}&=d^2+{strNW((maxAdStr-minAdStr)**2,True)} & & \\mid ~-{strNW((maxAdStr-minAdStr)**2,True)} ']+['\\\\']
        lsg=lsg+[F'{strNW(seiten[1]**2-(maxAdStr-minAdStr)**2,True)}&=d^2 & &\\mid \\sqrt{{~}}, \\mbox{{~umdrehen}}']+['\\\\']
        erg=F'd&={strNW((seiten[1]**2-(maxAdStr-minAdStr)**2)**0.5,True)}~{einheit}'
        lsg=lsg+['\\makebox[0pt][l]{\\uline{\phantom{'+erg.replace('&','')+'}}}']
        lsg=lsg+[erg+' &']+['\\\\']
    lsg=lsg+[F'U&={"+".join([strNW(x,True) for x in seiten])} & & \\\\']
    erg=F'U&={strNW(eval("+".join([str(x) for x in seiten])),True)}~{einheit}'
    lsg=lsg+['\\makebox[0pt][l]{\\uuline{\phantom{'+erg.replace('&','')+'}}}']
    lsg=lsg+[erg+' & &']+['\\\\']
    lsg=lsg+['\\end{aligned}$']
    lsg=lsg+['}']
    return [afg,lsg,[seiten]]



def erzeugePythagorasFormulierenAlt(seitenBeshr=True,pktBeschr=False,gemischt=False,mitBogen=True,mitText=True):
#Diese Funktion erzeugt eine Aufgaben, mit der aus vorgegebenen Seiten und/oder Punkten
#der Pythagoras formuliert werden soll.
    afg=['Formuliere den Pythagoras:'] if mitText else ['']
    winkel=['alpha','beta','gamma']
    winkelWahl=random.randint(0,2)
    seiten=['']*3
    while not(len(set(seiten))==len(seiten)):
        seiten = [random.choice(buchstabenKlein) for i in range(3)]
    punkte=[x.upper() for x in seiten]
    sLsg=list(seiten)
    pLsg=list(punkte)
    if gemischt:
        auswahl = [''] * 3
        while not(len(set(auswahl))==len(auswahl)):
            auswahl = [random.randint(0,2) for i in range(random.randint(1,2))]
        for i in auswahl:
            punkte[i]=''
        for i in range(3):
            if i not in auswahl:
                seiten[i]=''
    else:
        seiten=['']*3 if not seitenBeshr else seiten
        punkte=['']*3 if not pktBeschr else punkte
    kx=random.randint(1,4)
    ky=random.randint(1,4)
    rotWinkel=random.randint(0,360)
    afg=['\\pbox{\\hsize}{']+afg+['\\\\']
    afg=(afg if mitText else [])+dreieckRechtw(k=[kx,ky],label=seiten,punkte=punkte,mitBogen=mitBogen)
    #dreieckRechtwinklig(kx=kx,ky=ky,rotWinkel=rotWinkel,seiten=seiten,punkte=punkte,mitBogen=mitBogen,rechtWinkBei=winkel[winkelWahl])
    afg=afg+(['}'] if mitText else [])
    lsg=['\\pbox{\\hsize}{']
    lsg=lsg+dreieckRechtwinklig(kx=kx,ky=ky,rotWinkel=rotWinkel,seiten=sLsg,punkte=pLsg,mitBogen='True',rechtWinkBei=winkel[winkelWahl])
    lsg=lsg+['\\\\']
    lsg=lsg+['$'+sLsg[winkelWahl]+'^2='+sLsg[winkelWahl-1]+'^2+'+sLsg[winkelWahl-2]+'^2$']+['\\\\']
    lsg=lsg+['}']
    return [afg,lsg,[seiten,punkte]]

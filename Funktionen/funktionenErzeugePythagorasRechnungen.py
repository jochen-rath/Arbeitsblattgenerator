#!/usr/bin/env python
# coding: utf8

#Inhalt
#Diese Skript erzeugt skripte, aus denen das LaTeX Paket Tikz Zahlenstrahle erzeugen kann.

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())

def erzeugePythagorasBerechnen(seitenwahl=-1,mitBogen=True,mitText=True):
#Diese Funktion erzeugt eine Aufgabe, bei der 2 Seiten eines Rechtwinkligen Dreiecks vorgegeben sind.
#Es soll die fehlende Seite berechnet werden.
#Aufruf:
#     [afg,lsg,[seitenAfg]]=erzeugePythagorasBerechnen(seitenwahl,mitBogen,mitText)
#Seitenwahl: seitenwahl=0 --> a, seitenwahl=1 --> b, seitenwahl=2 --> c
#Die Seite c ist die Hypothenuse
    rechtWinkBei='gamma'  #-->a=kx,b=ky,c=hyp
    afg=['Berechne die fehlende Seite:'] if mitText else ['']
    einheit=random.choice(['mm','cm','dm','m','km'])
    seitenwahl=seitenwahl if (seitenwahl>=0 and seitenwahl<=3) else random.randint(0,2)
    seiten=['a','b','c']
    a,b=random.randint(40,100)/10.0,random.randint(20,100)/10.0
    c=(a**2+b**2)**0.5
    seitenAfg=[strNW(x,True)+' '+einheit for x in [a,b,c]]
    seitenAfg[seitenwahl]=seiten[seitenwahl]
    afg=afg+dreieckRechtwinklig(kx=a/2,ky=b/2,rotWinkel=random.randint(0,360),seiten=seitenAfg,mitBogen=mitBogen,rechtWinkBei=rechtWinkBei)
    setzePBox(afg)
    lsg=['\\pbox{\\linewidth}{']
    if seitenwahl==0:
        lsg=lsg+['$\\begin{aligned}']
        lsg=lsg+['a^2&=c^2-b^2 &\\mid \\sqrt{~}']+['\\\\']
        lsg=lsg+['a&=\\sqrt{c^2-b^2}&']+['\\\\']
        lsg=lsg+[ '&=\\sqrt{'+strNW(c,True)+'^2-'+strNW(b,True)+'^2}&']+['\\\\']
        lsg=lsg+[ '&=\\sqrt{'+strNW(c**2,True)+'-'+strNW(b**2,True)+'}&']+['\\\\']
        lsg=lsg+[ '&=\\sqrt{'+strNW(c**2-b**2,True)+'}&']+['\\\\']
        erg='a&='+strNW(a,True)+' \\mbox{ '+einheit+'}&'
        lsg=lsg+['\\makebox[0pt][l]{\\uuline{\phantom{'+erg.replace('&','')+'}}}']
        lsg=lsg+[erg]+['\\\\']
    if seitenwahl==1:
        lsg=lsg+['$\\begin{aligned}']
        lsg=lsg+['b^2&=c^2-a^2 &\\mid \\sqrt{~}']+['\\\\']
        lsg=lsg+['b&=\\sqrt{c^2-a^2}&']+['\\\\']
        lsg=lsg+[ '&=\\sqrt{'+strNW(c,True)+'^2-'+strNW(a,True)+'^2}&']+['\\\\']
        lsg=lsg+[ '&=\\sqrt{'+strNW(c**2,True)+'-'+strNW(a**2,True)+'}&']+['\\\\']
        lsg=lsg+[ '&=\\sqrt{'+strNW(c**2-a**2,True)+'}&']+['\\\\']
        erg='b&='+strNW(b,True)+' \\mbox{ '+einheit+'}&'
        lsg=lsg+['\\makebox[0pt][l]{\\uuline{\phantom{'+erg.replace('&','')+'}}}']
        lsg=lsg+[erg]+['\\\\']
    if seitenwahl==2:
        lsg=lsg+['$\\begin{aligned}']
        lsg=lsg+['c^2&=a^2+b^2 &\\mid \\sqrt{~}']+['\\\\']
        lsg=lsg+['c&=\\sqrt{a^2+b^2}&']+['\\\\']
        lsg=lsg+[ '&=\\sqrt{'+strNW(a,True)+'^2+'+strNW(b,True)+'^2}&']+['\\\\']
        lsg=lsg+[ '&=\\sqrt{'+strNW(a**2,True)+'+'+strNW(b**2,True)+'}&']+['\\\\']
        lsg=lsg+[ '&=\\sqrt{'+strNW(a**2+b**2,True)+'}&']+['\\\\']
        erg='c&='+strNW(c,True)+' \\mbox{ '+einheit+'}&'
        lsg=lsg+['\\makebox[0pt][l]{\\uuline{\phantom{'+erg.replace('&','')+'}}}']
        lsg=lsg+[erg]+['\\\\']
    lsg=lsg+['\\end{aligned}$}']
    return [afg,lsg,[seitenAfg]]

def erzeugePythagorasFormulieren(seitenBeshr=True,pktBeschr=False,gemischt=False,mitBogen=True,mitText=True):
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
    afg=(afg if mitText else [])+dreieckRechtwinklig(kx=kx,ky=ky,rotWinkel=rotWinkel,seiten=seiten,punkte=punkte,mitBogen=mitBogen,rechtWinkBei=winkel[winkelWahl])
    afg=afg+(['}'] if mitText else [])
    lsg=['\\pbox{\\hsize}{']
    lsg=lsg+dreieckRechtwinklig(kx=kx,ky=ky,rotWinkel=rotWinkel,seiten=sLsg,punkte=pLsg,mitBogen='True',rechtWinkBei=winkel[winkelWahl])
    lsg=lsg+['\\\\']
    lsg=lsg+['$'+sLsg[winkelWahl]+'^2='+sLsg[winkelWahl-1]+'^2+'+sLsg[winkelWahl-2]+'^2$']+['\\\\']
    lsg=lsg+['}']
    return [afg,lsg,[seiten,punkte]]


def erzeugeTrapezUmfangBerechnung(mitText=True):
    afg=['Berechne den Umfang:'] if mitText else ['']
    einheit=random.choice(['mm','cm','dm','m','km'])
    seitenBuchst=['a','b','c','d'] #[chr(i) for i in range(97,101)]
    seiten=[random.randint(30, 100)/10 for i in range(4)]
    seiten[1]=((seiten[0]-seiten[3])**2+seiten[2]**2)**0.5
    auswahl=random.randint(0,3)
    sAfg=[strNW(x,True)+' '+einheit for x in seiten]
    sAfg[auswahl]=''
    afg=afg+trapezEinSeiteSenkrecht(a=seiten[0]/2,c=seiten[2]/2,d=seiten[3]/2,aStr=sAfg[0],bStr=sAfg[1],cStr=sAfg[2],dStr=sAfg[3])
    lsg=['\\pbox{6cm}{']
    lsg=lsg+trapezEinSeiteSenkrecht(a=seiten[0]/2,c=seiten[2]/2,d=seiten[3]/2,aStr=sAfg[0],bStr=sAfg[1],cStr=sAfg[2],dStr=sAfg[3],zeichneX=True)
    lsg=lsg+['\\\\']
    lsg=lsg+['$\\begin{aligned}']
    if auswahl==0 or auswahl==3:
        para=3 if auswahl==0 else 0
        op='+' if (auswahl==0 and seiten[0]>seiten[3]) or (auswahl==3 and seiten[3]>seiten[0]) else '-'
        maxAdStr=max(seiten[0],seiten[3])
        minAdStr=min(seiten[0],seiten[3])
        lsg=lsg+[F'x^2&=\\sqrt{{b^2-c^2}} &']+['\\\\']
        lsg=lsg+[F'x^2&=\\sqrt{{{strNW(seiten[1],True)}^2-{strNW(seiten[2])}^2}} &']+['\\\\']
        lsg=lsg+[F'x^2&=\\sqrt{{{strNW(seiten[1]**2,True)}-{strNW(seiten[2]**2)}}} &']+['\\\\']
        lsg=lsg+[F'x^2&=\\sqrt{{{strNW(seiten[1]**2-seiten[2]**2,True)}}} &\\mid \\sqrt{{~}}']+['\\\\']
        x=(seiten[1]**2-seiten[2]**2)**0.5
        erg=F'x&={strNW(x,True)}~{einheit}'
        lsg=lsg+['\\makebox[0pt][l]{\\uline{\phantom{'+erg.replace('&','')+'}}}']
        lsg=lsg+[erg+' &']+['\\\\']
        lsg=lsg+[F'{seitenBuchst[auswahl]}&={seitenBuchst[para]}{op}x&']+['\\\\']
        lsg=lsg+[F'{seitenBuchst[auswahl]}&={strNW(seiten[para])}{op}{strNW(x,True)}&']+['\\\\']
        aOderD=F'{seitenBuchst[auswahl]}&={strNW(eval(F"{seiten[para]}{op}{x}"),True)}'
        lsg=lsg+['\\makebox[0pt][l]{\\uline{\phantom{'+aOderD.replace('&','')+'}}}']
        lsg=lsg+[aOderD+'&']+['\\\\']
    elif auswahl==1:
        maxAdStr=max(seiten[0],seiten[3])
        minAdStr=min(seiten[0],seiten[3])
        lsg=lsg+[F'b^2&=c^2+({strNW(maxAdStr)}-{strNW(minAdStr)})^2 &']+['\\\\']
        lsg=lsg+[F'b^2&={strNW(seiten[2])}^2+{strNW(maxAdStr-minAdStr)}^2 &']+['\\\\']
        lsg=lsg+[F'b^2&={strNW(seiten[2]**2)}+{strNW((maxAdStr-minAdStr)**2)} &']+['\\\\']
        lsg=lsg+[F'b^2&={strNW(seiten[2]**2+(maxAdStr-minAdStr)**2)} &\\mid \\sqrt{{~}}']+['\\\\']
        erg=F'b&={strNW((seiten[2]**2+(maxAdStr-minAdStr)**2)**0.5,True)}~{einheit}'
        lsg=lsg+['\\makebox[0pt][l]{\\uline{\phantom{'+erg.replace('&','')+'}}}']
        lsg=lsg+[erg+' &']+['\\\\']
    elif auswahl==2:
        maxAdStr=max(seiten[0],seiten[3])
        minAdStr=min(seiten[0],seiten[3])
        lsg=lsg+[F'c^2&={strNW(seiten[1],True)}^2-({strNW(maxAdStr,True)}-{strNW(minAdStr,True)})^2 &']+['\\\\']
        lsg=lsg+[F'c^2&={strNW(seiten[1],True)}^2-{strNW(maxAdStr-minAdStr,True)}^2 &']+['\\\\']
        lsg=lsg+[F'c^2&={strNW(seiten[1]**2,True)}-{strNW((maxAdStr-minAdStr)**2,True)} &']+['\\\\']
        lsg=lsg+[F'c^2&={strNW(seiten[1]**2-(maxAdStr-minAdStr)**2,True)} &\\mid \\sqrt{{~}}']+['\\\\']
        erg=F'c&={strNW((seiten[1]**2-(maxAdStr-minAdStr)**2)**0.5,True)}~{einheit}'
        lsg=lsg+['\\makebox[0pt][l]{\\uline{\phantom{'+erg.replace('&','')+'}}}']
        lsg=lsg+[erg+' &']+['\\\\']
    lsg=lsg+[F'U&={"+".join([strNW(x,True) for x in seiten])} \\\\']
    erg=F'U&={strNW(eval("+".join([str(x) for x in seiten])),True)}~{einheit}'
    lsg=lsg+['\\makebox[0pt][l]{\\uuline{\phantom{'+erg.replace('&','')+'}}}']
    lsg=lsg+[erg+' &']+['\\\\']
    lsg=lsg+['\\end{aligned}$']
    lsg=lsg+['}']
    return [afg,lsg,[seiten]]

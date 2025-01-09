#!/usr/bin/env python
# coding: utf8

#Inhalt
#Diese Skript erzeugt skripte, aus denen das LaTeX Paket Tikz Zahlenstrahle erzeugen kann.

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())
import random


def erzeugeKreisberechnungen(typ='',mitText=True):
#Diese Funktion erzeugt eine Aufgaben, zum Lösen von Wurzelrechnungen
    typen=['Umfang','Flaeche','UmfangFlaeche','Radius','UmfachNachFlaeche','FlaecheNachUmfang']
    einheit=random.choice(['mm','cm','dm','m','km'])
    if typ not in typen:
        typ=random.choice(typen)
    r=random.choice([random.randint(10,100)/10.0,random.randint(100,1000)/100.0])
    r_d=[r,2*r]
    r_dStr=['r','d']
    rd_auswahl=random.randint(0,1)
    afg,lsg="",""
    werte={'r':r,'d':2*r,'u':2*math.pi*r,'A':math.pi*r**2}
#Berechnungen von u usw.
    if True:
        uAusR=[f'u&=2\\pi · r & & \\\\']
        uAusR.append(f'u&= 2\\pi · {strNW(werte["r"],True)}& & \\\\')
        uAusR.append(f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{u ={strNW(werte["u"],True)}~~{einheit}}}}}}}')
        uAusR.append(f'u&={strNW(werte["u"],True)}~{einheit}& & \\\\')
        uAusD=[f'u&=\\pi · d & & \\\\']
        uAusD.append(f'u&= \\pi · {strNW(werte["d"],True)}& & \\\\')
        uAusD.append(f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{u ={strNW(werte["u"],True)}~~{einheit}}}}}}}')
        uAusD.append(f'u&={strNW(werte["u"],True)}~{einheit}& & \\\\')
        rAusD=[f'r&=d:2 & & \\\\']
        rAusD.append(f'r&={strNW(werte["d"],True)}:2 & & \\\\')    
        rAusD.append(f'\\makebox[0pt][l]{{\\uline{{\\phantom{{u ={strNW(werte["u"],True)}~~{einheit}}}}}}}')
        rAusD.append(f'r&={strNW(werte["r"],True)} & & \\\\')    
        A=[f'A&=\\pi·r^2 & & \\\\']
        A.append(f'A&=\\pi·{strNW(werte["r"],True)}^2 & & \\\\')
        A.append(f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{u ={strNW(werte["u"],True)}~~{einheit}}}}}}}')
        A.append(f'A&={strNW(werte["A"],True)}~{einheit}^2& & \\\\')
        rAusU=[f'u&=2\\pi · r & & \\\\']
        rAusU.append(f'{strNW(werte["u"],True)}&=2\\pi· r & &\\mid :(2·\\pi)\\mbox{{, umdrehen}} \\\\')
        rAusU.append(f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{u ={strNW(werte["u"],True)}~~{einheit}}}}}}}')
        rAusU.append(f'r&={strNW(werte["r"],True)}~{einheit}& & \\\\')
        rAusA=[f'A&=\\pi · r^2 & & \\\\']
        rAusA.append(f'{strNW(werte["A"],True)}&=\\pi· r^2 & &\\mid :\\pi \\\\')
        rAusA.append(f'{strNW(werte["A"]/math.pi,True)}&=r^2 & &\\mid \\sqrt{{~~}}\\mbox{{, umdrehen}}  \\\\')
        rAusA.append(f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{u ={strNW(werte["u"],True)}~~{einheit}}}}}}}')
        rAusA.append(f'r&={strNW(werte["r"],True)}~{einheit}& & \\\\')
    rechnung,geg,ges=[],[],[]  
    if typ=='Umfang':
        afg=F'{"Berechne den Kreisumfang für " if mitText else ""}${{{r_dStr[rd_auswahl]}={strNW(r_d[rd_auswahl])}~{einheit}~~\\rightarrow u=?}}$'
        lsg=F'$u={"2XXXXcdot" if not rd_auswahl else ""}\\pi\\cdot{strNW(r_d[rd_auswahl],True)}='
        lsg=lsg+strNW(eval(F'{"2*" if not rd_auswahl else "" }math.pi*{r_d[rd_auswahl]}'),True)+einheit+'$'
        lsg=lsg.replace('XXXX','\\')
        geg=[r_dStr[rd_auswahl]]
        ges=['u']
        rechnung=uAusR if r_dStr[rd_auswahl]=='r' else uAusD
    if typ=='Flaeche':
        afg=F'{"Berechne die Kreisfläche für " if mitText else ""}${{{r_dStr[rd_auswahl]}={strNW(r_d[rd_auswahl])}~{einheit}~~\\rightarrow A=?}}$'
        lsg=F'$A=\\pi\\cdot{"XXXXfrac{" if rd_auswahl else ""}{r_d[rd_auswahl]}^2{"}{4}" if rd_auswahl else ""}='
        lsg=lsg+strNW(eval(F'math.pi*{r_d[rd_auswahl]}**2{"/4" if rd_auswahl else ""}'),True)+einheit+'^2$'
        lsg=lsg.replace('XXXX','\\')
        geg=[r_dStr[rd_auswahl]]
        ges=['A']
        if r_dStr[rd_auswahl]=='d':
            rechnung=rechnung+rAusD
        rechnung=rechnung+A
    if typ=='UmfangFlaeche':
        afg=F'{"Berechne den Kreisumfang, die Fläche für " if mitText else ""}${{{r_dStr[rd_auswahl]}={strNW(r_d[rd_auswahl])}~{einheit}~~\\rightarrow u,A=?}}$'        
        geg=[r_dStr[rd_auswahl]]
        ges=['u','A']
        rechnung=uAusR if r_dStr[rd_auswahl]=='r' else uAusD
        if r_dStr[rd_auswahl]=='d':
            rechnung=rechnung+rAusD
        rechnung=rechnung+A
    if typ=='Radius':
        afg=F'{"Berechne den Radius für " if mitText else ""}${{u={strNW(2*math.pi*r,True)}~{einheit}~~\\rightarrow r=?}}$'
        geg=['u']
        ges=['r']
        rechnung=rAusU
    if typ=='UmfachNachFlaeche':
        afg=F'{"Berechne die Kreisfläche für " if mitText else ""}${{u={strNW(2*math.pi*r,True)}~{einheit}~~\\rightarrow A=?}}$'
        geg=['u']
        ges=['A']
        rechnung=rechnung+rAusU
        rechnung=rechnung+A
    if typ=='FlaecheNachUmfang':
        afg=F'{"Berechne den Kreisumfang für " if mitText else ""}${{A={strNW(math.pi*r**2,True)}~{einheit}^2~~\\rightarrow u=?}}$'
        geg=['A']
        ges=['u']
        rechnung=rechnung+rAusA
        rechnung=rechnung+uAusR
    lsg=['$\\begin{aligned}']
    lsg.append(f'\\mbox{{geg: }} {geg[0]}&={strNW(werte[geg[0]],True)}~{einheit}& &\\\\')
    for z in geg[1:]:
        lsg.append(f'{z}&={strNW(werte[z],True)}~{einheit}& &\\\\')
    lsg.append(f'\\mbox{{ges: }} {ges[0]}&=?& & \\\\')
    for z in ges[1:]:
        lsg.append(f'{z}&=?& &\\\\')
    lsg=lsg+rechnung
    lsg.append('\\end{aligned}$')
    return [afg,lsg,[r_d,rd_auswahl]]

def umfangDreieckMitHalbkreis(mitText=True):
    einheit=random.choice(['mm','cm','dm','m','km'])
    kx=random.randint(20,50)/10.0
    ky=random.randint(20,50)/10.0
    c = (kx ** 2 + ky ** 2) ** 0.5
    tikz=dreieckMitHalbkreis(kx=0.6*kx,ky=0.6*ky,seiten=['',F'{strNW(ky,True)} {einheit}',F'{strNW(kx,True)} {einheit}'],ohneHyp=True)
    if mitText:      
        afg=['\\pbox{\\linewidth}{']+['Berechne den Umfang von ']+tikz+['}']
    else:
        afg=tikz
    lsg = ['\\pbox{\\hsize}{']
    lsg=lsg+dreieckMitHalbkreis(kx=0.6*kx,ky=0.6*ky,seiten=[F'{strNW(c,True)} {einheit}',F'{strNW(ky,True)} {einheit}',F'{strNW(kx,True)} {einheit}'],ohneHyp=False)
    lsg=lsg+['\\\\']
    lsg=lsg+['$\\begin{aligned}']
    lsg=lsg+[F'u&={strNW(kx)} + {strNW(ky)}+\pi \\cdot x\\cdot \\frac12\\\\']
    lsg=lsg+[F'x^2&={strNW(kx)}^2 + {strNW(ky)}^2\\\\']
    lsg=lsg+[F'x^2&={strNW(kx**2+ky**2,True)}\\\\']
    lsg=lsg+[F'x&=\\sqrt{{{strNW(kx**2+ky**2,True)}}}\\\\']
    x =F'x&={strNW((kx**2+ky**2)**0.5,True)}~{einheit}\\\\'
    lsg = lsg + ['\\makebox[0pt][l]{\\uline{\phantom{' + x.replace('&', '') + '}}}']
    lsg = lsg + [x] + ['\\\\']
    lsg=lsg+[F'u&={strNW(kx)} + {strNW(ky)}+\pi \\cdot {strNW((kx**2+ky**2)**0.5,True)}\\cdot \\frac12\\\\']
    erg =F'u&={strNW(kx+ky+math.pi*((kx**2+ky**2)**0.5)*0.5,True)}~{einheit}\\\\'
    lsg = lsg + ['\\makebox[0pt][l]{\\uuline{\phantom{' + erg.replace('&', '') + '}}}']
    lsg = lsg + [erg] + ['\\\\']
    lsg=lsg+['\\end{aligned}$']
    lsg=lsg+['}']
    return [afg,lsg,[kx,ky]]

def erzeugeUmfangFlaecheKreisabschnitt(mitText=True):
    einheit='cm'
    r=random.randint(10,30)/10
    alpha=random.randint(10,359)
    afg = ['\\pbox{6cm}{']
    afg=afg+(['Bestimme die Bogenlänge und die Fläche von:\\\\']if mitText else [''])
    afg=afg+zeichneKreis(r=r,alpha=alpha,mitUmrandung=True)
    afg=afg+['}']
    lsg = ['\\pbox{7cm}{']
    lsg= lsg + ['Bogenlänge:\\\\']
    lsg=lsg+['$\\begin{aligned}']
    lsg=lsg+[F'b&=2\\pi r\\cdot\\frac{{alpha}}{{360}}=2\\pi \\cdot{strNW(r)}\\cdot\\frac{{{strNW(alpha)}}}{{360}}\\\\'.replace('alpha','\\alpha')]
    erg=F'b&={strNW(2*math.pi*r*alpha/360,True)} ~\\mbox{{{einheit}}}'
    lsg = lsg + ['\\makebox[0pt][l]{\\uuline{\phantom{' + erg.replace('&', '').replace('^','') + '}}}']
    lsg = lsg + [erg] + ['\\\\']
    lsg=lsg+['\\end{aligned}$\\\\']
    lsg=lsg+['Fläche:\\\\']
    lsg=lsg+['$\\begin{aligned}']
    lsg=lsg+[F'A&=\\pi r^2\\cdot\\frac{{alpha}}{{360}}=\\pi \\cdot{strNW(r)}^2\\cdot\\frac{{{strNW(alpha)}}}{{360}}\\\\'.replace('alpha','\\alpha')]
    lsg=lsg+[F'&=\\pi\\cdot {strNW(r**2)}\\cdot\\frac{{{strNW(alpha)}}}{{360}}\\\\']
    erg=F'A&={strNW(math.pi*r**2*alpha/360,True)}~\\mbox{{{einheit}}}^2'
    lsg = lsg + ['\\makebox[0pt][l]{\\uuline{\phantom{' + erg.replace('&', '').replace('^','') + '}}}']
    lsg = lsg + [erg] + ['\\\\']
    lsg=lsg+['\\end{aligned}$']
    lsg=lsg+['}']
    return [afg,lsg,[r,alpha]]
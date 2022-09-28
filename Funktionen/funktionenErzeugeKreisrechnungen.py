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
    if typ=='Umfang':
        afg=F'{"Berechne den Kreisumfang für " if mitText else ""}${{{r_dStr[rd_auswahl]}={strNW(r_d[rd_auswahl])}~{einheit}}}$'
        lsg=F'$u={"2XXXXcdot" if not rd_auswahl else ""}\\pi\\cdot{strNW(r_d[rd_auswahl],True)}='
        lsg=lsg+strNW(eval(F'{"2*" if not rd_auswahl else "" }math.pi*{r_d[rd_auswahl]}'),True)+einheit+'$'
        lsg=lsg.replace('XXXX','\\')
    if typ=='Flaeche':
        afg=F'{"Berechne die Kreisfläche für " if mitText else ""}${{{r_dStr[rd_auswahl]}={strNW(r_d[rd_auswahl])}~{einheit}}}$'
        lsg=F'$A=\\pi\\cdot{"XXXXfrac{" if rd_auswahl else ""}{r_d[rd_auswahl]}^2{"}{4}" if rd_auswahl else ""}='
        lsg=lsg+strNW(eval(F'math.pi*{r_d[rd_auswahl]}**2{"/4" if rd_auswahl else ""}'),True)+einheit+'^2$'
        lsg=lsg.replace('XXXX','\\')
    if typ=='UmfangFlaeche':
        afg=F'{"Berechne den Kreisumfang, die Fläche für " if mitText else ""}${{{r_dStr[rd_auswahl]}={strNW(r_d[rd_auswahl])}~{einheit}~~\\rightarrow u,A=?}}$'
        lsg=['$\\begin{aligned}']
        u=F'u&={"2XXXXcdot" if not rd_auswahl else ""}\\pi\\cdot{strNW(r_d[rd_auswahl],True)}='
        u=u+strNW(eval(F'{"2*" if not rd_auswahl else "" }math.pi*{r_d[rd_auswahl]}'),True)+einheit
        lsg=lsg+[u.replace('XXXX','\\')]
        lsg=lsg+['\\\\']
        A=F'A&=\\pi\\cdot{"XXXXfrac{" if rd_auswahl else ""}{strNW(r_d[rd_auswahl],True)}^2{"}{4}" if rd_auswahl else ""}='
        A=A+strNW(eval(F'math.pi*{r_d[rd_auswahl]}**2{"/4" if rd_auswahl else ""}'), True)+einheit+'^2'
        lsg=lsg+[A.replace('XXXX','\\')]
        lsg=lsg+['\\end{aligned}$']
    if typ=='Radius':
        afg=F'{"Berechne den Radius für " if mitText else ""}${{u={strNW(2*math.pi*r,True)}~{einheit}~~\\rightarrow r=?}}$'
        lsg=F'$r=\\frac{{u}}{{2\\pi}}=\\frac{{{strNW(2*math.pi*r,True)}}}{{2\\pi}}={strNW(r)}~{einheit}$'
    if typ=='UmfachNachFlaeche':
        afg=F'{"Berechne die Kreisfläche für " if mitText else ""}${{u={strNW(2*math.pi*r,True)}~{einheit}~~\\rightarrow A=?}}$'
        lsg=['$\\begin{aligned}']
        lsg=lsg+[F'r&=\\frac{{u}}{{2\\pi}}=\\frac{{{strNW(2*math.pi*r,True)}}}{{2\\pi}}={strNW(r)}~{einheit} \\\\']
        lsg=lsg+[F'A&=\\pi\\cdot{strNW(r,True)}^2={strNW(math.pi*r**2,True)}~{einheit}^2 \\\\']
        lsg=lsg+['\\end{aligned}$']
    if typ=='FlaecheNachUmfang':
        afg=F'{"Berechne den Kreisumfang für " if mitText else ""}${{A={strNW(math.pi*r**2,True)}~{einheit}^2~~\\rightarrow u=?}}$'
        lsg=['$\\begin{aligned}']
        lsg=lsg+[F'r&=\\sqrt{{\\frac{{A}}{{\\pi}}}}=\\sqrt{{\\frac{{{strNW(math.pi*r**2,True)}}}{{\\pi}}}}={strNW(r)}~{einheit} \\\\']
        erg = F'u&=2\\pi\\cdot{strNW(r,True)}={strNW(2*math.pi*r,True)}~{einheit}'
        lsg = lsg + ['\\makebox[0pt][l]{\\uuline{\phantom{' + erg.replace('&', '').replace('\\','') + '}}}']
        lsg = lsg + [erg+'\\\\']
        lsg=lsg+['\\end{aligned}$']
    return [afg,lsg,[r_d,rd_auswahl]]

def umfangDreieckMitHalbkreis(mitText=True):
    einheit=random.choice(['mm','cm','dm','m','km'])
    kx=random.randint(20,50)/10.0
    ky=random.randint(20,50)/10.0
    c = (kx ** 2 + ky ** 2) ** 0.5
    afg=['Berechne den Umfang von ' if mitText else '']
    afg=afg+dreieckMitHalbkreis(kx=0.6*kx,ky=0.6*ky,seiten=['',F'{strNW(ky,True)} {einheit}',F'{strNW(kx,True)} {einheit}'],ohneHyp=True)
    lsg = ['\\pbox{5cm}{']
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
#!/usr/bin/env python
# coding: utf8
import random


#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())

def erzeugeSchraegbilderAfg(typ='Trapez',anzSpalten=2,mitText=True):
    auswahl = {'Dreieck': ['dreiecksPrimsa3DLiegend(g=werte["g"],h_D=werte["h_D"],h_K=werte["h_K"],messen=True,nurVorderseite=nurVorderseite,schraegbild=True)']}
    auswahl['Quader'] = ['quader3D(a=werte["a"],b=werte["b"],c=werte["h_K"],schraegbild=True,nurVorderseite=nurVorderseite)']
    auswahl['Trapez'] = ['trapezPrismaLiegend3D(a=werte["a"],c=werte["c"],h_T=werte["h_T"],h_K=werte["h_K"],schraegbild=True,nurVorderseite=nurVorderseite)']
    auswahl['Stern'] = ['sternPrisma(l=werte["l"],h_K=werte["h_K"],nurVorderseite=nurVorderseite)']
    breite=6 if anzSpalten==2 else 14
    breite=breite/2 if typ=='Sechseck' else breite
    varis=['a','b','c','g','h','h_K','h_D','h_T','l']
    werte={}
    for v in varis:
        werte[v]=random.randint(15,10*min(8,breite))/10
        #Auf 0.5 Runden:
        werte[v]=0.5 * round((werte[v]+0.01) / 0.5)
    werte["l"]=werte['l']/2
    h_K=werte['h_K']
    aufg=[F'\\pbox{{{breite } cm}}{{{F"Vervollständige das Schrägbild mit der Körperhöhe $h_K={strNW(h_K)} cm$: &&&&" if mitText else F"$h_K={strNW(h_K)}  cm$&&&&"}'.replace('&&&&','\\\\')]
    nurVorderseite=True
    scope=globals()|locals()
    aufg=aufg+eval(auswahl[typ][0],scope)
    nurVorderseite=False
    scope=globals()|locals()
    lsg=[F'\\pbox{{{ breite} cm}}{{']
    lsg=lsg+eval(auswahl[typ][0],scope)
    aufg.append('}')
    lsg.append('}')
    return [aufg,lsg,[]]
    

def erzeugeQuaderOberVolBerech(breitePbox='\\hsize',maxDim=14,einheit='cm'):
#Diese Funktion erzeugt eine Aufgabe und Lösung zum Addieren und Subtrahieren von Dezimalzahlen
#Ausgabe: [aufg,lsg]=erzeugeQuaderOberVolBerech(breitePbox)
    aufg=['\\pbox{'+str(breitePbox)+'cm}{Berechne das Volumen und die Oberfläche von:\\\\']
    lsg=['\\pbox{'+str(breitePbox)+'cm}{']
    a,b,c=[random.randint(1,maxDim) for i in range(3)]
    aufg=aufg+quader(a=a, b=b, c=c,ursprung=[0,0],buchstabe='Q',aName='a='+strNW(a)+' '+einheit,bName='b='+strNW(b)+'  '+einheit,cName='c='+strNW(c)+'  '+einheit)
    lsg.append('\\begingroup\\setlength{\\jot}{0.02cm}')
    lsg.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
    lsg.append('\\begin{tikzpicture}[show background grid]')
    lsg.append('\\node[left] at (0,-0.25) {Geg.: };')
    lsg.append('\\node[right] at (0,-0.25) {a = '+strNW(a,True)+' '+einheit+'};')
    lsg.append('\\node[right] at (0,-0.75) {b = '+strNW(b,True)+' '+einheit+'};')
    lsg.append('\\node[right] at (0,-1.25) {c = '+strNW(c,True)+' '+einheit+'};')
    lsg.append('\\node[left] at (0,-1.75) {Ges.: };')
    lsg.append('\\node[right] at (0,-1.75) {V  = ? };')
    lsg.append('\\node[right] at (0,-2.25) {O  = ? };')
    lsg.append('\\node[below right] at (0,-2.75) {')
    lsg.append('$\\begin{aligned}')
    lsg.append('V\\ &=\\ a\\cdot b \\cdot c\\\\')
    lsg.append('V\\ &=\\ '+strNW(a,True)+' \\cdot '+strNW(b,True)+' \\cdot '+strNW(c,True)+'\\\\')
#    lsg.append('V\\ &=\\ '+strNW(a,True)+einheit+' \\cdot '+strNW(b,True)+einheit+' \\cdot '+strNW(c,True)+einheit+'\\\\')
    lsg.append('\makebox[0pt][l]{\\uuline{\\phantom{V\\ =\\ '+strNW(a*b*c,True)+'\ \\mbox{'+einheit+'3}}}}')
    lsg.append('V\\ &=\\ '+strNW(a*b*c,True)+'\ \\mbox{'+einheit+'}^3\\\\')
    lsg.append('O\\ &=\\ 2ab+2ac+2bc\\\\')
    lsg.append('O\\ &=\\ 2\\cdot'+strNW(a,True)+'\\cdot'+strNW(b,True)+'+2\\cdot'+strNW(a,True)+'\\cdot'+strNW(c,True)+'+2\\cdot'+strNW(b,True)+'\\cdot'+strNW(c,True)+'\\\\')
#    lsg.append('O\\ &=\\ 2\\cdot'+strNW(a,True)+einheit+'\\cdot'+strNW(b,True)+einheit+'+2\\cdot'+strNW(a,True)+einheit+'\\cdot'+strNW(c,True)+einheit+'+2\\cdot'+strNW(b,True)+einheit+'\\cdot'+strNW(c,True)+einheit+'\\\\')
    lsg.append('\makebox[0pt][l]{\\uuline{\\phantom{O\\ =\\ '+strNW(2*a*b+2*a*c+2*b*c,True)+'\ \\mbox{'+einheit+'2}}}}')
    lsg.append('O\\ &=\\ '+strNW(2*a*b+2*a*c+2*b*c,True)+'\ \\mbox{'+einheit+'}^2\\\\')
    lsg.append('\\end{aligned}$};')
    lsg.append('\\end{tikzpicture}') 
    lsg.append('\\endgroup')
    aufg.append('}')
    lsg.append('}')
    return [aufg,lsg,[]]

def erzeugeQuaderFehlSeiteBerech(anzSpalten=2,mitText=True):
#Diese Funktion erzeugt eine Aufgabe und Lösung zum Addieren und Subtrahieren von Dezimalzahlen
#Ausgabe: [aufg,lsg]=erzeugeQuaderOberVolBerech(breitePbox)
    breitePbox=7 if anzSpalten==2 else 14
    einheit=random.choice(['mm','cm','dm','m','km'])
    VO=['V','O']
    seiten=['a','b','c']
    a,b,c=[random.randint(1,30) for i in range(3)]
    ges=random.choice(seiten)
    geg=list(seiten)+[random.choice(VO)]
    geg.remove(ges)
    aufg=['\\pbox{'+str(breitePbox)+'cm}{']
    aufg=aufg+(['Berechne die fehlende Seite eines Quaders bei folgenden gegebenen Größen:\\\\'] if mitText else [])
    lsg=['\\pbox{'+str(breitePbox)+'cm}{']
    V,O=a*b*c,2*(a*b+a*c+b*c)
    scope = locals()
    aufg=aufg + [', '.join([F'${x}={eval(x,scope)}~{einheit}{"^3" if x =="V" else ("^2" if x =="O" else "")}$' for x in geg])]+['\\\\']
    lsg.append('\\begingroup\\setlength{\\jot}{0.02cm}')
    lsg.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
    lsg.append('\\begin{tikzpicture}[show background grid]')
    lsg.append('\\node[left] at (0,-0.25) {Geg.: };')
    for x in geg:
        lsg.append(F'\\node[right] at (0,{-0.25-0.5*(len(lsg)-5)}) {{${x}={strNW(eval(x))} {einheit}{"^3" if x =="V" else ("^2" if x =="O" else "")}$}};')
    lsg.append(F'\\node[left] at (0,{-0.25-0.5*(len(lsg)-5)}) {{Ges.: }};')
    lsg.append(F'\\node[right] at (0,{-0.25-0.5*(len(lsg)-6)}) {{{ges}  = {strNW(eval(ges))} {einheit} }};')
    lsg.append(F'\\node[below right] at (0,{-0.25-0.5*(len(lsg)-6)}) {{')
    lsg.append('$\\begin{aligned}')
    formel='V=a*b*c' if 'V' in geg else 'O=2*a*b+2*a*c+2*b*c'
    lsg.append(F'{formel.split("=")[0]}&={formel.split("=")[1].replace("*","&&cdot ")}& & \\\\'.replace('&&','\\'))
    for x in geg:
        formel = formel.replace(x, str(eval(x)))
    lsg.append(F'{formel.split("=")[0]}&={formel.split("=")[1].replace("*","&&cdot ")}& & \\\\'.replace('&&','\\'))
    formel=F'{formel.split("=")[1]}={formel.split("=")[0]}'
#    lsg.append(F'{formel.split("=")[0].replace("*","&&cdot ")}&={formel.split("=")[1]}& & \\\\'.replace('&&','\\'))
    lsg=lsg+loeseGleichungEinfachMitEinerVariabel(G=formel,variable=ges,mitTikzUmrandung=False)[1:]
#Einheit einfügen.
    t=lsg[-1].split('&')
    t[1]=t[1]+F'~{einheit}'
    lsg[-1]='&'.join(t)
#Ergebniss doppelt unterstreichen
    lsg.insert(-1,'\\makebox[0pt][l]{\\uuline{\\phantom{$' + lsg[-1].replace('&', '') + '$}}}')
    lsg.append('\\end{aligned}$};')
    lsg.append('\\end{tikzpicture}')
    lsg.append('\\endgroup')
    aufg.append('}')
    lsg.append('}')
    return [aufg,lsg,[]]

def erzeugeDreiecksPrismaOberVolBerech(breitePbox='\\textwidth',maxDim=14,mitText=True,messen=False,einheit='cm'):
#Diese Funktion erzeugt eine Aufgabe und Lösung zum Addieren und Subtrahieren von Dezimalzahlen
#Ausgabe: [aufg,lsg]=erzeugeQuaderOberVolBerech(breitePbox)
    aufg=[F'\\pbox{{{breitePbox}{"" if "text" in breitePbox else "cm"}}}{{Berechne das Volumen und die Oberfläche{" und miss vorher die Seitenlängen" if messen else ""}:\\\\'] if mitText else []
    lsg=[F'\\pbox{{{breitePbox}{"" if "text" in breitePbox else "cm"}}}{{']
    Cy,hK=[random.randint(10,maxDim*10)/10.0 for i in range(2)]
    Ax=random.randint(10,(maxDim-1)*10)/10.0
    Bx=random.randint(10,maxDim*10-int(Ax*10))/10.0
    Cx=0
    c=Bx+Ax
    a=((Bx-Cx)**2+Cy**2)**0.5
    b=((Ax-Cx)**2+Cy**2)**0.5
    g=abs(-Ax-Bx)
    h=(Cx**2+Cy**2)**0.5
    aufg=aufg+dreiecksPrimsa(Ax=Ax,Bx=Bx,Cx=Cx,Cy=Cy,hK=hK,ursprung=[0,0],messen=messen)+(['}']  if mitText else [])
    lsg.append('\\begingroup\\setlength{\\jot}{0.02cm}')
    lsg.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
    lsg.append('\\begin{tikzpicture}[show background grid]')
    l1=len(lsg)
    lsg.append(F'\\node[left] at (0,{(len(lsg)-l1)*(-0.5)-0.25}) {{Geg.: }};')
    lsg.append(F'\\node[right] at (0,{(len(lsg)-l1)*(-0.5)-0.25}) {{a = {strNW(a,True)} {einheit}}};')
    lsg.append(F'\\node[right] at (0,{(len(lsg)-l1)*(-0.5)-0.25}) {{b = {strNW(b,True)} {einheit}}};')
    lsg.append(F'\\node[right] at (0,{(len(lsg)-l1)*(-0.5)-0.25}) {{c = {strNW(c,True)} {einheit}}};')
    lsg.append(F'\\node[right] at (0,{(len(lsg)-l1)*(-0.5)-0.25}) {{g = {strNW(g,True)} {einheit}}};')
    lsg.append(F'\\node[right] at (0,{(len(lsg)-l1)*(-0.5)-0.25}) {{h = {strNW(h,True)} {einheit}}};')
    lsg.append(F'\\node[right] at (0,{(len(lsg)-l1)*(-0.5)-0.25}) {{$h_K$ = {strNW(hK,True)} {einheit}}};')
    lsg.append(F'\\node[left] at (0,{(len(lsg)-l1)*(-0.5)-0.25}) {{Ges.: }};')
    lsg.append(F'\\node[right] at (0,{(len(lsg)-l1)*(-0.5)-0.25}) {{V  = ? }};')
    lsg.append(F'\\node[right] at (0,{(len(lsg)-l1)*(-0.5)-0.25}) {{O  = ? }};')
    lsg.append(F'\\node[below right] at (0,{(len(lsg)-l1)*(-0.5)-0.25}) {{')
    lsg.append('$\\begin{aligned}')
    lsg.append('V\\ &=\\ G\\cdot h_K\\\\')
    lsg.append('O\\ &=\\ u\\cdot h_K+2\\cdot G\\\\')
    lsg.append('G\\ &=\\ g\\cdot h/2\\\\')
    lsg.append(F'G\\ &=\\ {strNW(g,True)}\\cdot {strNW(h,True)}/2\\\\')
    lsg.append(F'\makebox[0pt][l]{{\\uline{{\\phantom{{G\\ =\\ {strNW(g*h/2,True)} \\mbox{{{einheit}2}}}}}}}}')
    lsg.append(F'G\\ &=\\ {strNW(g*h/2,True)}~{einheit}^2\\\\')
    lsg.append('u\\ &=\\ a+b+c\\\\')
    lsg.append(F'u\\ &=\\ {strNW(a,True)}+{strNW(b,True)}+{strNW(c,True)}\\\\')
    lsg.append(F'\makebox[0pt][l]{{\\uline{{\\phantom{{u\\ =\\ {strNW(a+b+c,True)} \\mbox{{{einheit}2}}}}}}}}')
    lsg.append(F'u\\ &=\\ {strNW(a+b+c,True)}~{einheit}\\\\')
    lsg.append(F'V\\ &=\\ G\\cdot h_K\\\\')
    lsg.append(F'V\\ &=\\ {strNW(g*h/2,True)}\\cdot {strNW(hK,True)}\\\\')
    lsg.append(F'\makebox[0pt][l]{{\\uuline{{\\phantom{{V\\ =\\ {strNW(g*hK,True)} \\mbox{{{einheit}2}}}}}}}}')
    lsg.append(F'V\\ &=\\ {strNW(g*h/2*hK,True)}~{einheit}^3\\\\')
    lsg.append(F'O\\ &=\\ u\\cdot h_K+2G\\\\')
    lsg.append(F'O\\ &=\\ {strNW(a+b+c,True)}\\cdot {strNW(hK,True)}+2\\cdot {strNW(g*h/2,True)}\\\\')
    lsg.append(F'\makebox[0pt][l]{{\\uuline{{\\phantom{{V\\ =\\ {strNW((a+b+c)*hK,True)} \\mbox{{{einheit}2}}}}}}}}')
    lsg.append(F'O\\ &=\\ {strNW((a+b+c)*hK+2*g*h/2,True)}~{einheit}^2\\\\')
    lsg.append('\\end{aligned}$};')
    lsg.append('\\end{tikzpicture}')
    lsg.append('\\endgroup')
    lsg.append('}')
    return [aufg,lsg,[]]

def erzeugeTrapezPrismaOberVolBerech(anzSpalten=2,mitText=True,messen=False,einheit='cm'):
#Diese Funktion erzeugt eine Aufgabe und Lösung zum Addieren und Subtrahieren von Dezimalzahlen
#Ausgabe: [aufg,lsg]=erzeugeQuaderOberVolBerech(breitePbox)
    maxDim=7 if anzSpalten==2 else 14
    aufg=[F'\\pbox{{{7 if anzSpalten==2 else 14} cm}}{{Berechne das Volumen und die Oberfläche{" und miss vorher die Seitenlängen" if messen else ""}:\\\\'] if mitText else []
    lsg=[F'\\pbox{{{7 if anzSpalten==2 else 14} cm}}{{']
    a,c,hT,hK=[random.randint(10,maxDim*10)/10.0 for i in range(4)]
    aufg=aufg+dreiecksPrimsa(Ax=Ax,Bx=Bx,Cx=Cx,Cy=Cy,hK=hK,ursprung=[0,0],messen=messen)+(['}']  if mitText else [])
    lsg.append('\\begingroup\\setlength{\\jot}{0.02cm}')
    lsg.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
    lsg.append('\\begin{tikzpicture}[show background grid]')
    l1=len(lsg)
    lsg.append(F'\\node[left] at (0,{(len(lsg)-l1)*(-0.5)-0.25}) {{Geg.: }};')
    lsg.append(F'\\node[right] at (0,{(len(lsg)-l1)*(-0.5)-0.25}) {{a = {strNW(a,True)} {einheit}}};')
    lsg.append(F'\\node[right] at (0,{(len(lsg)-l1)*(-0.5)-0.25}) {{b = {strNW(b,True)} {einheit}}};')
    lsg.append(F'\\node[right] at (0,{(len(lsg)-l1)*(-0.5)-0.25}) {{c = {strNW(c,True)} {einheit}}};')
    lsg.append(F'\\node[right] at (0,{(len(lsg)-l1)*(-0.5)-0.25}) {{g = {strNW(g,True)} {einheit}}};')
    lsg.append(F'\\node[right] at (0,{(len(lsg)-l1)*(-0.5)-0.25}) {{h = {strNW(h,True)} {einheit}}};')
    lsg.append(F'\\node[right] at (0,{(len(lsg)-l1)*(-0.5)-0.25}) {{$h_K$ = {strNW(hK,True)} {einheit}}};')
    lsg.append(F'\\node[left] at (0,{(len(lsg)-l1)*(-0.5)-0.25}) {{Ges.: }};')
    lsg.append(F'\\node[right] at (0,{(len(lsg)-l1)*(-0.5)-0.25}) {{V  = ? }};')
    lsg.append(F'\\node[right] at (0,{(len(lsg)-l1)*(-0.5)-0.25}) {{O  = ? }};')
    lsg.append(F'\\node[below right] at (0,{(len(lsg)-l1)*(-0.5)-0.25}) {{')
    lsg.append('$\\begin{aligned}')
    lsg.append('V\\ &=\\ G\\cdot h_K\\\\')
    lsg.append('O\\ &=\\ u\\cdot h_K+2\\cdot G\\\\')
    lsg.append('G\\ &=\\ g\\cdot h/2\\\\')
    lsg.append(F'G\\ &=\\ {strNW(g,True)}\\cdot {strNW(h,True)}/2\\\\')
    lsg.append(F'\makebox[0pt][l]{{\\uline{{\\phantom{{G\\ =\\ {strNW(g*h/2,True)} \\mbox{{{einheit}2}}}}}}}}')
    lsg.append(F'G\\ &=\\ {strNW(g*h/2,True)}~{einheit}^2\\\\')
    lsg.append('u\\ &=\\ a+b+c\\\\')
    lsg.append(F'u\\ &=\\ {strNW(a,True)}+{strNW(b,True)}+{strNW(c,True)}\\\\')
    lsg.append(F'\makebox[0pt][l]{{\\uline{{\\phantom{{u\\ =\\ {strNW(a+b+c,True)} \\mbox{{{einheit}2}}}}}}}}')
    lsg.append(F'u\\ &=\\ {strNW(a+b+c,True)}~{einheit}\\\\')
    lsg.append(F'V\\ &=\\ G\\cdot h_K\\\\')
    lsg.append(F'V\\ &=\\ {strNW(g*h/2,True)}\\cdot {strNW(hK,True)}\\\\')
    lsg.append(F'\makebox[0pt][l]{{\\uuline{{\\phantom{{V\\ =\\ {strNW(g*hK,True)} \\mbox{{{einheit}2}}}}}}}}')
    lsg.append(F'V\\ &=\\ {strNW(g*h/2*hK,True)}~{einheit}^3\\\\')
    lsg.append(F'O\\ &=\\ u\\cdot h_K+2G\\\\')
    lsg.append(F'O\\ &=\\ {strNW(a+b+c,True)}\\cdot {strNW(hK,True)}+2\\cdot {strNW(g*h/2,True)}\\\\')
    lsg.append(F'\makebox[0pt][l]{{\\uuline{{\\phantom{{V\\ =\\ {strNW((a+b+c)*hK,True)} \\mbox{{{einheit}2}}}}}}}}')
    lsg.append(F'O\\ &=\\ {strNW((a+b+c)*hK+2*g*h/2,True)}~{einheit}^2\\\\')
    lsg.append('\\end{aligned}$};')
    lsg.append('\\end{tikzpicture}')
    lsg.append('\\endgroup')
    lsg.append('}')
    return [aufg,lsg,[]]


def erzeugeZylibderOberVolBerech(breitePbox='\\textwidth',maxDim=14,einheit='cm'):
#Diese Funktion erzeugt eine Aufgabe und Lösung zum Addieren und Subtrahieren von Dezimalzahlen
#Ausgabe: [aufg,lsg]=erzeugeQuaderOberVolBerech(breitePbox)
    aufg=['\\pbox{'+str(breitePbox)+('' if 'textwidth' in str(breitePbox) else 'cm')+'}{Berechne das Volumen und die Oberfläche von:\\\\']
    lsg=['\\pbox{'+str(breitePbox)+('' if 'textwidth' in str(breitePbox) else 'cm')+'}{']
    R,h=[random.randint(1,maxDim) for i in range(2)]
    R=R/2.0
#    aufg=aufg+zylinder(R=R, h=h, ursprung=[0,0],buchstabe='Z',rName='R='+strNW(R)+' '+einheit,hName='h='+strNW(h)+' '+einheit)
    aufg=aufg+zylinder3D(R=R, h=h, einheit=einheit)
    lsg.append('\\begingroup\\setlength{\\jot}{0.02cm}')
    lsg.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
    lsg.append('\\begin{tikzpicture}[show background grid]')
    lsg.append('\\node[left] at (0,-0.25) {Geg.: };')
    lsg.append('\\node[right] at (0,-0.25) {r = '+strNW(R,True)+' '+einheit+'};')
    lsg.append('\\node[right] at (0,-0.75) {h = '+strNW(h,True)+' '+einheit+'};')
    lsg.append('\\node[left] at (0,-1.75) {Ges.: };')
    lsg.append('\\node[right] at (0,-1.75) {V  = ? };')
    lsg.append('\\node[right] at (0,-2.25) {O  = ? };')
    lsg.append('\\node[below right] at (0,-2.75) {')
    lsg.append('$\\begin{aligned}')
    lsg.append('V\\ &=\\ \\pi\\cdot r^2\\cdot h \\\\')
    lsg.append('V\\ &=\\ \\pi\\cdot '+strNW(R**2,True)+' \\cdot '+strNW(h,True)+'\\\\')
    lsg.append('\makebox[0pt][l]{\\uuline{\\phantom{V\\ =\\ '+strNW(math.pi*R**2*h,True)+'\ \\mbox{'+einheit+'3}}}}')
    lsg.append('V\\ &=\\ '+strNW(math.pi*R**2*h,True)+'\ \\mbox{'+einheit+'}^3\\\\')
    lsg.append('O\\ &=\\ 2\\cdot G + M\\\\')
    lsg.append('O\\ &=\\ 2\\pi r^2+2\\pi r \\cdot h \\\\')
    lsg.append('O\\ &=\\ 2\\pi \\cdot '+strNW(R,True)+'^2+2\\pi \\cdot '+strNW(R,True)+' \\cdot '+strNW(h,True)+' \\\\')
    lsg.append('\makebox[0pt][l]{\\uuline{\\phantom{V\\ =\\ '+strNW(2*math.pi*R**2+2*math.pi*R*h,True)+'\ \\mbox{'+einheit+'2}}}}')
    lsg.append('O\\ &=\\ '+strNW(2*math.pi*R**2+2*math.pi*R*h,True)+'\ \\mbox{'+einheit+'}^2\\\\')
    lsg.append('\\end{aligned}$};')
    lsg.append('\\end{tikzpicture}') 
    lsg.append('\\endgroup')
    aufg.append('}')
    lsg.append('}')
    return [aufg,lsg,[]]

def erzeugeZylibderOberVolBerech(breitePbox='\\textwidth',maxDim=14,einheit='cm'):
#Diese Funktion erzeugt eine Aufgabe und Lösung zum Addieren und Subtrahieren von Dezimalzahlen
#Ausgabe: [aufg,lsg]=erzeugeQuaderOberVolBerech(breitePbox)
    aufg=['\\pbox{'+str(breitePbox)+('' if 'textwidth' in str(breitePbox) else 'cm')+'}{Berechne das Volumen und die Oberfläche von:\\\\']
    lsg=['\\pbox{'+str(breitePbox)+('' if 'textwidth' in str(breitePbox) else 'cm')+'}{']
    R,h=[random.randint(1,maxDim) for i in range(2)]
    R=R/2.0
#    aufg=aufg+zylinder(R=R, h=h, ursprung=[0,0],buchstabe='Z',rName='R='+strNW(R)+' '+einheit,hName='h='+strNW(h)+' '+einheit)
    aufg=aufg+zylinder3D(R=R, h_k=h, einheit=einheit)
    lsg.append('\\begingroup\\setlength{\\jot}{0.02cm}')
    lsg.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
    lsg.append('\\begin{tikzpicture}[show background grid]')
    lsg.append('\\node[left] at (0,-0.25) {Geg.: };')
    lsg.append('\\node[right] at (0,-0.25) {r = '+strNW(R,True)+' '+einheit+'};')
    lsg.append('\\node[right] at (0,-0.75) {h = '+strNW(h,True)+' '+einheit+'};')
    lsg.append('\\node[left] at (0,-1.75) {Ges.: };')
    lsg.append('\\node[right] at (0,-1.75) {V  = ? };')
    lsg.append('\\node[right] at (0,-2.25) {O  = ? };')
    lsg.append('\\node[below right] at (0,-2.75) {')
    lsg.append('$\\begin{aligned}')
    lsg.append('V\\ &=\\ \\pi\\cdot r^2\\cdot h \\\\')
    lsg.append('V\\ &=\\ \\pi\\cdot '+strNW(R**2,True)+' \\cdot '+strNW(h,True)+'\\\\')
    lsg.append('\makebox[0pt][l]{\\uuline{\\phantom{V\\ =\\ '+strNW(math.pi*R**2*h,True)+'\ \\mbox{'+einheit+'3}}}}')
    lsg.append('V\\ &=\\ '+strNW(math.pi*R**2*h,True)+'\ \\mbox{'+einheit+'}^3\\\\')
    lsg.append('O\\ &=\\ 2\\cdot G + M\\\\')
    lsg.append('O\\ &=\\ 2\\pi r^2+2\\pi r \\cdot h \\\\')
    lsg.append('O\\ &=\\ 2\\pi \\cdot '+strNW(R,True)+'^2+2\\pi \\cdot '+strNW(R,True)+' \\cdot '+strNW(h,True)+' \\\\')
    lsg.append('\makebox[0pt][l]{\\uuline{\\phantom{V\\ =\\ '+strNW(2*math.pi*R**2+2*math.pi*R*h,True)+'\ \\mbox{'+einheit+'2}}}}')
    lsg.append('O\\ &=\\ '+strNW(2*math.pi*R**2+2*math.pi*R*h,True)+'\ \\mbox{'+einheit+'}^2\\\\')
    lsg.append('\\end{aligned}$};')
    lsg.append('\\end{tikzpicture}')
    lsg.append('\\endgroup')
    aufg.append('}')
    lsg.append('}')
    return [aufg,lsg,[]]

def umfangsFormeln():
#Ich schreibe vor jeder Variable "vari", da man beim suche und ersetzen von a durch eine Zahl z.B. h_2,34 erhält.
#Durch das Vari wird es eindeutig. Hinterher muss das vari entfernt werden.
    umfang={'Trapez':['variu=varia+varib+varic+varid',['varia','varib','varic','varid']]}
    umfang['Rechteck']=['variu=varia+varib+varia+varib',['varia','varib']]
    umfang['Dreieck']=['variu=varia+varib+varic',['varia','varib','varic']]
    umfang['Sechseck']=['variu=6*varia',['varia']]
    umfang['Haus']=['variu=varia+varib+varic+varic+varib',['varia','varib','varic']]
    return umfang

def flaechenFormeln():
#Ich schreibe vor jeder Variable "vari", da man beim suche und ersetzen von a durch eine Zahl z.B. h_2,34 erhält.
#Durch das Vari wird es eindeutig. Hinterher muss das vari entfernt werden.
    flaeche={'Trapez':['variA=(varia+varic)*variStrh_a/2',['varia','varic','variStrh_a']]}
    flaeche['Rechteck']=['variA=varia*varib',['varia','varib']]
    flaeche['Dreieck']=['variA=varic*variStrh_c/2',['varic','variStrh_c']]
    flaeche['Sechseck']=['variA=2*(varia+varic)*variStrh_a/2',['varia','varic','variStrh_a']]
    flaeche['Haus']=['variA=varia*varib+varia*variStrh_a/2',['varia','varib','variStrh_a']]
    return flaeche
def prismaVolumenFormeln():
    prismaVolumen={'Allgemeinen':['variV=variG*variStrh_K',['variG','variStrh_K']]}
    flaechen=flaechenFormeln()
    for art in flaechen.keys():
        name = 'Quader' if art=='Rechteck' else art
        hoehe='variStrc' if name=='Quader' else 'variStrh_K'
        mitKlammer=True if ("+" in flaechen[art][0]) or ("-" in flaechen[art][0]) or ("/" in flaechen[art][0]) else False
        prismaVolumen[name]=[F'variV={"(" if mitKlammer else ""}{flaechen[art][0].split("=")[1]}{")" if mitKlammer else  ""}*{hoehe}',flaechen[art][1]+[hoehe]]
    return prismaVolumen

def prismaOberflaechenFormeln():
    prismaOberfl={'Allgemeinen':['variO=2*variG+variM',['variG','variM']]}
    flaechen=flaechenFormeln()
    umfaenge=umfangsFormeln()
    for art in flaechen.keys():
        name = 'Quader' if art=='Rechteck' else art
        hoehe='variStrc' if name=='Quader' else 'variStrh_K'
        mitKlammer=True if ("+" in flaechen[art][0]) or ("-" in flaechen[art][0]) or ("/" in flaechen[art][0]) else False
        mitKlammerU=True if ("+" in umfaenge[art][0]) or ("-" in umfaenge[art][0]) or ("/" in umfaenge[art][0]) else False
        prismaOberfl[name]=[F'variO=2*{"(" if mitKlammer else ""}{flaechen[art][0].split("=")[1]}{")" if mitKlammer else  ""}+{"(" if mitKlammerU else ""}{umfaenge[art][0].split("=")[1]}{")" if mitKlammerU else  ""}*{hoehe}',list(set(flaechen[art][1]+umfaenge[art][1]+[hoehe]))[::-1]]
    return prismaOberfl

def erzeugePrismaFehlendeSeiteBerechnen(anzSpalten=2,auswahl='',mitText=True,VoO=''):
    VoO= VoO if VoO in ['V','O'] else'V' if random.randint(0,1) >0 else 'O'
    einheit='cm'
    breite=6 if anzSpalten==2 else 14
    prismaVolumen=prismaVolumenFormeln()
    prismaOberfl=prismaOberflaechenFormeln()
    auswahl=auswahl if len(auswahl)>0 else random.choice(list(prismaVolumen.keys()))
    prisma=prismaVolumen[auswahl] if VoO=='V' else prismaOberfl[auswahl]
    formel=prisma[0]
    varis={}
    for v in prisma[1]:
        varis[v]=random.randint(15,100)
    V=prisma[0].split('=')[1]
    for v in varis.keys():
        V=V.replace(str(v),str(varis[v]))
    ges=random.choice(list(varis.keys()))
    ges={ges:varis[ges]}
    del varis[list(ges.keys())[0]]
    varis[F'vari{VoO}']=eval(V)
    prismaArt=F'{auswahl}{"" if auswahl=="Quader" else "-Prismas"}'
    seiteFlaeche='Fläche' if ges in ['G','M'] else 'Seite'
    afgText=F'Berechne die fehlende {seiteFlaeche} eines {prismaArt} bei folgenden gegebenen Größen: &&&&'
    aufg=[F'\\pbox{{{breite } cm}}{{{afgText if mitText else F"{prismaArt}:" }'.replace('&&&&','\\\\')]
    aufg=aufg+['; '.join([F'${art}={strNW(varis[art])}~{einheit}{"^3" if art==F"variV" else ("^2" if art in ["variG","variO","variM"] else "")}$' for art in list(varis.keys())])]
    lsg=[F'\\pbox{{{ breite} cm}}{{']
    lsg.append('\\begingroup\\setlength{\\jot}{0.02cm}')
    lsg.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
    lsg.append('\\begin{tikzpicture}[show background grid]')
    lsg.append('\\node[left] at (0,-0.25) {Geg.: };')
    nLsg=len(lsg)
    for x in list(varis.keys()):
        lsg.append(F'\\node[right] at (0,{-0.25-0.5*(len(lsg)-nLsg)}) {{${x}={strNW(varis[x],2)}~{einheit}{"^3" if x=="variV" else ("^2" if x in ["variG","variO","variM"] else "")}$}};')
    lsg.append(F'\\node[left] at (0,{-0.25-0.5*(len(lsg)-nLsg)}) {{Ges.: }};')
    nLsg = nLsg+1
    lsg.append(F'\\node[right] at (0,{-0.25-0.5*(len(lsg)-nLsg)}) {{${list(ges.keys())[0]}  = ?~cm{"^2" if list(ges.keys())[-1] in ["variG","variO","variM"] else ""}$}};')
    lsg.append(F'\\node[below right] at (0,{-0.25-0.5*(len(lsg)-nLsg)}) {{')
    lsg.append('$\\begin{aligned}')
    lsg.append(F'{formel.split("=")[0]}&={formel.split("=")[1]} & &§§mid~\\mbox{{Einsetzen}} \\\\')
    for x in list(varis.keys()):
        formelStrNw=formel.replace(x,strNW(varis[x],2).replace('.',''))
        formel=formel.replace(x,str(varis[x]))
    if not str(sympy.sympify(formel.split("=")[1]))==formelStrNw.split("=")[1]:
        lsg.append(F'{formelStrNw.split("=")[0]}&={formelStrNw.split("=")[1]} & &§§mid~\\mbox{{Zusammenfassen}} \\\\')
    lsg.append(F'{formelStrNw.split("=")[0]}&={sympy.sympify(formel.split("=")[1])} & &§§mid~\\mbox{{Umdrehen}} \\\\')
#    lsg.append(F'{sympy.sympify(formelStrNw.split("=")[1])}&={formelStrNw.split("=")[0]} & & \\\\')
    glLsg = loeseGleichungEinfachMitEinerVariabel(G=F'{sympy.sympify(formel.split("=")[1])} = {formelStrNw.split("=")[0].replace(".","").replace(",",".")}', variable=list(ges.keys())[0], latexAusgabe=True)
    glLsg=glLsg[6:-3]
    glLsg[-1]=F'{glLsg[-1].split("&")[0]}&{glLsg[-1].split("&")[1]}~{einheit}{"^2" if list(ges.keys())[-1] in ["variG","variO","variM"] else " "}&{glLsg[-1].split("&")[2]}&{glLsg[-1].split("&")[3]}'
    lsg=lsg+glLsg
    lsg.insert(-1,'\\makebox[0pt][l]{\\uuline{\\phantom{$' + lsg[-1].replace('&', '') + '$}}}')
    lsg.append('\\end{aligned}$};')
    lsg.append('\\end{tikzpicture}')
    lsg.append('\\endgroup')
    aufg.append('}')
    lsg.append('}')
    return [[ersetzePlatzhalterMitSymbolen(x) for x in aufg],[ersetzePlatzhalterMitSymbolen(x) for x in lsg],[]]

def erzeugePrismaErstmessenDannBerechnenAufgabe(anzSpalten=2,typ='Sechseck',mitText=True):
    einheit='cm'
    breite=6 if anzSpalten==2 else 14
    breite=breite/2 if typ=='Sechseck' else breite
#    for vari in 'a','b','c','g','h','h_K','h_D','h_a','h_c':
#        exec(F'vari{vari}=random.randint(15,10*min(8,breite))/10')
    varia,varib,varic,varig,varih,varih_K,varih_D,varih_a,varih_c=[random.randint(15,10*min(8,breite))/10 for i in range(9)]
    while abs(varia-varic)<0.5:
        varia,varic=[random.randint(15,10*min(8,breite))/10 for i in range(2)]
    if typ=='Sechseck':
        varic=round(2*varia*math.cos(60*math.pi/180)+varia,1)
        varih=round(varia*math.sin(60*math.pi/180),1)
    if typ=='Trapez':
        varib=round((varia**2+((varia-varic)/2)**2)**0.5,1)
        varid=varib
    if typ=='Dreieck':
        varidc=random.randint(10,int(varic)*10)/10
        varia=round((varih_c**2+varidc**2)**0.5,1)
        varib=round((varih_c**2+(varic-varidc)**2)**0.5,1)
    if typ=='Haus':
        varic=round(((varia/2)**2+varih_D**2)**0.5,1)
    geg=['varig','varia','varib','varic','varid','varih','varih_D','varih_K']
    ges=['V','O']
    messen=True
    auswahl={'Trapez':[['variG=(varia+varic)*varih/2','variu=varia+varib+varic+varid'],'trapezPrismaLiegend3D(a=varia,c=varic,h_T=varih,h_K=varih_K,messen=messen)',['varia','varib','varic','varid','varih_a','varih_K']]}
    auswahl['Dreieck']=[['variG=varic*varih_c/2','variu=varia+varib+varic'],'dreiecksPrimsa3DLiegend(g=varic,h_D=varih_c,h_K=varih_K,dg=varidc,messen=messen)',['varic','varih_c','varih_K']]
    auswahl['Sechseck']=[['variG=2*(varia+varic)*varih_a/2','variu=6*varia'],'sechseckPrimsa3D(a=varia,h_K=varih_K,messen=messen)',['varia','varic','varih_a','varih_K']]
    auswahl['Haus']=[['variG=varia*varib+varia*varih_D/2','variu=varia+varib+varic+varic+varib'],'hausPrisma(a=varia,b=varib,h_D=varih_D,h_K=varih_K, messen=messen)',['varia','varib','varic','varih_D','varih_K']]
    geg=auswahl[typ][2]
    aufg=[F'\\pbox{{{breite } cm}}{{{"Messe die Seiten und Berechne dann das Volumen und die Oberfläche von: &&&&" if mitText else ""}'.replace('&&&&','\\\\')]
    lsg=[F'\\pbox{{{ breite} cm}}{{']
    scope=globals()|locals()
    aufg=aufg+eval(auswahl[typ][1],scope)
    messen=False
    scope=globals()|locals()
    lsg=lsg+eval(auswahl[typ][1],scope)+['\\\\']
    nLsg=len(lsg)
    lsg.append('\\begingroup\\setlength{\\jot}{0.02cm}')
    lsg.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
    lsg.append('\\begin{tikzpicture}[show background grid]')
    lsg.append('\\node[left] at (0,-0.25) {Geg.: };')
    for x in geg:
        lsg.append(F'\\node[right] at (0,{-0.25-0.5*(len(lsg)-4-nLsg)}) {{${x}={strNW(eval(x),1)}~{einheit}$}};')
    lsg.append(F'\\node[left] at (0,{-0.25-0.5*(len(lsg)-4-nLsg)}) {{Ges.: }};')
    lsg.append(F'\\node[right] at (0,{-0.25-0.5*(len(lsg)-5-nLsg)}) {{${ges[0]}  = ?~cm^3$}};')
    lsg.append(F'\\node[right] at (0,{-0.25-0.5*(len(lsg)-5-nLsg)}) {{${ges[1]}  = ?~cm^2$}};')
    lsg.append(F'\\node[below right] at (0,{-0.25-0.5*(len(lsg)-5-nLsg)}) {{')
    lsg.append('$\\begin{aligned}')
    lsg.append(F'V&=G\\cdot h_K & & \\\\')
    lsg.append(F'O&=2\\cdot G + M & & \\\\')
    lsg.append(F'\\\\')
    formelG=auswahl[typ][0][0]
    G=eval(formelG.split("=")[1],scope)
    lsg.append(F'{formelG.split("=")[0]}&={formelG.split("=")[1].replace("*","&&cdot ")}& & \\\\'.replace('&&','\\').replace("/",":"))
    for x in geg:
        formelG = formelG.replace(x, strNW(eval(x),1))
    lsg.append(F'{formelG.split("=")[0]}&={formelG.split("=")[1].replace("*","&&cdot ")}& & \\\\'.replace("&&","\\").replace("/",":"))
    lsg.append(F'{formelG.split("=")[0]}&={strNW(G,2)}~cm^2& & \\\\'.replace('&&','\\').replace('/',':'))
#Zwischenergebniss einfach unterstreichen
    lsg.insert(-1,'\\makebox[0pt][l]{\\uline{\\phantom{$' + lsg[-1].replace('&', '') + '$}}}')
    lsg.append(F'V&=G\\cdot h_K & & \\\\')
    lsg.append(F'V&={strNW(G,2)}\\cdot {strNW(varih_K,2)} & & \\\\')
    lsg.append(F'V&={strNW(G*varih_K,2)} cm^3& & \\\\')
# Ergebniss doppelt unterstreichen
    lsg.insert(-1,'\\makebox[0pt][l]{\\uuline{\\phantom{$' + lsg[-1].replace('&', '') + '$}}}')
    lsg.append(F'\\\\')
    lsg.append(F'M&=u\\cdot h_K & & \\\\')
    formelU=auswahl[typ][0][1]
    U=eval(formelU.split("=")[1],scope)
    lsg.append(F'{formelU.split("=")[0]}&={formelU.split("=")[1].replace("*","&&cdot ")}& & \\\\'.replace('&&','\\').replace("/",":"))
    for x in geg:
        formelU = formelU.replace(x, strNW(eval(x),1))
    lsg.append(F'{formelU.split("=")[0]}&={formelU.split("=")[1].replace("*","&&cdot ")}& & \\\\'.replace("&&","\\").replace("/",":"))
    lsg.append(F'{formelU.split("=")[0]}&={strNW(U,2)}~cm& & \\\\'.replace('&&','\\').replace('/',':'))
#Zwischenergebniss einfach unterstreichen
    lsg.insert(-1,'\\makebox[0pt][l]{\\uline{\\phantom{$' + lsg[-1].replace('&', '') + '$}}}')
    lsg.append(F'M&=u\\cdot h_K & & \\\\')
    lsg.append(F'M&={strNW(U,2)}\\cdot {strNW(varih_K,2)} & & \\\\')
    lsg.append(F'M&={strNW(U*varih_K,2)} cm^2& & \\\\')
    # Zwischenergebniss einfach unterstreichen
    lsg.insert(-1, '\\makebox[0pt][l]{\\uline{\\phantom{$' + lsg[-1].replace('&', '') + '$}}}')
    lsg.append(F'O&=2\\cdot G + M & & \\\\')
    lsg.append(F'O&=2\\cdot {strNW(G,2)} + {strNW(U*varih_K,2)} & & \\\\')
    lsg.append(F'O&={strNW(2*G+U*varih_K,2)} cm^2& & \\\\')
    # Zwischenergebniss einfach unterstreichen
    lsg.insert(-1,'\\makebox[0pt][l]{\\uuline{\\phantom{$' + lsg[-1].replace('&', '') + '$}}}')
    lsg.append('\\end{aligned}$};')
    lsg.append('\\end{tikzpicture}')
    lsg.append('\\endgroup')
    aufg.append('}')
    lsg.append('}')
    return [[ersetzePlatzhalterMitSymbolen(x) for x in aufg],[ersetzePlatzhalterMitSymbolen(x) for x in lsg],[]]
def erzeugeQuaderMitLochBerech(breitePbox='\\textwidth',maxDim=14,einheit='cm',werte=[],namen=[]):
#Diese Funktion erzeugt eine Aufgabe und Lösung zum Addieren und Subtrahieren von Dezimalzahlen
#Ausgabe: [aufg,lsg,zahlen]=erzeugeQuaderMitLochBerech(breitePbox,maxDim,einheit,werte)
#
#     breitePbox=Breite der Aufgabe
#     maxDim=Maximale Seitenlaenge.
#     einheit=cm,m ...
#     werte=[] --> Zufällige Werte, Ansonsten werte=[a,b,c,R] 
    aufg=['\\pbox{'+str(breitePbox)+('' if 'textwidth' in str(breitePbox) else 'cm')+'}{Berechne das Volumen und die Oberfläche von:\\\\']
    lsg=['\\pbox{'+str(breitePbox)+('' if 'textwidth' in str(breitePbox) else 'cm')+'}{']
    if len(werte)==0:
        a,b,c=[random.randint(1,maxDim) for i in range(3)]
        while min(a-1,c-1) <2:
            a, b, c=[random.randint(1, maxDim) for i in range(3)]
        R=random.randint(1,min(a-1,c-1))/2.0
    else:
        a,b,c,R=werte
    h=b
    if len(namen)==0:
        aName,bName,cName,rName='a='+strNW(a)+' '+einheit,'b='+strNW(b)+'  '+einheit,'c='+strNW(c)+'  '+einheit,'r='+strNW(R)+' '+einheit
    else:
        aName,bName,cName,rName=namen
    aufg=aufg+quaderMitLoch(a=a, b=b, c=c,R=R, ursprung=[0,0],buchstabe='W',aName=aName,bName=bName,cName=cName,rName=rName)
    lsg.append('\\begingroup\\setlength{\\jot}{0.02cm}')
    lsg.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
    lsg.append('\\begin{tikzpicture}[show background grid]')
    lsg.append('\\node[left] at (0,-0.25) {Geg.: };')
    lsg.append('\\node[right] at (0,-0.25) {a = '+strNW(a,True)+' '+einheit+'};')
    lsg.append('\\node[right] at (0,-0.75) {b = '+strNW(b,True)+' '+einheit+'};')
    lsg.append('\\node[right] at (0,-1.25) {c = '+strNW(c,True)+' '+einheit+'};')
    lsg.append('\\node[right] at (0,-1.75) {r = '+strNW(R,True)+' '+einheit+'};')
    lsg.append('\\node[right] at (0,-2.25) {h = '+strNW(h,True)+' '+einheit+'};')
    lsg.append('\\node[left] at (0,-2.75) {Ges.: };')
    lsg.append('\\node[right] at (0,-2.75) {V  = ? };')
    lsg.append('\\node[right] at (0,-3.25) {O  = ? };')
    lsg.append('\\node[below right] at (0,-3.75) {')
    lsg.append('$\\begin{aligned}')
    lsg.append('V_Q\\ &=\\ a\\cdot b \\cdot c\\\\')
    lsg.append('V_Q\\ &=\\ '+strNW(a,True)+' \\cdot '+strNW(b,True)+' \\cdot '+strNW(c,True)+'\\\\')
#    lsg.append('V\\ &=\\ '+strNW(a,True)+einheit+' \\cdot '+strNW(b,True)+einheit+' \\cdot '+strNW(c,True)+einheit+'\\\\')
    lsg.append('\makebox[0pt][l]{\\uline{\\phantom{V\\ =\\ '+strNW(a*b*c,True)+'\ \\mbox{'+einheit+'3}}}}')
    lsg.append('V_Q\\ &=\\ '+strNW(a*b*c,True)+'\ \\mbox{'+einheit+'}^3\\\\')
    lsg.append('V_Z\\ &=\\ \\pi\\cdot r^2\\cdot h \\\\')
    lsg.append('V_Z\\ &=\\ \\pi\\cdot '+strNW(R**2,True)+' \\cdot '+strNW(h,True)+'\\\\')
    lsg.append('\makebox[0pt][l]{\\uline{\\phantom{V\\ =\\ '+strNW(math.pi*R**2*h,True)+'\ \\mbox{'+einheit+'3}}}}')
    lsg.append('V_Z\\ &=\\ '+strNW(math.pi*R**2*h,True)+'\ \\mbox{'+einheit+'}^3\\\\')
    lsg.append('V\\ &=\\ V_Q - V_Z \\\\')
    lsg.append('V\\ &=\\ '+strNW(a*b*c,True)+'\ \\mbox{'+einheit+'}^3 -  '+strNW(math.pi*R**2*h,True)+'\ \\mbox{'+einheit+'}^3 \\\\')
    lsg.append('\makebox[0pt][l]{\\uuline{\\phantom{V\\ =\\ '+strNW(a*b*c-math.pi*R**2*h,True)+'\ \\mbox{'+einheit+'3}}}}')
    lsg.append('V\\ &=\\ '+strNW(a*b*c-math.pi*R**2*h,True)+'\ \\mbox{'+einheit+'}^3 \\\\')
    lsg.append('O_Q\\ &=\\ 2ab+2ac+2bc\\\\')
    lsg.append('O_Q\\ &=\\ 2\\cdot'+strNW(a,True)+'\\cdot'+strNW(b,True)+'+2\\cdot'+strNW(a,True)+'\\cdot'+strNW(c,True)+'+2\\cdot'+strNW(b,True)+'\\cdot'+strNW(c,True)+'\\\\')
    lsg.append('\makebox[0pt][l]{\\uline{\\phantom{OQ\\ =\\ '+strNW(2*a*b+2*a*c+2*b*c,True)+'\ \\mbox{'+einheit+'2}}}}')
    lsg.append('O_Q\\ &=\\ '+strNW(2*a*b+2*a*c+2*b*c,True)+'\ \\mbox{'+einheit+'}^2\\\\')
    lsg.append('G_Z\\ &=\\ \\pi r^2\\\\')
    lsg.append('G_Z\\ &=\\ \\pi \\cdot '+strNW(R,True)+'^2\\\\')
    lsg.append('\makebox[0pt][l]{\\uline{\\phantom{GZ=\\ =\\ '+strNW(math.pi*R**2,True)+'\ \\mbox{'+einheit+'2}}}}')
    lsg.append('G_Z\\ &=\\ '+strNW(math.pi*R**2,True)+'\ \\mbox{'+einheit+'}^2\\\\')
    lsg.append('M_Z\\ &=\\ 2\\pi r \\cdot c \\\\')
    lsg.append('M_Z\\ &=\\ 2\\pi \\cdot '+strNW(R,True)+' \\cdot '+strNW(h,True)+' \\\\')
    lsg.append('\makebox[0pt][l]{\\uline{\\phantom{MZ\\ =\\ '+strNW(2*math.pi*R*h,True)+'\ \\mbox{'+einheit+'2}}}}')
    lsg.append('M_Z\\ &=\\ '+strNW(2*math.pi*R*h,True)+'\ \\mbox{'+einheit+'}^2\\\\')
    lsg.append('O\\ &=\\ O_Q - 2 \\cdot G_Z + M_Z\\\\')
    lsg.append('O\\ &=\\ '+strNW(2*a*b+2*a*c+2*b*c,True)+' - 2 \\cdot '+strNW(math.pi*R**2,True)+' + '+strNW(2*math.pi*R*h,True)+'\\\\')
    lsg.append('\makebox[0pt][l]{\\uline{\\phantom{O\\ =\\ '+strNW(2*a*b+2*a*c+2*b*c-2*math.pi*R**2+2*math.pi*R*h,True)+'\ \\mbox{'+einheit+'2}}}}')
    lsg.append('O\\ &=\\ '+strNW(2*a*b+2*a*c+2*b*c-2*math.pi*R**2+2*math.pi*R*h,True)+'\ \\mbox{'+einheit+'}^2\\\\')
    lsg.append('\\end{aligned}$};')
    lsg.append('\\end{tikzpicture}') 
    lsg.append('\\endgroup')
    aufg.append('}')
    lsg.append('}')
    return [aufg,lsg,[a,b,c,R]]
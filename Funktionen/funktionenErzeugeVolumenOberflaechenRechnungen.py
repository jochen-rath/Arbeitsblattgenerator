#!/usr/bin/env python
# coding: utf8

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())



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


def erzeugeZylibderOberVolBerech(breitePbox='\\textwidth',maxDim=14,einheit='cm'):
#Diese Funktion erzeugt eine Aufgabe und Lösung zum Addieren und Subtrahieren von Dezimalzahlen
#Ausgabe: [aufg,lsg]=erzeugeQuaderOberVolBerech(breitePbox)
    aufg=['\\pbox{'+str(breitePbox)+('' if 'textwidth' in str(breitePbox) else 'cm')+'}{Berechne das Volumen und die Oberfläche von:\\\\']
    lsg=['\\pbox{'+str(breitePbox)+('' if 'textwidth' in str(breitePbox) else 'cm')+'}{']
    R,h=[random.randint(1,maxDim) for i in range(2)]
    R=R/2.0
    aufg=aufg+zylinder(R=R, h=h, ursprung=[0,0],buchstabe='Z',rName='R='+strNW(R)+' '+einheit,hName='h='+strNW(h)+' '+einheit)
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
        R=random.randint(1,min(a,c))/2.0
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
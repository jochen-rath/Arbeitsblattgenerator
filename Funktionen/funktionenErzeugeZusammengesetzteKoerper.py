#!/usr/bin/env python
# coding: utf8


#Aufruf:
#       exec(open("Funktionen/funktionenErzeugeGeometrieAufgaben.py").read())
#Diese Skript stellte verschiedene Figuren bereit, die Zeichnungen mit dem Latex-Paket Tikz erzeugen
#       exec(open("Funktionen/funktionen.py").read())

def mehrereZylinder(mitText=True):
    gesamtHoehe=15
    einheit='cm'
    n=random.randint(2,3)
    maxH=int(gesamtHoehe/n)
    werte={}
    h=0
    for w in [f'{x}_{i+1}' for x in ['r','h'] for i in range(n) ]:
        exec(f'werte["{w}"]={random.randint(10,25)/5 if w[0]=="r" else random.randint(10,maxH*10)/10}')
    radien=[werte[key] for key in list(werte.keys()) if key[0]=='r']
    hoehen=[werte[key] for key in list(werte.keys()) if key[0]=='h']
    afgText=[F'Bestimme das Volumen und die Oberfläche von:']
    zyl=mehrereZylinder3D(radien=radien, hoehen=hoehen,einheit=einheit)
    afg=zyl if not mitText else ['\\pbox{\\linewidth}{']+afgText+['\\\\']+zyl+['}']
    lsg=[]
    lsg.append('\\begingroup\\setlength{\\jot}{0.02cm}')
    lsg.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
    lsg.append('\\begin{tikzpicture}[show background grid]')
    lsg.append('\\node[left] at (0,-0.25) {Geg.: };')
    for i,w in enumerate(list(werte.keys())):
        lsg.append(f'\\node[right] at (0,{-0.25-i*0.5}) {{$ {w}= {strNW(werte[w],True)}~{einheit}$}};')
    lsg.append(f'\\node[left] at (0,{-0.25-(i+1)*0.5}) {{Ges.: }};')
    lsg.append(f'\\node[right] at (0,{-0.25-(i+1)*0.5}) {{V  = ? }};')
#    lsg.append(f'\\node[right] at (0,{-0.25-(i+2)*0.5}) {{O  = ? }};')
    lsg.append(f'\\node[below right] at (0,{-0.25-(i+3)*0.5}) {{')
    lsg.append('$\\begin{aligned}')
    lsg.append(f'V& = {"+".join([f"V_{i+1}" for i in range(n)])} \\\\')
    for i in range(n):
        werte[f'G_{i+1}']=math.pi*werte[f"r_{i+1}"]**2
        werte[f'M_{i+1}']=2*math.pi*werte[f'r_{i+1}']*werte[f'h_{i+1}']
        werte[f'V_{i+1}']=math.pi*werte[f'r_{i+1}']**2*werte[f'h_{i+1}']
        lsg.append(f'V_{i+1}& = \\pi·r_{i+1}^2·h_{i+1}  = \\pi·{strNW(werte[f"r_{i+1}"],True)}^2·{strNW(werte[f"h_{i+1}"],True)}= {strNW(werte[f"V_{i+1}"],True)} ~{einheit}^3\\\\')
#        lsg.insert(-1,'\\makebox[0pt][l]{\\uline{\\phantom{$' + lsg[-1].replace('&', '') + '$}}}')
    lsg.append(f'V& = {"+".join([f"V_{i+1}" for i in range(n)])} \\\\')
    lsg.append(f'V& = {"+".join([strNW(werte[f"V_{i+1}"],True) for i in range(n)])} \\\\')
    lsg.append(f'V& = {strNW(sum([werte[f"V_{i+1}"] for i in range(n)]),True)}~{einheit}^3\\\\')
    lsg.insert(-1,'\\makebox[0pt][l]{\\uuline{\\phantom{$' + lsg[-1].replace('&', '') + '$}}}')
    O=f'{"+".join([f"M_{i+1}" for i in range(n)])}+G_1+G_{n}+{"+".join([(f"(G_{i+2}-G_{i+1})" if werte[f"r_{i+2}"]>werte[f"r_{i+1}"] else f"(G_{i+1}-G_{i+2})")for i in range(n-1)])}'
    Owerte,Oerg=O,O
    for w in list(werte.keys()):
        Owerte=Owerte.replace(w,strNW(werte[w],True))
        Oerg=Oerg.replace(w,str(werte[w]))
    lsg.append(f'O& = {O}\\\\')
    for i in range(n):
        lsg.append(f'G_{i+1}& = \\pi·r_{i+1}^2=\\pi·{strNW(werte[f"r_{i+1}"],True)}^2={strNW(werte[f"G_{i+1}"],True)} ~{einheit}^2  \\\\')
        lsg.append(f'M_{i+1}& = 2 · \\pi·r_{i+1}= 2 ·\\pi·{strNW(werte[f"r_{i+1}"],True)}  = {strNW(werte[f"M_{i+1}"],True)} ~{einheit}^2 \\\\')
    lsg.append(f'O& = {Owerte}\\\\')
    lsg.append(f'O& = {strNW(eval(Oerg),True)}~{einheit}^2\\\\')
    lsg.insert(-1,'\\makebox[0pt][l]{\\uuline{\\phantom{$' + lsg[-1].replace('&', '') + '$}}}')
    lsg.append('\\end{aligned}$};')
    lsg.append('\\end{tikzpicture}')
    lsg.append('\\endgroup')
    return [afg,lsg,[werte]]

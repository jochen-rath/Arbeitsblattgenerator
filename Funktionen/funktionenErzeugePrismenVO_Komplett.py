#!/usr/bin/env python
# coding: utf8
import random


#Aufruf:
#import os
#		import os
#		os.chdir(f'{os.path.expanduser("~")}/Schule/Arbeitsblattgenerator')
#       exec(open("Funktionen/funktionen.py").read())


def erzeugeQuaderOberVolBerechKomplett(einheit='cm',mitText=True,anzSpalten=[2,2]):
#Diese Funktion erzeugt eine Aufgabe und Lösung zum Addieren und Subtrahieren von Dezimalzahlen
#Ausgabe: [aufg,lsg]=erzeugeQuaderOberVolBerech(breitePbox)
    breitePbox='\\hsize'
    groesse='{17 cm}' if anzSpalten[0] == 1 else '{7 cm}'
    aufg=[f'\\pbox{groesse}{{']
    aufg=aufg + (['Berechne das Volumen und die Oberfläche von:\\\\'] if mitText else [])
    lsg=[]
    #lsg=['\\pbox{'+str(breitePbox)+'cm}{']
    maxDim=14 if anzSpalten[0] == 1 else 5
    a,b,c=[random.randint(20,maxDim*10)/10 for i in range(3)]
    aufg=aufg+quader(a=a, b=b, c=c,ursprung=[0,0],buchstabe='Q',aName='a='+strNW(a)+' '+einheit,bName='b='+strNW(b)+'  '+einheit,cName='c='+strNW(c)+'  '+einheit)
    aufg=aufg+quaderLoesungsskizze(a=a,b=b,c=c,einheit=einheit,LSG=False)
    lsg=quaderLoesungsskizze(a=a,b=b,c=c,einheit=einheit,LSG=True)
    aufg.append('}')
    return [aufg,lsg,[]]

def quaderLoesungsskizze(a=3,b=4,c=3,einheit='cm',LSG=False):
    struktur=[]
    struktur.append('\\begingroup\\setlength{\\jot}{0.02cm}')
    struktur.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
    struktur.append('\\begin{tikzpicture}[show background grid]')
    struktur.append('\\node at (7,0) {} ;')
    struktur.append('\\node[left] at (0,1.25) {\mbox{Formeln:} };')
    struktur.append(f'\\node[right] at (0,0.75) {{$V={"a \\cdot b \\cdot c" if LSG else ""}$}};')
    struktur.append(f'\\node[right] at (0,0.25) {{$O={"2\\cdot a \\cdot b +2\\cdot a \\cdot c+2\\cdot b \\cdot c" if LSG else ""}$}};')
    struktur.append('\\node[left] at (0,-0.25) {Geg.: };')
    struktur.append(f'\\node[right] at (0,-0.25) {{$a = {strNW(a,True)}~{einheit}$}};')
    struktur.append(f'\\node[right] at (0,-0.75) {{$b = {strNW(b,True)}~{einheit}$}};')
    struktur.append(f'\\node[right] at (0,-1.25) {{$c = {strNW(c,True)}~{einheit}$}};')
    struktur.append('\\node[left] at (0,-1.75) {Ges.: };')
    struktur.append('\\node[right] at (0,-1.75) {V  = ? };')
    struktur.append('\\node[right] at (0,-2.25) {O  = ? };')
    struktur.append('\\node[below right] at (0,-2.75) {')
    struktur.append('$\\begin{aligned}')
    struktur.append(f'V\\ &=\\ {"a\\cdot b \\cdot c" if LSG else ""}\\\\')
    struktur.append(f'V\\ &=\\ {f"{strNW(a,True)}\\cdot {strNW(b,True)} \\cdot {strNW(c,True)}" if LSG else ""}\\\\')
    struktur.append(f'V\\ &=\\ {f"{strNW(a*b*c,True)}~{einheit}^3" if LSG else ""}\\\\')
    struktur.insert(-1,'\\makebox[0pt][l]{\\uuline{\\phantom{$' + struktur[-1].replace('&', '') + '$}}}')
    struktur.append(f'O\\ &={f"\\ 2\\cdot a \\cdot b +2\\cdot a \\cdot c+2\\cdot b \\cdot c" if LSG else ""}\\\\')
    struktur.append(f'O\\ &={f"\\ 2\\cdot {strNW(a,True)} \\cdot {strNW(b,True)} +2\\cdot {strNW(a,True)} \\cdot {strNW(c,True)}+2\\cdot {strNW(b,True)} \\cdot {strNW(c,True)}" if LSG else ""}\\\\')
    struktur.append(f'O\\ &={f"\\ {strNW(2*a*b+2*a*c+2*b*c,True)}~{einheit}^2" if LSG else ""}\\\\')
    struktur.insert(-1,'\\makebox[0pt][l]{\\uuline{\\phantom{$' + struktur[-1].replace('&', '') + '$}}}')
    struktur.append('\\end{aligned}$};')
    struktur.append('\\end{tikzpicture}') 
    struktur.append('\\endgroup')
    return struktur

def erzeugePrismaVolOMitVorgabe(typ="Dreieck",einheit='cm',ganzeZahlen=True,mitFormeln=True,stehend=True,mitText=True,anzSpalten=[2,2]):
    breitePbox=6.5 if anzSpalten==2 else 13
    maxDim=14 if anzSpalten[0] == 1 else 5
    seitenFormeln={'Dreieck':[['a','b','c','h_c','h_K'],['{c}*{h_c}/2','\\frac{{c}\\cdot{h_c}}{2}'],['{a}+{b}+{c}','{a}+{b}+{c}']]}
    seitenFormeln['Trapez']=[['a','b','c','d','h_a','h_K'],['({a}+{c})*{h_a}/2','\\frac{({a}+{c})\\cdot{h_a}}{2}'],['{a}+{b}+{c}+{d}','{a}+{b}+{c}+{d}']]
    varis={}
    for seite in seitenFormeln[typ][0]:
        varis[seite]=random.randint(3,50)*(1 if ganzeZahlen else 1/10)
    if typ=='Dreieck':
        while varis['a']+varis['b']<varis['c'] or varis['c']+varis['b']<varis['a'] or varis['a']+varis['c']<varis['b']:
            for seite in seitenFormeln[typ][0]:
                varis[seite]=random.randint(3,50)*(1 if ganzeZahlen else 1/10)
        alpha=math.acos((varis['a']**2-varis['b']**2-varis['c']**2)/(-2*varis['b']*varis['c']))
        varis['h_c']=varis['b']*math.sin(alpha)
    if typ=='Trapez':
        varis['h_a']=min([varis['b'],varis['d']])*random.randint(7,9)/10
    varisLsg=dict(varis)
    aufg=[F'\\pbox{{{breitePbox}{"cm"}}}{{Berechne das Volumen und die Oberfläche:\\\\'] if mitText else []
    aufg=aufg+prismenNichtMassstab(typ=typ,varis=varis,stehend=stehend)
    aufg=aufg+['\\\\']
    aufg=aufg+prismaLsgSchema(varis=varis,G=seitenFormeln[typ][1],u_G=seitenFormeln[typ][2],mitLSG=False,mitFormeln=mitFormeln)
    aufg=aufg+['}']
    lsg=prismaLsgSchema(varis=varisLsg,G=seitenFormeln[typ][1],u_G=seitenFormeln[typ][2],mitLSG=True)
    return [aufg,lsg,[]]

def prismaLsgSchema(varis={'a':4,'b':3,'c':5,'h_c':2.7,'h_K':5},G=['{c}*{h_c}/2','\\frac{{c}\\cdot{h_c}}{2}'],u_G=['{a}+{b}+{c}','{a}+{b}+{c}'],einheit='cm',mitLSG=True,mitFormeln=False):
    formeln={'V':['{G}*{h_K}','{G}\\cdot {h_K}']}
    formeln['O']=['{M}+2*{G}','{M}+2\\cdot{G}']
    formeln['M']=['{u_G}*{h_K}','{u_G}\\cdot{h_K}']
    formeln['G']=G
    formeln['u_G']=u_G
    schema=[]
    schema.append('\\begingroup\\setlength{\\jot}{0.02cm}')
    schema.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
    schema.append('\\begin{tikzpicture}[show background grid]')
    l1=len(schema)
    if not mitLSG:
        schema.append(F'\\node at (4,0) {{}};') 
    schema.append(F'\\node[left] at (0,{(len(schema)-l1)*(-0.5)-0.25}) {{\\mbox{{Formeln:}} }};')
    l1=l1+1
    for f in list(formeln.keys()):
        schema.append(F'\\node[right] at (0,{(len(schema)-l1)*(-0.5)-0.25}) {{${f} ={f" {formeln[f][1]}" if (mitLSG or mitFormeln) else ""}$}};')
    schema.append(F'\\node[left] at (0,{(len(schema)-l1)*(-0.5)-0.25}) {{Geg.: }};')
    l1=l1+1
    for x in list(varis.keys()):
        schema.append(F'\\node[right] at (0,{(len(schema)-l1)*(-0.5)-0.25}) {{${x}={f"{strNW(varis[x],2)}~{einheit}" if (mitLSG or mitFormeln) else ""}$}};')
    schema.append(F'\\node[left] at (0,{(len(schema)-l1)*(-0.5)-0.25}) {{Ges.: }};')
    l1=l1+1
    schema.append(F'\\node[right] at (0,{(len(schema)-l1)*(-0.5)-0.25}) {{V  = ? }};')
    schema.append(F'\\node[right] at (0,{(len(schema)-l1)*(-0.5)-0.25}) {{O  = ? }};')
    schema.append(F'\\node[below right] at (0,{(len(schema)-l1)*(-0.5)-0.25}) {{')
    schema.append('$\\begin{aligned}')
    for zeichen in list(formeln.keys())[::-1]:
        formel=formeln[zeichen][0]
        formelText=formeln[zeichen][1]
        schema.append(f'{zeichen}\\ &={"\\phantom{" if not mitLSG else ""}\\ {formelText}{"}" if not mitLSG else ""}\\\\')
        for x in varis.keys():
            formel = formel.replace(f'{{{x}}}',f'{varis[x]}')
            formelText = formelText.replace(f'{{{x}}}',f'{{{strNW(varis[x],2)}}}')
        schema.append(f'{zeichen}\\ &={"\\phantom{" if not mitLSG else ""}\\ {formelText}{"}" if not mitLSG else ""}\\\\')
        varis[zeichen]=eval(formel)
        if mitLSG:
            schema.append(f'{zeichen}\\ &=\\ {strNW(varis[zeichen],2)} {einheit}{"^3" if zeichen in ["V"] else ("^2" if zeichen in ["O","M","G"] else "")}\\\\')
        else:
            schema.append(f'{zeichen}\\ &=\\phantom{{\\ {strNW(varis[zeichen],2)} {einheit}{"^3" if zeichen in ["V"] else ("^2" if zeichen in ["O","M","G"] else "")}}}\\\\')
        schema.insert(-1,f'\\makebox[0pt][l]{{\\u{"u" if zeichen in ["V","O"] else ""}line{{\\phantom{{${schema[-1].replace("&", "")}$}}}}}}')
    schema.append('\\end{aligned}$};')
    schema.append('\\end{tikzpicture}')
    schema.append('\\endgroup')
    return schema

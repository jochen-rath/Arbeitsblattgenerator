#!/usr/bin/env python
# coding: utf8

#Diese Datei enthält verschiedene Funktionen, zur Erzeugung von Aufgaben zur Berechnung von Termen und Gleichungen


#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())


opZumText={'*':'·','/':':','+':'+','-':'-'}
invOp={'+':'-','-':'+','*':'/','/':'*'}
linie='\\rule{1cm}{0.15mm}'
linie='\\uline{\\qquad}'

def erzeugeTikzAlignedUmrandung(alignedBefehle=['x&=5+8']):
    latexcommand=[]
    latexcommand.append('\\begingroup\\setlength{\\jot}{-0.03cm}')
    latexcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')  
    latexcommand.append('\\begin{tikzpicture}[show background grid]')  
    latexcommand.append('\\node[below right] at (0,0.1) {')  
    latexcommand.append('$\\begin{aligned}')
    latexcommand.append('\\end{aligned}$};')
    latexcommand.append('\\end{tikzpicture}')   
    latexcommand.append('\\endgroup')
    return latexcommand[:5]+alignedBefehle+latexcommand[-3:]

def erzeugePlusMinusDifferenziert(mitZahlen=False):
    x=random.randint(-50,50)
    a=random.randint(1,50)
    op=random.choice(['+','-'])
    b=eval(f'{x}{op}{a}')
    G=f'x{op}{a}={b}'
    afg=[f'x{op}{a} & ={b} & & \\mid {f"{invOp[op]}{a}" if mitZahlen else linie} \\\\[0.5cm]']
    if mitZahlen:
        afg.append(f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{x = {linie} }}}}}}')
    afg.append(f'x & = {linie}  & & \\\\[0.5cm]')
    afg.append(f'\\mbox{{Probe}}: \\qquad&   & & \\\\')
    afg.append(f'x{op}{a} & ={b} & &  \\\\[0.5cm]')
    afg.append(f'{x if mitZahlen else linie}{op}{a} & ={b} & &  \\\\[0.5cm]')
    if mitZahlen:
        afg.append(f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{{linie} = {b} }}}}}}')
    afg.append(f'{linie} & ={b} & &  \\\\[0.5cm]')
    lsg=[f'x{op}{a} & ={b} & & \\mid \\uline{{~\\textcolor{{red}}{{{invOp[op]}{a}}}~}} \\\\[0.5cm]']
    lsg.append(f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{x = {linie} }}}}}}')
    lsg.append(f'x & =  \\textcolor{{red}}{{{x}}} & & \\\\[0.5cm]')
    lsg.append(f'\\mbox{{Probe}}: \\qquad&   & & \\\\[0.5cm]')
    lsg.append(f'x{op}{a} & ={b} & &  \\\\[0.5cm]')
    lsg.append(f'\\uline{{~\\textcolor{{red}}{{{x}}}~}}{op}{a} & ={b} & &  \\\\[0.5cm]')
    lsg.append(f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{x = {linie} }}}}}}')
    lsg.append(f'\\uline{{~\\textcolor{{red}}{{{b}}}~}} & ={b} & &  \\\\[0.5cm]')
    afg=erzeugeTikzAlignedUmrandung(afg)
    lsg=erzeugeTikzAlignedUmrandung(lsg)
    return [afg,lsg,[]]

def erzeugeMalGeteiltDifferenziert(mitZahlen=False):
    op=random.choice(['*','/'])
    if op=='*':
        x=random.randint(1,12)
        a=random.randint(2,12)
        b=x*a
    else:
        a=random.randint(2,12)
        b=random.randint(2,12)
        x=a*b        
    afg=[f'{(f"{a}·x" if mitZahlen else f"{a}x") if op=="*" else f"$$frac{{x}}{{{a}}}"} & ={b} & & \\mid {f"{opZumText[invOp[op]]}{a}" if mitZahlen else linie} \\\\[0.5cm]'.replace('$$','\\')]
    if mitZahlen:
        afg.append(f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{x = {linie} }}}}}}')
    afg.append(f'x & = {linie}  & & \\\\[0.5cm]')
    afg.append(f'\\mbox{{Probe}}: \\qquad&   & & \\\\')
    afg.append(f'x{opZumText[op]}{a} & ={b} & &  \\\\[0.5cm]')
    afg.append(f'{x if mitZahlen else linie}{opZumText[op]}{a} & ={b} & &  \\\\[0.5cm]')
    if mitZahlen:
        afg.append(f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{x = {linie} }}}}}}')
    afg.append(f'{linie} & ={b} & &  \\\\[0.5cm]')
    lsg=[f'x{opZumText[op]}{a} & ={b} & & \\mid \\uline{{~\\textcolor{{red}}{{{opZumText[invOp[op]]}{a}}}~}} \\\\[0.5cm]']
    lsg.append(f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{x = {linie} }}}}}}')
    lsg.append(f'x & =   \\uline{{~\\textcolor{{red}}{{{x}}}~}} & &  \\\\[0.5cm]')
    lsg.append(f'\\mbox{{Probe}}: \\qquad&   & & \\\\[0.5cm]')
    lsg.append(f'x{opZumText[op]}{a} & ={b} & &  \\\\[0.5cm]')
    lsg.append(f' \\uline{{~\\textcolor{{red}}{{{x}}}~}}{opZumText[op]}{a} & ={b} & &  \\\\[0.5cm]')
    lsg.append(f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{x = {linie} }}}}}}')
    lsg.append(f' \\uline{{~\\textcolor{{red}}{{{b}}}~}} & ={b} & &  \\\\')
    afg=erzeugeTikzAlignedUmrandung(afg)
    lsg=erzeugeTikzAlignedUmrandung(lsg)
    return [afg,lsg,[]]

def listZuAligned(eingabe):
    ausgabe=[]
    maxSpalten=1
    for zeile in eingabe:
        maxSpalten=max(maxSpalten,len(zeile))
        if not (True in ['makebox' in x for x in zeile]):
            ausgabe.append(f'{"&".join(zeile)}  \\\\[0.5cm]')
        else:
            ausgabe.append(''.join(zeile))
    return ausgabe

def lsgRot(rot,mitLsg=False):
    return '\\textcolor{red}{'+str(rot)+'}' if mitLsg else rot
def schMit(a,mittenDrin=False,mitLsg=False):
#Schreibe Mittendrin, d.h. diese Funktion wird von einer anderen Aufgabe aufgerufen
    return a if not mittenDrin else (lsgRot(a,mitLsg) if mitLsg else linie)

def schreibeMalPlusMinus(a=-2,b=-3,x=6,mitZahlen=False,mitLsg=False,umdrehen=False,mitDrin=False):
    c=a*x+b
    op='-' if b<0 else '+'
    calc=[[f'{schMit(a,mitDrin,mitLsg)}x{op}{schMit(abs(b),mitDrin,mitLsg)} ',f'={schMit(c,mitDrin,mitLsg)}',' ',f'\\mid {lsgRot(f"{invOp[op]}{abs(b)}",mitLsg) if mitZahlen or mitLsg else linie}']]
    calc.append([f'{schMit(a,mitDrin,mitLsg)}x',f'= {lsgRot(c-b,mitLsg) if mitLsg else linie}',' ',f'\\mid {lsgRot(f":{a}",mitLsg) if mitZahlen or mitLsg else linie}'])
    calc.append([f'x',f'={lsgRot(x,mitLsg) if mitLsg else linie}',' ',' '])
    calc.append([f'\\mbox{{Probe}}: \\qquad',' ',' ',' '])
    if mittenDrin:
        return calc
    calc.append([f'{a}x{op}{abs(b)}',f'={c}',' ',' ',])
    calc.append([f'{a}·{lsgRot(x if x>0 else f"({x})",mitLsg) if mitZahlen or mitLsg else linie}{op}{abs(b)}',f'={c} ',' ',' '])
    calc.append([f'{lsgRot(a*x,mitLsg) if mitZahlen or mitLsg else linie}{op}{abs(b)} ',f'={c} ',' ',' '])
    calc.append([f'{lsgRot(c,mitLsg) if mitLsg else linie} ',f'={c}',' ',' '])
#Unterstreichen
    if umdrehen:
        for i in 0,1,4,5,6,7:
            calc[i][0],calc[i][1]=calc[i][1].replace('=',''),f'={calc[i][0]}'
        calc.insert(2,[f'{lsgRot(x,mitLsg) if mitLsg else linie}','=x',' ',f'\\mid {lsgRot("$$mbox{{umdrehen}}",mitLsg) if mitLsg else linie} '.replace('$$','\\')])
    if mitZahlen or mitLsg:
        calc.insert(-1,[f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{{x} = {x}\quad }}}}}}'])
        calc.insert(3 if umdrehen else 2,[f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{{x} = {x} }}}}}}'])
    return listZuAligned(calc)


def schreibeMalPlusMinus(a=-2,b=-3,x=6,c=0,mitZahlen=False,mitLsg=False,umdrehen=False,mitDrin=False):
#mitDrin=mittenDrin,schMit=schreibeMittendrin: Die Zahl wird nicht geschrieben, wenn die Funktion
#von einer anderen Lösungsfunktion aufgerufen wird.
#    a*x+b=c*x+d
    d=a*x+b-c*x
    calc=[]
    L=f'{schMit(a,mitDrin,mitLsg)}x{vZ(b)}{schMit(abs(b),mitDrin,mitLsg)}'
    if not c==0:
        R=f'{schMit(d,mitDrin,mitLsg)}{vZ(c)}{schMit(abs(c),mitDrin,mitLsg)}x' if umdrehen else f'{schMit(abs(c),mitDrin,mitLsg)}x{vZ(d)}{schMit(abs(d),mitDrin,mitLsg)}'
        calc.append([f'{L}',f'={R}',' ',f' \\mid {lsgRot(invOp[vZ(c)]+str(abs(c))+"x",mitLsg) if mitZahlen or mitLsg else linie}'])
        L=f'{lsgRot(a-c,mitLsg) if mitLsg else linie}x{vZ(b)}{schMit(abs(b),mitDrin,mitLsg)}'
        R=f'{d if mitLsg else linie}'
    else:
        R=f'{schMit(d,mitDrin,mitLsg)}'
    calc.append([f'{L}',f'={R}',' ',f' \\mid {lsgRot(invOp[vZ(b)]+str(abs(b)),mitLsg) if mitZahlen or mitLsg else linie}'])    
    calc.append([f'{lsgRot(a-c,mitLsg)}x',f'={lsgRot(d-b,mitLsg)}',' ',f'\\mid {lsgRot(":"+("(" if a-c<0 else "" )+f"{a-c}"+(")" if a-c<0 else "" ),mitLsg) if mitZahlen or mitLsg else linie}'])
    calc.append([f'x',f'={lsgRot(x,mitLsg) if mitLsg else linie}',' ',' '])
    calc.append([f'\\mbox{{Probe}}: \\qquad',' ',' ',' '])
    if mitDrin:
        return calc
    calc.append([f'{a}x{vZ(b)}{abs(b)}',f'={c}',' ',' ',])
    calc.append([f'{a}·{lsgRot(x if x>0 else f"({x})",mitLsg) if mitZahlen or mitLsg else linie}{vZ(b)}{abs(b)}',f'={c} ',' ',' '])
    calc.append([f'{lsgRot(a*x,mitLsg) if mitZahlen or mitLsg else linie}{vZ(b)}{abs(b)} ',f'={c} ',' ',' '])
    calc.append([f'{lsgRot(c,mitLsg) if mitLsg else linie} ',f'={c}',' ',' '])
#Unterstreichen
    if umdrehen:
        for i in 0,1,4,5,6,7:
            calc[i][0],calc[i][1]=calc[i][1].replace('=',''),f'={calc[i][0]}'
        calc.insert(2,[f'{lsgRot(x,mitLsg) if mitLsg else linie}','=x',' ',f'\\mid {lsgRot("$$mbox{{umdrehen}}",mitLsg) if mitLsg else linie} '.replace('$$','\\')])
    if mitZahlen or mitLsg:
        calc.insert(-1,[f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{{x} = {x}\quad }}}}}}'])
        calc.insert(3 if umdrehen else 2,[f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{{x} = {x} }}}}}}'])
    return listZuAligned(calc)


def schreibeMalPlusMinusBeideSeiten(a=-4,b=-6,c=7,x=5,mitZahlen=False,mitLsg=False,gedreht=False,mittenDrin=False):
    #Löst eine Gleichung der Form: a*x+b=c*x+d
    d=a*x+b-c*x
    L=f'{schMit(a,mittenDrin,mitLsg)}x{vZ(b)}{schMit(abs(b),mittenDrin,mitLsg)}'
    R=f'{schMit(d,mittenDrin,mitLsg)}{vZ(c)}{schMit(abs(c),mittenDrin,mitLsg)}x' if gedreht else f'{schMit(abs(c),mittenDrin,mitLsg)}x{vZ(d)}{schMit(abs(d),mittenDrin,mitLsg)}'
    calc=[[f'{L}',f'={R}',' ',f' \\mid {lsgRot(invOp[vZ(c)]+str(abs(c))+"x",mitLsg) if mitZahlen or mitLsg else linie}']]
    calc=calc+schreibeMalPlusMinus(a=a-c,b=b,x=x,mitZahlen=mitZahlen,mitLsg=mitLsg,mittenDrin=True)
    if mittenDrin:
        return calc
    calc.append([f'{L}',f'={R}',' ',' ',])    
    L=f'{a if not mittenDrin else (lsgRot(a,mitLsg) if mitLsg else linie)}·{lsgRot(x if x>0 else f"({x})",mitLsg) if mitZahlen or mitLsg else linie}{vorz["b"]}{abs(b) if not mittenDrin else (lsgRot(abs(b),mitLsg) if mitLsg else linie)}'
    R=f'{d}{vorz["c"]}{abs(c)}·{lsgRot(x if x>0 else f"({x})",mitLsg) if mitZahlen or mitLsg else linie}' if gedreht else f'{c}·{lsgRot(x if x>0 else f"({x})",mitLsg) if mitZahlen or mitLsg else linie}{vorz["d"]}{abs(d)}'
    calc.append([f'{L}',f'={R}',' ',' ',])
    L=f'{lsgRot(a*x,True) if mitLsg else linie}{vorz["b"]}{abs(b)}'
    R=f'{d}{vorz["c"]}{lsgRot(abs(c)*x,mitLsg) if mitLsg else linie}' if gedreht else f'{lsgRot(c*x,True) if mitLsg else linie}{vorz["d"]}{abs(d)}'
    calc.append([f'{L}',f'={R}',' ',' ',]) 
    calc.append([f'{lsgRot(a*x+b,mitLsg) if mitLsg else linie}',f'={lsgRot(c*x+d,mitLsg) if mitLsg else linie}',' ',' ',])       
    return listZuAligned(calc)

def schreibeErstZusammenfassen(x=-13,wL=[6, 5, 37, -28],wR=[-1, -9, 35, -299],iL= [0, 2, 3, 1],iR=[3, 2, 1, 0],mitZahlen=False,mitLsg=False):
    wxL=[f'{vZ(wL[0])}{abs(wL[0])}x',f'{vZ(wL[1])}{abs(wL[1])}x',f'{vZ(wL[2])}{abs(wL[2])}',f'{vZ(wL[3])}{abs(wL[3])}']
    wxR=[f'{vZ(wR[0])}{abs(wR[0])}x',f'{vZ(wR[1])}{abs(wR[1])}x',f'{vZ(wR[2])}{abs(wR[2])}',f'{vZ(wR[3])}{abs(wR[3])}']
    L=''.join([wxL[i] for i in iL])
    R=''.join([wxR[i] for i in iR])
    L,R=L[1:] if L[0]=='+' else L,R[1:] if R[0]=='+' else R
    calc=[[f'{L}',f'={R}',' ',f' \\mid {"$$mbox{Zusammenfassen}" if mitZahlen or mitLsg else linie}'.replace('$$','\\')]]
    calc=calc+schreibeMalPlusMinusBeideSeiten(a=wL[0]+wL[1],b=wL[2]+wL[3],c=wR[0]+wR[1],x=x,mitZahlen=mitZahlen,mitLsg=mitLsg,mittenDrin=True)
    return listZuAligned(calc)
    
def erzeugeMalPlusMinusDifferenziert(mitZahlen=False,xRechts=False):
    op=random.choice(['+','-'])
    x=random.randint(1,12) if random.randint(0,1)>0 else -random.randint(1,12) 
    a=random.randint(2,10)
    b=random.randint(1,50)
    c=a*x+b if op=='+' else a*x-b
    afg=schreibeMalPlusMinus(a=a,b=b,x=x,mitZahlen=mitZahlen,mitLsg=False,umdrehen=xRechts)
    lsg=schreibeMalPlusMinus(a=a,b=b,x=x,mitZahlen=mitZahlen,mitLsg=True,umdrehen=xRechts)
    afg=erzeugeTikzAlignedUmrandung(afg)
    lsg=erzeugeTikzAlignedUmrandung(lsg)
    return [afg,lsg,[]]
    

def erzeugeMalPlusMinusBeideSeitenDifferenziert(mitZahlen=False):
    a,b,c,d=1,1,1,1
    gedreht=random.choice([True,False])
    while int(a)==int(d) or a==c or int(d)==0:
        x=random.randint(1,20) if random.randint(0,1)>0 else -random.randint(1,20) 
        a=random.randint(2,10)
        b=random.choice([random.randint(-50,-1),random.randint(1,50)])
        c=random.randint(2,10) if random.randint(0,1)>0 else -random.randint(2,10) 
        d=a*x+b-c*x
    afg=erzeugeTikzAlignedUmrandung(schreibeMalPlusMinusBeideSeiten(a=a,b=b,c=c,x=x,mitZahlen=mitZahlen,mitLsg=False))
    lsg=erzeugeTikzAlignedUmrandung(schreibeMalPlusMinusBeideSeiten(a=a,b=b,c=c,x=x,mitZahlen=mitZahlen,mitLsg=True))
    return [afg,lsg,[]]

def vZ(x):
    return "+" if x>0 else "-"

def erzeugeGlErstZusammenfassenDifferenziert(mitZahlen=False,nurLinks=True,xRechts=False):
    wL,wR=4*[0],4*[0]
    while 0 in wL or 0 in wR or x==0:
        wL=[random.randint(-12,12),random.randint(-12,12),random.randint(-50,50),random.randint(-50,50)]
        wR=[random.randint(-12,12),random.randint(-12,12),random.randint(-50,50),random.randint(-50,50)]
        x=random.randint(-30,30)
        wR[-1]=wL[0]*x+wL[1]*x+wL[2]+wL[3]-wR[0]*x-wR[1]*x-wR[2]
    iL,iR=list(range(4)),list(range(4))
    random.shuffle(iL)
    random.shuffle(iR)
    return x,wL,wR,iL,iR
    op=random.choice(['+','-'])
    x=random.randint(1,12) if random.randint(0,1)>0 else -random.randint(1,12) 
    a=random.randint(2,10)
    b=random.randint(1,50)
    c=a*x+b if op=='+' else a*x-b
    afg=schreibeMalPlusMinus(a=a,b=b,x=x,mitZahlen=mitZahlen,mitLsg=False,umdrehen=xRechts)
    lsg=schreibeMalPlusMinus(a=a,b=b,x=x,mitZahlen=mitZahlen,mitLsg=True,umdrehen=xRechts)
    afg=erzeugeTikzAlignedUmrandung(afg)
    lsg=erzeugeTikzAlignedUmrandung(lsg)
    return [afg,lsg,[]]
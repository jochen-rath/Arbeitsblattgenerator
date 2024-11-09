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

def erzeugeMalPlusMinusDifferenziert(mitZahlen=False):
    op=random.choice(['+','-'])
    x=random.randint(1,12) if random.randint(0,1)>0 else -random.randint(1,12) 
    a=random.randint(2,10)
    b=random.randint(1,50)
    c=a*x+b if op=='+' else a*x-b
    afg=[f'{a}x{op}{b} & ={c} & & \\mid {f"{invOp[op]}{b}" if mitZahlen else linie} \\\\[0.5cm]']
    afg=afg+[f'{a}x & ={linie} & & \\mid {f":{a}" if mitZahlen else linie} \\\\[0.5cm]']
    if mitZahlen:
        afg.append(f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{x = {linie} }}}}}}')
    afg=afg+[f'x & = {linie}  & & \\\\[0.5cm]']
    afg.append(f'\\mbox{{Probe}}: \\qquad&   & & \\\\')
    afg.append(f'{a}x{op}{b} & ={c}& &  \\\\[0.5cm]')
    afg.append(f'{a}·{(x if x>0 else f"({x})") if mitZahlen else linie}{op}{b} & ={c} & &  \\\\[0.5cm]')
    afg.append(f'{a*x if mitZahlen else linie}{op}{b} & ={c} & &  \\\\[0.5cm]')
    if mitZahlen:
        afg.append(f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{x = {linie} }}}}}}')
    afg.append(f'{linie} & ={c} & &  \\\\[0.5cm]')
    lsg=[f'{a}x{op}{b} & ={c} & & \\mid \\uline{{~\\textcolor{{red}}{{{f"{invOp[op]}{b}"}}}~}} \\\\[0.5cm]']
    lsg=lsg+[f'{a}{opZumText["*"]}x & =\\uline{{~\\textcolor{{red}}{{{eval(f"{c}{invOp[op]}{b}")}}}~}} & & \\mid \\uline{{~\\textcolor{{red}}{{{f":{a}"}}}~}} \\\\[0.5cm]']
    lsg.append(f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{x = {linie} }}}}}}')
    lsg=lsg+[f'x & = \\uline{{~\\textcolor{{red}}{{{x}}}~}}  & & \\\\[0.5cm]']
    lsg.append(f'\\mbox{{Probe}}: \\qquad&   & & \\\\[0.5cm]')
    lsg.append(f'{a}x{op}{b} & ={c}& &  \\\\[0.5cm]')
    lsg.append(f'{a}·\\uline{{~\\textcolor{{red}}{{{(x if x>0 else f"({x})")}}}~}}{op}{b} & ={c} & &  \\\\[0.5cm]')
    lsg.append(f'\\uline{{~\\textcolor{{red}}{{{a*x}}}~}}{op}{b} & ={c} & &  \\\\[0.5cm]')
    lsg.append(f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{x = {linie} }}}}}}')
    lsg.append(f'\\uline{{~\\textcolor{{red}}{{{c}}}~}} & ={c} & &  \\\\[0.5cm]')
    afg=erzeugeTikzAlignedUmrandung(afg)
    lsg=erzeugeTikzAlignedUmrandung(lsg)
    return [afg,lsg,[]]
    
def erzeugeMalPlusMinusXRechtsDifferenziert(mitZahlen=False):
    op=random.choice(['+','-'])
    x=random.randint(1,12) if random.randint(0,1)>0 else -random.randint(1,12) 
    a=random.randint(2,10)
    b=random.randint(1,50)
    c=a*x+b if op=='+' else a*x-b
    afg=[f'{c}& = {a}x{op}{b} & & \\mid {f"{invOp[op]}{b}" if mitZahlen else linie} \\\\[0.5cm]']
    afg=afg+[f' {linie} & ={a}x& & \\mid {f":{a}" if mitZahlen else linie} \\\\[0.5cm]']
    afg=afg+[f' {linie} & =x& & \\mid {"$$mbox{umdrehen}" if mitZahlen else linie} \\\\[0.5cm]'.replace('$$','\\')]
    if mitZahlen:
        afg.append(f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{x = {linie} }}}}}}')
    afg=afg+[f'x & = {linie}  & & \\\\[0.5cm]']
    afg.append(f'\\mbox{{Probe}}: \\quad&   & & \\\\')
    afg.append(f'{c} & = {a}x{op}{b}& &  \\\\[0.5cm]')
    afg.append(f' {c}& = {a}·{(x if x>0 else f"({x})") if mitZahlen else linie}{op}{b}& &  \\\\[0.5cm]')
    afg.append(f'{c}& = {a*x if mitZahlen else linie}{op}{b} & &  \\\\[0.5cm]')
    if mitZahlen:
        afg.append(f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{x = {linie} }}}}}}')
    afg.append(f'{c} & ={linie} & &  \\\\[0.5cm]')
    lsg=[f'{c} & ={a}x{op}{b} & & \\mid \\uline{{~\\textcolor{{red}}{{{f"{invOp[op]}{b}"}}}~}} \\\\[0.5cm]']
    lsg=lsg+[f'\\uline{{~\\textcolor{{red}}{{{eval(f"{c}{invOp[op]}{b}")}}}~}} & ={a}{opZumText["*"]}x  & & \\mid \\uline{{~\\textcolor{{red}}{{{f":{a}"}}}~}} \\\\[0.5cm]']
    lsg=lsg+[f'\\uline{{~\\textcolor{{red}}{{{x}}}~}} & = x  & & \\mid \\mbox{{umdrehen}} \\\\[0.5cm]']
    lsg.append(f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{x = {linie} }}}}}}')
    lsg=lsg+[f'x & = \\uline{{~\\textcolor{{red}}{{{x}}}~}}  & & \\\\[0.5cm]']
    lsg.append(f'\\mbox{{Probe}}: \\quad&   & & \\\\[0.5cm]')
    lsg.append(f'{c}& ={a}x{op}{b} & &  \\\\[0.5cm]')
    lsg.append(f'{c} & ={a}·\\uline{{~\\textcolor{{red}}{{{(x if x>0 else f"({x})")}}}~}}{op}{b} & &  \\\\[0.5cm]')
    lsg.append(f'{c} & =\\uline{{~\\textcolor{{red}}{{{a*x}}}~}}{op}{b}& &  \\\\[0.5cm]')
    lsg.append(f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{x = {linie} }}}}}}')
    lsg.append(f'{c}& = \\uline{{~\\textcolor{{red}}{{{c}}}~}} & &  \\\\[0.5cm]')
    afg=erzeugeTikzAlignedUmrandung(afg)
    lsg=erzeugeTikzAlignedUmrandung(lsg)
    return [afg,lsg,[]]
    

def erzeugeMalPlusMinusBeideSeitenDifferenziert(mitZahlen=False):
    a,b,c,d=1,1,1,1
    gedreht=random.choice([True,False])
    while int(a)==int(d) or a==c:
        x=random.randint(1,20) if random.randint(0,1)>0 else -random.randint(1,20) 
        a=random.randint(2,10)
        b=random.choice([random.randint(-50,-1),random.randint(1,50)])
        c=random.randint(2,10) if random.randint(0,1)>0 else -random.randint(2,10) 
        d=a*x+b-c*x
    vorzeiB="+" if b>0 else "-"
    vorzeiC="+" if c>0 else "-"
    vorzeiD="+" if d>0 else "-"
    vorzeiAC="+" if a-c>0 else "-"
    vorzeiCX="+" if c*x>0 else "-"
    L=f'{a}x{vorzeiB}{abs(b)}'
    R=f'{d}{vorzeiC}{abs(c)}x' if gedreht else f'{c}x{vorzeiD}{abs(d)}'
    afg=[f'{L} & ={R} & & \\mid {f"{invOp[vorzeiC]}{abs(c)}x" if mitZahlen else linie} \\\\[0.5cm]']
#    afg.append(f'{(f"{a-c}x" if not a-c==1 else "") if mitZahlen else linie} {vorzeiB}{abs(b)}& ={d} & & \\mid {f"{invOp[vorzeiB]}{abs(b)}" if mitZahlen else linie} \\\\[0.5cm]')
    afg.append(f'{linie} {vorzeiB}{abs(b)}& ={d} & & \\mid {f"{invOp[vorzeiB]}{abs(b)}" if mitZahlen else linie} \\\\[0.5cm]')
    if not a-c==1:
        klammer=f':{f"({vorzeiAC}" if a-c<0 else ""}{abs(a-c)}{f")" if a-c<0 else ""}'
#        afg.append(f'{f"{a-c}x" if mitZahlen else linie} & ={linie} & & \\mid {f"{klammer}" if mitZahlen else linie} \\\\[0.5cm]')
        afg.append(f'{linie} & ={linie} & & \\mid {f"{klammer}" if mitZahlen else linie} \\\\[0.5cm]')
    if mitZahlen:
        afg.append(f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{x = {linie} }}}}}}')
    afg.append(f'{"x" if mitZahlen else linie}  & = {linie}  & & \\\\[0.5cm]')
    afg.append(f'\\mbox{{Probe}}: \\qquad&   & & \\\\')
    afg.append(f'{L} & ={R}& &  \\\\[0.5cm]')
    L=f'{a}·{(x if x>0 else f"({x})") if mitZahlen else linie}{vorzeiB}{abs(b)} '
    R=f'{d}{vorzeiC}{abs(c)}·{(x if x>0 else f"({x})") if mitZahlen else linie}' if gedreht else f'{c}·{(x if x>0 else f"({x})") if mitZahlen else linie}{vorzeiD}{abs(d)}'
    afg.append(f'{L} & ={R}& &  \\\\[0.5cm]')
    L=f'{linie}{vorzeiB}{abs(b)} '
    R=f'{d}{vorzeiC}{linie}' if gedreht else f'{linie}{vorzeiD}{abs(d)}'
    afg.append(f'{L} & ={R}& &  \\\\[0.5cm]')
    if mitZahlen:
        afg.append(f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{{linie} = {linie} }}}}}}')
    afg.append(f'{linie} & ={linie} & &  \\\\[0.5cm]')
    L=f'{a}x{vorzeiB}{abs(b)}'
    R=f'{d}{vorzeiC}{abs(c)}x' if gedreht else f'{c}x{vorzeiD}{abs(d)}'
    lsg=[f'{L} & ={R} & & \\mid ~\\textcolor{{red}}{{{invOp[vorzeiC]}{abs(c)}x}} \\\\[0.5cm]']
    lsg.append(f'~\\textcolor{{red}}{{{f"{a-c}" if not a-c==1 else ""}x}}{vorzeiB}{abs(b)}& ={d} & & \\mid ~\\textcolor{{red}}{{{f"{invOp[vorzeiB]}{abs(b)}"}}} \\\\[0.5cm]')
    if not a-c==1:
        klammer=f'~\\textcolor{{red}}{{:{f"({vorzeiAC}" if a-c<0 else ""}{abs(a-c)}{f")" if a-c<0 else ""}}}'
        lsg.append(f'{a-c}x & =~\\textcolor{{red}}{{{d-b}}} & & \\mid {klammer} \\\\[0.5cm]')
    lsg.append(f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{x = {linie} }}}}}}')
    lsg.append(f'x & = ~\\textcolor{{red}}{{{x}}}  & & \\\\[0.5cm]')
    lsg.append(f'\\mbox{{Probe}}: \\qquad&   & & \\\\')
    lsg.append(f'{L} & ={R}& &  \\\\[0.5cm]')
    L=f'{a}·\\textcolor{{red}}{{{(x if x>0 else f"({x})")}}}{vorzeiB}{abs(b)} '
    R=f'{d}{vorzeiC}{abs(c)}·\\textcolor{{red}}{{{(x if x>0 else f"({x})")}}}' if gedreht else f'{c}·\\textcolor{{red}}{{{(x if x>0 else f"({x})")}}}{vorzeiD}{abs(d)}'
    lsg.append(f'{L} & ={R}& &  \\\\[0.5cm]')
    L=f'\\textcolor{{red}}{{{a*x}}}{vorzeiB}{abs(b)} '
    R=f'{d}{vorzeiCX}\\textcolor{{red}}{{{abs(c*x)}}}' if gedreht else f'\\textcolor{{red}}{{{c*x}}}{vorzeiD}{abs(d)}'
    lsg.append(f'{L} & ={R}& &  \\\\[0.5cm]')
    lsg.append(f'\\makebox[0pt][l]{{\\uuline{{\\phantom{{{a*x+b} = {a*x+b} }}}}}}')
    lsg.append(f'\\textcolor{{red}}{{{a*x+b}}} & =\\textcolor{{red}}{{{c*x+d}}} & &  \\\\[0.5cm]')
    afg=erzeugeTikzAlignedUmrandung(afg)
    lsg=erzeugeTikzAlignedUmrandung(lsg)
    return [afg,lsg,[]]
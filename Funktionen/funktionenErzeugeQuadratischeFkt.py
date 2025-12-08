#!/usr/bin/env python
# coding: utf8
#Aufruf:
#		import os
#		os.chdir(f'{os.path.expanduser("~")}/Schule/Arbeitsblattgenerator')
#       exec(open("Funktionen/funktionen.py").read())

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())

def erzeugeParabelFkt(hoehe=12,mitB=False,mitC=True,aGleich1=False):
    yMax=1000
    yMin=1000
    a=0 if not aGleich1 else 1
    while (a==0) or abs(yMax)>hoehe or abs(yMin)>hoehe:
        a=random.randint(-20,20)/10 if not aGleich1 else 1
        b=random.randint(5,15)/10 if mitB else 0
        c=random.randint(-30,30)/10  if mitC else 0
        xMax=3 if  hoehe>8 else 2
        xMin=-xMax
        xWerte=list(range(xMin,xMax+1))
        if not b==0:
            xWerte=xWerte+[-b]
            xWerte=list(set(xWerte))
            xWerte.sort()
        yWerte=[a*(x+b)**2+c for x in xWerte]
        yMax=max(yWerte) if max(yWerte)>0 else 0
        yMin=min(yWerte) if min(yWerte)<0 else 0
    fktStr= f'y={strNW(a)}\cdot x^2'
    if not b==0:
        fktStr= f'y={strNW(a)}\cdot (x{"+" if b>0 else "-"}{strNW(abs(b))})^2'
    if not c==0:
        fktStr=f'{fktStr}{"+" if c>0 else "-"}{strNW(abs(c))}'
    return a,b,c,fktStr,xWerte,yWerte,xMin,xMax,yMin,yMax

def erzeugeQuadFunkTabDiaAfg(diagrammVorgegeben=True,mitText=True,nurText=False,mitB=False,mitC=True,anzSpalten=[1,1]):
#y=a*(x+b)^2+c
    a,b,c,fktStr,xWerte,yWerte,xMin,xMax,yMin,yMax=erzeugeParabelFkt(hoehe=(12 if  anzSpalten[0] <2 else 8),mitB=mitB,mitC=mitC)
    afg=[F'\\parbox{{{14 if  anzSpalten[0]<2 else 7}cm}}{{\\raggedright ']
    afg=afg+([F'Übertrage die Werte der Funktion ${fktStr}$ in die Tabelle und zeichne die Funktion.\\'] if mitText else [F'${fktStr}$'])
    tabelle=tikzTabelle(tabelle=[['x']+[strNW(x) for x in xWerte],['y']+['']*len(xWerte),],dim=[1.5 if  anzSpalten[0]<2 else 1.0 ,0.5],spaltenBreite=[],zeilenHoehe=[],newCBuchst='A',tabellenPos=[0,-1.5])
    tabelleLsg=tikzTabelle(tabelle=[['x']+[strNW(x) for x in xWerte],['y']+[strNW(y,True) for y in yWerte],],dim=[1.5 if  anzSpalten[0]<2 else 1.0 ,0.5],spaltenBreite=[],zeilenHoehe=[],newCBuchst='A',tabellenPos=[0,-1.5])
    if diagrammVorgegeben:
        diagramm=diagrammTikzVorgBreiteHoehe(zuPlotten=[],xAchse=[xMin,xMax,(xMax-xMin)+1],yAchse=[yMin,yMax,(yMax-yMin)+1],xlabel='x',ylabel='y',urspr=[0,0],mitUmrandung=False)
    else:
        diagramm=[F'\\node at (7,11) {{ }};']
    afg=afg+ ([] if nurText else (tabelle[:-1]+diagramm+[tabelle[-1]]))
    afg=afg+ ([] if nurText else ['}'])
    if nurText:
        afg=F'{"Zeichne die Wertetabelle und das Diagramm zur Funktion: " if mitText else ""}${fktStr}$'
    textNode=[[-b,c,F'{strNW(c,True)}','below' if a>0 else 'above']]
    diagramm=diagrammTikzVorgBreiteHoehe(zuPlotten=[[F'{a}*(x+{b})*(x+{b})+{c}','red']],textNode=textNode,koordinaten=[[x,yWerte[i]] for i,x in enumerate(xWerte)],xAchse=[xMin,xMax,(xMax-xMin)+1],yAchse=[yMin,yMax,(yMax-yMin)+1],xlabel='x',ylabel='y',urspr=[0,0],mitUmrandung=False)
    lsg=tabelleLsg[:-1]+diagramm+[tabelle[-1]]
    return [afg,lsg,[a,b,c]]

def erzeugeQuadVariAuslesen(mitB=False,mitC=False,erkenneBC=False,mitText=True,anzSpalten=[1,1]):
    if erkenneBC:
        mitB,mitC=True,True
    a,b,c,fktStr,xWerte,yWerte,xMin,xMax,yMin,yMax=erzeugeParabelFkt(hoehe=(12 if  anzSpalten[0] <2 else 8),mitB=mitB,mitC=mitC,aGleich1=erkenneBC)
    diagramm=diagrammTikzVorgBreiteHoehe(zuPlotten=[[F'{a}*(x+{b})*(x+{b})+{c}','black']],xAchse=[xMin,xMax,(xMax-xMin)+1],yAchse=[yMin,yMax,(yMax-yMin)+1],xlabel='x',ylabel='y')
    term='a*(x+b)**2+c'
    afg=[F'\\parbox{{{14 if  anzSpalten[0]<2 else 7}cm}}{{\\raggedright ']
    bestimme=f'{"a" if not erkenneBC else ""}{(", " if not erkenneBC else "")+"b" if mitB else ""}{", c" if mitC else ""}'
    gleichung=f'{"a\cdot " if not erkenneBC else ""}{"(x+b)^2" if mitB else "x^2"}{"+c" if mitC else ""}'
    afg=afg+[f'Bestimme {bestimme} der Parabelgleichung ${gleichung}$ für die Parabel \\']
    afg=afg+diagramm
    afg=afg+['}']
    lsg=[F'\\parbox{{{14 if  anzSpalten[0]<2 else 7}cm}}{{\\raggedright ']
    lsg=lsg+[f'{f"a={strNW(a)}" if not erkenneBC else ""}{(", " if not erkenneBC else "")+f"b={strNW(b)}" if not b==0 else ""}{f", c={strNW(c)}" if not c==0 else ""}']
    aBest=[2]+[[[-b,c],[-b+1,c],[-b+1,c+a]]] if not erkenneBC else [2]
    beschr=[[-b+1,c+a/2,f'a={strNW(a)}','right']]  if not erkenneBC else []
    beschr=beschr+[[-b+0.5,c,f'+1','below' if a<0 else 'above']]   if not erkenneBC else []
    if mitC:
        aBest=aBest+[[[-b,c],[-b,0]]]
        beschr=beschr+[[-b,c/2,f'c={strNW(c)}','right']]
    if mitB:
        aBest=aBest+[[[-b,c],[0,c]]]
        beschr=beschr+[[-b/2,c,f'b={strNW(b)}','above' if a<0 else 'below']]
    diagramm=diagrammTikzVorgBreiteHoehe(zuPlotten=[[F'{a}*(x+{b})*(x+{b})+{c}','black']],streckenzug=aBest,textNode=beschr,xAchse=[xMin,xMax,(xMax-xMin)+1],yAchse=[yMin,yMax,(yMax-yMin)+1],xlabel='x',ylabel='y')
    lsg=lsg+diagramm
    lsg=lsg+['}']
    return [afg,lsg,[a,b,c]]

def erzeugeFindNullstellenQuaFkt(mitA=True,mitB=True,mitC=True,mitText=True,anzSpalten=[1,1]):
    a,c= 1,1
    while (a>0 and c>0) or (a<0 and c<0):
        a,b,c,fktStr,xWerte,yWerte,xMin,xMax,yMin,yMax=erzeugeParabelFkt(hoehe=(12 if  anzSpalten[0] <2 else 8),mitB=mitB,mitC=mitC,aGleich1=not mitA)
        if random.randint(0,6)>5:
            break
    if fktStr.split('y=')[1].startswith('1\\cdot'):
        fktStr=f'y={fktStr.split("y=")[1][7:]}'
    afg=[f'{"Bestimme die Nullstellen der Funktion " if mitText else ""}${fktStr}$']
    term=f'{f"{a}*" if not a==1 else ""}{f"(x+{b})" if mitB else "x"}**2{"+" if c>0 else ""}{f"{c}" if mitC else ""}'
    textNode=[]
    nullPkte=[]
    diagramm=diagrammTikzVorgBreiteHoehe(zuPlotten=[[F'{a}*(x+{b})*(x+{b})+{c}','black']],koordinaten=nullPkte,textNode=textNode,xAchse=[xMin,xMax,(xMax-xMin)+1],yAchse=[yMin,yMax,(yMax-yMin)+1],xlabel='x',ylabel='y')
    lsgUmB=[F'\\parbox{{{14 if  anzSpalten[0]<2 else 7}cm}}{{\\raggedright ']
    lsgUmE=['}']
    if (a>0 and c<0) or (a<0 and c>0):
        lsg=quadFktnullStellenBerechPQFormel(fkt=term,mitTikzUmrandung=True)
        p,q=[2*b,b**2+c/a]
        x1=-p/2+((p/2)**2-q)**0.5
        x2=-p/2-((p/2)**2-q)**0.5
        textNode=[[x1,0,f'$x_1={strNW(x1,True)}$','above'],[x2,0,f'$x_2={strNW(x2,True)}$','above']]
        textNode=textNode+[[-b,c,f'$b={strNW(b,True)};~c={strNW(c,True)}$','above' if a<0 else 'below']]
        if x2<xMin:
            xWerte=[x2]+xWerte
            yWerte=[0]+yWerte
            xMin=x2-0.5
        if x1>xMax:
            xWerte=xWerte+[x1]
            yWerte=yWerte+[0]
            xMax=x1+0.5
        y1=a*(x1+b)**2+c
        y2=a*(x2+b)**2+c
        nullPkte=[[x1,0],[x2,0],[-b,c]]
        yMin=min(c,-1) if c<0 else 0
        yMax=max(c,1) if c>0 else 0
        ursprY=-abs(yMax-yMin)-6
        diagramm=diagrammTikzVorgBreiteHoehe(zuPlotten=[[F'{a}*(x+{b})*(x+{b})+{c}','black']],koordinaten=nullPkte,textNode=textNode,xAchse=[x2-0.5,x1+0.5,(x1-x2+1)+1],yAchse=[yMin,yMax,(yMax-yMin)+1],xlabel='x',ylabel='y',urspr=[0,ursprY],mitUmrandung=False)
        lsg=lsg[0:-2]+diagramm+lsg[-2:]
    elif c==0:
        lsg=[f'Nullstelle: x={strNW(-b)} \\\\'] + diagramm
        lsg=lsgUmB+lsg+lsgUmE
    else:
        lsg=[f'Es existieren keine Nullstellen zur Funktion ${fktStr}$.\\\\']  + diagramm
        lsg=lsgUmB+lsg+lsgUmE
    return [afg,lsg,[]]
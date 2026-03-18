#!/usr/bin/env python
# coding: utf8


#Aufruf:
#       exec(open("Funktionen/funktionenTikzZeichnungen.py").read())
#Diese Skript stellte verschiedene Figuren bereit, die Zeichnungen mit dem Latex-Paket Tikz erzeugen
#       exec(open("Funktionen/funktionen.py").read())
#Aufruf:
#		import os
#		os.chdir(f'{os.path.expanduser("~")}/Schule/Arbeitsblattgenerator')
#       exec(open("Funktionen/funktionen.py").read())

def dreieckUmkreis(alphaAussen=45,beta=45,c=4,a=5,mitLsg=True):
    tikzcommand=[]
    tikzcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
    tikzcommand.append('\\noindent\\begin{tikzpicture}[show background grid]')
    tikzcommand.append(f'\\draw[thick,black] (0,0) coordinate (A) -- ++({alphaAussen}:{c}) coordinate (B) -- ++({180-(beta-alphaAussen)}:{a}) coordinate (C) --cycle ;')
    tikzcommand.append(f'\\coordinate (MAB) at ($(A)!0.5!(B)$);')
    tikzcommand.append(f'\\coordinate (MS1) at ($(MAB)!{1.1*a}cm!90:(B)$);')
    tikzcommand.append(f'\\coordinate (MBC) at ($(B)!0.5!(C)$);')
    tikzcommand.append(f'\\coordinate (MS2) at ($(MBC)!{1.1*a}cm!90:(C)$);')
    tikzcommand.append(f'\\coordinate (MAC) at ($(C)!0.5!(A)$);')
    tikzcommand.append(f'\\coordinate (MS3) at ($(MAC)!{1.1*a}cm!90:(A)$);')
    tikzcommand.append(f'\\coordinate(M) at (intersection of MAC--MS3 and MAB--MS1);')
    tikzcommand.append(f'\\draw[thick,blue] ($(M)!-1!(MAB)$) {"--" if mitLsg else ""} ($(M)!2!(MAB)$);')
    tikzcommand.append(f'\\draw[thick,blue] ($(M)!-1!(MBC)$) {"--" if mitLsg else ""} ($(M)!2!(MBC)$);')
    tikzcommand.append(f'\\draw[thick,blue] ($(M)!-1!(MAC)$) {"--" if mitLsg else ""} ($(M)!2!(MAC)$);')
    if mitLsg:
        tikzcommand.append(f'\\node (kreis) at (M) [draw,thick,red, circle through=(A)] {{}};')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand    
    

def dreieckInnenkreis(alpha=45,a=4,b=5,mitLsg=True):
    #Sinussatz: a/b=sin(alpha)/sin(beta)
    #sin(beta)=b/a*sin(alpha)
    beta=math.degrees(math.asin(b/a*math.sin(math.radians(alpha))))
    gamma=180-alpha-beta
    rotate=0
    tikzcommand=[]
    tikzcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
    tikzcommand.append('\\noindent\\begin{tikzpicture}[show background grid]')
    tikzcommand.append(f'\\draw[thick,black] (0,0)coordinate (A) -- ++({alpha}:{b}) coordinate (C) -- ++({-beta}:{a}) coordinate (B) --cycle ;')
    tikzcommand.append(f'\\draw[thick,blue] (0,0) {"--" if mitLsg else ""} ++({alpha/2}:{1.3*a}) coordinate (WH1);')
    tikzcommand.append(f'\\draw[thick,blue] (B) {"--" if mitLsg else ""} ++({180-beta/2}:{1.3*a})  coordinate (WH2);')
    tikzcommand.append(f'\\draw[thick,blue] (C) {"--" if mitLsg else ""} ++({180+alpha+gamma/2}:{1.3*a})  coordinate (WH3);')
    tikzcommand.append(f'\\coordinate(M) at (intersection of A--WH1 and B--WH2);')
#Finde den Punkt auf AB mit dem kleinsten Abstand zum Mittelpunkt, Tikz Projektion
    tikzcommand.append(f'\\coordinate(R) at ($(A)!(M)!(B)$);')
    if mitLsg:
        tikzcommand.append(f'\\node (kreis) at (M) [draw,thick,red, circle through=(R)] {{}};')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand        



def dreieckRechtw(k=[5,6],label=['5 dm','6 dm',''],punkte=['','',''],mitBogen=True,dR=-1):
    dR=dR if dR>0 else random.randint(0,360)
    ur=[random.randint(0,10)/10,random.randint(0,10)/10]
    hyp=(k[0]**2+k[1]**2)**0.5
    winkel=90
    seitenPos={0:'below,sloped',1:'above,sloped',2:'above,sloped'}
    if dR>39:
        seitenPos={0:'below,sloped',1:'above,sloped',2:'below,sloped'}
    if dR>90:
        seitenPos={0:'above,sloped',1:'above,sloped',2:'below,sloped'}
    if dR>179:
        seitenPos={0:'above,sloped',1:'below,sloped',2:'below,sloped'}
    if dR>219:
        seitenPos={0:'above,sloped',1:'below,sloped',2:'above,sloped'}
    if dR>269:
        seitenPos={0:'below,sloped',1:'below,sloped',2:'above,sloped'}
#l1 ist immer die Seite links von dem Winkel, gedreht gegen Uhrzeigersinn.
#Beschriftungen
#Dreieck zeichnen
    sL=['']*len(label)
    for i,l in enumerate(label):
        sL[i]=f'node[{seitenPos[i]}]{{{l}}}'
    pktLabel1=f"[label={dR-180}:{punkte[0]}]" if len(punkte[0])>0 else ""
    pktLabel2=f"[label={dR}:{punkte[1]}]" if len(punkte[1])>0 else ""
    pktLabel3=f"[label={90+dR}:{punkte[2]}]" if len(punkte[2])>0 else ""
    tikzcommand=[f'\\coordinate{pktLabel1} (E) at ({ur[0]},{ur[1]});']
    tikzcommand.append(f'\\coordinate{pktLabel2} (F) at ($(E)+({dR}:{k[0]})$);')
    tikzcommand.append(f'\\coordinate{pktLabel3} (G) at ($(F)+({dR+winkel}:{k[1]})$);')
    tikzcommand.append(f'\\draw (E) coordinate -- {sL[0]} (F) -- {sL[1]} (G)   --{sL[2]} (E);')
    if mitBogen:    
        tikzcommand.append(F'\\pic [draw,thick, -,angle radius=0.6cm, "•"] {{angle = G--F--E}};')        
    return erzeugeTikzUmrandung(tikzcommand)

    
def dreieckSinusSatz(abc=[4,3,6],labels={'a':['a','red'],'b':['b','blue'],'c':['c','green']},drehung=45,lsg=False):
    a,b,c=abc
    alpha=math.degrees(math.acos((a**2-b**2-c**2)/(-2*b*c)))
    beta=math.degrees(math.acos((b**2-a**2-c**2)/(-2*a*c)))
    gamma=180-alpha-beta
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    tikzcommand.append(F'\\draw[thick,black,rotate={drehung}] (0,0) coordinate(A)  ++({c},0) coordinate(B)  ++({alpha+gamma}:{a} ) coordinate(C) ;')
    tikzcommand.append(F'\\draw[thick,{labels["c"][1] if lsg else "black"}] (A) -- node[below,sloped]{{{labels["c"][0]}}} (B);')
    tikzcommand.append(F'\\draw[thick,{labels["a"][1] if lsg else "black"}] (B) -- node[below,sloped]{{{labels["a"][0]}}} (C);')
    tikzcommand.append(F'\\draw[thick,{labels["b"][1] if lsg else "black"}] (C) -- node[below,sloped]{{{labels["b"][0]}}} (A);')
    tikzcommand.append(F'\\pic [draw,thick,{labels["a"][1] if lsg else "black"}, -,angle radius=0.6cm, "${abcZuGr[labels["a"][0]]}$"] {{angle = B--A--C}};')
    tikzcommand.append(F'\\pic [draw,thick,{labels["b"][1] if lsg else "black"}, -,angle radius=0.6cm, "${abcZuGr[labels["b"][0]]}$"] {{angle = C--B--A}};')     
    tikzcommand.append(F'\\pic [draw,thick,{labels["c"][1] if lsg else "black"}, -,angle radius=0.6cm, "${abcZuGr[labels["c"][0]]}$"] {{angle = A--C--B}};')     
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand
    
    
    
def dreieckSWScBetaa(A=[4,40,"A","a","$\\alpha$"],B=[3,60,"B","b","$\\beta$"],C=[5,80,"C","c","$\\gamma$"]):
#
    x0=random.randint(0,5)/10
    y0=random.randint(0,5)/10
    sW=random.randint(-45,45)
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    tikzcommand.append(F'\\draw[thick,black] ({x0},{y0}) coordinate(A) -- node[below,sloped]{{{C[3]}}} ++({sW}:{C[0]}) coordinate(B) -- node[above,sloped]{{{A[3]}}} ++({180-B[1]+sW}:{A[0]} ) coordinate(C) -- node[above,sloped]{{{B[3]}}} cycle;')
    tikzcommand.append(F'\\pic [draw,thick, -,angle radius=0.7cm, "{A[4]}"] {{angle = B--A--C}};')
    tikzcommand.append(F'\\pic [angle radius=0.3cm, "{A[2]}"] {{angle = C--A--B}};')
    tikzcommand.append(F'\\pic [draw,thick, -,angle radius=0.7cm, "{B[4]}"] {{angle = C--B--A}};')
    tikzcommand.append(F'\\pic [angle radius=0.3cm, "{B[2]}"] {{angle = A--B--C}};')
    tikzcommand.append(F'\\pic [draw,thick, -,angle radius=0.7cm, "{C[4]}"] {{angle = A--C--B}};')
    tikzcommand.append(F'\\pic [angle radius=0.3cm, "{C[2]}"] {{angle = B--C--A}};')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand


def planfigurRWSinusKosinus(urspr=[0,0],rW='B',wBez=[],ges='',markieren=[],laengenBez=[],coordinaten=[],winkelWerte=['','',''],mitTikzUmrandung=True):
    tikzcommand=[]
    wBez=random.sample(list(abcZuGr.keys()),3) if len(wBez)==0 else wBez
    gesNr=wBez.index(ges) if ges.lower() in wBez else -1
    if mitTikzUmrandung:
        tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
        tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    seitenPkte={wBez[0]:'(B) -- (C)',wBez[1]:'(A) -- (C)',wBez[2]:'(A) -- (B)'}
    coords={wBez[0].upper():['(0,0)','(4,0)','(0,3)','•',f'${abcZuGr[wBez[1]]}$',f'${abcZuGr[wBez[2]]}$','(B) -- (C)']}
    coords[wBez[1].upper()]=['(0,0)','(4,0)','(4,3)',f'${abcZuGr[wBez[0]]}$','•',f'${abcZuGr[wBez[2]]}$','(A) -- (C)']
    coords[wBez[2].upper()]=['(0,0)','(5,0)',f'({math.degrees(math.asin(4/5))}:3)',f'${abcZuGr[wBez[0]]}$',f'${abcZuGr[wBez[1]]}$','•','(B) -- (A)']
    if len(coordinaten)>0:
        for bez in wBez:
            for i,c in enumerate(coordinaten):
                coords[bez.upper()][i]=c
    tikzcommand.append(f'\\draw[thick,black] {coords[rW][0]} coordinate(A) -- node[below,sloped]{{{wBez[2] if len(laengenBez)==0 else laengenBez[2]}}} {coords[rW][1]} coordinate(B) -- node[above,sloped]{{{wBez[0] if len(laengenBez)==0 else laengenBez[0]}}} {coords[rW][2]} coordinate(C) -- node[above,sloped]{{{wBez[1] if len(laengenBez)==0 else laengenBez[1]}}} cycle; ')
    tikzcommand.append(f'\\node[left] at (A)  {{{wBez[0].upper()}}};')
    tikzcommand.append(f'\\node[right] at (B) {{{wBez[1].upper()}}};')
    tikzcommand.append(f'\\node[above] at (C) {{{wBez[2].upper()}}};')
    tikzcommand.append(F'\\pic [draw,thick, {"red" if gesNr==0 else "black"},angle radius=0.7cm, "{winkelWerte[0] if len(winkelWerte[0])>0 else coords[rW][3]}"] {{angle = B--A--C}};')
    tikzcommand.append(F'\\pic [draw,thick, {"red" if gesNr==1 else "black"},angle radius=0.7cm, "{winkelWerte[1] if len(winkelWerte[1])>0 else coords[rW][4]}"] {{angle = C--B--A}};')
    tikzcommand.append(F'\\pic [draw,thick, {"red" if gesNr==2 else "black"},angle radius=0.7cm, "{winkelWerte[2] if len(winkelWerte[2])>0 else coords[rW][5]}"] {{angle = A--C--B}};')
    for m in markieren:
        tikzcommand.append(F'\\draw[thick,red] {seitenPkte[m]};')
    if mitTikzUmrandung:
        tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand



def dreieckWSWKonstr(werte=[40,5,80],seite='b',mitLsg=True,zeichnePlanfigur=True,mitHilfe=False):
    markieren={'a':['beta','a','gamma'],'b':['gamma','b','alpha'],'c':['alpha','c','beta']}
    urspr={'c':[-3,0],'a':[-6,0],'b':[-4,-3]}
    dR=0#random.randint(-10,10)
    sW={'c':0,'a':90+dR,'b':180+90+dR}
    pktBez={'a':['B','C','A'],'b':['C','A','B'],'c':['A','B','C']}
    seitenBez={'a':['a','b','c'],'b':['b','c','a'],'c':['c','a','b']}
    labelPos={'A':225,'B':315,'C':90}
    seitenPos={'a':'above,sloped','b':'above,sloped','c':'below,sloped'}
#w1 ist immer der Winkel links auf der Strecke, gedreht gegen Uhrzeigersinn.
    w1=sW[seite]+werte[0]
    w2=sW[seite]+180-werte[2]
    l=werte[1]
#Beschriftungen
    pktLabel1=f"[label={labelPos[pktBez[seite][0]]}:{pktBez[seite][0]}]" if mitLsg and pktBez[seite][0] in markieren[seite] else ""
    pktLabel2=f"[label={labelPos[pktBez[seite][1]]}:{pktBez[seite][1]}]" if mitLsg and pktBez[seite][1] in markieren[seite] else ""
    pktLabel3=f"[label={labelPos[pktBez[seite][2]]}:{pktBez[seite][2]}]" if mitLsg and pktBez[seite][2] in markieren[seite] else ""
    seitenLabel1=(f" -- " if (mitLsg or mitHilfe)  else "") + (f"node[{seitenPos[seitenBez[seite][0]]}] {{{seitenBez[seite][0]}}}" if (mitLsg or mitHilfe) and seitenBez[seite][0] in markieren[seite] else "")
    seitenLabel2=(f" -- " if mitLsg else "") + (f"node[{seitenPos[seitenBez[seite][1]]}] {{{seitenBez[seite][1]}}}" if mitLsg and seitenBez[seite][1] in markieren[seite] else "")
    seitenLabel3=(f" -- " if mitLsg else "") + (f"node[{seitenPos[seitenBez[seite][2]]}] {{{seitenBez[seite][2]}}}" if mitLsg and seitenBez[seite][2] in markieren[seite] else "")+("  cycle" if mitLsg else "")
#Dreieck zeichnen
    tikzcommand=[f'\\coordinate{pktLabel1} (E) at (0,0);']
    tikzcommand.append(f'\\node (E2) at ($(E)+({w1}:1)$) {{}};')
    tikzcommand.append(f'\\coordinate{pktLabel2} (F) at ({sW[seite]}:{l});')
    tikzcommand.append(f'\\node (F2) at ($(F)+({w2}:1)$) {{}};')
    tikzcommand.append(f'\\coordinate{pktLabel3} (G) at (intersection of E--E2 and F--F2);')
    tikzcommand.append(f'\\draw (E) coordinate ({pktBez[seite][0]}) {seitenLabel1} (F) coordinate ({pktBez[seite][1]})  {seitenLabel2} (G) coordinate ({pktBez[seite][2]})  {seitenLabel3};')    
    if mitLsg:
        tikzcommand.append(dreieckMarkieren(seiteWinkel=markieren[seite][0],farbe='black'))
        tikzcommand.append(dreieckMarkieren(seiteWinkel=markieren[seite][2],farbe='black'))
    if mitLsg or zeichnePlanfigur:
        tikzcommand=tikzcommand+planfigur(urspr=urspr[seite],markieren=markieren[seite] if mitLsg else [])
    else:
        tikzcommand.append(f'\\node (U) at  ({urspr[seite][0]},{urspr[seite][1]}) {{}};')
    return erzeugeTikzUmrandung(tikzcommand)

def dreieckSWSKonstr(werte=[4,60,5],winkel='gamma',mitLsg=True,zeichnePlanfigur=True,mitHilfe=False):
    markieren={'alpha':['b','alpha','c'],'beta':['c','beta','a'],'gamma':['a','gamma','b']}
    urspr={'alpha':[-3,0],'beta':[-3-werte[0],0],'gamma':[-5,-3]}
    dR=0 #random.randint(-10,10)
    sW={'alpha':werte[1],'beta':180,'gamma':270+dR}
    pktBez={'alpha':['A','C','B'],'beta':['B','A','C'],'gamma':['C','B','A']}
    seitenBez={'alpha':['b','a','c'],'beta':['c','b','a'],'gamma':['a','c','b']}
    labelPos={'A':225,'B':315,'C':90}
    seitenPos={'a':'above,sloped','b':'above,sloped','c':'below,sloped'}
#l1 ist immer die Seite links von dem Winkel, gedreht gegen Uhrzeigersinn.
    l1=werte[0]
    l2=werte[2]
#Beschriftungen
    pktLabel1=f"[label={labelPos[pktBez[winkel][0]]}:{pktBez[winkel][0]}]" if mitLsg and pktBez[winkel][0] in markieren[winkel] else ""
    pktLabel2=f"[label={labelPos[pktBez[winkel][1]]}:{pktBez[winkel][1]}]" if mitLsg and pktBez[winkel][1] in markieren[winkel] else ""
    pktLabel3=f"[label={labelPos[pktBez[winkel][2]]}:{pktBez[winkel][2]}]" if mitLsg and pktBez[winkel][2] in markieren[winkel] else ""
    seitenLabel1=(f" -- " if mitLsg or (mitHilfe and not winkel=='alpha') else "") + (f"node[{seitenPos[seitenBez[winkel][0]]}] {{{seitenBez[winkel][0]}}}" if (mitLsg or (mitHilfe and not winkel=='alpha')) and seitenBez[winkel][0] in markieren[winkel] else "")
    seitenLabel2=(f" -- " if mitLsg else "") + (f"node[{seitenPos[seitenBez[winkel][1]]}] {{{seitenBez[winkel][1]}}}" if mitLsg and seitenBez[winkel][1] in markieren[winkel] else "")
    seitenLabel3=(f" -- " if mitLsg  or (mitHilfe and winkel=='alpha') else "") + (f"node[{seitenPos[seitenBez[winkel][2]]}] {{{seitenBez[winkel][2]}}}" if (mitLsg or (mitHilfe and winkel=='alpha'))  and seitenBez[winkel][2] in markieren[winkel] else "")
#Dreieck zeichnen
    tikzcommand=[f'\\coordinate{pktLabel1} (E) at (0,0);']
    tikzcommand.append(f'\\coordinate{pktLabel2} (F) at ({sW[winkel]}:{l1});')
    tikzcommand.append(f'\\coordinate{pktLabel3} (G) at ({sW[winkel]-werte[1]}:{l2});')
    tikzcommand.append(f'\\draw (E) coordinate ({pktBez[winkel][0]})  {seitenLabel1} (F) coordinate ({pktBez[winkel][1]})  {seitenLabel2} (G) coordinate ({pktBez[winkel][2]})  {seitenLabel3} (E);')
    if mitLsg:
        tikzcommand.append(dreieckMarkieren(seiteWinkel=markieren[winkel][1],farbe='black'))
    if mitLsg or zeichnePlanfigur:
        tikzcommand=tikzcommand+planfigur(urspr=urspr[winkel],markieren=markieren[winkel] if mitLsg else [])
    else:
        tikzcommand.append(f'\\node (U) at  ({urspr[winkel][0]},{urspr[winkel][1]}) {{}};')
    return erzeugeTikzUmrandung(tikzcommand)

def dreieckSSSKonstr(werte=[4,5,6],mitLsg=True,zeichnePlanfigur=True,mitHilfe=False):
    a,b,c=werte
    markieren=['a','b','c']
    if abs((a**2-b**2-c**2)/(-2*b*c))>1:
        alpha=-1
    else:
        alpha=math.acos((a**2-b**2-c**2)/(-2*b*c))*180/math.pi
    winkelStartUmA=-10
    winkelEndUmA=190 if alpha > 90 or alpha <0 else 100
    winkelStartUmB=-10 if b>c and alpha<45 else 80
    winkelEndUmB=190
    urspr=[-3,0]
    labelPos={'A':225,'B':315,'C':90}
    seitenPos={'a':'above,sloped','b':'above,sloped','c':'below,sloped'}
#l1 ist immer die Seite links von dem Winkel, gedreht gegen Uhrzeigersinn.
    b=werte[1]
    c=werte[2]
#Beschriftungen
    seitenLabel1=(f"-- node[{seitenPos['c']}] {{{'c'}}}" if mitLsg or mitHilfe else "")
    seitenLabel2=(f"-- node[{seitenPos['a']}] {{{'a'}}}" if mitLsg else "")
    seitenLabel3=(f"-- node[{seitenPos['b']}] {{{'b'}}}" if mitLsg else "")
#Dreieck zeichnen
    tikzcommand=[f'\\coordinate (A) at (0,0);']
    tikzcommand.append(f'\\coordinate (B) at (0:{c});')
    tikzcommand.append(f'\\coordinate (C) at ({alpha}:{b});')
    if alpha>0:
        tikzcommand.append(f'\\draw (A) {seitenLabel1} (B)   {seitenLabel2} (C)  {seitenLabel3} (A);')
    else:
        tikzcommand.append(f'\\draw (A) {seitenLabel1} (B);')
    if mitLsg:
        tikzcommand.append(F'\\draw[thick,red] ($(A)+({winkelStartUmA}:{b})$) arc ({winkelStartUmA}:{winkelEndUmA}:{b} cm);')
        tikzcommand.append(F'\\draw[thick,red] ($(B)+({winkelStartUmB}:{a})$) arc ({winkelStartUmB}:{winkelEndUmB}:{a} cm);')
    if mitLsg or zeichnePlanfigur:
        tikzcommand=tikzcommand+planfigur(urspr=urspr,markieren=markieren if mitLsg else [])
    else:
        tikzcommand.append(f'\\node (U) at  ({urspr[0]},{urspr[1]}) {{}};')
    return erzeugeTikzUmrandung(tikzcommand)
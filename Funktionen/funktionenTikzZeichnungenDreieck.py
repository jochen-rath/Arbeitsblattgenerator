#!/usr/bin/env python
# coding: utf8


#Aufruf:
#       exec(open("Funktionen/funktionenTikzZeichnungen.py").read())
#Diese Skript stellte verschiedene Figuren bereit, die Zeichnungen mit dem Latex-Paket Tikz erzeugen
#       exec(open("Funktionen/funktionen.py").read())


def dreieckSeitenvorgabe(werte,seiten):
#Diese Funktionen zeichnet ein Dreieck bei vorgegebenen Seitenlängen.
#Eingabe:
#              tikzcommand=dreieckSeitenvorgabe(werte,seiten)
#
#mit
#       werte=[a,b,c] die Seitenlängen. c ist die untere Seite, a links und b rechts.#
#       seiten=['a','b','c'] die Beschriftung der Seiten.
    a,b,c=werte
    #Kosinussatz zur Berechnung von Alpha
    alpha=math.acos((a**2-b**2-c**2)/(-2*b*c))
    A=[0,0]
    B=[c,0]
    C=[math.cos(alpha)*a,math.sin(alpha)*a]
    tikzcommand=[]
    tikzcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
    tikzcommand.append('\\noindent\\begin{tikzpicture}[show background grid]')
    tikzcommand.append(F'\\draw[black, very thick] ({A[0]}cm,{A[1]}cm) -- node[below] {{{seiten[2]}}} ({B[0]}cm,{B[1]}cm);')
    tikzcommand.append(F'\\draw[black, very thick] ({B[0]}cm,{B[1]}cm) -- node[right] {{{seiten[0]}}} ({C[0]}cm,{C[1]}cm);')
    tikzcommand.append(F'\\draw[black, very thick] ({C[0]}cm,{C[1]}cm) -- node[left] {{{seiten[1]}}}  ({A[0]}cm,{A[1]}cm);')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand


def bestimmePkteBezWinkelWennRechtWinkBeiAlpha(kx,ky,rotWinkel,bL,pktPos):
    hyp=(kx**2+ky**2)**0.5
    A = [0, 0]
    B = [round(kx * math.sin((math.radians(90 + rotWinkel))), 6),
         round(kx * math.cos((math.radians(90 + rotWinkel))), 6)]
    C = [round(ky * math.sin((math.radians(rotWinkel))), 6), round(ky * math.cos((math.radians(rotWinkel))), 6)]
    bogenStart = [round(bL * math.sin((math.radians(rotWinkel))), 6), round(bL * math.cos(math.radians(rotWinkel)), 6)]
    bogenWinkel = [90 - rotWinkel, -rotWinkel]
    rechtWPunkt = [round(bL / 2 * math.sin((math.radians(45 + rotWinkel))), 6),
                   round(bL / 2 * math.cos(45 + math.radians(rotWinkel)), 6)]
    pktA = [round(bL / 2 * math.sin((math.radians(225 + rotWinkel))), 6),
            round(bL / 2 * math.cos((math.radians(225 + rotWinkel))), 6)]
    distPktB = kx + pktPos / (2 ** 0.5)
    winkelPktB = 90 + math.degrees(math.asin(pktPos / distPktB))
    pktB = [round(distPktB * math.sin((math.radians(winkelPktB + rotWinkel))), 6),
            round(distPktB * math.cos((math.radians(winkelPktB + rotWinkel))), 6)]
    distPktC = ky + pktPos / (2 ** 0.5)
    winkelPktC = math.degrees(math.asin(pktPos / distPktC))
    pktC = [round(distPktC * math.sin((math.radians(winkelPktC + rotWinkel))), 6),
            round(distPktC * math.cos((math.radians(winkelPktC + rotWinkel))), 6)]
    return A,B,C,bogenStart,bogenWinkel,rechtWPunkt,pktA,pktB,pktC


def bestimmePkteBezWinkelWennRechtWinkBeiBetta(kx,ky,rotWinkel,bL,pktPos):
    hyp=(kx**2+ky**2)**0.5
    winkelB = math.degrees(math.asin(kx / hyp))
    A = [round(kx * math.sin((math.radians(90 + rotWinkel))), 6),
         round(kx * math.cos((math.radians(90 + rotWinkel))), 6)]
    B = [round(hyp * math.sin((math.radians(winkelB + rotWinkel))), 6),
         round(hyp * math.cos(math.radians(winkelB + rotWinkel)), 6)]
    C = [round(ky * math.sin((math.radians(rotWinkel))), 6), round(ky * math.cos(math.radians(rotWinkel)), 6)]
    cBS = (kx ** 2 + (ky - bL) ** 2) ** 0.5
    alphaBS = math.degrees(math.asin(kx / cBS))
    bogenStart = [round(cBS * math.sin((math.radians(alphaBS + rotWinkel))), 6),
                  round(cBS * math.cos(math.radians(alphaBS + rotWinkel)), 6)]
    bogenWinkel = [270 - rotWinkel, 180 - rotWinkel]
    cWP = ((ky - bL / 2) ** 2 + (kx - bL / 2) ** 2) ** 0.5
    alphaWP = math.degrees(math.asin((kx - bL / 2) / cWP))
    rechtWPunkt = [round(cWP * math.sin((math.radians(alphaWP + rotWinkel))), 6),
                   round(cWP * math.cos(math.radians(alphaWP + rotWinkel)), 6)]
    distPktA = kx + pktPos / (2 ** 0.5)
    winkelPktA = 90 + math.degrees(math.asin(pktPos / distPktA))
    pktA = [round(distPktA * math.sin((math.radians(winkelPktA + rotWinkel))), 6),
            round(distPktA * math.cos((math.radians(winkelPktA + rotWinkel))), 6)]
    distPktB = hyp + pktPos
    pktB = [round(distPktB * math.sin((math.radians(winkelB + rotWinkel))), 6),
            round(distPktB * math.cos((math.radians(winkelB + rotWinkel))), 6)]
    distPktC = ky + pktPos / (2 ** 0.5)
    winkelPktC = -math.degrees(math.asin(pktPos / distPktC))
    pktC = [round(distPktC * math.sin((math.radians(winkelPktC + rotWinkel))), 6),
            round(distPktC * math.cos((math.radians(winkelPktC + rotWinkel))), 6)]
    return A,B,C,bogenStart,bogenWinkel,rechtWPunkt,pktA,pktB,pktC


def bestimmePkteBezWinkelWennRechtWinkBeiGamma(kx,ky,rotWinkel,bL,pktPos):
    hyp=(kx**2+ky**2)**0.5
    winkelB = math.degrees(math.asin(kx / hyp))
    A = [0, 0]
    B = [round(hyp * math.sin((math.radians(winkelB + rotWinkel))), 6),
         round(hyp * math.cos(math.radians(winkelB + rotWinkel)), 6)]
    C = [round(ky * math.sin((math.radians(rotWinkel))), 6), round(ky * math.cos((math.radians(rotWinkel))), 6)]
    bogenStart = [round((ky - bL) * math.sin((math.radians(rotWinkel))), 6),
                  round((ky - bL) * math.cos((math.radians(rotWinkel))), 6)]
    bogenWinkel = [270 - rotWinkel, 360 - rotWinkel]
    cWP = ((ky - bL / 2) ** 2 + bL / 2 ** 2) ** 0.5
    alphaWP = math.degrees(math.asin((bL / (2 * cWP))))
    rechtWPunkt = [round(cWP * math.sin((math.radians(alphaWP + rotWinkel))), 6),
                   round(cWP * math.cos(math.radians(alphaWP + rotWinkel)), 6)]
    pktA = [round(pktPos * math.sin((math.radians(225 + rotWinkel))), 6),
            round(pktPos * math.cos((math.radians(225 + rotWinkel))), 6)]
    distPktB = hyp + pktPos
    pktB = [round(distPktB * math.sin((math.radians(winkelB + rotWinkel))), 6),
            round(distPktB * math.cos((math.radians(winkelB + rotWinkel))), 6)]
    distPktC = ky + pktPos / (2 ** 0.5)
    winkelPktC = -math.degrees(math.asin(pktPos / distPktC))
    pktC = [round(distPktC * math.sin((math.radians(winkelPktC + rotWinkel))), 6),
            round(distPktC * math.cos((math.radians(winkelPktC + rotWinkel))), 6)]
    return A,B,C,bogenStart,bogenWinkel,rechtWPunkt,pktA,pktB,pktC


def dreieckRechtwinklig(kx=3,ky=2,rotWinkel=90,mitBogen=True,seiten=['a','b','c'],punkte=[],rechtWinkBei='beta',mitUmrandung=True):
#Diese Funktion erzeugt ein rechtwinkliges Dreieck, bei dem gilt, dass die Katheten in x und y Richtung zeigen, bevor das Dreieck um
#den Rotationswinkel rotWinkel gedreht wird.
#Dreiecksbezeichnungen: Seite a liegt zwischen Punkt B und C
#                       Seite b liegt zwischen Punkt A und C
#                       Seite c liegt zwischen Punkt A und B
#
#Input:
#   dreieckRechtwinklig(kx,ky,rotWinkel,mitBogen,seiten,punkte,rechtWinkBei)
#       kx= Kathete in x-Richtung
#       ky= Kathete in y-Richtung
# Beispiel
#    tikzcommand=dreieckRechtwinklig(kx=3,ky=2,rotWinkel=90,mitBogen=True,seiten=['a','b','c'],punkte=[],rechtWinkBei='beta')
#Wenn rechtWinkBei='alpha' ist, dann folgt: a=hyp,b=ky,c=kx
#Wenn rechtWinkBei='beta' ist, dann folgt: a=kx,b=hyp,c=ky
#Wenn rechtWinkBei='gamma' ist, dann folgt: a=kx,b=ky,c=hyp
    seiten=seiten if len(seiten)>2 else ['','','']
    punkte=punkte if len(punkte)>2 else ['','','']
#    punkte=['A','B','C']
#    seiten=['a','b','c']
    seitenPos=['below']*len(seiten)
    tikzcommand=[]
    bL=0.5   #Bogenlaenge
    pktPos=0.25
    if rechtWinkBei.lower()=='alpha':
        A,B,C,bogenStart,bogenWinkel,rechtWPunkt,pktA,pktB,pktC=bestimmePkteBezWinkelWennRechtWinkBeiAlpha(kx,ky,rotWinkel,bL,pktPos)
    elif rechtWinkBei.lower()=='beta':
        A,B,C,bogenStart,bogenWinkel,rechtWPunkt,pktA,pktB,pktC=bestimmePkteBezWinkelWennRechtWinkBeiBetta(kx,ky,rotWinkel,bL,pktPos)
    elif rechtWinkBei.lower()=='gamma':
        A,B,C,bogenStart,bogenWinkel,rechtWPunkt,pktA,pktB,pktC=bestimmePkteBezWinkelWennRechtWinkBeiGamma(kx,ky,rotWinkel,bL,pktPos)
    else:
        return 'Error: Keine Position für rechten Winkel gewählt. Wähle alpha, beta oder gamma.'
    posDistanz=0.5
    seitenPos[0]=seitenPos[0] if abs(B[0]-C[0])>posDistanz else 'left'
    seitenPos[1]=seitenPos[1] if abs(A[0]-C[0])>posDistanz else 'left'
    seitenPos[2]=seitenPos[2] if abs(A[0]-B[0])>posDistanz else 'left'
    tikzcommand=[]
    if mitUmrandung:
        tikzcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
        tikzcommand.append('\\noindent\\begin{tikzpicture}[show background grid]')
    tikzcommand.append('\\draw[black, very thick] ('+str(A[0])+'cm,'+str(A[1])+'cm) -- node['+seitenPos[2]+'] {'+seiten[2]+'} ('+str(B[0])+'cm,'+str(B[1])+'cm);')
    tikzcommand.append('\\draw[black, very thick] ('+str(B[0])+'cm,'+str(B[1])+'cm) -- node['+seitenPos[0]+'] {'+seiten[0]+'} ('+str(C[0])+'cm,'+str(C[1])+'cm);')
    tikzcommand.append('\\draw[black, very thick] ('+str(C[0])+'cm,'+str(C[1])+'cm) -- node['+seitenPos[1]+'] {'+seiten[1]+'} ('+str(A[0])+'cm,'+str(A[1])+'cm);')
    tikzcommand.append('\\node at ('+str(pktA[0])+'cm,'+str(pktA[1])+'cm) {'+punkte[0]+'};')
    tikzcommand.append('\\node at ('+str(pktB[0])+'cm,'+str(pktB[1])+'cm) {'+punkte[1]+'};')
    tikzcommand.append('\\node at ('+str(pktC[0])+'cm,'+str(pktC[1])+'cm) {'+punkte[2]+'};')

    if mitBogen:
#        for bogenStart,bogenWinkel,bezPos,bezPkt in winkelBezeichnungen
        tikzcommand.append('\\draw[black] (' + str(bogenStart[0]) + 'cm,' + str(bogenStart[1]) + 'cm) arc ('+str(bogenWinkel[0])+':'+str(bogenWinkel[1])+':'+str(bL)+');')
        tikzcommand.append('\\node[circle,draw=black, fill=black, inner sep=0pt,minimum size=2pt] at (' + str(rechtWPunkt[0]) + 'cm,' + str(rechtWPunkt[1]) + 'cm) {};')
#        tikzcommand.append('\\node at (' + str(bezPos[0]) + 'cm,' + str(bezPos[1]) + 'cm) {'+bezPkt+'};')
    if mitUmrandung:
        tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand

def tabelleEinheitenUmrechnen():
    einheiten=['mm','cm','dm','m','km']
    faktor=['10','10','10','10','1000']
    tikzcommand=['\\begin{tikzpicture}[baseline=0]']
    tikzcommand.append('node[draw,circle] (1) at (0,0cm) {mm};')
    tikzcommand.append('node[draw,circle] (2) at (0,1.5cm) {cm};')
    tikzcommand.append('node[draw,circle] (3) at (0,3cm) {dm};')
    tikzcommand.append('node[draw,circle] (4) at (0,4.5cm) {m};')
    tikzcommand.append('node[draw,circle] (7) at (0,9cm) {km};')
    tikzcommand.append('draw [->] (2) to [out=190,in=170] node[left] {$\cdot 10$}  (1) ;')
    tikzcommand.append('draw [->] (3) to [out=190,in=170] node[left] {$\cdot 10$}  (2);')
    tikzcommand.append('draw [->] (4) to [out=190,in=170] node[left] {$\cdot 10$}  (3);')
    tikzcommand.append('draw [->] (7) to [out=190,in=170] node[left] {$\cdot 1000$}  (4);')
    tikzcommand.append('draw [->] (1) to [out=10,in=350] node[right] {$: 10$} (2);')
    tikzcommand.append('draw [->] (2) to [out=10,in=350] node[right] {$: 10$} (3);')
    tikzcommand.append('draw [->] (3) to [out=10,in=350] node[right] {$: 10$} (4);')
    tikzcommand.append('draw [->] (4) to [out=10,in=350] node[right] {$: 1000$} (7);')
    tikzcommand.append('node[draw,circle] (11) at (5,0cm) {mm$^2$};')
    tikzcommand.append('node[draw,circle] (12) at (5,1.5cm) {cm$^2$};')
    tikzcommand.append('node[draw,circle] (13) at (5,3cm) {dm$^2$};')
    tikzcommand.append('node[draw,circle] (14) at (5,4.5cm) {m$^2$};')
    tikzcommand.append('node[draw,circle] (15) at (5,6cm) {a};')
    tikzcommand.append('node[draw,circle] (16) at (5,7.5cm) {ha};')
    tikzcommand.append('node[draw,circle] (17) at (5,9cm) {km$^2$};')
    tikzcommand.append('draw [->] (12) to [out=190,in=170] node[left] {$\cdot 100$}  (11) ;')
    tikzcommand.append('draw [->] (13) to [out=190,in=170] node[left] {$\cdot 100$}  (12);')
    tikzcommand.append('draw [->] (14) to [out=190,in=170] node[left] {$\cdot 100$}  (13);')
    tikzcommand.append('draw [->] (15) to [out=190,in=170] node[left] {$\cdot 100$}  (14);')
    tikzcommand.append('draw [->] (16) to [out=190,in=170] node[left] {$\cdot 100$}  (15);')
    tikzcommand.append('draw [->] (17) to [out=190,in=170] node[left] {$\cdot 100$}  (16);')
    tikzcommand.append('draw [->] (11) to [out=10,in=350] node[right] {$: 100$} (12);')
    tikzcommand.append('draw [->] (12) to [out=10,in=350] node[right] {$: 100$} (13);')
    tikzcommand.append('draw [->] (13) to [out=10,in=350] node[right] {$: 100$} (14);')
    tikzcommand.append('draw [->] (14) to [out=10,in=350] node[right] {$: 100$} (15);')
    tikzcommand.append('draw [->] (15) to [out=10,in=350] node[right] {$: 100$} (16);')
    tikzcommand.append('draw [->] (16) to [out=10,in=350] node[right] {$: 100$} (17);')
    tikzcommand.append('end{tikzpicture}')

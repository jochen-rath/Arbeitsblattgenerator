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

    
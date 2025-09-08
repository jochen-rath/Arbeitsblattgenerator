#!/usr/bin/env python
# coding: utf8


#Aufruf:
#       exec(open("Funktionen/funktionenTikzZeichnungen.py").read())
#Diese Skript stellte verschiedene Figuren bereit, die Zeichnungen mit dem Latex-Paket Tikz erzeugen
#       exec(open("Funktionen/funktionen.py").read())


def dreieckRechtw(k=[5,6],label=['5 dm','6 dm',''],punkte=['','',''],mitBogen=True,dR=-1):
    dR=dR if dR>0 else random.randint(0,360)
    ur=[random.randint(0,10)/10,random.randint(0,10)/10]
    hyp=(k[0]**2+k[1]**2)**0.5
    winkel=90
    seitenPos={0:'below,sloped',1:'above,sloped',2:'above,sloped'}
    if dR>90:
        seitenPos={0:'above,sloped',1:'above,sloped',2:'above,sloped'}
    if dR>179:
        seitenPos={0:'above,sloped',1:'below,sloped',2:'above,sloped'}
    if dR>169:
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

    
#!/usr/bin/env python
# coding: utf8

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())

def erzeugeSchiffeVersenken(anzSpalten=[2,2]):
    schiffe=[[1,0],[2,4],[3,3],[4,2],[5,1]]    #--> [Schiffgröße,Anzahl]
    grenzen=[0,10,5,1]
#    templateContent,templateStyles=entpackeOdtDatei(template)
    schiffKoord=erzeugeListeMitSchiffskoordinaten(schiffe,grenzen)
    groesse='{!}{9 cm}' if anzSpalten[0] == 1 else '{6 cm}{!}'
    afg=[f'\\resizebox{groesse}{{']+zeichneSchiffe(schiffKoord=schiffKoord)+['}']
    groesse='{!}{9 cm}' if anzSpalten[1] == 1 else '{6 cm}{!}'
    lsg=[f'\\resizebox{groesse}{{']+zeichneSchiffe(schiffKoord=[])+['}']
    return [afg,lsg,[]]

def erzeugeListeMitSchiffskoordinaten(schiffe,grenzen):
    #Koordinaten erzeugen
    nichtErzeugt=True
    while nichtErzeugt:
        nichtErzeugt=False
        schiffKoord=[]
        z=0
        for schiff in schiffe:
            for anzahlSchiffe in range(schiff[1]):
                falschePosition=True
                while falschePosition and z<100:
                    z=z+1
                    falschePosition=False
                    richtung=random.getrandbits(1)   #0 --> x Richtung, 1 --> y Richtung
                    koord=[list(np.random.randint(grenzen[0],grenzen[1],2))]
                    for k in [x for sublist in schiffKoord for x in sublist]:
                        dist=np.sqrt((koord[0][0]-k[0])**2+(koord[0][1]-k[1])**2)
                        if dist<=1.1:
                            falschePosition=True
                    for x in range(schiff[0]-1):
                        koord2=list(koord[0])
                        koord2[richtung]=koord2[richtung]+x+1
                        for k in [x for sublist in schiffKoord for x in sublist]:
                            dist=np.sqrt((koord2[0]-k[0])**2+(koord2[1]-k[1])**2)
    #                        print("Schiff=[{5},{6}]: np.sqrt(({0}-{1})**2+({2}-{3})**2)={4}".format(koord2[0],k[0],koord2[1],k[1],dist,schiff[0],schiff[1]))
                            if dist<=1.1:
                                falschePosition=True
                        if max(koord2)>grenzen[1]:
                            falschePosition=True
                        koord.append(koord2)
                schiffKoord.append(koord)
        if z>=100:
            nichtErzeugt=True
            print(z)
    return schiffKoord

def zeichneSchiffe(schiffKoord=[[[9, 6], [10, 6]], [[2, 3], [3, 3]]]):
    tikzcommand=[]
    tikzcommand.append("\\begin{tikzpicture}")
    tikzcommand.append("\\begin{axis}[    axis lines = middle, scale only axis=true, at={(0cm,0cm)},")
    tikzcommand.append("    grid=major,clip=false,")
    tikzcommand.append("    major grid style={line width=1pt,draw=gray},")
    tikzcommand.append("    axis lines=middle,")
    tikzcommand.append("    width=10.5 cm, xmin = 0.0, xmax = 10.5,xtick distance = 1.0,")
    tikzcommand.append("    height=10.5cm, ymin = 0.0, ymax = 10.5, ytick distance = 1.0,")
    tikzcommand.append("    xlabel={X},x label style={at={(current axis.right of origin)},anchor=west},")
    tikzcommand.append("    ylabel={Y},y label style={at={(current axis.above origin)},anchor=west}")
    tikzcommand.append("]")
    for schiffe in schiffKoord:
        for x,y in schiffe:
            tikzcommand.append(f'    \\node[circle,draw=black, fill=black] at (axis cs:{x},{y}) {{}};')
    tikzcommand.append("\\end{axis}")
    tikzcommand.append("\\end{tikzpicture}")
    return tikzcommand

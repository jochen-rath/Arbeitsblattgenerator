#!/usr/bin/env python
# coding: utf8

#Inhalt

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())

def saeulenKreisStreifenDiagrammeZeichnen(werte=[['VW','Mercedes','Audi','BMW','Honda',],[250,200,180,170,100]],titel='Autos pro Stunde',typ='LSG',streifen=False):
    zuordnen=True if (typ=='zuordnen') else False
    zeichnenEinfarben=True if (typ=='ZeichnenUndEinfaerben') else False
    zeichnen=True if (typ=='Zeichnen') else False
    zeichnenUndBerechnen=True if (typ=='ZeichnenUndBerechnen') else False
    alles=True  if (typ=='alles') else False
    farben=tikzFarben[1:]
    R=3
    pWerte=[x/sum(werte[1])*100 for x in werte[1]]
    if not zeichnenUndBerechnen:
        werte.append([F'{strNW(round(x+0.0000000001),True)} \%' for x in pWerte])
    else:
        werte.append([' ' for x in pWerte])
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    dia,hoehe=saeulenDiagrammTikzVorgBreiteHoehe(werte=werte,yAchse=[0,max(werte[1]),20],ylabel=titel,urspr=[0,0],mitUmrandung=False,gibHoeheZurueck=True,farben=farben,typ=typ)
    if not alles:
        tikzcommand=tikzcommand+dia
    if streifen:
        hoehe=hoehe+0.5
    tikzcommand=tikzcommand+tikzTabelle(tabelle=werte,dim=[2.0,0.5],newCBuchst='X',tabellenPos=[0,hoehe+3],mitUmrandung=False)
    if streifen:
        streifenUrsp=[0,hoehe]
        streifenL=10
        if not alles:
            tikzcommand.append(F'\\draw[draw=black] ({streifenUrsp[0]},{streifenUrsp[1]}) rectangle ++(10,1);')
        l = 0
        if not (zeichnen or zeichnenUndBerechnen or alles):
            for i in range(len(pWerte)):
                p = pWerte[i]
                if zeichnenEinfarben:
                    tikzcommand.append(F'\\draw[thick] ({l},{streifenUrsp[1]}) rectangle ++({p/100*10},1);')
                else:
                    tikzcommand.append( F'\\draw[thick,pattern=north west lines, pattern color={farben[i]}] ({l},{streifenUrsp[1]}) rectangle ++({p/100*10},1);')
                if not (zuordnen or zeichnenEinfarben):
                    tikzcommand.append( F'\\node at ({l+p/100*10/2},{streifenUrsp[1] +0.5}) {{\\textbf{{ {werte[0][i]} }} }};')
                l=l+p/100*10
    else:
        kreisUrsp=[10,hoehe-R]
        if not alles:
            tikzcommand.append(F'\\draw ({kreisUrsp[0]},{kreisUrsp[1]}) circle ({R} cm);')
            tikzcommand.append(F'\\draw[fill=black] ({kreisUrsp[0]},{kreisUrsp[1]}) circle (0.05 cm);')
        w=0
        if not (zeichnen or zeichnenUndBerechnen or alles):
            for i in range(len(pWerte)):
                p=pWerte[i]
                if zeichnenEinfarben:
                    tikzcommand.append(F'\\draw[thick] ({kreisUrsp[0]},{kreisUrsp[1]}) -- +({w}:{R}) arc ({w}:{w+p/100*360}:{R}) -- ({kreisUrsp[0]},{kreisUrsp[1]});')
                else:
                    tikzcommand.append(F'\\draw[thick,pattern=north west lines, pattern color={farben[i]}] ({kreisUrsp[0]},{kreisUrsp[1]}) -- +({w}:{R}) arc ({w}:{w+p/100*360}:{R}) -- ({kreisUrsp[0]},{kreisUrsp[1]});')
                if not (zuordnen or zeichnenEinfarben):
                    tikzcommand.append(F'\\node[rotate={w+p/100*360/2}] at ($({kreisUrsp[0]},{kreisUrsp[1]})+({w+p/100*360/2}:{R/2})$) {{\\textbf{{ {werte[0][i]} }} }};')
                w=w+p/100*360
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand

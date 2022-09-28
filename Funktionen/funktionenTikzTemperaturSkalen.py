#!/usr/bin/env python
# coding: utf8


#Aufruf:
#       exec(open("Funktionen/funktionenTikzTemperaturSkalen.py").read())
#Diese Skript stellte verschiedene Figuren bereit, die Zeichnungen mit dem Latex-Paket Tikz erzeugen
#       exec(open("Funktionen/funktionen.py").read())



def temperaturSkalaSiedepunkt(R=0.25,H=13,NP=1,SW=1,T=28,ursprung=[0,0],mitLsg=False,mitUmrandung=True,ohneStuetzpkte=True,mitHintergrund=True):
    SP=NP+10*SW
    tikzcommand=[]
    if SP>H:
        print("Siedepunkt ist Hoeher als Thermometer")
        return tikzcommand
    siedetemp='' if (ohneStuetzpkte and not mitLsg) else '100 $^\\circ$C'
    schmelztemp='' if (ohneStuetzpkte and not mitLsg) else '0 $^\\circ$C'
    tikzcommand.append('\\renewcommand\\R{'+str(R)+'}   ')
    tikzcommand.append('\\renewcommand\\Hoehe{'+str(H)+'}')
    tikzcommand.append('\\renewcommand\\NP{'+str(NP)+'}')
    tikzcommand.append('\\renewcommand\\SP{'+str(SP)+'}')
    tikzcommand.append('\\renewcommand\\SW{'+str(SW)+'}')
    tikzcommand.append('\\renewcommand\\NPplusSW{'+str(NP+SW)+'}')
    tikzcommand.append('\\renewcommand\\NPplusSWplusSW{'+str(NP+2*SW)+'}')
    tikzcommand.append('\\renewcommand\\SPminusSW{'+str(SP-SW)+'}')
    tikzcommand.append('\\renewcommand\\TempHoehe{'+str(T/10*SW+NP)+'}')
    if mitUmrandung:
        if mitHintergrund:
            tikzcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
            tikzcommand.append('\\noindent\\begin{tikzpicture}[show background grid]')
        else:
            tikzcommand.append('\\noindent\\begin{tikzpicture}[]')
    tikzcommand.append('\\draw[black] ('+str(ursprung[0])+',0cm) -- ('+str(ursprung[0])+',\\Hoehe+'+str(ursprung[1])+'); ')
    tikzcommand.append('\\draw[black] (2*\\R+'+str(ursprung[0])+',0+'+str(ursprung[1])+') -- (2*\\R+'+str(ursprung[0])+',\\Hoehe+'+str(ursprung[1])+'); ')
    tikzcommand.append('\\draw[black] (\\R*0.2+'+str(ursprung[0])+',\\NP+'+str(ursprung[1])+') -- (1.8*\\R+'+str(ursprung[0])+',\\NP+'+str(ursprung[1])+'); ')
    tikzcommand.append(F'\\node[right] at (2.2*\\R+{str(ursprung[0])},\\NP+{str(ursprung[1])}) {{{schmelztemp}}};')
    tikzcommand.append('\\draw[black] (\\R*0.2+'+str(ursprung[0])+',\\SP+'+str(ursprung[1])+') -- (1.8*\\R+'+str(ursprung[0])+',\\SP+'+str(ursprung[1])+'); ')
    tikzcommand.append(F'\\node[right] at (2.2*\\R+{str(ursprung[0])},\\SP+{str(ursprung[1])}) {{{siedetemp}}};')
    tikzcommand.append('\\draw ('+str(ursprung[0])+',0+'+str(ursprung[1])+') arc (180:360:\\R) ;')
    tikzcommand.append('\\draw ('+str(ursprung[0])+',\\Hoehe+'+str(ursprung[1])+') arc (180:0:\\R) ;')
    tikzcommand.append('\\draw[red,thick] (\\R+'+str(ursprung[0])+',-\\R+'+str(ursprung[1])+') -- (\\R+'+str(ursprung[0])+',\\TempHoehe+'+str(ursprung[1])+'); ')
    if mitLsg:
        tikzcommand.append('\\foreach \\schritt [count=\\xi] in {\\NPplusSW,\\NPplusSWplusSW,...,\\SPminusSW}')
        tikzcommand.append('{')
        tikzcommand.append(' \\draw[black] (\\R*0.2+'+str(ursprung[0])+',\\schritt+'+str(ursprung[1])+') -- (1.8*\\R+'+str(ursprung[0])+',\\schritt+'+str(ursprung[1])+');')
        tikzcommand.append(' \\node[right] at (2.2*\\R+'+str(ursprung[0])+',\\schritt+'+str(ursprung[1])+') {  \\pgfmathparse{10*(\\xi)}% Evaluate the expression')
        tikzcommand.append('   \\pgfmathprintnumber[    % Print the result')
        tikzcommand.append('       fixed,')
        tikzcommand.append('       fixed zerofill,')
        tikzcommand.append('       precision=0')
        tikzcommand.append('   ]{\\pgfmathresult} $^\\circ$C')
        tikzcommand.append('  };%')
        tikzcommand.append('  }')
        tikzcommand.append('\\node[below] at (\\R+'+str(ursprung[0])+',-\\R+'+str(ursprung[1])+') {T='+str(T)+' $^\\circ$C};')
    if mitUmrandung:
        tikzcommand.append('\end{tikzpicture}')
    return tikzcommand


def temperaturSkalaRationaleZahlen(T=5,multi=1,verschiebung=5,R=0.25,H=13,NP=5,SW=1.0,ursprung=[0,0],mitLsg=False,mitUmrandung=True,ohneStuetzpkte=True,mitHintergrund=True):
    SP=NP+10*SW
    tikzcommand=[]
    if mitUmrandung:
        if mitHintergrund:
            tikzcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
            tikzcommand.append('\\noindent\\begin{tikzpicture}[show background grid]')
        else:
            tikzcommand.append('\\noindent\\begin{tikzpicture}[]')
    tikzcommand.append(F'\\draw[black] ({ursprung[0]},0cm) -- ({ursprung[0]},{H+ursprung[1]}); ')
    tikzcommand.append(F'\\draw[black] ({2*R+ursprung[0]},0cm) -- ({2*R+ursprung[0]},{H+ursprung[1]}); ')
    tikzcommand.append('\\draw ('+str(ursprung[0])+',0+'+str(ursprung[1])+') arc (180:360:\\R) ;')
    tikzcommand.append('\\draw ('+str(ursprung[0])+',\\Hoehe+'+str(ursprung[1])+') arc (180:0:\\R) ;')
    tikzcommand.append(F'\\draw[red,thick] ({R+ursprung[0]},{-R+ursprung[1]}) -- ({R+ursprung[0]},{T++ursprung[1]}); ')
    for temp in range(10):
        tikzcommand.append(F' \\draw[black] ({R*0.2+ursprung[0]},{temp+ursprung[1]}) -- ({1.8*R+ursprung[0]}),{temp+ursprung[1]});')
        tikzcommand.append(F' \\node[right] at ({R*2.2+ursprung[0]},{schritt+ursprung[1]}) {{{4}$^\\circ$C}};')
    if mitLsg:
        tikzcommand.append('\\node[below] at (\\R+'+str(ursprung[0])+',-\\R+'+str(ursprung[1])+') {T='+str(T)+' $^\\circ$C};')
    if mitUmrandung:
        tikzcommand.append('\end{tikzpicture}')
    return tikzcommand

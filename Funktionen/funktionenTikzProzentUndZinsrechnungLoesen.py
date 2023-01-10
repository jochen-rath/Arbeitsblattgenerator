#!/usr/bin/env python
# coding: utf8

#Diese Datei enthält verschiedene Funktionen, zur Erzeugung von Aufgaben zur Prozentrechnung

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())


    

def dreiSatz(links=['50','1','100'],rechts=['50','$\ $','$\ $'],title=['\%','\euro{}'],startPos=[0,0],tikzUmrandung=True,ohneKlammernRechts=False,ohneKlammernLinks=False,breit=False):
#Diese Funktion erzeugt eine Tikz-Zeichnung zum Dreisatz.
#Aufruf: 
#     tikzcommand=dreiSatz(links=['50','1','100'],rechts=['50','$\ $','$\ $'],title=['\%','\euro{}'],startPos=[0,0])
    if tikzUmrandung:
        tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
        tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    else:
        tikzcommand=['']
    breite=2.5 if breit else 1.5
    tikzcommand.append('\\draw[black] ('+str(startPos[0])+'cm,'+str(startPos[1])+'cm) -- ('+str(startPos[0])+'cm,'+str(startPos[1]-3)+'cm); ')
    tikzcommand.append(F'\\draw[black] ({startPos[0]-breite} cm,{startPos[1]-0.5}cm) -- ({startPos[0]+breite}cm,{startPos[1]-0.5}cm); ')
    if breit:
        tikzcommand.append(F'\\node[left] at ({startPos[0]} cm,{startPos[1]-0.25}cm) {{{title[0]}}};')
        tikzcommand.append(F'\\node[right] at ({startPos[0]} cm,{startPos[1]-0.255}cm) {{{title[1]}}};')
    else:
        tikzcommand.append('\\node[below] at ('+str(startPos[0]-0.75)+' cm,'+str(startPos[1])+'cm) {'+title[0]+'};')
        tikzcommand.append('\\node[below] at  ('+str(startPos[0]+0.75)+' cm,'+str(startPos[1])+'cm) {'+title[1]+'};')
    tikzcommand.append('\\node[circle] (1) at ('+str(startPos[0]-0.75)+' cm,'+str(startPos[1]-0.75)+'cm) {'+links[0]+'};')
    tikzcommand.append('\\node[circle] (2) at ('+str(startPos[0]-0.75)+' cm,'+str(startPos[1]-1.75)+'cm) {'+links[1]+'};')
    tikzcommand.append('\\node[circle] (3) at ('+str(startPos[0]-0.75)+' cm,'+str(startPos[1]-2.75)+'cm) {'+links[2]+'};')
    tikzcommand.append('\\node[circle] (4) at ('+str(startPos[0]+0.75)+' cm,'+str(startPos[1]-0.75)+'cm) {'+rechts[0]+'};')
    tikzcommand.append('\\node[circle] (5) at ('+str(startPos[0]+0.75)+' cm,'+str(startPos[1]-1.75)+'cm) {'+rechts[1]+'};')
    tikzcommand.append('\\node[circle] (6) at ('+str(startPos[0]+0.75)+' cm,'+str(startPos[1]-2.75)+'cm) {'+rechts[2]+'};')
    if not ohneKlammernLinks:
        tikzcommand.append('\\draw[->] (1) to [out=190,in=170] node[left] {$:'+links[0]+'$}  (2) ;')
        tikzcommand.append('\\draw[->] (2) to [out=190,in=170] node[left] {$\cdot '+links[2]+'$}  (3) ;')
    if not ohneKlammernRechts:
        tikzcommand.append('\\draw[->] (4) to [out=350,in=10] node[right] {$:'+links[0]+'$}  (5) ;')
        tikzcommand.append('\\draw[->] (5) to [out=350,in=10] node[right] {$\cdot '+links[2]+'$}  (6) ;')
    if tikzUmrandung:
        tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand

def grundwertBerechnen(inhalte=[['2a',678,5,'Bücher'],['2b',329,4.7,'Autos']],bez=['G','W','p\\%']):
#Diese Funktion erzeugt eine Latex-Ausgabe, welche die Lösung einer gesuchten Grundwertaufgabe entspricht.
#
#     latexcommand=grundwertBerechnen(inhalt)
#
#  inhalt=[['2a',678,5,'Bücher'],['2b',329,4.7,'Autos']]
    latexcommand=['']
    for inhalt in inhalte:
        nr=inhalt[0]+(') ' if len(inhalt[0])>0 else'')
        W=inhalt[1]
        pP=inhalt[2]
        E=inhalt[3]
        G=W*100/pP
        latexcommand.append('\\begin{tabularx}{\\textwidth}{C{1.0cm} C{1.0cm} X C{1.0cm} X }')
        latexcommand.append('\\arrayrulecolor{black}')
        latexcommand.append(nr+'&Geg.:& '+bez[1]+'='+strNW(W,True)+'\ '+E+'& Ges.:& '+bez[0]+'=?\\\\')
        latexcommand.append('& & '+bez[2]+'='+strNW(pP,True)+'\ & &')
        latexcommand.append('\\end{tabularx}')
        latexcommand.append('')
        latexcommand.append('\\begin{equation*}')
        latexcommand.append('\\begin{split}')
        latexcommand.append(''+bez[0]+'&=W\\cdot 100 : '+bez[2]+' \\\\')
        latexcommand.append(''+bez[0]+'&='+strNW(W,True)+'\\cdot 100 : '+strNW(pP,True)+'\ \\\\')
        latexcommand.append(''+bez[0]+'&='+strNW(G,True)+'\\ \\mbox{'+E+'}')
        latexcommand.append('\\end{split}')
        latexcommand.append('\\end{equation*}')
        latexcommand.append('\\begin{equation*}')
        latexcommand.append('\\begin{split}')
        latexcommand.append(strNW(pP,True)+'\\ \\% & \\ \\hat=\\ '+strNW(W,True)+'\\ \\mbox{'+E+'} \\\\')
        latexcommand.append('100\\ \\% &\\ \\hat=\\ '+strNW(G,True)+'\\ \\mbox{'+E+'} \\\\')
        latexcommand.append('\\end{split}')
        latexcommand.append('\\end{equation*}')
        latexcommand.append('\\hrule')
    return latexcommand

def ausgabeProzentwertBerechnenFuerTabelle(inhalte=[['2a',420,56,'\euro{}'],['2b',78536,'kg']],mitDreisatz=True,bez=['G','W','p']):
#Diese Funktion erzeugt eine Latex-Ausgabe, welche die Lösung einer gesuchten Prozentsatzaufgabe entspricht.
#Die Ausgabe wird in einer Tikz-Zeichnung ausgegeben, damit man die Lösung in einer Tabelle zusammenfassen kann.
#     latexcommand=prozentsatzBerechnen(inhalt)
#
#  inhalt=[[bez,G,pP,'Einheit']]
#  inhalt=[['2a',125,50,'Schüler'],['2b',60,27,'km']]
    latexcommand=['']
    for inhalt in inhalte:
        nr=inhalt[0]+(') ' if len(inhalt[0])>0 else'')
        G=inhalt[1]
        pP=inhalt[2]
        W=G*pP/100
        E=inhalt[3]
        latexcommand.append('\\begingroup\\setlength{\\jot}{0.02cm}')
        latexcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')  
        latexcommand.append('\\begin{tikzpicture}[show background grid]')  
        latexcommand.append('\\node[left] at (0,-0.25) {'+nr+'Geg.: };')  
        latexcommand.append('\\node[right] at (0,-0.25) {'+bez[0]+' = '+strNW(G,True)+' '+E+'};') 
        latexcommand.append('\\node[right] at (0,-0.75) {'+bez[2]+'\\% = '+strNW(pP,True)+'\%};')  
        latexcommand.append('\\node[left] at (0,-1.-0.25) {Ges.: };')  
        latexcommand.append('\\node[right] at (0,-1.-0.25) {'+bez[1]+'  = ? };')  
        latexcommand.append('\\node[below right] at (0,-1.75) {')  
        latexcommand.append('$\\begin{aligned}')  
        latexcommand.append(''+bez[1]+'\\ &=\\ '+bez[0]+'\\cdot '+bez[2]+' : 100 \\\\')
        latexcommand.append(''+bez[1]+'\\ &=\\ '+strNW(G,True)+'\\cdot '+strNW(pP,True)+'\ :\ 100 \\\\')
        latexcommand.append('\makebox[0pt][l]{\\uuline{\\phantom{W\\%\\ =\\ '+strNW(W,True)+'\ \\mbox{'+E+'}}}}')
        latexcommand.append(''+bez[1]+'\\ &=\\ '+strNW(W,True)+'\ \\mbox{'+E+'}')
        latexcommand.append('\\end{aligned}$};')
        if mitDreisatz:
            latexcommand=latexcommand+dreiSatz(links=[strNW(100,True),'1',strNW(pP,True)],rechts=[strNW(G,True),strNW(G/100,True),strNW(W,True)],title=['\%',E],startPos=[1,-4],tikzUmrandung=False)
        latexcommand.append('\\end{tikzpicture}')   
        latexcommand.append('\\endgroup')
    return latexcommand
    
def ausgabeProzentsatzBerechnenFuerTabelle(inhalte=[['2a',125,50,'Schüler'],['2b',60,27,'km']],mitDreisatz=True,bez=['G','W','p']):
#Diese Funktion erzeugt eine Latex-Ausgabe, welche die Lösung einer gesuchten Prozentsatzaufgabe entspricht.
#Die Ausgabe wird in einer Tikz-Zeichnung ausgegeben, damit man die Lösung in einer Tabelle zusammenfassen kann.
#     latexcommand=prozentsatzBerechnen(inhalt)
#
#  inhalt=[[bez,G,W,'Einheit']]
#  inhalt=[['2a',125,50,'Schüler'],['2b',60,27,'km']]
    latexcommand=['']
    for inhalt in inhalte:
        nr=inhalt[0]+(') ' if len(inhalt[0])>0 else'')
        G=inhalt[1]
        W=inhalt[2]
        pP=W/G*100
        E=inhalt[3]
        latexcommand.append('\\begingroup\\setlength{\\jot}{0.02cm}')
        latexcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')  
        latexcommand.append('\\begin{tikzpicture}[show background grid]')  
        latexcommand.append('\\node[left] at (0,-0.25) {'+nr+'Geg.: };')  
        latexcommand.append('\\node[right] at (0,-0.25) {'+bez[0]+' = '+strNW(G,True)+' '+E+'};') 
        latexcommand.append('\\node[right] at (0,-0.75) {'+bez[1]+' = '+strNW(W,True)+' '+E+'};')  
        latexcommand.append('\\node[left] at (0,-1.25) {Ges.: };')  
        latexcommand.append('\\node[right] at (0,-1.25) {'+bez[2]+'\\%  = ? };')  
        latexcommand.append('\\node[below right] at (0,-1.85) {')  
        latexcommand.append('$\\begin{aligned}')  
        latexcommand.append(''+bez[2]+'\\ &=\\ '+bez[1]+'\\cdot 100 : '+bez[0]+' \\\\')
        latexcommand.append(''+bez[2]+'\\ &=\\ '+strNW(W,True)+'\\cdot 100 : '+strNW(G,True)+'\ \\\\')
        latexcommand.append('\makebox[0pt][l]{\\uuline{\\phantom{p\\%\\ =\\ '+strNW(pP,True)+'\\% }}}')
        latexcommand.append('p\\ &=\\ '+strNW(pP,True)+'\\% ')
        latexcommand.append('\\end{aligned}$};')
        if mitDreisatz:
            latexcommand=latexcommand+dreiSatz(links=[strNW(G,True),'1',strNW(W,True)],rechts=['100',strNW(100/G,True),strNW(pP,True)],title=[E,'\%'],startPos=[1,-4],tikzUmrandung=False)
        latexcommand.append('\\end{tikzpicture}')   
        latexcommand.append('\\endgroup')
    return latexcommand

def ausgabeGrundwertBerechnenFuerTabelle(inhalte=[['2a',264,55,'\euro{}'],['2b',1680,24,'kg']],mitDreisatz=True,bez=['G','W','p']):
#Diese Funktion erzeugt eine Latex-Ausgabe, welche die Lösung einer gesuchten Prozentsatzaufgabe entspricht.
#Die Ausgabe wird in einer Tikz-Zeichnung ausgegeben, damit man die Lösung in einer Tabelle zusammenfassen kann.
#     latexcommand=prozentsatzBerechnen(inhalt)
#
#  inhalt=[[bez,W,pP,'Einheit']]
#  inhalt=[['2a',125,50,'Schüler'],['2b',60,27,'km']]
    latexcommand=['']
    for inhalt in inhalte:
        nr=inhalt[0]+(') ' if len(inhalt[0])>0 else'')
        W=inhalt[1]
        pP=inhalt[2]
        G=W*100/pP
        E=inhalt[3]
        latexcommand.append('\\begingroup\\setlength{\\jot}{0.02cm}')
        latexcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')  
        latexcommand.append('\\begin{tikzpicture}[show background grid]')  
        latexcommand.append('\\node[left] at (0,-0.25) {'+nr+'Geg.: };')  
        latexcommand.append('\\node[right] at (0,-0.25) {'+bez[1]+' = '+strNW(W,True)+' '+E+'};') 
        latexcommand.append('\\node[right] at (0,-0.75) {'+bez[2]+'\\% = '+strNW(pP,True)+'\%};')  
        latexcommand.append('\\node[left] at (0,-1.-0.25) {Ges.: };')  
        latexcommand.append('\\node[right] at (0,-1.-0.25) {'+bez[0]+'  = ? };')  
        latexcommand.append('\\node[below right] at (0,-1.75) {')  
        latexcommand.append('$\\begin{aligned}')  
        latexcommand.append(''+bez[0]+'\\ &=\\ '+bez[1]+'\\cdot 100 : '+bez[2]+' \\\\')
        latexcommand.append(''+bez[0]+'\\ &=\\ '+strNW(W,True)+'\\cdot\\ 100\\ :'+strNW(pP,True)+' \\\\')
        latexcommand.append('\makebox[0pt][l]{\\uuline{\\phantom{G\\%\\ =\\ '+strNW(G,True)+'\ \\mbox{'+E+'}}}}')
        latexcommand.append(''+bez[0]+'\\ &=\\ '+strNW(G,True)+'\ \\mbox{'+E+'}')
        latexcommand.append('\\end{aligned}$};')
        if mitDreisatz:
            latexcommand=latexcommand+dreiSatz(links=[strNW(pP,True),'1',strNW(100,True)],rechts=[strNW(W,True),strNW(W/pP,True),strNW(G,True)],title=['\%',E],startPos=[1,-4],tikzUmrandung=False)
        latexcommand.append('\\end{tikzpicture}')   
        latexcommand.append('\\endgroup')
    return latexcommand

def ausgabeVerminderteGrundwertBerechnenFuerTabelle(inhalte=[['2a',420,56,'\euro{}'],['2b',78536,'kg']],mitDreisatz=True,bez=['G','W','p','G_{V-}']):
#Diese Funktion erzeugt eine Latex-Ausgabe, welche die Lösung einer gesuchten Prozentsatzaufgabe entspricht.
#Die Ausgabe wird in einer Tikz-Zeichnung ausgegeben, damit man die Lösung in einer Tabelle zusammenfassen kann.
#     latexcommand=prozentsatzBerechnen(inhalt)
#
#  inhalt=[[bez,G,pP,'Einheit']]
#  inhalt=[['2a',125,50,'Schüler'],['2b',60,27,'km']]
    latexcommand=['']
    for inhalt in inhalte:
        nr=inhalt[0]+(') ' if len(inhalt[0])>0 else'')
        G=inhalt[1]
        pP=inhalt[2]
        vermind=100-pP
        W=G*pP/100
        E=inhalt[3]
        latexcommand.append('\\begingroup\\setlength{\\jot}{0.02cm}')
        latexcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')  
        latexcommand.append('\\begin{tikzpicture}[show background grid]')  
        latexcommand.append('\\node[left] at (0,-0.25) {'+nr+'Geg.: };')  
        latexcommand.append('\\node[right] at (0,-0.25) {'+bez[1]+' = '+strNW(G,True)+' '+E+'};') 
        latexcommand.append('\\node[right] at (0,-0.75) {'+bez[2]+'\\% = '+strNW(pP,True)+'\%};')  
        latexcommand.append('\\node[left] at (0,-1.-0.25) {Ges.: };')  
        latexcommand.append('\\node[right] at (0,-1.-0.25) {$'+bez[3]+'$  = ? };')  
        latexcommand.append('\\node[below right] at (0,-1.75) {')  
        latexcommand.append('$\\begin{aligned}')  
        latexcommand.append(''+bez[1]+'\\ &=\\ '+bez[0]+'\\cdot '+bez[2]+' : 100 \\\\')
        latexcommand.append(''+bez[1]+'\\ &=\\ '+strNW(G,True)+'\\cdot '+strNW(pP,True)+'\ :\ 100 \\\\')
        latexcommand.append('\makebox[0pt][l]{\\uline{\\phantom{W\\%\\ =\\ '+strNW(W,True)+'\ \\mbox{'+E+'}}}}')
        latexcommand.append(''+bez[1]+'\\ &=\\ '+strNW(W,True)+'\ \\mbox{'+E+'}')
        latexcommand.append('\\end{aligned}$};')
        if mitDreisatz:
            latexcommand=latexcommand+dreiSatz(links=[strNW(100,True),'1',strNW(pP,True)],rechts=[strNW(G,True),strNW(G/100,True),strNW(W,True)],title=['\%',E],startPos=[1,-4],tikzUmrandung=False)
        latexcommand.append('\\node[below right] at (0,'+str(-4-2.75-1.0)+') {')  
        latexcommand.append('$\\begin{aligned}')  
        latexcommand.append(''+bez[3]+' &=\\ '+bez[0]+'-'+bez[1]+' \\\\') 
        latexcommand.append(''+bez[3]+' &=\\ '+strNW(G,True)+'-'+strNW(W,True)+' \\\\')
        latexcommand.append('\makebox[0pt][l]{\\uuline{\\phantom{GV- =\\ '+strNW(G-W,True)+'\ \\mbox{'+E+'}}}}')
        latexcommand.append(''+bez[3]+' &=\\ '+strNW(G-W,True)+'\ \\mbox{'+E+'}')
        latexcommand.append('\\end{aligned}$};')
        latexcommand.append('\\end{tikzpicture}')   
        latexcommand.append('\\endgroup')
    return latexcommand

def ausgabeVerminderteGrundwertAusgebenMitQ(inhalte=[['2a',420,56,'\euro{}'],['2b',78536,'kg']],bez=['G','W','p','G_{V-}']):
#Diese Funktion erzeugt eine Latex-Ausgabe, welche die Lösung einer gesuchten Prozentsatzaufgabe entspricht.
#Die Ausgabe wird in einer Tikz-Zeichnung ausgegeben, damit man die Lösung in einer Tabelle zusammenfassen kann.
#     latexcommand=prozentsatzBerechnen(inhalt)
#
#  inhalt=[[bez,G,pP,'Einheit']]
#  inhalt=[['2a',125,50,'Schüler'],['2b',60,27,'km']]
    latexcommand=['']
    for inhalt in inhalte:
        nr=inhalt[0]+(') ' if len(inhalt[0])>0 else'')
        G=inhalt[1]
        pP=inhalt[2]
        vermind=100-pP
        W=G*pP/100
        W2=G*vermind/100
        E=inhalt[3]
        latexcommand.append('\\begingroup\\setlength{\\jot}{0.02cm}')
        latexcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')  
        latexcommand.append('\\begin{tikzpicture}[show background grid]')  
        latexcommand.append('\\node[left] at (0,-0.25) {'+nr+'Geg.: };')  
        latexcommand.append('\\node[right] at (0,-0.25) {'+bez[0]+' = '+strNW(G,True)+' '+E+'};') 
        latexcommand.append('\\node[right] at (0,-0.75) {'+bez[2]+'\\% = '+strNW(pP,True)+'\%};')  
        latexcommand.append('\\node[left] at (0,-1.-0.25) {Ges.: };')  
        latexcommand.append('\\node[right] at (0,-1.-0.25) {$'+bez[3]+'$  = ? };')  
        latexcommand.append('\\node[below right] at (0,-1.75) {')  
        latexcommand.append('$\\begin{aligned}')  
        latexcommand.append(''+bez[1]+'\\ &=\\ '+bez[0]+'\\cdot '+bez[2]+' : 100 \\\\')
        latexcommand.append(''+bez[1]+'\\ &=\\ '+strNW(G,True)+'\\cdot '+strNW(pP,True)+'\ :\ 100 \\\\')
        latexcommand.append('\makebox[0pt][l]{\\uline{\\phantom{W\\ \\ =\\ '+strNW(W,True)+'\ \\mbox{'+E+'}}}}')
        latexcommand.append(''+bez[1]+'\\ &=\\ '+strNW(W,True)+'\ \\mbox{'+E+'} \\\\')
        latexcommand.append('\makebox[0pt][l]{\\uuline{\\phantom{GV\\ =\\ G-W=\\ '+strNW(G,True)+'-'+strNW(W,True)+'=\ '+strNW(G-W,True)+'\ \\mbox{'+E+'}}}}')
        latexcommand.append(''+bez[3]+'\\ &=\\ G-W=\\ '+strNW(G,True)+'-'+strNW(W,True)+'=\ '+strNW(G-W,True)+'\ \\mbox{'+E+'}')
        latexcommand.append('\\end{aligned}$};')
        latexcommand.append('\\node[below right] at (0,-4.75) {')  
        latexcommand.append('$\\begin{aligned}')  
        latexcommand.append('q\\ &=\\ 100 - p\\% \\\\')
        latexcommand.append('q\\ &=\\ 100 - '+strNW(pP,True)+' \\\\')
        latexcommand.append('q\\ &=\\ '+strNW(100-pP,True)+' \\\\')
        latexcommand.append(''+bez[1]+'\\ &=\\ '+bez[0]+'\\cdot '+bez[2]+' : 100 \\\\')
        latexcommand.append(''+bez[1]+'\\ &=\\ '+strNW(G,True)+'\\cdot '+strNW(100-pP,True)+'\ :\ 100 \\\\')
        latexcommand.append('\makebox[0pt][l]{\\uuline{\\phantom{W\\%\\ =\\ '+strNW(W2,True)+'\ \\mbox{'+E+'}}}}')
        latexcommand.append(''+bez[3]+'='+bez[1]+'\\ &=\\ '+strNW(W2,True)+'\ \\mbox{'+E+'}')
        latexcommand.append('\\end{aligned}$};')
        latexcommand.append('\\end{tikzpicture}')   
        latexcommand.append('\\endgroup')
    return latexcommand

def ausgabeVermehrterGrundwertBerechnenFuerTabelle(inhalte=[['2a',420,56,'\euro{}'],['2b',78536,'kg']],mitDreisatz=True,bez=['G','W','p','G_{V+}']):
#Diese Funktion erzeugt eine Latex-Ausgabe, welche die Lösung einer gesuchten Prozentsatzaufgabe entspricht.
#Die Ausgabe wird in einer Tikz-Zeichnung ausgegeben, damit man die Lösung in einer Tabelle zusammenfassen kann.
#     latexcommand=prozentsatzBerechnen(inhalt)
#
#  inhalt=[[bez,G,pP,'Einheit']]
#  inhalt=[['2a',125,50,'Schüler'],['2b',60,27,'km']]
    latexcommand=['']
    for inhalt in inhalte:
        nr=inhalt[0]+(') ' if len(inhalt[0])>0 else'')
        G=inhalt[1]
        pP=inhalt[2]
        W=G*pP/100
        E=inhalt[3]
        latexcommand.append('\\begingroup\\setlength{\\jot}{0.02cm}')
        latexcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')  
        latexcommand.append('\\begin{tikzpicture}[show background grid]')  
        latexcommand.append('\\node[left] at (0,-0.25) {'+nr+'Geg.: };')  
        latexcommand.append('\\node[right] at (0,-0.25) {'+bez[0]+' = '+strNW(G,True)+' '+E+'};') 
        latexcommand.append('\\node[right] at (0,-0.75) {'+bez[2]+'\\% = '+strNW(pP,True)+'\%};')  
        latexcommand.append('\\node[left] at (0,-1.-0.25) {Ges.: };')  
        latexcommand.append('\\node[right] at (0,-1.-0.25) {$'+bez[3]+'$  = ? };')  
        latexcommand.append('\\node[below right] at (0,-1.75) {')  
        latexcommand.append('$\\begin{aligned}')  
        latexcommand.append(''+bez[1]+'\\ &=\\ '+bez[0]+'\\cdot '+bez[2]+' : 100 \\\\')
        latexcommand.append(''+bez[1]+'\\ &=\\ '+strNW(G,True)+'\\cdot '+strNW(pP,True)+'\ :\ 100 \\\\')
        latexcommand.append('\makebox[0pt][l]{\\uline{\\phantom{W\\%\\ =\\ '+strNW(W,True)+'\ \\mbox{'+E+'}}}}')
        latexcommand.append(''+bez[1]+'\\ &=\\ '+strNW(W,True)+'\ \\mbox{'+E+'}')
        latexcommand.append('\\end{aligned}$};')
        if mitDreisatz:
            latexcommand=latexcommand+dreiSatz(links=[strNW(100,True),'1',strNW(pP,True)],rechts=[strNW(G,True),strNW(G/100,True),strNW(W,True)],title=['\%',E],startPos=[1,-4],tikzUmrandung=False)
        latexcommand.append('\\node[below right] at (0,'+str(-4-2.75-1.0)+') {')  
        latexcommand.append('$\\begin{aligned}')  
        latexcommand.append(''+bez[3]+' &=\\ '+bez[0]+'+'+bez[1]+' \\\\') 
        latexcommand.append(''+bez[3]+' &=\\ '+strNW(G,True)+'+'+strNW(W,True)+' \\\\')
        latexcommand.append('\makebox[0pt][l]{\\uuline{\\phantom{GV- =\\ '+strNW(G-W,True)+'\ \\mbox{'+E+'}}}}')
        latexcommand.append(''+bez[3]+' &=\\ '+strNW(G+W,True)+'\ \\mbox{'+E+'}')
        latexcommand.append('\\end{aligned}$};')
        latexcommand.append('\\end{tikzpicture}')   
        latexcommand.append('\\endgroup')
    return latexcommand

def ausgabeVermehrterGrundwertAusgebenMitQ(inhalte=[['2a',420,56,'\euro{}'],['2b',78536,'kg']],bez=['G','W','p','G_{V+}']):
#Diese Funktion erzeugt eine Latex-Ausgabe, welche die Lösung einer gesuchten Prozentsatzaufgabe entspricht.
#Die Ausgabe wird in einer Tikz-Zeichnung ausgegeben, damit man die Lösung in einer Tabelle zusammenfassen kann.
#     latexcommand=prozentsatzBerechnen(inhalt)
#
#  inhalt=[[bez,G,pP,'Einheit']]
#  inhalt=[['2a',125,50,'Schüler'],['2b',60,27,'km']]
    latexcommand=['']
    for inhalt in inhalte:
        bez=inhalt[0]+(') ' if len(inhalt[0])>0 else'')
        G=inhalt[1]
        pP=inhalt[2]
        vermehr=100+pP
        W=G*pP/100
        W2=G*vermehr/100
        E=inhalt[3]
        latexcommand.append('\\begingroup\\setlength{\\jot}{0.02cm}')
        latexcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')  
        latexcommand.append('\\begin{tikzpicture}[show background grid]')  
        latexcommand.append('\\node[left] at (0,-0.25) {'+bez+'Geg.: };')  
        latexcommand.append('\\node[right] at (0,-0.25) {'+bez[0]+' = '+strNW(G,True)+' '+E+'};') 
        latexcommand.append('\\node[right] at (0,-0.75) {'+bez[2]+'p\\% = '+strNW(pP,True)+'\%};')  
        latexcommand.append('\\node[left] at (0,-1.-0.25) {Ges.: };')  
        latexcommand.append('\\node[right] at (0,-1.-0.25) {'+bez[3]+'  = ? };')  
        latexcommand.append('\\node[below right] at (0,-1.75) {')  
        latexcommand.append('$\\begin{aligned}')  
        latexcommand.append(''+bez[1]+'\\ &=\\ '+bez[0]+'\\cdot '+bez[2]+' : 100 \\\\')
        latexcommand.append(''+bez[1]+'\\ &=\\ '+strNW(G,True)+'\\cdot '+strNW(pP,True)+'\ :\ 100 \\\\')
        latexcommand.append('\makebox[0pt][l]{\\uline{\\phantom{W\\ \\ =\\ '+strNW(W,True)+'\ \\mbox{'+E+'}}}}')
        latexcommand.append(''+bez[1]+'\\ &=\\ '+strNW(W,True)+'\ \\mbox{'+E+'} \\\\')
        latexcommand.append('\makebox[0pt][l]{\\uuline{\\phantom{GV\\ =\\ G-W=\\ '+strNW(G,True)+'-'+strNW(W,True)+'=\ '+strNW(G-W,True)+'\ \\mbox{'+E+'}}}}')
        latexcommand.append(''+bez[3]+'\\ &=\\ '+bez[0]+'+'+bez[1]+'=\\ '+strNW(G,True)+'+'+strNW(W,True)+'=\ '+strNW(G+W,True)+'\ \\mbox{'+E+'}')
        latexcommand.append('\\end{aligned}$};')
        latexcommand.append('\\node[below right] at (0,-4.75) {')  
        latexcommand.append('$\\begin{aligned}')  
        latexcommand.append('q\\ &=\\ 100 + '+bez[2]+'\\% \\\\')
        latexcommand.append('q\\ &=\\ 100 + '+strNW(pP,True)+' \\\\')
        latexcommand.append('q\\ &=\\ '+strNW(100+pP,True)+' \\\\')
        latexcommand.append(''+bez[1]+'\\ &=\\ '+bez[0]+'\\cdot q : 100 \\\\')
        latexcommand.append(''+bez[1]+'\\ &=\\ '+strNW(G,True)+'\\cdot '+strNW(100+pP,True)+'\ :\ 100 \\\\')
        latexcommand.append('\makebox[0pt][l]{\\uuline{\\phantom{W\\%\\ =\\ '+strNW(W2,True)+'\ \\mbox{'+E+'}}}}')
        latexcommand.append(''+bez[3]+'='+bez[1]+'\\ &=\\ '+strNW(W2,True)+'\ \\mbox{'+E+'}')
        latexcommand.append('\\end{aligned}$};')
        latexcommand.append('\\end{tikzpicture}')   
        latexcommand.append('\\endgroup')
    return latexcommand

def prozentsatzBerechnen(inhalte=[['2a',125,50,'Schüler'],['2b',60,27,'km']],bez=['G','W','p']):
#Diese Funktion erzeugt eine Latex-Ausgabe, welche die Lösung einer gesuchten Prozentsatzaufgabe entspricht.
#
#     latexcommand=prozentsatzBerechnen(inhalt)
#
#  inhalt=[[bez,G,W,'Einheit']]
#  inhalt=[['2a',125,50,'Schüler'],['2b',60,27,'km']]
    latexcommand=['']
    for inhalt in inhalte:
        nr=inhalt[0]
        G=inhalt[1]
        W=inhalt[2]
        pP=W/G*100
        E=inhalt[3]
        latexcommand.append('\\begin{tabularx}{\\textwidth}{C{1.0cm} C{1.0cm} X C{1.0cm} X }')
        latexcommand.append('\\arrayrulecolor{black}')
        latexcommand.append(nr+'&Geg.:& '+bez[0]+'\ =\ '+strNW(G,True)+'\ '+E+'& Ges.:& '+bez[1]+'\\%\\ =\ ?\\\\')
        latexcommand.append('& & '+bez[1]+'\ =\ '+strNW(W,True)+'\ & &')
        latexcommand.append('\\end{tabularx}')
        latexcommand.append('')
        latexcommand.append('\\begin{alignat*}{1}')
        latexcommand.append(''+bez[2]+'\\%\\ &=\\ '+bez[1]+'\\cdot 100 : '+bez[0]+' \\\\')
        latexcommand.append(''+bez[0]+'\\ &=\\ '+strNW(W,True)+'\\cdot 100 : '+strNW(G,True)+'\ \\\\')
        latexcommand.append('\makebox[0pt][l]{\\uuline{\\phantom{p\\%\\ =\\ '+strNW(pP,True)+'\\% }}}')
        latexcommand.append(''+bez[0]+'\\%\\ &=\\ '+strNW(pP,True)+'\\% ')
        latexcommand.append('\\end{alignat*}')
        latexcommand=latexcommand+dreiSatz(links=[strNW(G,True),'1',strNW(W,True)],rechts=['100',strNW(100/G,True),strNW(pP,True)],title=[E,'\\%'],startPos=[0,0])        
        latexcommand.append('\\begin{alignat*}{1}')
        latexcommand.append(strNW(pP,True)+'\\ \\% & \\ \\hat=\\ '+strNW(W,True)+'\\ \\mbox{'+E+'} \\\\')
        latexcommand.append('100\\ \\% &\\ \\hat=\\ '+strNW(G,True)+'\\ \\mbox{'+E+'} \\\\')
        latexcommand.append('\\end{alignat*}')
        
        latexcommand.append('\\hrule')
    return latexcommand
    
def grundwertBerechnenSchnell(inhalt=[['3a',4,5,'LKW'],['3b',180,10,'Mädchen']],bez=['G','W','p']):
#Diese Funktion stellt die Lösung von Grundwertberechnungen dar, die man im Kopf lösen kann. 
#Aufruf:
#             latexcommand=grundwertBerechnenSchnell(inhalt)
#Mit
#           inhalt=[[Bez,Wert,Prozentsatz,Einheit]]
#Beispiel
#           inhalt=[['3a',4,5,'LKW'],['3b',180,10,'Mädchen']]
    latexcommand=['']
    for inhalt in inhalte:
        nr=inhalt[0]
        W=inhalt[1]
        pP=inhalt[2]
        E=inhalt[3]
        G=W*100/pP
        latexcommand.append(nr)
        latexcommand.append('\\begin{equation*}')
        latexcommand.append('\\begin{split}')
        latexcommand.append(strNW(pP,True)+'\\ \\% & \\ \\hat=\\ '+strNW(W,True)+'\\ \\mbox{'+E+'} \\\\')
        latexcommand.append('100\\ \\% &\\ \\hat=\\ '+strNW(100/pP,True)+'\\cdot '+strNW(W,True)+'\\ \\mbox{'+E+'}\\ =\\ '+strNW(G,True)+'\\ \\mbox{'+E+'} \\\\')
        latexcommand.append('\\end{split}')
        latexcommand.append('\\end{equation*}')
        latexcommand.append('\\hrule')
    return latexcommand

def mehrereDreisaetze(inhalte=[['1a)',['50','1','100'],['50','$\ $','$\ $'],['\%','\euro{}']],['Lsg',['50','1','100'],['30','$\\frac{3}{5}$','60'],['\%','\euro{}']]],anzProZeile=3,ohneKlammernRechts=False):
#Diese Funktion ruft die Funktion dreiSatz() auf, um mehrere Dreisätze in ein Bild zu schreiben.
#Aufruf:
#        tikzcommand=  mehrereDreisaetze(inhalte)
#Beispiel:
#        tikzcommand=  mehrereDreisaetze(inhalte=[['1a',['50','1','100'],['30','$\ $','$\ $'],['\%','\euro{}']],['1b',['50','1','100'],['50','$\ $','$\ $'],['\%','\euro{}']]])
#
#      inhalte = Liste mit folgendem Aufbau: [[Bezeichnung,Linke Spalte,Rechte Spalte,Titel],...]
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    startPos=np.array([0,0])
    for i,inhalt in enumerate(inhalte):
        print(inhalt)
        tikzcommand.append('\\node[below] at ('+str(startPos[0]-2.5)+'cm,'+str(startPos[1])+'cm) {'+inhalt[0]+'};')
        tikzcommand=tikzcommand+dreiSatz(links=inhalt[1],rechts=inhalt[2],title=inhalt[3],startPos=startPos,tikzUmrandung=False,ohneKlammernRechts=ohneKlammernRechts)
        startPos=startPos+[6,0]
        if (i+1)%anzProZeile==0:
            startPos=np.array([0,startPos[1]-4])
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand

def tagesMonatsZinsenBerechnen(inhalt=[100,12,4],art='Monatszinsen'):
#Diese Funktion erzeugt eine Latex-Ausgabe, welche die Tages oder Monatszinsen berechnet.
#
#     latexcommand=tagesMonatsZinsenBerechnen(inhalt=[K,p,time],art='Monatszinsen' oder 'Tageszinsen)
    latexcommand=['']
    K=inhalt[0]
    pP=inhalt[1]
    t=inhalt[2]
    maxT=12 if art=='Monatszinsen' else 360
    nameT='m' if art=='Monatszinsen' else 'd'
    nameTLang='Monate' if art=='Monatszinsen' else 'Tage'
    latexcommand.append('\\begingroup\\setlength{\\jot}{0.15cm}')
    latexcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')  
    latexcommand.append('\\begin{tikzpicture}[show background grid]')  
    latexcommand.append('\\node[left] at (0,-0.25) {Geg.: };')  
    latexcommand.append('\\node[right] at (0,-0.25) {K\ =\ '+strNW(K,True)+'\\ \\euro{}};') 
    latexcommand.append('\\node[right] at (0,-0.75) {p\ \\%=\ '+strNW(pP,True)+'\\%};')  
    latexcommand.append('\\node[right] at (0,-1.25) {'+nameT+'\ =\ '+strNW(t,True)+'\\ '+nameTLang+'};')  
    latexcommand.append('\\node[left] at (0,-1.75) {Ges.: };')  
    latexcommand.append('\\node[right] at (0,-1.75) {$ Z\\ =\\ ?$};')  
    latexcommand.append('\\node[below right] at (0,-2.25) {') 
    latexcommand.append('$\\begin{aligned}')  
    latexcommand.append('Z\\ &=\\frac{K\\cdot p}{100}\\cdot \\frac{'+nameT+'}{'+strNW(maxT)+'} \\\\')
    latexcommand.append('Z\\ &=\\frac{'+strNW(K)+'\\cdot '+strNW(pP)+'}{100}\\cdot \\frac{'+strNW(t)+'}{'+strNW(maxT)+'} \\\\')
    latexcommand.append('\makebox[0pt][l]{\\uuline{\\phantom{Z\\ =\\ '+strNW(K*pP*t/(maxT*100),runden=True)+'\\ \\euro{} }}}')
    latexcommand.append('Z\\ &=\\ '+strNW(K*pP*t/(maxT*100),runden=True)+'\\ \\mbox{\\euro{}} ')
    latexcommand.append('\\end{aligned}$};')
    latexcommand.append('\\end{tikzpicture}')   
    latexcommand.append('\\endgroup')
    return latexcommand


def tagesMonatsZinsenBerechnenKapitalGesucht(inhalt=[100,12,4],art='Monatszinsen'):
#Diese Funktion erzeugt eine Latex-Ausgabe, welche die Tages oder Monatszinsen berechnet.
#
#     latexcommand=tagesMonatsZinsenBerechnen(inhalt=[K,p,time],art='Monatszinsen' oder 'Tageszinsen)
    latexcommand=['']
    Z=inhalt[0]
    pP=inhalt[1]
    t=inhalt[2]
    maxT=12 if art=='Monatszinsen' else 360
    nameT='m' if art=='Monatszinsen' else 'd'
    nameTLang='Monate' if art=='Monatszinsen' else 'Tage'
    latexcommand.append('\\begingroup\\setlength{\\jot}{0.15cm}')
    latexcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')  
    latexcommand.append('\\begin{tikzpicture}[show background grid]')  
    latexcommand.append('\\node[left] at (0,-0.25) {Geg.: };')  
    latexcommand.append('\\node[right] at (0,-0.25) {Z\ =\ '+strNW(Z,True)+'\\ \\euro{}};') 
    latexcommand.append('\\node[right] at (0,-0.75) {p\ \\%=\ '+strNW(pP,True)+'\\%};')  
    latexcommand.append('\\node[right] at (0,-1.25) {'+nameT+'\ =\ '+strNW(t,True)+'\\ '+nameTLang+'};')  
    latexcommand.append('\\node[left] at (0,-1.75) {Ges.: };')  
    latexcommand.append('\\node[right] at (0,-1.75) {$ K\\ =\\ ?$};')  
    latexcommand.append('\\node[below right] at (0,-2.25) {') 
    latexcommand.append('$\\begin{aligned}')
    latexcommand=latexcommand+formeEinfacheFormelNachVorgabenUm(G='Z=K*p/100*'+nameT+'/'+str(maxT),gesucht='K',mitTikzUmrandung=False)
    latexcommand.append('\\\\')
    latexcommand.append('K\\ &=\\frac{'+strNW(maxT*100)+'\\cdot '+strNW(Z)+'}{'+strNW(t)+'\\cdot'+strNW(pP)+'} \\\\')
    latexcommand.append('\makebox[0pt][l]{\\uuline{\\phantom{Z\\ =\\ '+strNW(Z*maxT*100/(t*pP),runden=True)+'\\ \\euro{} }}}')
    latexcommand.append('K\\ &=\\ '+strNW(Z*maxT*100/(t*pP),runden=True)+'\\ \\mbox{\\euro{}} ')
    latexcommand.append('\\end{aligned}$};')
    latexcommand.append('\\end{tikzpicture}')   
    latexcommand.append('\\endgroup')
    return latexcommand


def tagesMonatsZinsenBerechnenZinssatzGesucht(inhalt=[100,12,4],art='Monatszinsen'):
#Diese Funktion erzeugt eine Latex-Ausgabe, welche die Tages oder Monatszinsen berechnet.
#
#     latexcommand=tagesMonatsZinsenBerechnen(inhalt=[K,p,time],art='Monatszinsen' oder 'Tageszinsen)
    latexcommand=['']
    K=inhalt[0]
    Z=inhalt[1]
    t=inhalt[2]
    maxT=12 if art=='Monatszinsen' else 360
    nameT='m' if art=='Monatszinsen' else 'd'
    nameTLang='Monate' if art=='Monatszinsen' else 'Tage'
    latexcommand.append('\\begingroup\\setlength{\\jot}{0.15cm}')
    latexcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')  
    latexcommand.append('\\begin{tikzpicture}[show background grid]')  
    latexcommand.append('\\node[left] at (0,-0.25) {Geg.: };')  
    latexcommand.append('\\node[right] at (0,-0.25) {K\ =\ '+strNW(K,True)+'\\ \\euro{}};') 
    latexcommand.append('\\node[right] at (0,-0.75) {Z=\ '+strNW(Z,True)+'\\euro{}};')  
    latexcommand.append('\\node[right] at (0,-1.25) {'+nameT+'\ =\ '+strNW(t,True)+'\\ '+nameTLang+'};')  
    latexcommand.append('\\node[left] at (0,-1.75) {Ges.: };')  
    latexcommand.append('\\node[right] at (0,-1.75) {p\\%\\ =\\ ?};')  
    latexcommand.append('\\node[below right] at (0,-2.25) {') 
    latexcommand.append('$\\begin{aligned}')
    latexcommand=latexcommand+formeEinfacheFormelNachVorgabenUm(G='Z=K*p/100*'+nameT+'/'+str(maxT),gesucht='p',mitTikzUmrandung=False)
    latexcommand.append('\\\\')
    latexcommand.append('p\\ &=\\frac{'+strNW(maxT*100)+'\\cdot '+strNW(Z)+'}{'+strNW(t)+'\\cdot'+strNW(K)+'} \\\\')
    latexcommand.append('\makebox[0pt][l]{\\uuline{\\phantom{Z\\ =\\ '+strNW(Z*maxT*100/(t*K),runden=True)+'\\ \\euro{} }}}')
    latexcommand.append('p\\%\\ &=\\ '+strNW(Z*maxT*100/(t*K),runden=True)+'\\% ')
    latexcommand.append('\\end{aligned}$};')
    latexcommand.append('\\end{tikzpicture}')   
    latexcommand.append('\\endgroup')
    return latexcommand
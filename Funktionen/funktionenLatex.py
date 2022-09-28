#!/usr/bin/env python
# coding: utf8

#Diese Datei enthält verschiedene Funktionen, die zur Erstellung einer Latex tex-Datei benötigt werden.

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())
import os

buchstaben="A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()+"a b c d e f g h i j k l m n o p q e s t u v w x y z".split()

def erzeugeEinfachesLatexdokument(inhalt,size=2):
    pfad='Ausgabe'
    if not os.path.exists(pfad):
        os.mkdir(pfad)
    file='newFile.tex'
    ausgabeName=os.path.join(pfad,file)
    writeLatexDoc(latexHead(size=size)+beginDoc()+inhalt+['\\end{document}'],ausgabeName)
    os.chdir(pfad)
    os.system('xelatex '+file)
    os.chdir('..')

def latexHead(arraystretch=False,size=2):
    head=[]
    head.append('\\documentclass[12pt]{article}')
    head.append('\\usepackage[table]{xcolor}')
    head.append('\\usepackage{tabularx}')
    head.append('\\usepackage{graphicx}')
    head.append('\\usepackage{hyperref}')
    head.append('\\usepackage{verbatim}')
    head.append('\\usepackage{geometry}')
#Unterstreichen
    head.append('\\usepackage{ulem}')
#Euro Sympol:
    head.append('\\usepackage[official]{eurosym}')
####Bilder mit Latex erstellen: tikz
    head.append('\\usepackage{tikz}')
    head.append('\\usetikzlibrary{arrows,backgrounds}')     #Für Karo Hintergrund
####Diagramme und Funkionen zeichnen:
    head.append('\\usepackage{pgfplots}')
####Nutz die letzte Version von pgfplots:
    head.append('\\pgfplotsset{compat = newest}')
#Special Command for distance between table line an tikz picture
    head.append('\\usetikzlibrary{fit}')  
    head.append('\\newcommand\\addvmargin[1]{')
#Spezielles Packet, um gebogene Pfeile in Tikz darstellen zu können
    head.append('\\usetikzlibrary{arrows}') 
    head.append('\\node[fit=(current bounding box),inner ysep=#1,inner xsep=0]{};}')
    head.append('\\usepackage{cancel}')
#    head.append('\\usepackage[utf8]{inputenc}')
    head.append('\\usepackage{fontspec}')
    head.append('\\usepackage{array}  ')
    head.append('\\geometry{a4paper, top='+str(size)+'cm, left='+str(size)+'cm, right='+str(size)+'cm, bottom='+str(size)+'cm, headsep=1cm}')
    head.append('\\usepackage{tabu}')
    head.append('\\usepackage{pst-node}')
    head.append('\\usepackage{colortbl}')
    head.append('\\usepackage{array}')
#Deutsche Anfuehrungszeichen
    head.append('\\usepackage{german}')
#Ich möchte im ganzen Dokument keinen Einzug (Indention) haben.
    head.append('\\setlength\\parindent{0pt}')
#Dickere Vertikale Linie
    head.append('\\newcolumntype{?}{!{\\vrule width 1pt}}')
#Dicker Horizontale Linie:
    head.append('\\usepackage{makecell}')
#Extra Platz in Tabellen bei \frac. Sonst ist der Bruch direkt auf Tabellenlinie
#Führt zu Problemen,wenn an die Werte in Karo Papiert eintragen will.
    if arraystretch:
        head.append('\\renewcommand{\\arraystretch}{2.5}')
#    tabelle.append('\\setlength\\extrarowheight{2pt}')
### Zeilenumbruch in Tabellen sind mit einer pbox möglich:
    head.append('\\usepackage{pbox}')
#Für Mathematische Symbole in der Formelumgebung:
    head.append('\\usepackage{amssymb}')
    head.append('\\usepackage{amsmath}')
    head.append('\\usepackage{booktabs}')
#Folgende Zeilen sind dazu da, um anzugeben ob die Werte in den Zellen Zentriert, Links- oder Rechtsbündig geschrieben werden sollen.
    head.append('\\newcolumntype{L}[1]{>{\\raggedright\\let\\newline\\\\\\arraybackslash\\hspace{0pt}}m{#1}}')
    head.append('\\newcolumntype{C}[1]{>{\\centering\\let\\newline\\\\\\arraybackslash\\hspace{0pt}}m{#1}}')
    head.append('\\newcolumntype{R}[1]{>{\\raggedleft\\let\\newline\\\\\\arraybackslash\\hspace{0pt}}m{#1}}')
    return head

def setzeGleichheitszeichenAufLinie(gleichheitszeichen):
    ausgabe=[]
    for gzMarker in gleichheitszeichen:
        if type(gzMarker) == type(''):
            ausgabe.append('\\nput[labelsep=0.3]{90}{'+gzMarker+'}{$ = $}')
        else:
            ausgabe.append('\\nput[labelsep=0.3]{90}{'+gzMarker[0]+'}{$ '+gzMarker[1]+' $}')
    print('Ausgabe='+str(ausgabe))
    return ausgabe



def writeLatexDoc(inhalt,ausgabeName='newfile.tex'):
    with open(ausgabeName, 'w') as f:
        f.write('\n'.join(inhalt))

def beginDoc(kopf='',title='',anfang='',wichtig='',vspace=1):
    if False:
       wichtig='\\textbf{Wichtig:} Schreibe jede Ziffer in genau ein Kästchen.\\\\'
    begin=[]
    begin.append('\\begin{document}')
    begin.append('\\rightline{'+kopf+'}')
    begin.append('\\centerline{{\Large '+title+'}} ')
    if not vspace==0:
        begin.append('\\vspace{'+str(vspace)+'cm}')
    if isinstance(anfang, list):
        for line in anfang:
            begin.append('\\noindent '+line+'\\\\')
    else:
        begin.append('\\noindent '+anfang+('' if 'begin' in anfang else '\\\\'))
    begin.append(wichtig)
    begin.append('')
    return begin

def erzeugeLatexSection(sectionTitel,inhalt):
    section=[]
    section.append('\\section{'+sectionTitel+'}')
    section.append(inhalt)
    return section

def seitenwechsel(kopf='',title=''):
    wechsel=[]
    wechsel.append('\\newpage')
    wechsel.append('\\rightline{'+kopf+'}')
    if len(title)>0:
        wechsel.append('\\centerline{{\large '+title+'}} ')
    wechsel.append('\\vspace{0.5cm}')
    wechsel.append('')
    return wechsel

def fuegeFilecontentInTikzEin(name='',linien=[],extra=[],x=0,y=0,mitUmrandung=True,nurAnfang=False,nurEnde=False):
    tikzTabelle=[]
    if mitUmrandung or nurAnfang:
        tikzTabelle.append('\\begin{center}')
        tikzTabelle.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
        tikzTabelle.append('\\begin{tikzpicture}[show background grid]')
    if not (nurAnfang or nurEnde):
        tikzTabelle.append('\\node[black,below right] at ('+str(-0.15+x)+','+str(0.15+y)+') {\\input{'+name+'.tex}};')
        for l in linien:
            tikzTabelle.append('\\draw[black] ('+str(l[0]+x)+','+str(l[1]+y)+') -- ('+str(l[2]+x)+','+str(l[3]+y)+') ;')
        for ex in extra:
            tikzTabelle.append('\\node at ('+str(ex[0]+x)+','+str(ex[1]+y)+') {'+ex[2]+'} ;')
    if mitUmrandung or nurEnde:
        tikzTabelle.append('\\end{tikzpicture}')
        tikzTabelle.append('\\end{center}')
    return tikzTabelle


def schreibeMehrereTabellenInEinTikz(tabListe=[],anzNebeneinander=2,abstandx=2,abstandy=1):
#Diese Funktion ruft öfters fuegeFilecontentInTikzEin auf, um mehrere Tabellen in eine Tikz Zeichnung zu schreiben.
#tabListe=[[[filecontensCode1,name1,tabelle1,linien1],[filecontensCode2,name2,tabelle2,linien2],...]
    tikzTabellen=fuegeFilecontentInTikzEin(mitUmrandung=False, nurAnfang=True)
    x=0
    y=0
    for i,tab in enumerate(tabListe):
        print('x='+str(x))
        print('y='+str(y))
        print('name='+tab[1])
        tikzTabellen=tikzTabellen+fuegeFilecontentInTikzEin(tab[1],linien=tab[3],extra=tab[4],x=x,y=-y,mitUmrandung=False)
        x=x+len(tab[2][0])*0.5+abstandx
        if (i+1)%anzNebeneinander==0:
            y=y+max([len(x[2]) for x in tabListe[(i+1)-anzNebeneinander:i+1]])*0.5+abstandy
            x=0
    tikzTabellen=tikzTabellen+fuegeFilecontentInTikzEin(mitUmrandung=False, nurEnde=True)
    return tikzTabellen

def erzeugeTabelleFilecontents(tabelle,name='tabelle'):
#Diese Funktion erzeugt eine Latex Code mit dem man eine Tabelle am Anfang eines Latexdokuments generiert, um diese
#dann in einer Tikz-Zeichnung einfügen zu könne.
#
#Aufruf:    filecontent=erzeugeTabelleFilecontents(tabelle,name)
    n=len(tabelle[0])
    m=len(tabelle)
    filecontent=['\\begin{filecontents*}{'+name+'.tex}']
    filecontent.append('\\resizebox*{'+str(n*0.5)+'cm}{'+str(m*0.5)+'cm}{\\begin{tabular}{*{'+str(n)+'}{c}}')
    for zeile in tabelle:
        filecontent.append('&'.join(zeile)+'\\\\')
    filecontent.append('\\end{tabular}}')
    filecontent.append('\\end{filecontents*}')
    return filecontent


def initialisiereTabellenwerte(anzZeilenSpalten):
#Initialisiere Tabellenwerte
#Achtung t=[['']*5]*6 geht nicht, da bei Python die Referenzen der Liste kopiert werden.
#D.h. t[2][3]=6 führt zu t=[['', '', '', 6, ''], ['', '', '', 6, ''], ['', '', '', 6, ''], ...
#Der Letzte Eintrag der Tabelle gibt die Tabellenlinie an
    tabellenWerte=[[['\\phantom{M)} & ']*(anzZeilenSpalten[0][1]-1)+['\\phantom{M)}','\\\\\\hline'] for j in range(anzZeilenSpalten[0][0])]]
    for i in range(len(anzZeilenSpalten)-1):
        tabellenWerte.append([['\\phantom{M)} & ']*(anzZeilenSpalten[i+1][1]-1)+['\\phantom{M)}','\\\\\\hline'] for j in range(anzZeilenSpalten[i+1][0])])    
    return tabellenWerte
#!/usr/bin/env python
# coding: utf8

#Diese Datei enthält verschiedene Funktionen, mit denen man Latex-Tabellen erzeugen kann, die Aufgaben oder Lösungen enthalten.

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())


def erzeugeEinfacheTabelle(inhalt=[['a)','afg1'],['b)','afg2']],spalten=2,nurThermometerAufgaben=False):
#inhalt=[['a)',afg1],['b)',afg2],usw]
    breite=7 if spalten==2 else 15
    if nurThermometerAufgaben:
        spalten=4
        breite=3.5
    tabelle=[]
    spaltendef='|'
    for i in range(spalten):
        spaltendef=spaltendef+'C{0.75cm}|X|'
    tabelle.append('\\begin{xltabular}{\\textwidth}{'+spaltendef+'}')
    tabelle.append('\\arrayrulecolor{black}\\hline')
    for i,inh in enumerate(inhalt):
        tabelle.append(inh[0]+'&') #+inh[1])
        if ('tikzpicture' in inh[1]) and not any([x in inh[1] for x in ['resizebox','$$','adjustbox']]):
            tabelle.append(F'\\begin{{adjustbox}}{{max width={breite} cm}}')
            tabelle.append(inh[1])
            tabelle.append(F'\\end{{adjustbox}}')
        else:
            tabelle.append(inh[1])
        tabelle.append('&' if (i+1)%spalten>0 else '\\\\\\hline' )
    tabelle.append('\\end{xltabular}')
    tabelle.append('\\vspace{0.5cm}')
    return tabelle

def erzeugeEinfacheTabelleMitSeitenumbruch(inhalt=[['a)','afg1'],['b)','afg2']],spalten=2,anzZeilen=1):
#inhalt=[['a)',afg1],['b)',afg2],usw]
    tabelle=[]
    spaltendef='|'
    for i in range(spalten):
        spaltendef=spaltendef+'C{1.0cm}|X|'
    tabelle.append('\\begin{tabularx}{\\textwidth}{'+spaltendef+'}')
    tabelle.append('\\arrayrulecolor{black}\\hline')
    for i,inh in enumerate(inhalt):
        tabelle.append(inh[0]+'&{'+inh[1]+'}')
        tabelle.append('&' if (i+1)%spalten>0 else '\\\\\\hline' )
        if ((i+1)/spalten+1) % anzZeilen==0:
            tabelle.append('\\end{tabularx}')
            tabelle.append('\\vspace{0.5cm}')
            tabelle.append('\\begin{tabularx}{\\textwidth}{'+spaltendef+'}')
            tabelle.append('\\arrayrulecolor{black}\\hline')
    tabelle.append('\\end{tabularx}')
    tabelle.append('\\vspace{0.5cm}')
    return tabelle
def erzeugeTabellen10minAfgLsg(rechnungen,beschreibung=''):
#Diese Funktion erstellt eine Tabelle der Form:
#           a) Aufgaben 1          b) Aufgabe 2
#           c) Aufgaben 3          d) Aufgabe 4
#usw.
#Eingabe: art=[typen]  --> Liste mit Typen.
    aufgaben=[]
    lsgen=[]
    rechnungen=[]
    zeile=''
    for i,typ in enumerate(typen):
        if typ=='ggT':
            with open('/taeglicheUebungen/Mathe6/ggT.txt') as f:
                rechnungen.append('ggT('+random.choice(f.read().split('\n'))+')')
            textAfg='Berechne '+ rechnungen[-1]
            textLsg='Berechne '+ rechnungen[-1]
        if typ=='kgV':
            with open('/taeglicheUebungen/Mathe6/kgV.txt') as f:
                rechnungen.append('kgV('+random.choice(f.read().split('\n'))+')')
            text='Berechne '+ rechnungen[-1]
        if typ=='Basis':
            rechnungen.append([random.choice(erzeugeGemischteRechnung()[-4:])[1],typ])
        if typ=='Kopf':
            rechnungen.append([erzeugeKopfrechenAufgabe().split('=')[0],typ])   
        if typ=='erweitern':
#           Aufgabe=[Faktor,Zaehler,Nenner]
            text='Erweiter mit dem Faktor '+r[1][0]+': $\\frac{'+r[1][1]+'}{'+r[1][2]+'}$'
        if 'kuerzen' == r[2]:
#           Aufgabe=[Zaehler,Nenner]
            text='Kürze soweit wie möglich: $\\frac{'+r[1][0]+'}{'+r[1][1]+'}$'
        if 'kuerzenMitTeiler' == r[2]:
#           Aufgabe=[Teiler,Zaehler,Nenner]
            text='Kürze mit dem Teiler '+r[1][0]+': $\\frac{'+r[1][1]+'}{'+r[1][2]+'}$'
        if 'bruchVergleichen' == r[2]:
#           Aufgabe=[[z1,n1],[z2,n2]]
            text='Vergleiche $\\frac{'+str(r[1][0][0])+'}{'+str(r[1][0][1])+'}$ mit  $\\frac{'+str(r[1][1][0]) +'}{'+str(r[1][1][1])+'}$'
        if 'Bruchteil' == r[2]:
#           Aufgabe=[Ganzes,z,n,]
            text='Berechne $\\frac{'+r[1][1]+'}{'+r[1][2]+'}$ von '+r[1][0]+' '+r[1][4]
        if 'GanzesBerechnen' == r[2]:
            text='Bestimme: $\\frac{'+r[1][1]+'}{'+r[1][2]+'}$ von \\rule{1cm}{0.4pt} sind '+r[1][3]+' '+r[1][4]
        if 'BruchAddSub' in r[2]:
           r1=[[str(y) for y in x] if isinstance(x,list) else x for x in r[1]]
           if True:
               bruch1='\\frac{'+r1[0][0]+'}{'+r1[0][1]+'}' if random.randint(1,10) > 3 else schreibeGemZahl(int(r1[0][0]),int(r1[0][1]))
               bruch2='\\frac{'+r1[2][0]+'}{'+r1[2][1]+'}' if random.randint(1,10) > 3 else schreibeGemZahl(int(r1[2][0]),int(r1[2][1]))
           else:
               bruch1='\\frac{'+r1[0][0]+'}{'+r1[0][1]+'}'
               bruch2='\\frac{'+r1[2][0]+'}{'+r1[2][1]+'}'
           random.randint(1,10)
           text='$'+bruch1+r1[1]+bruch2+'=$'
        if 'GemischteZahlzuBruch' == r[2]:
            text='Schreibe als Bruch $'+r[1][2]+'\\frac{'+r[1][3]+'}{'+r[1][4]+'}$'
        if 'BruchzuGemischteZahl' == r[2]:
            text='Schreibe als gemischte Zahl $\\frac{'+r[1][0]+'}{'+r[1][1]+'}$'
        if 'rechneLaengenEinheitenUm' == r[2] or 'rechneQuadrateEinheitenUm' == r[2]:
            text=r[1][0]
        if 'UmfangMessen' == r[2] or 'FlaecheMessen' == r[2] or 'FlaecheUmfang' == r[2]:
#            text=r[1][0]
            text=['\\pbox{20cm}{Berechne den Umfang, die Fläche \\\\ und beschrifte: \\\\']+r[1][0]+['}']
        if 'ZusGesetztFl'== r[2]:
            text=['\\pbox{20cm}{Berechne die Fläche und beschrifte: \\\\']+zusammengesetzteRechtecke(r[1])+['}']
        if 'ZusGesetztFlSchwer'== r[2]:
            text=['\\pbox{20cm}{Berechne die Fläche und beschrifte: \\\\']+zusammengesetzteRechteckeSchwer(r[1])+['}']
#Tikz Bilder sind als Listen gespeichert
        if isinstance(text,list):
           text[0]=zeile+r[0]+' & '+text[0]
           for k in range(len(text)-1):
               tabelle.append(text[k])
           zeile=text[-1]
#Ende Tikz Bilder sind als Listen gespeichert
        else:
           zeile=zeile+r[0]+' & '+text
        if i%2>0:
           tabelle.append(zeile+'\\\\\\hline')
           zeile=''
        else:
           zeile=zeile+' & '
    tabelle.append('\\end{tabularx}')
    tabelle.append('\\vspace{0.5cm}')
    tabelle.append('')
    tabelle.append('')
    return tabelle

def erzeugeTabelle10minRechnung(rechnungen,beschreibung=''):
#Diese Funktion erstellt eine Tabelle der Form:
#           a) Aufgaben 1          b) Aufgabe 2
#           c) Aufgaben 3          d) Aufgabe 4
#usw.
#Eingabe: rechnungen=Liste mit Aufgaben, wobei ein Eintrag folgendes Format haben muss:
#         rechnungen[i]=['b)',Aufgabe,'Typ']
    tabelle=[]
    tabelle.append('\\noindent\\begin{tabularx}{\\textwidth}{|C{1.0cm}|X|C{1.0cm}|X|}')
#    tabelle.append('\\renewcommand{\\arraystretch}{1.5}')
#    tabelle.append('\\setlength\\extrarowheight{2pt}')
    tabelle.append('\\arrayrulecolor{black}\\hline')
    zeile=''
    for i,r in enumerate(rechnungen):
       text='Berechne '+str(r[1]).replace('*','$\cdot$').replace('/',':')
       if 'erweitern' == r[2]:
#           Aufgabe=[Faktor,Zaehler,Nenner]
            text='Erweiter mit dem Faktor '+r[1][0]+': $\\frac{'+r[1][1]+'}{'+r[1][2]+'}$'
       if 'kuerzen' == r[2]:
#           Aufgabe=[Zaehler,Nenner]
            text='Kürze soweit wie möglich: $\\frac{'+r[1][0]+'}{'+r[1][1]+'}$'
       if 'kuerzenMitTeiler' == r[2]:
#           Aufgabe=[Teiler,Zaehler,Nenner]
            text='Kürze mit dem Teiler '+r[1][0]+': $\\frac{'+r[1][1]+'}{'+r[1][2]+'}$'
       if 'bruchVergleichen' == r[2]:
#           Aufgabe=[[z1,n1],[z2,n2]]
            text='Vergleiche $\\frac{'+str(r[1][0][0])+'}{'+str(r[1][0][1])+'}$ mit  $\\frac{'+str(r[1][1][0]) +'}{'+str(r[1][1][1])+'}$'
       if 'Bruchteil' == r[2]:
#           Aufgabe=[Ganzes,z,n,]
            text='Berechne $\\frac{'+r[1][1]+'}{'+r[1][2]+'}$ von '+r[1][0]+' '+r[1][4]
       if 'GanzesBerechnen' == r[2]:
            text='Bestimme: $\\frac{'+r[1][1]+'}{'+r[1][2]+'}$ von \\rule{1cm}{0.4pt} sind '+r[1][3]+' '+r[1][4]
       if 'BruchAddSub' in r[2]:
           r1=[[str(y) for y in x] if isinstance(x,list) else x for x in r[1]]
           if True:
               bruch1='\\frac{'+r1[0][0]+'}{'+r1[0][1]+'}' if random.randint(1,10) > 3 else schreibeGemZahl(int(r1[0][0]),int(r1[0][1]))
               bruch2='\\frac{'+r1[2][0]+'}{'+r1[2][1]+'}' if random.randint(1,10) > 3 else schreibeGemZahl(int(r1[2][0]),int(r1[2][1]))
           else:
               bruch1='\\frac{'+r1[0][0]+'}{'+r1[0][1]+'}'
               bruch2='\\frac{'+r1[2][0]+'}{'+r1[2][1]+'}'
           random.randint(1,10)
           text='$'+bruch1+r1[1]+bruch2+'=$'
       if 'GemischteZahlzuBruch' == r[2]:
            text='Schreibe als Bruch $'+r[1][2]+'\\frac{'+r[1][3]+'}{'+r[1][4]+'}$'
       if 'BruchzuGemischteZahl' == r[2]:
            text='Schreibe als gemischte Zahl $\\frac{'+r[1][0]+'}{'+r[1][1]+'}$'
       if 'rechneLaengenEinheitenUm' == r[2] or 'rechneQuadrateEinheitenUm' == r[2]:
            text=r[1][0]
       if 'UmfangMessen' == r[2] or 'FlaecheMessen' == r[2] or 'FlaecheUmfang' == r[2]:
#            text=r[1][0]
            text=['\pbox{20cm}{Berechne den Umfang, die Fläche \\\\ und beschrifte: \\\\']+r[1][0]+['}']
       if 'ZusGesetztFl'== r[2]:
            text=['\pbox{20cm}{Berechne die Fläche und beschrifte: \\\\']+zusammengesetzteRechtecke(r[1])+['}']
       if 'ZusGesetztFlSchwer'== r[2]:
            text=['\pbox{20cm}{Berechne die Fläche und beschrifte: \\\\']+zusammengesetzteRechteckeSchwer(r[1])+['}']
#Tikz Bilder sind als Listen gespeichert
       if isinstance(text,list):
           text[0]=zeile+r[0]+' & '+text[0]
           for k in range(len(text)-1):
               tabelle.append(text[k])
           zeile=text[-1]
#Ende Tikz Bilder sind als Listen gespeichert
       else:
           zeile=zeile+r[0]+' & '+text
       if i%2>0:
           tabelle.append(zeile+'\\\\\\hline')
           zeile=''
       else:
           zeile=zeile+' & '
    tabelle.append('\\end{tabularx}')
    tabelle.append('\\vspace{0.5cm}')
    tabelle.append('')
    tabelle.append('')
    return tabelle


def erzeugeTabelle10minLoesungen(loesungen,anzSpalten=1):
    tabelle=[]
    if anzSpalten==1:
        tabelle.append('\\noindent\\begin{tabularx}{\\textwidth}{|C{1.0cm}|X|}')
    if anzSpalten==2:
        tabelle.append('\\noindent\\begin{tabularx}{\\textwidth}{|C{1.0cm}|X|C{1.0cm}|X|}')
    tabelle.append('\\arrayrulecolor{black}\\hline')
    for i in range(len(loesungen)):
#Tikz Zeichnungen werden in Tabellen gespeichert.
        if isinstance(loesungen[i][1],list):
            tabelle.append(loesungen[i][0]+'&')
            for j in range(len(loesungen[i][1][:-1])):
                tabelle.append(loesungen[i][1][j])
            print(loesungen[i][1])
            tabelle.append(loesungen[i][1][-1])
        else:
            tabelle.append(loesungen[i][0]+'&'+loesungen[i][1].replace('*',' · ').replace('/',' : '))
            for j in range(2,len(loesungen[i])):
                tabelle.append(' &'+loesungen[i][j])
        if anzSpalten==1:
            tabelle[-1]=tabelle[-1]+'\\\\'+'\\hline'
        if anzSpalten==2:
#Die Range fängt mit 0 an, deshalb hat die erste Spalte die Nummer 0: 0%2=0
            if i % 2==0:
                tabelle[-1]=tabelle[-1]+'&'
            else:
                tabelle[-1]=tabelle[-1]+'\\\\'+'\\hline'
    tabelle.append('\\end{tabularx}')
    tabelle.append('\\vspace{0.5cm}')
    tabelle.append('')
    tabelle.append('')
    return tabelle

def schreibe10minRechnungenInTabelle(rechnungen,tabellenWerte,tabellenWerteNr):
    gleichheitszeichen=[]
    startZeile=1
    for r in rechnungen:
        if '*' in r[1]:
            startZeile=erzeugeMultiplikationenStellengerecht([r],tabellenWerte,tabellenWerteNr,1,mitLoesung=True,startZeile=startZeile,rechnungenProReihe=1)
        if '/' in r[1]:
            startZeile=erzeugeDivisionStellengerecht([r],tabellenWerte,tabellenWerteNr,0,mitLoesung=True,startZeile=startZeile,rechnungenProReihe=1)
        if 'erweitern' == r[2]:
            startZeile,gleichheitszeichen=schreibeBruchErweitern(r,tabellenWerte,tabellenWerteNr,startZeile=startZeile,markers=gleichheitszeichen)
        if 'kuerzen' == r[2] or 'kuerzenMitTeiler' == r[2]:
            startZeile,gleichheitszeichen=schreibeBruchKuerzen(r,tabellenWerte,tabellenWerteNr,startZeile=startZeile,markers=gleichheitszeichen)
        if 'reihe' == r[2]:
            startZeile,gleichheitszeichen=schreibenReihenBruch(r,tabellenWerte,tabellenWerteNr,startZeile=startZeile,markers=gleichheitszeichen)
        if 'reihePosZufaellig' == r[2]:
            startZeile,gleichheitszeichen=schreibenReihenBruchBeliebig(r,tabellenWerte,tabellenWerteNr,startZeile=startZeile,markers=gleichheitszeichen)
    print('startZeile='+str(startZeile))
    for i in range(len(tabellenWerte[tabellenWerteNr])):
        for j in range(len(tabellenWerte[tabellenWerteNr][i])):
             if '*' in tabellenWerte[tabellenWerteNr][i][j]:
                 tabellenWerte[tabellenWerteNr][i][j]=tabellenWerte[tabellenWerteNr][i][j].replace('*','$\cdot$')
    return gleichheitszeichen
    


def erzeugeTabelleMitMultiplikationAufgaben(rechnungen):
#Diese Funktion erzeugt eine Tabelle der Form:
#    |a) | x*y | b)| a*b |
#    |c) | c*d | d)| v*w |
    tabelle=[]
    tabelle.append('\\noindent\\begin{tabularx}{\\textwidth}{|C{1.0cm}|X|C{1.0cm}|X|}')
    tabelle.append('\\arrayrulecolor{black}\\hline')
    for i in range(int(len(rechnungen)/2)):
       tabelle.append(rechnungen[2*i][0]+'&'+rechnungen[2*i][1].replace('*',' · ').replace('/',' : ')+'&'+rechnungen[2*i+1][0]+'&'+rechnungen[2*i+1][1].replace('*',' · ').replace('/',' : ')+'\\\\\\hline')
    tabelle.append('\\end{tabularx}')
    tabelle.append('\\vspace{0.5cm}')
    tabelle.append('')
    tabelle.append('')
    return tabelle


def erzeugeLatexTabelleMitRechnungen(werte):
    tabelle=[]
    tabelle.append('\\noindent\\resizebox*{'+str(int((len(werte[0])-1)/2))+'cm}{'+str(int(len(werte)/2))+'cm} {\\begin{tabular}{|*{'+str(len(werte[0])-1)+'}{c|}}')
    tabelle.append('\\arrayrulecolor{lightgray}\\hline')
    for line in werte:
        tabelle.append(''.join(line))
    tabelle.append('\\end{tabular}}')
    return tabelle


def erzeugeTabelleMitAufgaben(rechnungen):
#Diese Funktion erzeugt eine Tabelle der Form:
#    |a) | Aufgabe 1 | b)| Aufgabe 2 |
#    |c) | Aufgabe 3 | d)| Aufgabe 4 |
    tabelle=[]
    tabelle.append('\\noindent\\begin{tabularx}{\\textwidth}{|C{1.0cm}|X|C{1.0cm}|X|}')
    tabelle.append('\\arrayrulecolor{black}\\hline')
    for i in range(int(len(rechnungen)/2)):
       tabelle.append(rechnungen[2*i][0][0]+'&'+(' '+rechnungen[2*i][0][1]+' ').join([str(x) for x in rechnungen[2*i][1][:-1]])+'&'+rechnungen[2*i+1][0][0]+'&'+(' '+rechnungen[2*i+1][0][1]+' ').join([str(x) for x in rechnungen[2*i+1][1][:-1]])+'\\\\\\hline')
    tabelle.append('\\end{tabularx}')
    tabelle.append('\\vspace{0.5cm}')
    tabelle.append('')
    tabelle.append('')
    return tabelle

def erzeugeTabelleMitGemischtenAufgaben(rechnungen):
    tabelle=[]
    tabelle.append('\\noindent\\begin{tabularx}{\\textwidth}{|C{1.0cm}|X|C{1.0cm}|X|}')
    tabelle.append('\\arrayrulecolor{black}\\hline')
    for i in range(2):
       tabelle.append(rechnungen[2*i][0]+'&'+rechnungen[2*i][1].replace('*',' · ')+'='+'&'+rechnungen[2*i+1][0]+'&'+rechnungen[2*i+1][1].replace('*',' · ')+'='+'\\\\\\hline')
    for i in range(2,4):
       tabelle.append(rechnungen[2*i][0]+'&'+rechnungen[2*i][1].replace('*',' · ')+'&'+rechnungen[2*i+1][0]+'&'+rechnungen[2*i+1][1].replace('*',' · ')+'\\\\\\hline')
    tabelle.append('\\end{tabularx}')
    tabelle.append('\\vspace{0.5cm}')
    tabelle.append('')
    tabelle.append('')
    return tabelle


    
def erzeugeTabelleReihenRechnungen(rechnungen):
    tabelle=[]
    tabelle.append('\\noindent\\begin{tabularx}{\\textwidth}{|C{1.0cm}|X|}')
    tabelle.append('\\arrayrulecolor{black}\\hline')
    for i in range(len(rechnungen)):
        tabelle.append(rechnungen[i][0]+'&'+rechnungen[i][1]+'\\\\\\hline')
    tabelle.append('\\end{tabularx}')
    tabelle.append('\\vspace{0.5cm}')
    tabelle.append('')
    tabelle.append('')
    return tabelle

    
def erzeugeTabelleMitGemischtenAufgabenMitLoesungen(rechnungen):
    tabelle=[]
    tabelle.append('\\noindent\\begin{tabularx}{\\textwidth}{|C{1.0cm}|X|C{1.0cm}|X|}')
    tabelle.append('\\arrayrulecolor{black}\\hline')
    for i in range(int(len(rechnungen)/2)):
       tabelle.append(rechnungen[2*i][0]+'&'+rechnungen[2*i][1].replace('*',' · ')+'='+str(int(eval(rechnungen[2*i][1].replace(':','/'))))+'&'+rechnungen[2*i+1][0]+'&'+rechnungen[2*i+1][1].replace('*',' · ')+'='+str(int(eval(rechnungen[2*i+1][1].replace(':','/'))))+'\\\\\\hline')
    tabelle.append('\\end{tabularx}')
    tabelle.append('\\vspace{0.5cm}')
    tabelle.append('')
    tabelle.append('')
    return tabelle

def erzeugeTabelleMitKlammerAufgaben(rechnungen):
    tabelle=[]
    tabelle.append('\\noindent\\begin{tabularx}{\\textwidth}{|C{1.0cm}|X|C{1.0cm}|X|}')
    tabelle.append('\\arrayrulecolor{black}\\hline')
    for i in range(int(len(rechnungen)/2)):
       tabelle.append(rechnungen[2*i][0]+'&'+''.join(rechnungen[2*i][1:])+'&'+rechnungen[2*i+1][0]+'&'+''.join(rechnungen[2*i+1][1:])+'\\\\\\hline')
    tabelle.append('\\end{tabularx}')
    tabelle.append('\\vspace{0.5cm}')
    tabelle.append('')
    tabelle.append('')
    return tabelle
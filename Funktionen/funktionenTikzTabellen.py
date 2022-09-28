#!/usr/bin/env python
# coding: utf8

#Diese Datei enthält verschiedene Funktionen, die zur Erstellung einer Latex tex-Datei benötigt werden.

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())

def schreibeAufgInTabelleInKaro(tabelle,ursp=[0,0],linien=[],mitUmrandung=True):
    latexcommand=[]
    if mitUmrandung:
        latexcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')  
        latexcommand.append('\\begin{tikzpicture}[show background grid]') 
    for j,zeile in enumerate(tabelle):
        for i,inh in enumerate(zeile):
             latexcommand.append('\\node at ('+str(i*0.5+ursp[0]+0.25)+','+str(-j*0.5+ursp[1]+0.25)+') { '+str(inh)+'};') 
    latexcommand.append('\\node at ('+str(ursp[0])+','+str(-j*0.5-0.5+ursp[1]-0.25)+') {  };') 
    for l in linien:
        latexcommand.append('\\draw[line width=1pt] ('+str(l[0][0]+ursp[0])+','+str(l[0][1]+ursp[1])+') -- ('+str(l[1][0]+ursp[0])+','+str(l[1][1]+ursp[1])+');') 
    if mitUmrandung:
        latexcommand.append('\\end{tikzpicture}')    
    return latexcommand  

def tikzTabelle(tabelle=[[1,2,3,4,5,6],[2,3,4,5,6,7],[3,4,5,6,7,8]],dim=0.5,spaltenBreite=[],zeilenHoehe=[],newCBuchst='X',tabellenPos=[0,0],mitUmrandung=True):
#Diese Funktion erzeugt eine Tabelle für Tikz-Zeichnungen. Das Ziel ist es die Tabelle so zu erstellen, dass die Linien
#auf einem 0,5x0,5cm² Karokästchen liegen.
#
#      Aufruf:  tikzTabelle(tabelle=[[1,2,3,4,5,6],[2,3,4,5,6,7],[3,4,5,6,7,8]],dim=0.5,zeilenHoehe=[],spaltenBreite=[])
#
#Eingabe:   tabelle=Liste von Listen der Art: [[Zeile1],[Zeile2],...]
#               dim=0.5 Wenn Jede Zeile und Spalte 0.5 cm breite/hoch sein soll oder [1.5,0.5] wenn die Spalten 1.5 cm breit und 0.5 cm Hoch sein sollen.
#           zeilenhoehe=[0.5,0.5,1.5,1, ....] so kann man jede Zeilenhöhe individuel einstellen.
#           spaltenBreite=[0.5,0.5,1.5,1, ....] so kann man jede Spaltenbreite individuel einstellen.
#           newCBuchst=Buchstabe fuer eine LateX Variabel, um die Tabelle in einem spaeteren Latex Dokument manuell zu verschieben. Wenn man mehrer Tabelle so erzeugt, koennen
#                      die Variabeln doppelt oder dreifach vorkommen. Deshalb kann man diesen Variablennamen fuer newcommand hier anpassen.
    dimX,dimY=dim if type(dim)==int or type(dim)==float  else dim[0], dim if type(dim)==int or type(dim)==float else dim[1]
#    urspr=[0,0]
    spaltenBreite=spaltenBreite if len(spaltenBreite)>0 else [dimX]*len(tabelle[0])
    spaltenPos=[sum(spaltenBreite[:i]) for i in range(len(spaltenBreite))]
    zeilenHoehe=zeilenHoehe if len(zeilenHoehe)>0 else [-dimY]*len(tabelle)
    zeilenPos=[sum(zeilenHoehe[:i]) for i in range(len(zeilenHoehe))]
    breite,hoehe=spaltenPos[-1]+spaltenBreite[-1],zeilenPos[-1]+zeilenHoehe[-1]
    latexcommand=[]
    latexcommand.append('\\newcommand\\X'+newCBuchst+'{'+str(tabellenPos[0])+'}')
    latexcommand.append('\\newcommand\\Y'+newCBuchst+'{'+str(tabellenPos[1])+'}')
    if mitUmrandung:
        latexcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')  
        latexcommand.append('\\begin{tikzpicture}[show background grid]')  
# Das "++" vor dem zweiten Wert in rectangle ist ein Inkrement.
    latexcommand.append('\\draw[line width=1pt] (\\X'+newCBuchst+',\\Y'+newCBuchst+') rectangle ++('+str(breite)+','+str(hoehe)+');') 
    for i in range(len(tabelle)):
        latexcommand.append('\\draw[line width=1pt] (\\X'+newCBuchst+',\\Y'+newCBuchst+'+'+str(zeilenPos[i])+') -- (\\X'+newCBuchst+'+'+str(breite)+',\\Y'+newCBuchst+'+'+str(zeilenPos[i])+');') 
    for i in range(len(tabelle[0])):
        latexcommand.append('\\draw[line width=1pt] (\\X'+newCBuchst+'+'+str(spaltenPos[i])+',\\Y'+newCBuchst+') -- (\\X'+newCBuchst+'+'+str(spaltenPos[i])+',\\Y'+newCBuchst+'+'+str(hoehe)+');') 
    for j in range(len(tabelle)):
        for i in range(len(tabelle[0])):
             latexcommand.append('\\node at (\\X'+newCBuchst+'+'+str(spaltenPos[i]+spaltenBreite[i]/2)+',\\Y'+newCBuchst+'+'+str(zeilenPos[j]+zeilenHoehe[j]/2)+') { '+str(tabelle[j][i])+'};') 
    if mitUmrandung:
        latexcommand.append('\\end{tikzpicture}') 
    return latexcommand




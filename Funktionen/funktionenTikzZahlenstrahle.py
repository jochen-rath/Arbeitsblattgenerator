#!/usr/bin/env python
# coding: utf8

#Inhalt
#Diese Skript erzeugt skripte, aus denen das LaTeX Paket Tikz Zahlenstrahle erzeugen kann.

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())


def zahlenstrahlNatuerlicheZahlenSenkrechtTikz(zahlenstrahl,mitZahlen=True,Y0=0,X0=0,hoehe=-1,beginEnd=True):
#zahlenstrahl=[Haupteinteilung,Untereinteilung]
#Haupteinteilung=[[x1,wert1],[x2,wert2],...
#  x1,x2,... Werte von 0 bis 10. wert1, wert2 der Zahlenstrahlwert
#Untereinteilung=[xx1,xx2,xx3,...]
#  dx1,dx2 = Schrittweite. Normal: xx2-xx1=xx3-xx2, usw
    Haupteinteilung=zahlenstrahl[0]
    Untereinteilung=zahlenstrahl[1]
    if hoehe<0:
        hoehe=Haupteinteilung[-1][0]-Haupteinteilung[0][0]+0.5
    if beginEnd:
        tikzcommand=['\\noindent\\begin{tikzpicture}[baseline=0]']
    else:
        tikzcommand=[]
#Über dem Zahlenstrahl soll 0,5cm platz sein
#Deshalb male ich eine weiße senkrechte linie bei x=0
#    tikzcommand.append('\draw[white] ('+str(X0+0.5)+','+str(Y0)+') -- ('+str(X0-0.2)+','+str(Y0)+');')
    tikzcommand.append('\\draw[-latex] ('+str(X0)+','+str(Y0)+') -- ('+str(X0)+','+str(Y0+hoehe)+') ;')
    for y,wert in Haupteinteilung:
        wert=wert if type(wert)==str else strNW(wert)
        tikzcommand.append('\\draw[black] ('+str(X0+0.1)+','+str(y+Y0)+') -- ('+str(X0-0.1)+','+str(Y0+y)+')'+(' node[left] {$'+wert+'$} ;') if mitZahlen else (' ;'))
    for xx in Untereinteilung:
        tikzcommand.append('\\draw[black] ('+str((xx))+','+str(Y0+0.05)+') -- ('+str((xx))+','+str(Y0-0.05)+');')
    if beginEnd:
        tikzcommand.append('\\end{tikzpicture}')
        tikzcommand.append('\\newline')
    return tikzcommand

    

def zahlenstrahlNatuerlicheZahlenTikz(zahlenstrahl=[[[0,0],[1,2],[2,4],[3,6]],[]],mitZahlen=True,Y0=0,X0=0,laenge=-1,beginEnd=True):
#zahlenstrahl=[Haupteinteilung,Untereinteilung]
#Haupteinteilung=[[x1,wert1],[x2,wert2],...
#  x1,x2,... Werte von 0 bis 10. wert1, wert2 der Zahlenstrahlwert
#Untereinteilung=[xx1,xx2,xx3,...]
#  dx1,dx2 = Schrittweite. Normal: xx2-xx1=xx3-xx2, usw
    Haupteinteilung=zahlenstrahl[0]
    Untereinteilung=zahlenstrahl[1]
    if laenge<0:
        laenge=Haupteinteilung[-1][0]-Haupteinteilung[0][0]+0.5
    if beginEnd:
#        tikzcommand=['\\noindent\\begin{tikzpicture}[baseline=0]']
        tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
        tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    else:
        tikzcommand=[]
#Über dem Zahlenstrahl soll 0,5cm platz sein
#Deshalb male ich eine weiße senkrechte linie bei x=0
#    tikzcommand.append('\draw[white] ('+str(X0)+','+str(Y0+0.5)+') -- ('+str(X0)+','+str(Y0-0.2)+');')
    tikzcommand.append(F'\\draw[-latex] ({X0},{Y0}) -- ({X0+laenge},{Y0}) ;')
    for x,wert in Haupteinteilung:
        wert=wert if type(wert)==str else strNW(wert)
        tikzcommand.append('\\draw[black] ('+str(x)+','+str(Y0+0.1)+') -- ('+str(x)+','+str(Y0-0.1)+')'+(' node[below] {$'+wert+'$} ;') if mitZahlen else (' ;'))
    for xx in Untereinteilung:
        tikzcommand.append('\\draw[black] ('+str((xx))+','+str(Y0+0.05)+') -- ('+str((xx))+','+str(Y0-0.05)+');')
    if beginEnd:
        tikzcommand.append('\\end{tikzpicture}')
        tikzcommand.append('\\newline')
    return tikzcommand



def zahlenstrahlBruchDezimalzahlenTikz(zahlenstrahl,pfeile=[],laenge=10,mitLSG=False,mitBeginEnd=True):
#zahlenstrahl=[Haupteinteilung,Untereinteilung]
#Haupteinteilung=[[x1,wert1],[x2,wert2],...
#  x1,x2,... Werte von 0 bis laenge. wert1, wert2 der Zahlenstrahlwert
#Untereinteilung=[xx1,xx2,xx3,...]
#  dx1,dx2 = Schrittweite. Normal: xx2-xx1=xx3-xx2, usw
    Haupteinteilung=zahlenstrahl[0]
    Untereinteilung=zahlenstrahl[1]
    tikzcommand=['\\noindent\\begin{tikzpicture}[baseline=0]'] if mitBeginEnd else []
#Über dem Zahlenstrahl soll 0,5cm platz sein
#Deshalb male ich eine weiße senkrechte linie bei x=0
    if not mitLSG:
        tikzcommand.append('\\node at (0,1.5cm) { };')
#    tikzcommand.append('\draw[white] (0.0,0.5) -- (0.0,-0.2);')
    tikzcommand.append('\\draw[-latex] (0,0) -- ('+str(int(laenge)+0.5)+',0) ;')
    for x,wert in Haupteinteilung:
        wert=wert if type(wert)==str else strNW(wert)
        tikzcommand.append('\\draw[black] ('+str(x)+',0.1) -- ('+str(x)+',-0.1)'+(' node[below] {$'+wert+'$} ;'))
    for xx in Untereinteilung:
        tikzcommand.append('\\draw[black] ('+str(xx)+',0.05) -- ('+str(xx)+',-0.05);')
    for i,p in enumerate(pfeile):
        if mitLSG:
            tikzcommand.append('\\draw[-latex] ('+str(p[0])+','+('0.5' if i%2==0 else '0.75')+') -- ('+str(p[0])+',0.2) ;') 
            tikzcommand.append('\\draw ('+str(p[0])+(',0.35' if i%2==0 else ',0.75')+')node[above] {'+ p[1]+'} ;')
        else:
            tikzcommand.append('\\draw[-latex] ('+str(p[0])+',0.65) -- ('+str(p[0])+',0.2) ;') 
            tikzcommand.append('\\draw ('+str(p[0])+',0.4)node[above] {'+ (p[1] if mitLSG else ' ') +'} ;')
    if mitBeginEnd:
        tikzcommand.append('\\end{tikzpicture}')
        tikzcommand.append('\\newline')
    return tikzcommand


def zahlenstrahlBestimmeMitte(start=6,schrittweite=12,laenge=5,mitLsg=False,mitSchritt=False):
#Diese Funktion erzeugt einen Zahlenstrahl, bei dem die Mitte von zwei Zahlen gesucht ist.
#Man muss die mittlere Zahl bestimmen, indem die Schrittweite erkannt und dann halbiert werden muss.
#Aufruf:
#       tikzcommand=zahlenstrahlBestimmeMitte(start=6,schrittweite=12,laenge=5,mitLsg=False,mitSchritt=False)
#
#   start, schrittweite klar.
#   laenge = Wie lang der Zahlenstrahl sein soll.
#   mitLsg = Gib die Loesung aus.
#   mitSchritt = Gib die Schrittweite, aber keine Loesung aus.
    tikzcommand=['\\noindent\\begin{tikzpicture}[baseline=0]']
    tikzcommand.append('\\node at (0,1.5cm) { };')
    tikzcommand.append(F'\\draw[-latex] (0,0) -- ({laenge},0) ;')
    tikzcommand.append(F'\\draw[black] (0.5,0.1) -- (0.5,-0.1) node[below] {{${strNW(start)}$}} ;')
    tikzcommand.append(F'\\draw[black] ({laenge-0.5},0.1) -- ({laenge-0.5},-0.1) node[below] {{${strNW(start+schrittweite)}$}} ;')
    tikzcommand.append(F'\\draw[black] ({laenge/2},0.05) -- ({laenge/2},-0.05) node[below] {{${strNW(start+schrittweite/2) if mitLsg else ""}$}} ;')
    tikzcommand.append(F'\\node[] (1) at ({0.5},0.11) {{}};')
    tikzcommand.append(F'\\node[] (2) at ({laenge/2},0.06) {{}};')
    tikzcommand.append(F'\\node[] (3) at ({laenge-0.5},0.11) {{}};')
    tikzcommand.append(F'\draw [->] (1) to [out=60,in=120] node[above] {{$+{strNW(schrittweite/2) if (mitLsg or mitSchritt) else ""}$}}  (2) ;')
    tikzcommand.append(F'\draw [->] (1) to [out=90,in=90] node[above] {{$+{strNW(schrittweite) if (mitLsg or mitSchritt) else ""}$}}  (3) ;')
    tikzcommand.append('\\end{tikzpicture}')
    tikzcommand.append('\\newline')
    return tikzcommand

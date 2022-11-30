#!/usr/bin/env python
# coding: utf8
#	exec(open("Aufrufe/Skalen/erzeuge0bis100GradCelsiusSkalen.py").read())
import random

exec(open("Funktionen/funktionen.py").read())

def main():
#Setze Variablen:
    title='Erzeuge 0  $^\circ$C bis 100  $^\circ$C Skalen und bestimme die Temperatur'
    anfang='{\\bf Aufgabe:}'
    anfang=anfang+' \\begin{itemize}'
    anfang=anfang+'\\item Beschrifte die Stützpunkte'
    anfang=anfang+'\\item Zeichne alle 10 $^\\circ$C Schritte einen Strich '
    anfang=anfang+'\\item Beschrifte die Striche '
    anfang=anfang+'\\item Bestimme die Temperatur '
    anfang=anfang+'\\end{itemize}'
    lsgText='Loesungen '+title
    dateiName='01_SkalenErzeugen'
    datum='\\rule{4cm}{0.15mm}'    #Wird kein Datum angeben, wird das morgige Datum genommen.
#    parameter=[[1,1,28],[2,1,76],[3,0.5,40],[5,0.5,75],[3,0.6,36],[5,0.7,10],[4,0.8,87],[3,0.6,43]]
    parameter=[[1,1,43]]
#    parameter=[[random.randint(1,3),random.randint(4,10)/10,random.randint(5,95)] for i in range(8)]
#    parameter=[[random.randint(1,3),random.choice([0.5,1.0]),random.randint(5,95)] for i in range(4)]
#    parameter=[[random.randint(1,3),[1.0,1.0,0.5,0.5][i],random.randint(5,95)] for i in range(4)]
    hintergrund=False
#    parameter=[[1,1,30],[2,1,80],[1.5,0.5,40],[5,0.5,90],[2,1,35],[3,0.5,85],[4,0.5,15],[3,1,47]]
    erzeugeArbeitsblatt(title,lsgText,dateiName,datum,anfang,parameter,hintergrund)

def erzeugeArbeitsblatt(title,lsgText,dateiName,datum,anfang,parameter,hintergrund):
    ausgabeName='newFile'
    dateiName,datum=filename(dateiName,datum=datum)
    kopfzeile='Datum: '+datum
#Erzeuge Aufgaben:
#if True:
    tabAfg,tabLsg,para=erzeugeTemperaturskalen(parameter=parameter,mitHintergrund=hintergrund)
    head=latexHead(arraystretch=True)
    begin=beginDoc(kopf=kopfzeile,title=title,anfang=anfang)
    os.chdir('Ausgabe')
    writeLatexDoc(head+begin+tabAfg+seitenwechsel(kopfzeile,lsgText)+tabLsg+['\\end{document}'],ausgabeName+'.tex')
    os.system('xelatex '+ausgabeName+'.tex')
    os.rename(ausgabeName+'.pdf',dateiName+'.pdf')
    [os.remove(file) for file in os.listdir() if ausgabeName in file]
    os.chdir('..')



if __name__ == '__main__':
    main()
#!/usr/bin/env python
# coding: utf8
#	exec(open("Aufrufe/Dezimalzahlen/erzeugeDezimalzahlenAddierenSubtrahieren.py").read())
exec(open("Funktionen/funktionen.py").read())

def main():
#Setze Variablen:
    title='Addieren und Subtrahieren von Dezimalzahlen'
    einfach=False
    if einfach:
        anfang='Berechne so:\\\\ $0,5+0,3=\square \\rightarrow 5+3=8 \\rightarrow 0,5+0,3=0,8$\\\\'
        anfang=anfang+'$3,5+1,7=\square \\rightarrow 35+17=52 \\rightarrow 3,5+1,7=5,2$\\\\'
        anfang=anfang+'$3,4-1,6=\square \\rightarrow 34-16=18 \\rightarrow 3,4-1,6=1,8$\\\\'
    else:
        anfang=''
    lsgText='Loesungen '+title
    dateiName='02_AddSubVonDezimalzahlen'
    datum='27.01.2021'    #Wird kein Datum angeben, wird das morgige Datum genommen.
    if einfach:
        auswahl=[[1,'+',4], [1,'-',4], [1,random.choice(['+','-']),4], [1,random.choice(['+','-']),4]]           #[Kommastellen,Anzahl]
    else:
        auswahl=[[2,'+',2], [2,'-',2],[3,'+',2], [3,'-',2]]           #[Kommastellen,Anzahl]
    erzeugeArbeitsblatt(title,lsgText,dateiName,datum,anfang,auswahl)

def erzeugeArbeitsblatt(title,lsgText,dateiName,datum,anfang,auswahl):
    ausgabeName='newFile'
    dateiName,datum=filename(dateiName,datum=datum)
    kopfzeile='Datum: '+datum
#Erzeuge Aufgaben:
#if True:
    afg=[]
    lsg=[]
    for i,a in enumerate(auswahl):
        a,l,d=deziZahlenAddierenSubtrahieren(a[0],a[1],a[2],True)
        afg.append([buchstabenKlein[i]+')',a])
        lsg.append([buchstabenKlein[i]+')',l])
    tabAfg=erzeugeEinfacheTabelle(afg,2)
    tabLsg=erzeugeEinfacheTabelle(lsg,2)
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
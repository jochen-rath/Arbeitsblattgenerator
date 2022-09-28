#!/usr/bin/env python
# coding: utf8
#	exec(open("Aufrufe/Dezimalzahlen/erzeugeDezimalzahlenSchriftlichAddierenSubtrahieren.py").read())
exec(open("Funktionen/funktionen.py").read())

def main():
#Setze Variablen:
    title='Schriftliches Addieren und Subtrahieren von Dezimalzahlen'
    einfach=False
    anfang='Löse folgende Additions- und Subtraktionsaufgaben in dem Du die Aufgaben stellengerecht untereinander'
    anfang=anfang+'aufschreibst und berechnest.'
    lsgText='Loesungen '+title
    dateiName='02_SchritAddSubVonDezimalzahlen'
    datum='29.01.2021'    #Wird kein Datum angeben, wird das morgige Datum genommen.
    auswahl=[[3,2,'+'], [3,2,'-'],[4,3,'+'], [4,3,'-'],[3,4,'+'], [3,4,'-'],[4,5,'+'], [4,5,'-']]           #[Kommastellen,AnzahlSummanden]
    erzeugeArbeitsblatt(title,lsgText,dateiName,datum,anfang,auswahl)

def erzeugeArbeitsblatt(title,lsgText,dateiName,datum,anfang,auswahl):
    ausgabeName='newFile'
    dateiName,datum=filename(dateiName,datum=datum)
    kopfzeile='Datum: '+datum
#Erzeuge Aufgaben:
#if True:
    afg=[]
    lsg=[]
    fc=[]
    fcLsg=[]
    for i,a in enumerate(auswahl):
        a,l,f,fL=deziZahlenSchriftAddierenSubtrahieren(a[0],a[1],a[2],False,name=ausgabeName+'_tab_'+buchstabenKlein[i],ohneText=True)
        afg.append([buchstabenKlein[i]+')',a])
        lsg.append([buchstabenKlein[i]+')',l])
        fc.append(f)
        fcLsg.append(fL)
    tabAfg=erzeugeEinfacheTabelle(afg,1)
    tabLsg=erzeugeEinfacheTabelle(lsg,1)
    tabLsgVollst=schreibeMehrereTabellenInEinTikz(fcLsg,anzNebeneinander=3)
    leer=leererKaroBereich(x=16.7,y=15)
#Achtung: Wenn Arraystretch verwendet wird, werden die Zahlen in den Tabellen in Tikz sehr klein.
    head=latexHead(arraystretch=False)
    begin=beginDoc(kopf=kopfzeile,title=title,anfang=anfang)
    filecontent=[]
    for f in fc:
        filecontent=filecontent+f[0]
    for f in fcLsg:
        filecontent=filecontent+f[0]
    writeLatexDoc(filecontent+head+begin+tabAfg+leer+seitenwechsel(kopfzeile,lsgText)+tabLsg+tabLsgVollst+['\\end{document}'],os.path.join('Ausgabe',ausgabeName+'.tex'))
    os.chdir('Ausgabe')
    os.system('xelatex '+ausgabeName+'.tex')
    os.rename(ausgabeName+'.pdf',dateiName+'.pdf')
    [os.remove(file) for file in os.listdir() if ausgabeName in file]
    os.chdir('..')



if __name__ == '__main__':
    main()
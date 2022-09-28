#!/usr/bin/env python
# coding: utf8
#	exec(open("Aufrufe/KoerperUndFlaechen/AB_QuaderMitLochMessenAusrechnen.py").read())

exec(open("Funktionen/funktionen.py").read())
def main():
#Setze Variablen:
    title='Quader mit Loch'
    lsgText='Loesungen '+title
    dateiName='quaderMitLoch'
    datum=''    #Wird kein Datum angeben, wird das morgige Datum genommen.
    anfang='Miss die Seitenlängen des Quaders und den Radius des Lochs. Übertrage die Werte in die Zeichnung. Berechne anschließend das Volumen und die Oberfläche das Quaders mit einem Loch.'
    erzeugeArbeitsblatt(title,lsgText,dateiName,datum,anfang)

def erzeugeArbeitsblatt(title,lsgText,dateiName,datum,anfang):
    ausgabeName='newFile'
    dateiName,datum=filename(dateiName,datum=datum)
    kopfzeile='Datum: '+datum
#Erzeuge Aufgaben:
#if True:
    a,l,d=erzeugeQuaderMitLochBerech(breitePbox=17,einheit='cm',werte=[7,1.2,4,1],namen=['a=','b=','c=','R='])
    head=latexHead(arraystretch=True)
    begin=beginDoc(kopf=kopfzeile,title=title,anfang=anfang)
    os.chdir('Ausgabe')
    writeLatexDoc(head+begin+a+['\\\\']+leererKaroBereich(x=17,y=16)+['\\\\']+leererKaroBereich(x=17,y=25)+seitenwechsel(kopfzeile,lsgText)+l+['\\end{document}'],ausgabeName+'.tex')
    os.system('xelatex '+ausgabeName+'.tex')
    os.rename(ausgabeName+'.pdf',dateiName+'.pdf')
    [os.remove(file) for file in os.listdir() if ausgabeName in file]
    os.chdir('..')



if __name__ == '__main__':
    main()
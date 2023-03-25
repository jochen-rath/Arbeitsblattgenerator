#!/usr/bin/env python
# coding: utf8
import os.path


#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())

def findeListenKeyVonEintrag(auswahl=['addSubSchriftSchwer','deziDivi3Stellen','addSubSchriftSchwer']):
    liste=MoeglicheRechnungen(gebeListeZurueck=True)
    auswahlThemen=[]
    for calc in auswahl:
        for key in liste.keys():
            if calc in [x[0] for x in liste[key]]:
                auswahlThemen.append([calc,[x[1] for x in liste[key] if x[0]==calc][0],key])
    return auswahlThemen

def sortiereRechnungenInDictionaryNachThemen(auswahl=['addSubSchriftSchwer','deziDivi3Stellen','addSubSchriftSchwer']):
    auswahlDetails=findeListenKeyVonEintrag(auswahl)
    themen=list(set([x[2] for x in auswahlDetails]))
    unterthemen=list(set([x[1] for x in auswahlDetails]))
    rechnungenSortiert={}
    for thema in themen:
        untersortierung={}
        for unterthema in unterthemen:
            rechnungen=[]
            for calc in auswahlDetails:
                if calc[2]==thema and calc[1]==unterthema:
                    rechnungen.append(calc[0])
            if len(rechnungen)>0:
                untersortierung[unterthema]=rechnungen
        if len(untersortierung)>0:
            rechnungenSortiert[thema]=untersortierung
    return rechnungenSortiert

def erzeugeArbeit(auswahl,title,dateiName,datum,anfang):
    mitText=True
    aufgaben=sortiereRechnungenInDictionaryNachThemen(auswahl)
    dateiName,datum=filename(dateiName,datum=(datetime.date.today() + datetime.timedelta(days=1)).strftime("%d.%m.%Y") if datum=="KeinDatum" else datum)
#Erzeuge Arbeitsaufgaben
    lsg=[]
    punkte=[]
    for i,key in enumerate(aufgaben.keys()):
        aufgabenLatex=[]
        aufgabenLatex.append(F'\\section{{{key}}}')
        p=0
        for key2 in aufgaben[key]:
            afg=[]
            if len(aufgaben[key])>0:
                aufgabenLatex.append(F'\\subsection{{{key2}}}')
            for j,aus in enumerate(aufgaben[key][key2]):
                a,l,d=erzeuge10minRechnung(aus,mitText)
                if isinstance(a,list):
                    a='\n'.join(a)
                if isinstance(l,list):
                    l='\n'.join(l)
                afg.append([buchstabenKlein[j]+')',a])
                lsg.append([buchstabenKlein[j]+')',l])
            aufgabenLatex=aufgabenLatex+erzeugeEinfacheTabelle(afg,1)
            p=p+len(afg)
        aufgabenLatex.append(F'\\begin{{flushright}}')
        aufgabenLatex.append(F'\\underline{{\\hspace{{2cm}}/ \\pkteAfg{zahlenWoerter[i+1]} Punkte}}')
        aufgabenLatex.append(F'\\end{{flushright}}')
        with open(os.path.join('Ausgabe',F'{dateiName}_{i+1:02d}_Aufgabe{i:02d}.tex'), 'w') as f:
            f.write('\n'.join(aufgabenLatex))
        punkte.append(p)
    with open(os.path.join('Ausgabe', F'{dateiName}_01_Kopfseite.tex'), 'w') as f:
        f.write('\n'.join(schreibeArbeitKopfseite(fach='Mathematik', title=title, jahr='2022/2023',datum=datum,punkte=punkte)))
    tabLsg=erzeugeEinfacheTabelleMitSeitenumbruch(lsg,1)
    erzeugeEinfachesLatexdokument(tabLsg, size=2, file=F'{dateiName}_lsg.tex')
    arbeit=erzeugeArbeitLatex(dateiName,punkte=punkte)
    head=latexHead(arraystretch=True)
    writeLatexDoc(head+['\\begin{document}']+arbeit+['\\end{document}'], os.path.join('Ausgabe', dateiName+'.tex'))
    os.chdir('Ausgabe')
    os.system('xelatex '+dateiName+'.tex')
    for endung in ['aux','log','out']:
        os.remove(dateiName+'.'+endung)
        os.remove(F'{dateiName}_lsg.{endung}')
    os.system(F'zip {dateiName}.zip {dateiName}* ')
    os.chdir('..')
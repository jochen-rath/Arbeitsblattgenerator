#!/usr/bin/env python
# coding: utf8

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())


def erzeugeMultiplikationen(maxStellenFaktorZwei=2,ohneUebertrag=False,normal=False,schwer=False):
    #
    #Erzeuge Rechnungen
    calc=str(random.randint(101,999))+'*'+str(random.randint(2,10**maxStellenFaktorZwei))
    if ohneUebertrag and not schwer:
        while int(bestimmeUebertragVomProdukt(calc.split('*')[0],calc.split('*')[1])) > 0:
            calc=str(random.randint(100,1000))+'*'+str(random.randint(2,10**maxStellenFaktorZwei))
    if normal:
        calc=str(random.randint(101,999))+'*'+str(random.randint(10,100))
    if schwer:
        calc=str(random.randint(1001,9999))+'*'+str(random.randint(10,1000))
    afg='$'+calc.replace('*','\\cdot')+'$'
    lsg=schreibeMultiplikationenStellengerecht(calc,mitLsg=True)
    return [afg,lsg,calc]
    
def erzeugeDivision(zweiStellig=False,mitRest=False,ersteZifferDividierbar=False,nurSubtraktion=False, nurMultiplikation=False, nurErgebnisEintragen=False, nurRunterZiehen=False,nurLinien=False,trageRestEin=False):
    #
    #Erzeuge Rechnungen
    etwasTrue=True if (nurSubtraktion or nurMultiplikation or nurErgebnisEintragen or nurRunterZiehen or nurLinien or trageRestEin) else False
    if not ersteZifferDividierbar:   
        quotient=random.randint(11,999)
        divisor=random.randint(11 if zweiStellig else 2, 15 if zweiStellig else 9)
    else:
        ersteZifferKlDiv=True
        while ersteZifferKlDiv:
            quotient=random.randint(11,999)
            divisor=random.randint(11 if zweiStellig else 2, 15 if zweiStellig else 9)
            dividend=str(divisor*quotient)
            if int(dividend[0])>divisor:
                ersteZifferKlDiv=False
    calc=str(quotient*divisor)+'/'+str(divisor) if not (mitRest or trageRestEin) else str(random.randint(11,999))+'/'+str(random.randint(2,10-1))  
    afg=calc.replace('/',':') if not etwasTrue else erzeugeDivisionStellengerecht(calc, nurSubtraktion=nurSubtraktion, nurMultiplikation=nurMultiplikation, nurErgebnisEintragen=nurErgebnisEintragen, nurRunterZiehen=nurRunterZiehen,nurLinien=nurLinien,trageRestEin=trageRestEin)
    lsg=erzeugeDivisionStellengerecht(calc,mitLoesung=True)
    return [afg, lsg , calc]
    

def bestimmeUebertragVomProdukt(zahl,faktor):
#Trenne den Uebertrag vom Produkt
#   zahl und faktor sind Strings.
#    bestimmeUebertragVomProdukt(str(zahl),str(faktor))
    faktor=int(faktor)
    uebertrag='0'                #Produkt ohne Uebertrag
    for k in zahl[::-1]:
        erg=str(int(k)*faktor+int(uebertrag[-1]))
        uebertrag=uebertrag+('0' if len(erg)==1 else erg[0])
    uebertrag=uebertrag[1:]
    return uebertrag[::-1]

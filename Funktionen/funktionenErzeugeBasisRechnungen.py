#!/usr/bin/env python
# coding: utf8

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())


def erzeugeKopfrechenAufgabe():
    operator=random.choice(['+','-','*','/'])
    if operator=='+':
       calc=str(random.randint(1,99))+' + '+str(random.randint(1,99))
       erg=eval(calc)
    if operator=='-':
       differenz=random.randint(1,50)
       subtrahend=random.randint(1,50)
       calc=str(differenz+subtrahend)+' - '+str(subtrahend)
       erg=differenz
    if operator=='*':
       calc=str(random.randint(1,20))+' * '+str(random.randint(1,10))
       erg=eval(calc)
       calc=calc.replace('*','·')
    if operator=='/':
       quotient=random.randint(1,20)
       divisor=random.randint(1,10)
       calc=str(quotient*divisor)+' : '+str(divisor)
       erg=quotient
    return [calc+' = ',calc+' = '+strNW(erg),erg]

def erzeugePlusMinusMalGeteiltAufgabe():
    operator=random.choice(['+','-','*','/'])
    if operator=='+':
       calc=str(random.randint(int(1),int(1000)))+' + '+str(random.randint(int(1),int(1000)))
       erg=eval(calc)
    if operator=='-':
       differenz=random.randint(int(1),int(1e3))
       subtrahend=random.randint(int(1),int(1e3))
       calc=str(differenz+subtrahend)+' - '+str(subtrahend)
       erg=differenz
    if operator=='*':
       calc=str(random.randint(int(1),int(1e3)))+' * '+str(random.randint(int(1),int(1e2)))
       erg=eval(calc)
       calc=calc.replace('*','·')
    if operator=='/':
       quotient=random.randint(int(1),int(50))
       divisor=random.randint(int(1),int(10))
       calc=str(quotient*divisor)+' : '+str(divisor)
       erg=quotient
    return [calc+' = ',calc+' = '+strNW(erg),erg]


def erzeugeGemischteRechnungDifferenziert(rechnungen):
#8 rechnungen: 4 Kopfrechnungen, und je 1 schrift. Add, Subtr, Multi und Division
    rechnungen=[]
    rechnungen.append(['',str(random.randint(1,99))+' + '+str(random.randint(1,20))])
    differenz=random.randint(1,20)
    subtrahend=random.randint(1,20)
    rechnungen.append(['',str(differenz+subtrahend)+' - '+str(subtrahend)])
    rechnungen.append(['',str(random.randint(1,12))+' * '+str(random.randint(1,10))])
    quotient=random.randint(1,12)
    divisor=random.randint(1,10)
    rechnungen.append(['',str(quotient*divisor)+' : '+str(divisor)])
    rechnungen.append(['',str(random.randint(101,999))+' + '+str(random.randint(10,199))])
    differenz=random.randint(10,700)
    subtrahend=random.randint(10,200)
    rechnungen.append(['',str(differenz+subtrahend)+' - '+str(subtrahend)])
    rechnungen.append(erzeugeMultiplikationenDifferenziert(1)[0])
    rechnungen.append(erzeugeDivision(1)[0])
    for i in range(len(rechnungen)):
        rechnungen[i][0]=buchstaben[26+i]+')'
    return rechnungen

def erzeugeGemischteRechnung():
#8 rechnungen: 4 Kopfrechnungen, und je 1 schrift. Add, Subtr, Multi und Division
    rechnungen=[]
    rechnungen.append(['',str(random.randint(1,99))+' + '+str(random.randint(1,20))])
    differenz=random.randint(1,20)
    subtrahend=random.randint(1,20)
    rechnungen.append(['',str(differenz+subtrahend)+' - '+str(subtrahend)])
    rechnungen.append(['',str(random.randint(1,20))+' * '+str(random.randint(1,10))])
    quotient=random.randint(1,20)
    divisor=random.randint(1,10)
    rechnungen.append(['',str(quotient*divisor)+' : '+str(divisor)])
    rechnungen.append(['',str(random.randint(101,999))+' + '+str(random.randint(10,199))])
    differenz=random.randint(10,700)
    subtrahend=random.randint(10,200)
    rechnungen.append(['',str(differenz+subtrahend)+' - '+str(subtrahend)])
    rechnungen.append(erzeugeMultiplikationen(1,normal=True)[0])
    rechnungen.append(erzeugeDivision(1)[0])
    for i in range(len(rechnungen)):
        rechnungen[i][0]=buchstaben[26+i]+')'
    return rechnungen


def erzeugeGroßeZahlenAddierenSubtrahieren(op='+'):
    z1=random.randint(21,75)
    z2=random.randint(1,z1)
    multi=eval(f'1e{random.randint(1,4)}')
    modi=0 if random.randint(1,4)<4 else random.randint(1,5)
    z1,z2=int(z1*multi)+modi , eval(F'{int(z2*multi)}{"-" if op=="+" else "+"}{modi}')
    afg=F'{strNW(z1)}+{strNW(z2)}=' if op=='+' else F'{strNW(z1)}-{strNW(z2)}'
    lsg=F'{strNW(z1)}+{strNW(z2)}={strNW(z1+z2)}' if op=='+' else F'{strNW(z1)}-{strNW(z2)}={strNW(z1-z2)}'
    return [afg,lsg,[]]



def erzeugeGroßeZahlenMultiplizierenDividieren(op='*'):
    z1=random.randint(1,12)
    z2=random.randint(1,10)
    fak1=random.randint(2,4)
    fak2=random.randint(1,fak1)
    multi,multi2=eval(f'1e{fak1}'),eval(f'1e{fak2}')
    z1,z2=int(z1*multi) if op=='*' else int(z1*z2*multi), int(z2*multi2)
    afg=F'{strNW(z1)} · {strNW(z2)}=' if op=='*' else F'{strNW(z1)} : {strNW(z2)}'
    lsg=F'{strNW(z1)} · {strNW(z2)}={strNW(z1*z2)}' if op=='*' else F'{strNW(z1)}:{strNW(z2)}={strNW(z1/z2)}'
    return [afg,lsg,[]]
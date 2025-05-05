#!/usr/bin/env python
# coding: utf8

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())



def erzeugeSchrAdditionsSubtraktionsRechnung(differenzierung=0,operator='+',breitePbox=5):
    #
    #Erzeuge Rechnungen
	#	0=Schwacher Schüler
	#	1=Normaler Schüler
	#	2=Starker Schüler
    #Ausgabe:  r= r=[[['a)', '-', '-'], [403, 251, 152]], [['b)', '+', '+'], [184, 262, 446]], ...
    if differenzierung==0:
        anzSummanend=1
        summe=np.random.randint(1e2,1e3)
    if differenzierung==1:
        anzSummanend=np.random.randint(1,3)
        summe=np.random.randint(1e2,3e3)
    if differenzierung==2:
        anzSummanend=np.random.randint(1,4)
        summe=np.random.randint(1e2,1e4)
    calc=[None]* (anzSummanend+2)
    for j in range(anzSummanend):
        calc[j]=np.random.randint(0,summe-sum(calc[:j]))
    calc[-2]=summe-sum(calc[:-2])
    calc[-1]=summe
    if operator=='-':
        calc=calc[::-1]
    calc=[['']+[operator]*(len(calc)-2)+[''],calc]
    afg=str(calc[1][0])+operator+operator.join([str(x) for x in calc[1][1:-1]])
    if differenzierung==0:
        afg='\\pbox{'+str(breitePbox)+'cm}{'+afg+': \\\\' +'\n'.join(schreibeRechnungStellengerecht(calc,mitLoesung=False))+'}'
    lsg=schreibeRechnungStellengerecht(calc,mitLoesung=True)
    return [afg,lsg,calc]
    
def erzeugeKlammerrechnungen(grenzen=[1e2,3e3]):
    anSummanden=np.random.randint(1,3)
    klammerpos=np.random.randint(0,anSummanden+1)
    calc=['-1']
    while eval(''.join(calc))<1:
        calc=[str(x) for x in np.random.randint(grenzen[0],grenzen[1],anSummanden+1)]
        calc.insert(1,random.choice(['+','-']))
        if anSummanden>1:
            calc.insert(3,random.choice(['+','-']))
    klErg=calc[klammerpos*2]
    calc.insert(klammerpos*2,'(')
    calc.insert(klammerpos*2+2,')')
    S1=np.random.randint(grenzen[0],grenzen[1])
    S2=S1-int(klErg)
    calc[klammerpos*2+2:1]=[str(S1),'+' if S2<0 else '-' ,str(abs(S2))]
    del calc[klammerpos*2+1]
    return calc
    
def klarmmerRechnungen():
    term="a*(b+c)+d"
    a={'Ohne':1, 'einfach':random.randint(2,10),'dezi':random.randint(1,10)/10,'bruch':f'{random.randint(1,10)}/{random.randint(2,10)}'}
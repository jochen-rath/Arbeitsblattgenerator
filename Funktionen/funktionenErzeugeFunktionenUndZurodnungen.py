#!/usr/bin/env python
# coding: utf8

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())
import random


def erzeugeUmfangsFunktion(typ='Dreieck',mitText=True):
    if typ=='Rechteck':
        x = [random.randint(20, 50) / 10 for i in range(2)]
        x=x+x
        skizze=rechteckTikz(x[0]/2,x[1]/2,beschrSeiten=True,texta=F'{strNW(x[0])}e',textb=F'{strNW(x[1])}e')
    elif typ=='Dreieck':
        x = [random.randint(20, 50) / 10 for i in range(3)]
        skizze=dreieckSeitenvorgabe(werte=[y/2 for y in x],seiten=[F'{strNW(y,True)}e' for y in x])
    else:
        return ['error','error','']
    afg=(['Gib die Umfangsformel an für'] if mitText else [])+skizze
    lsg = ['\\pbox{5cm}{']
    lsg=lsg+['$\\begin{aligned}']
    lsg=lsg+[F'U&={"+".join([F"{strNW(y)}e" for y in x])}\\\\']
    lsg=lsg+[F'U&=({"+".join([strNW(y) for y in x])})e\\\\']
    lsg=lsg+[F'U&={strNW(eval("+".join([str(y) for y in x])))}e\\\\']
    lsg=lsg+['\\end{aligned}$']
    lsg=lsg+['}']
    return [afg,lsg,[]]


def erzeugeLineareFunktion(art='linear',steigung='bruch',maxM=5):
#Diese Funktion erzeugt eine lineare Funktion. 
    m=random.randint(1,maxM)
    if steigung=='bruch':
        m=[random.randint(1,2*maxM),random.randint(1,maxM)]
        while ((m[0]/m[1]>maxM) or (m[0]==m[1]) or (m[0]/m[1]<0.2)):
            m=[random.randint(1,5),random.randint(1,5)]
            print('m='+str(m))
    if steigung=='dezi':
        m=random.randint(1,maxM*10)*0.1
    b=0
    if art=='linear':
        b=random.choice([-1,1])*random.randint(1,5)
    return [m,b]

def minMaxY(term,variabel,x):
#Diese Funktion sucht den minimalen und Maximalen y Werte, zwischen -x und x.
#Achtung, noch basierend auf einer linearen Funktion.
#
#     [minY,maxY]=minMaxY(term,variabel,x)
    minY=math.floor(evalFunc(term,variabel,-x))
    maxY=math.ceil(evalFunc(term,variabel,x))
    if minY>maxY:
        temp=maxY
        maxY=minY
        minY=temp
    return [minY,maxY]

def evalFunc(term,variabel='x',x=0):
#Diese Funktion berechnet den Wert aus einem Stringterm, wenn man die Variabel und x vorgibt.
#
#       Bsp: y=x*4+3 --> x=2 --> y=11
#
#       y=evalFunc(term,variabel='x',x=0)
    return float(sympy.simplify(term).subs(sympy.symbols(variabel),x))

def erzeugeAfgLineareFunktionZeichnen(art='linear',steigung='bruch',achsenlaenge=10,maxX=5,maxM=None,minX=None,mitText=True):
    if not minX:
        minX=-maxX
    [m,b]=erzeugeLineareFunktion(art=art,steigung=steigung,maxM=(maxX if maxM==None else maxM))
    afg=['$y='+(frac(m[0],m[1]) if type(m)==list else ('' if m==1 else strNW(m)))+'x'+('' if b==0 else ('+' if b>0 else '-')+strNW(abs(b)))+'$']
    if mitText:
        afg=['Zeichne die Funktion '+afg[0]+' und das Steigungsdreieck in ein Koordinatensystem.']
    term=(str(m[0]/m[1]) if type(m)==list else str(m))+'*x+'+str(b)
    termText=(frac(m[0],m[1]) if type(m)==list else strNW(m))+'\\cdot x'+((('+'+str(b)) if b>0 else str(b)) if not (b ==0) else '')
    yAchsenSettings=setzeAchsenEinteilungLaenge(minMaxY(term,'x',maxX)+[achsenlaenge*1.5])[1:-1]
    xStei=(m[1] if type(m)==list else 1)
    yStei=(evalFunc(term,x=xStei)-evalFunc(term,x=0))
    beschreibung=[[maxX,evalFunc(term,variabel='x',x=maxX),'$y='+termText+'$','left'],[xStei/2,evalFunc(term,variabel='x',x=0),strNW(xStei),'above','red'],[xStei,yStei/2+b,strNW(yStei),'right','red']]
    streckenzug=[[0,evalFunc(term,x=0)],[m[1] if type(m)==list else 1,evalFunc(term,x=0)],[m[1] if type(m)==list else 1,evalFunc(term,x=m[1] if type(m)==list else 1)],[0,evalFunc(term,x=0)]]
    lsg=diagrammTikzVorgBreiteHoehe(zuPlotten=[[term,'black']],streckenzug=streckenzug,textNode=beschreibung,xAchse=[minX,maxX,achsenlaenge],yAchse=list(yAchsenSettings)+[achsenlaenge*1.5])
    werte=[m,b]
    return [afg,lsg,werte]

def erzeugeAfgLineareFktErkennen(art='linear',steigung='bruch',achsenlaenge=10,maxX=3,maxM=5,breitePbox=6,mitText=True):
    m=[1000,1000]
    if steigung=='bruch':
        nichtPassend=True
        while nichtPassend:
            nichtPassend=False
            [m,b]=erzeugeLineareFunktion(art=art,steigung=steigung,maxM=(maxX if maxM==None else maxM))            
            if m[1]>maxX or m[0]/m[1]>1.5:
                nichtPassend=True
    else:
        [m, b] = erzeugeLineareFunktion(art=art, steigung=steigung, maxM=(maxX if maxM == None else maxM))
    term=(str(m[0]/m[1]) if type(m)==list else str(m))+'*x+'+str(b)
    yAchsenSettings=setzeAchsenEinteilungLaenge(minMaxY(term,'x',maxX)+[achsenlaenge*1.5])[1:-1]
    afg=['\\pbox{'+str(breitePbox)+'cm}{Gib die Funktionsgleichung an: \\\\'] if mitText else []
    afg=afg+diagrammTikzVorgBreiteHoehe(zuPlotten=[[term,'black']],xAchse=[-maxX,maxX,achsenlaenge],yAchse=list(yAchsenSettings)+[achsenlaenge])+(['}']  if mitText else [])
    termText=(frac(m[0],m[1]) if type(m)==list else strNW(m))+'\\cdot x'+((('+'+str(b)) if b>0 else str(b)) if not (b ==0) else '')
    lsg=['$y='+termText+'$']
    werte=[m,b]
    return [afg,lsg,werte]

def erzeugeAfgLinearFktWertetabelle(variabel='x',wertTab=3,achsenlaenge=10):
#Diese Funktion erzeugt eine Aufgabe, in der die Schüler aus einer linearen Funktion eine Wertetabelle erstellen sollen, welche dann in ein Diagramm übertragen werden soll.
#
#Aufruf:
#          [afg,lsg,werte]=erzeugeAfgLineareFunktionenWertetabelle(variabel='x',wertTab=3,achsenlaenge=10)
#
#            variabel: Name der Variabel
#             wertTab: Von wo nach wo gehen die Werte der Wertetabelle, von -wertTab nach +wertTab
#        achsenlaenge: Angabe in cm, wie lange eine Achse maximal sein soll. Sie wird je nach resultierenden Tick eventuell kürzer sein.
    term=variabel+'+'+variabel
    while not term.count(variabel)==1:
        term=erzeugeTerm(variablen=variabel,anzahl=2,variMaxAnzProUnterterm=2,maxMulti=5,mitKommazahl=False)
    afg=['Erstelle die Wertetabelle von -'+strNW(wertTab)+' bis '+strNW(wertTab)+' und zeichne den Graphen von $'+variabel+'~\\rightarrow~'+ersetzePlatzhalterMitSymbolen(term)+'$.']
    [minY,maxY]=minMaxY(term,variabel,wertTab)
    yTickDist,yMin,yMax,hoehe=setzeAchsenEinteilungLaenge([minY,maxY,achsenlaenge])
    print('hoehe='+str(hoehe))
    lsg=tikzTabelle(tabelle=[[variabel]+list(range(-wertTab,wertTab+1)),['$'+term.replace('*','\\cdot ')+'$']+[sympy.simplify(term).subs(sympy.symbols(variabel),x) for x in range(-wertTab,wertTab+1)]],dim=0.5,spaltenBreite=[2]+[1.0]*(2*wertTab+1),tabellenPos=[0,-0.0])
    lsg=lsg[:-1]+diagrammTikzVorgBreiteHoehe(zuPlotten=[[term,'black']],koordinaten=[[x,sympy.simplify(term).subs(sympy.symbols(variabel),x)]for x in range(-wertTab,wertTab+1)],xAchse=[-wertTab,wertTab,achsenlaenge],yAchse=[minY,maxY,achsenlaenge*1.5],xlabel='x',ylabel='y',urspr=[0,-hoehe-2],mitUmrandung=False)+[lsg[-1]]
    werte=[term]
    return [afg,lsg,werte]
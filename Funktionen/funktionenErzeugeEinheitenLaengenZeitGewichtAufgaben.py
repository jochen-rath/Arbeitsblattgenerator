#!/usr/bin/env python
# coding: utf8

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())

    
def einheitenListe():
    groessen={'km':1e3,'m':1,'dm':1e-1,'cm':1e-2,'mm':1e-3,'km^2':1e6,'ha':1e4,'a':1e2,'m^2':1,'dm^2':1e-2,'cm^2':1e-4,'mm^2':1e-6,
              't':1e6,'kg':1e3,'g':1,'mg':1e-3,'y':365*24*60*60+60*60*6,'w':7*24*60*60,'d':24*60*60,'h':60*60,'min':60,'s':1,'ms':1e-3}
    einheitenZuTimedelta={'d':'days','s':'seconds','mys':'microseconds','ms':'milliseconds','min':'minutes', 'h':'hours','w':'weeks'}
    einheiten={'laengen':['km','m','dm','cm','mm'],'flaechen':['km^2','ha','a','m^2','dm^2','cm^2','mm^2'],'gewicht':['t','kg','g','mg'],'zeit':['y','d','h','min','s','ms'],'zeitOhne':['h','min','s']}
    return [groessen,einheitenZuTimedelta,einheiten]


def erzeugeZeitBestimmenAfg(mitText=True,breitePbox=5):
    stunde=random.randint(1,12)
    minute=random.randint(1,60)
    afg=(['\\pbox{'+str(breitePbox)+'cm}{Wie Spät ist es? \\\\'] if mitText else []) + tikzAnalogeUhr(stunde=stunde,minute=minute)
    afg=afg+(['}'] if mitText else [])
    lsg=['Es ist '+str(stunde)+' Uhr und '+str(minute)+' Minuten']
    return [afg,lsg,[stunde,minute]]

def erzeugeAddiereUhrzeit(schwer=False,breitePbox=5):
    [uhrzeit,lsg,[stunde,minute]]=erzeugeZeitBestimmenAfg(mitText=False,breitePbox=breitePbox)
    addStunde=random.randint(1,12)
    addMinute=0 if not schwer else random.randint(1,59)
    lsgZahl=stunde*60+addStunde*60+minute+addMinute
    h,min,s=str(datetime.timedelta(minutes=lsgZahl)).split(':')
    h=int(h)%12
    lsg=['Es ist '+str(h)+' Uhr und '+str(min)+' Minuten']
    afg=['\\pbox{'+str(breitePbox)+'cm}{'] 
    afg.append('\n'.join(uhrzeit))
    afg.append('+'+strNW(addStunde)+' Stunden '+('' if not schwer else ('und '+strNW(addMinute)+' Minuten'))+'}')
    return [afg,lsg,[h,min]]

def addiereSubtrahiereEinheiten(art='',mitKomma=False,einheitPaar=[]):
#if True:
    groessen,einheitenZuTimedelta,einheiten=einheitenListe()
#Einige Aufgaben sollen Addition und Subtraktion verschiedener Einheitenarten beinhalten
    if random.randint(0,6)<6:
#Keine Negativen Zahlen
        lsgZahl=-1
        while lsgZahl<0:
#Wähle eine Einheitenart aus:
            art=art if len(art)>0 else random.choice(list(einheiten.keys()))
#Wähle zwei Einheiten der Art:
            E1,E2=[random.choice(einheiten[art]),random.choice(einheiten[art])] if len(einheitPaar)==0 else einheitPaar
            klE=E1 if groessen[E1] < groessen[E2] else E2
            grE=E1 if groessen[E1] > groessen[E2] else E2
#Erzeuge eine Aufgabe:
            op=random.choice(['+','-'])
            d1=random.randint(1,999) if E1==klE else random.randint(1,99)
            d2=random.randint(1,999) if E2==klE else random.randint(1,99)
            if mitKomma and not art=='zeit':
                d1=d1+random.randint(0,99)*1e-2
                d2=d2+random.randint(0,99)*1e-2
            afg=['$'+strNW(d1)+'~'+E1+'~'+op+'~'+strNW(d2)+'~'+E2+'=$']
#Mit round werden Lösungen wie 10.003,0000000000000001 verhindert.
            lsgZahl=round(eval(str(d1)+'*'+str(groessen[E1])+op+str(d2)+'*'+str(groessen[E2])),6)
            lsg=['$\\begin{aligned}']
            lsg.append(afg[0][1:-2]+' &='+strNW(eval(str(d1)+'*'+str(groessen[E1])+'/'+str(groessen[klE])))+'~'+klE+' '+op+' '+strNW(eval(str(d2)+'*'+str(groessen[E2])+'/'+str(groessen[klE])))+'~'+klE+'\\\\')
            if not klE==grE:
                lsg.append(' &='+strNW(eval(str(lsgZahl)+'/'+str(groessen[klE])))+'~'+klE+'\\\\')
            if art=='zeit':
                h,min,s=str(datetime.timedelta(seconds=lsgZahl)).replace('days','~\\mbox{Tage}').replace('day','~\\mbox{Tag}').split(':')
                lsg.append(' &='+h+'\\mbox{ Stunden, }'+str(int(min))+'\\mbox{ Minuten, }'+str(int(s))+'\\mbox{ Sekunden, }'+'\\\\')
            else:
                lsg.append(' &='+strNW(eval(str(lsgZahl)+'/'+str(groessen[grE])))+'~'+grE+'\\\\')
            lsg.append('\\end{aligned}$')  
            if  groessen[grE] / groessen[klE] > 1e6:
                lsgZahl=-1
    else:
        art1,art2=1,1
        while art1==art2:
            art1,art2=art if len(art)>0 else random.choice(list(einheiten.keys())),random.choice(list(einheiten.keys()))
            E1,E2=random.choice(einheiten[art1]),random.choice(einheiten[art2])
            E1=('$' if '^' in E1 else '') + E1 + ('$' if '^' in E1 else '') 
            E2=('$' if '^' in E2 else '') + E2 + ('$' if '^' in E2 else '') 
            op=random.choice(['+','-'])
            d1,d2=random.randint(1,20),random.randint(1,20)
            afg=[str(d1)+' '+E1+' '+op+' '+str(d2)+' '+E2+'=']
            lsg=['Man kann '+E1+' und '+E2+' nicht '+('addieren' if op=='+' else 'subtrahieren')+'.']
    return [afg,lsg,[d1,d2,op,E1,E2]]



def rechneEinheitenUm(art='laengen',kleiner1Zahlen=False,einfach=False,einSchritt=False,mitKomma=False,vonObenNachUnten=False):
# Aufruf:
#      [aufgabe,lsg,wert]=rechneEinheitenUm(art,kleiner1Zahlen,einfach,einSchritt,mitKomma,vonObenNachUnten)
#
#Standard:
#      rechneEinheitenUm(art='laengen',kleiner1Zahlen=False,einfach=False,einSchritt=False,mitKomma=False,vonObenNachUnten=False)
#
#Bedeutung:
#      art= laengen, zeit, flaechen, gewicht
#      kleiner1Zahlen= True oder False, soll z.B. Zahlen wie 0.5 m zugelassen werden?
#      einfach= True oder False, soll z.B. entweder nur Zahlen von 0 bis 10 oder 0 bis 1000?
#      einSchritt= True oder False, soll z.B. sollen nur aufgaben von m auf cm oder auch von km auf mm gestellt werden? Also ein oder mehrere Schritte?
#      mitKomma= True oder False, soll z.B. z.B. 5,6 h umgewandelt werden. Bei nicht einfach auch 5,63 h.
#      vonObenNachUnten= True oder False, Soll nur die Größere in die Kleiner Einheit umgewandelt werden oder ist es auch von klein nach groß möglich?
    groessen,einheitenZuTimedelta,einheiten=einheitenListe()
    if not (art in einheiten.keys()):
        return [art + " kenne ich nicht.",[],[]]
    erg=-1
    while erg<0:
        auswahlEinheit=einheiten[art]
        wert=random.choice([random.randint(1,9),random.randint(10,99),random.randint(100,999)])
        wert=random.randint(1,10) if einfach else wert
        nachKomma=random.randint(1,9)/10 if einfach else random.choice([random.randint(1,9)/10,random.randint(1,99)/100])
        wert=wert + (0 if not mitKomma else +nachKomma)
        ind=random.randint(0,len(auswahlEinheit)-2)
        if art=='zeit' and einfach:
            ind=random.randint(2,len(auswahlEinheit)-2)
        G=auswahlEinheit[ind:ind+2] if einSchritt else random.sample(auswahlEinheit,2)
        if not vonObenNachUnten:
            random.shuffle(G)
        if groessen[G[0]]<groessen[G[1]]:
            wert=wert if mitKomma else wert*groessen[G[1]]/groessen[G[0]]
        aufgabe=['\\rule{0pt}{0.75cm}'+strNW(wert)+' $'+G[0]+'$= \\rule{3cm}{0.15mm} $'+G[1]+'$']
        erg=wert*groessen[G[0]]/groessen[G[1]]
        teilen=False
        if mitKomma:
            multiDiviWert='~\\cdot~'+strNW(groessen[G[0]]/groessen[G[1]])
        else:
            multiDiviWert=('~\\cdot~'+strNW(groessen[G[0]]/groessen[G[1]])) if groessen[G[0]]/groessen[G[1]]>1 else ('~:~'+strNW(groessen[G[1]]/groessen[G[0]]))
        lsg=[strNW(wert)+' $'+G[0]+'$='+strNW(wert)+'$'+multiDiviWert+ '~'+G[1]+'$= \\underline{'+strNW(erg)+'} $'+G[1]+'$']
        if erg<1:
            erg=erg if kleiner1Zahlen else -1
    return [aufgabe,lsg,wert]

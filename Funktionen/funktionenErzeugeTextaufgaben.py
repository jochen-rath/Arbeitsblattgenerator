#!/usr/bin/env python
# coding: utf8
import random


#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())
openAiModel = 'gpt-4-turbo'  # "gpt-3.5-turbo"
def ladeOpenAi():
    keyfile=F'{os.path.expanduser("~")}/OpenAiKey.txt'
    if os.path.isfile(keyfile):
        with open(keyfile, 'r') as datei:
            key = datei.read().replace('\n', '')

        client = openai.OpenAI(api_key=key, )
        return client
    else:
        return 'Kein Key'

def chatGptAnweisung():
    return  'Schreibe nur die Frage und den Antwortsatz auf. Schreibe Frage vor der Frage und Antwortsatz vor dem Antwortsatz. Schreibe XXX im Antwortsatz, anstatt der Zahlen'

def stelleChatGptDieFrage(frage='Erstelle mit eine Sachaufgabe zur Multiplikation'):
    try:
        client = ladeOpenAi()
        completion = client.chat.completions.create(model=openAiModel,  messages=[    {"role": "user", "content": F'{frage} {chatGptAnweisung()}'}  ])
        afg=completion.choices[0].message.content.split('Antwortsatz:')[0].replace('%','\\%').replace('^','').replace('Frage:','')
        antwortsatz=completion.choices[0].message.content.split('Antwortsatz:')[1].replace('^','')
    except:
        afg='Kein ChatGPT Kontakt'
        antwortsatz=f'Dies ist ein sehr sehr sehr langer Antworttext, um die Ausgabe zu testen. Das Ergebnis ist XXX. Die Frage war: {frage}'
    return afg,antwortsatz

def fuegeAntwortsatzEin(erg=0,antwortsatz='Langer Text',dy='0',lsg=['0']*4,anzSpalten=2,listPos=3):
    lsg.insert(len(lsg) - listPos, F'\\node[left] at (1,{dy}) {{Antwort:}};')
    if len(antwortsatz.split(' '))>10 or anzSpalten>1:
        trenn=4 if anzSpalten>1 else 12 #int(len(antwortsatz.split(' '))/2)
        a=[antwortsatz.split(' ')[i*trenn:(i+1)*trenn] for i in range(int(len(antwortsatz.split(' '))/trenn))]
        a=a if int(len(antwortsatz.split(' '))/trenn)==len(antwortsatz.split(' '))/trenn else a+[antwortsatz.split(' ')[int(len(antwortsatz.split(' '))/trenn)*trenn:]]
        for i,teilSatz in enumerate(a):
           lsg.insert(len(lsg) - listPos, F'\\node[right] at (1,{dy}-{0.5*i}) {{{" ".join(teilSatz).replace("%","$$%").replace("XXX",strNW(erg))}}};'.replace('$$','\\'))
    else:
        lsg.insert(len(lsg) - listPos, F'\\node[right] at (1,{dy}) {{{antwortsatz.replace("%","$$%").replace("XXX",strNW(erg))}}};'.replace('$$','\\'))
#    return lsg

def erzeugeSchriftMultiDiviAufgabe(multi=True,anzSpalten=2):
    e=random.choice(einheiten)
    if multi:
        einheitenMulti=['\euro{}','km','m','g','l','kg','cm','Autos','LKW','Knöpfe']
        e=random.choice(einheitenMulti)
    z1=random.choice([random.randint(12,99),random.randint(101,999)]) if multi else random.randint(2,150)
    z2=random.choice([random.randint(2,9),random.randint(10,99)]) if multi else random.randint(2,15)
    z3=z1*z2
    if not multi:
        z1,z3=z3,z1
    typ='Multiplikation' if multi else 'Division'
    chatgptFrage=F'Erstell mir eine Sachaufgabe zur {typ} mit {z1} {e} {"und" if multi else "durch"} {z2}.'
    afg,antwortsatz=stelleChatGptDieFrage(frage=chatgptFrage)
    lsg=schreibeMultiplikationenStellengerecht(F'{z1}*{z2}') if multi else erzeugeDivisionStellengerecht(F'{z1}/{z2}',mitLoesung=True)
    verschiebung=F'{"" if multi else "-1"}'
    fuegeAntwortsatzEin(erg=z3,antwortsatz=antwortsatz,dy=F'{verschiebung}-2.25{"" if z2<10 else "-1"}',lsg=lsg,anzSpalten=anzSpalten)
    return [[ersetzePlatzhalterMitSymbolen(x) for x in [afg]], [ersetzePlatzhalterMitSymbolen(x) for x in lsg], []]

def erzeugeSchriftAddiSubtrakAufgabe(addi=True,anzSpalten=2):
    z1=random.choice([random.randint(11,999),random.randint(1001,9999)])
    z2=random.choice([random.randint(11,99),random.randint(100,999)])
    z3=z1+z2
    if not addi:
        z1,z3=z3,z1
    e=random.choice(einheiten)
    typ='Addition' if addi else 'Subktraktion'
    chatgptFrage=F'Erstell mir eine Sachaufgabe zur {typ} mit {z1} und {z2} {e}.'
    afg,antwortsatz=stelleChatGptDieFrage(frage=chatgptFrage)
    lsg=schreibeRechnungStellengerecht([['','+' if addi else '-',''],[z1,z2,z3]])
    fuegeAntwortsatzEin(erg=z3,antwortsatz=antwortsatz,dy=F'-2.25',lsg=lsg,anzSpalten=anzSpalten)
    return [[ersetzePlatzhalterMitSymbolen(x) for x in [afg]], [ersetzePlatzhalterMitSymbolen(x) for x in lsg], []]



def erzeugeProzentwertTextAufgabe(ges='',HS=False,umformen=False,anzSpalten=2):
    werte=erzeugeProzentRechnungen(HS=HS)
    art=werte[3]
    varis={'G':[werte[0],art],'W':[werte[1],art],'p':[werte[2],'\\%']}
    benennung={'G':'Grundwert','W':'Prozentwert','p':'Prozentsatz'}
    geg=list(varis.keys())
    if len(ges)<1:
        ges=random.choice(geg)
    geg.remove(ges)
    formel='W=G*p/100'
    if ges=='W':
        aufgabe=F'Prozentsatz ist {strNW(varis[geg[1]][0])} {varis[geg[1]][1]} und Grundwert ist {strNW(varis[geg[0]][0])} {varis[geg[0]][1]} und gesucht ist der {benennung[ges]}'.replace('\\','')
    if ges=='G':
        aufgabe=F'Prozentwert {strNW(varis[geg[0]][0])} {varis[geg[0]][1]} und Prozentsatz {strNW(varis[geg[1]][0])} {varis[geg[1]][1]}  und gesucht ist der {benennung[ges]}'.replace('\\','')
    if ges=='p':
        aufgabe=F'Prozentwert {strNW(varis[geg[1]][0])} {varis[geg[1]][1]} und Grundwert {strNW(varis[geg[0]][0])} {varis[geg[0]][1]}  und gesucht ist der {benennung[ges]}'.replace('\\','')
    chatgptFrage=F'Erstell mir eine Prozentwertaufgabe mit {aufgabe}. Schreibe nur die Frage und den Antwortsatz auf. Schreibe Frage vor der Frage und Antwortsatz vor dem Antwortsatz. Schreibe XXX im Antwortsatz, anstatt der Zahlen'
    afg,antwortsatz=stelleChatGptDieFrage(frage=chatgptFrage)
    verschiebung=0
    if umformen:
        lsg=loeseFunktion(formel=formel, varis=varis, ges=ges, breite=5, kommaAusgabe=True)
        weite=[idx for idx, s in enumerate(lsg) if 'aligned' in s]
        verschiebung=(weite[1]-weite[0])/2
    else:
        if ges=='W':
            lsg=ausgabeProzentwertBerechnenFuerTabelle(inhalte=[['',varis['G'][0],varis['p'][0],varis['G'][1]]],mitDreisatz=True,bez=['G','W','p'])
        if ges=='p':
            lsg=ausgabeProzentsatzBerechnenFuerTabelle(inhalte=[['',varis['G'][0],varis['W'][0],varis['G'][1]]],mitDreisatz=True,bez=['G','W','p'])
        if ges=='G':
            lsg=ausgabeGrundwertBerechnenFuerTabelle(inhalte=[['',varis['W'][0],varis['p'][0],varis['W'][1]]],mitDreisatz=True,bez=['G','W','p'])
        verschiebung=6
    fuegeAntwortsatzEin(erg=varis[ges][0],antwortsatz=antwortsatz,dy=F'-1.75-{verschiebung}',lsg=lsg,anzSpalten=anzSpalten)
    return [[ersetzePlatzhalterMitSymbolen(x) for x in [afg]],[ersetzePlatzhalterMitSymbolen(x) for x in lsg],[]]

def erzeugeVermindVermehrtGrundwertAfg( HS=False,mitDreisatz=False,anzSpalten=2):
    openAiModel='gpt-4-turbo'   #"gpt-3.5-turbo"
    werte=erzeugeProzentRechnungen(HS=HS)
    art=werte[3]
    varis={'G':[werte[0],art],'W':[werte[1],art],'p':[werte[2],'\\%']}
    benennung={'G':'Grundwert','W':'Prozentwert','p':'Prozentsatz'}
    ges=random.choice(['vermehrte','verminderte'])
    chatgptFrage=F'Erstell mir eine {ges} Prozentwertaufgabe mit dem Grundwerte {varis["G"][0]} {varis["G"][1]} und dem {ges}n Prozentsatz {varis["p"][0]}. Schreibe nur die Frage und den Antwortsatz auf. Schreibe Frage vor der Frage und Antwortsatz vor dem Antwortsatz. Schreibe XXX im Antwortsatz, anstatt der Zahlen. Schreibe die Zahlen mit einem Dezimalkomma'
    afg,antwortsatz=stelleChatGptDieFrage(frage=chatgptFrage)
    if ges=='verminderte':
        lsg=ausgabeVerminderteGrundwertBerechnenFuerTabelle(inhalte=[['',varis['G'][0],varis['p'][0],varis['G'][1]]],mitDreisatz=mitDreisatz)
        erg=varis['G'][0]-varis['G'][0]*varis['p'][0]/100
    else:
        lsg=ausgabeVermehrterGrundwertBerechnenFuerTabelle(inhalte=[['',varis['G'][0],varis['p'][0],varis['G'][1]]],mitDreisatz=mitDreisatz)
        erg=varis['G'][0]+varis['G'][0]*varis['p'][0]/100
    fuegeAntwortsatzEin(erg=erg,antwortsatz=antwortsatz,dy=F'-10.25{"" if mitDreisatz else "+3.5"}',lsg=lsg,anzSpalten=anzSpalten,listPos=2)
    return [afg,lsg,[]]

def erzeugeZinsrechnungTextAufgabe(ges='',HS=False,umformen=False,anzSpalten=2):
    K=random.choice([random.randint(100,10000),random.randint(10000,100000)])
    p=random.choice([random.randint(1,10)/10,random.randint(10,100)/10])
    werte=[K,round(K*p/100,2),p]
    art='€'
    varis={'K':[werte[0],art],'Z':[werte[1],art],'p':[werte[2],'\\%']}
    benennung={'K':'Kapital','Z':'Zinsen','p':'Zinsatz'}
    artikel={'K':'ist das','Z':'sind die','p':'ist der'}
    geg=list(varis.keys())
    if len(ges)<1:
        ges=random.choice(geg)
    geg.remove(ges)
    formel='Z=K*p/100'
    chatgptFrage=F'Erstell mir eine Zinsrechenaufgabe mit {benennung[geg[1]]} ist {strNW(varis[geg[1]][0])} {varis[geg[1]][1]} und {benennung[geg[0]]} ist {strNW(varis[geg[0]][0])} {varis[geg[0]][1]} und gesucht {artikel[ges]} {benennung[ges]}'.replace('\\','')
    afg,antwortsatz=stelleChatGptDieFrage(frage=chatgptFrage)
    verschiebung=0
    if umformen:
        lsg=loeseFunktion(formel=formel, varis=varis, ges=ges, breite=5, kommaAusgabe=True)
        weite=[idx for idx, s in enumerate(lsg) if 'aligned' in s]
        verschiebung=(weite[1]-weite[0])/2
    else:
        if ges=='Z':
            lsg=ausgabeProzentwertBerechnenFuerTabelle(inhalte=[['',varis['K'][0],varis['p'][0],varis['K'][1]]],mitDreisatz=True,bez=['K','Z','P'])
        if ges=='p':
            lsg=ausgabeProzentsatzBerechnenFuerTabelle(inhalte=[['',varis['K'][0],varis['Z'][0],varis['K'][1]]],mitDreisatz=True,bez=['K','Z','p'])
        if ges=='K':
            lsg=ausgabeGrundwertBerechnenFuerTabelle(inhalte=[['',varis['Z'][0],varis['p'][0],varis['Z'][1]]],mitDreisatz=True,bez=['K','Z','p'])
        verschiebung=6
    fuegeAntwortsatzEin(erg=varis[ges][0],antwortsatz=antwortsatz,dy=F'-1.75-{verschiebung}',lsg=lsg,anzSpalten=anzSpalten) 
    return [[ersetzePlatzhalterMitSymbolen(x) for x in [afg]],[ersetzePlatzhalterMitSymbolen(x) for x in lsg],[]]

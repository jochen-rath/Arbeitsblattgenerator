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

def erzeugeSchriftMultiDiviAufgabe(multi=True):
    z1=random.choice([random.randint(12,99),random.randint(101,999)]) if multi else random.randint(2,150)
    z2=random.choice([random.randint(2,9),random.randint(10,99)]) if multi else random.randint(2,15)
    z3=z1*z2
    if not multi:
        z1,z3=z3,z1
    e=random.choice(einheiten)
    typ='Multiplikationsaufgabe' if multi else 'Divisionsaufgabe'
    client = ladeOpenAi()
    chatgptFrage=F'Erstell mir eine ausführliche {typ} mit {z1} {e} {"und" if multi else "durch"} {z2} {e}.'
    completion = client.chat.completions.create(model=openAiModel,  messages=[    {"role": "user", "content": F'{chatgptFrage} {chatGptAnweisung()}'}  ])
    afg=completion.choices[0].message.content.split('Antwortsatz:')[0].replace('%','\\%').replace('^','').replace('Frage:','')
    antwortsatz=completion.choices[0].message.content.split('Antwortsatz:')[1].replace('^','')
    lsg=schreibeMultiplikationenStellengerecht(F'{z1}*{z2}') if multi else erzeugeDivisionStellengerecht(F'{z1}/{z2}',mitLoesung=True)
    verschiebung=F'{"" if multi else "-1"}'
    if len(antwortsatz.split(' '))>10:
        trenn=int(len(antwortsatz.split(' '))/2)
        a1=' '.join(antwortsatz.split(' ')[0:trenn])
        a2=' '.join(antwortsatz.split(' ')[trenn:])
        lsg.insert(len(lsg) - 3, F'\\node[right] at (-1,{verschiebung}-1.75{"" if z2<10 else "-1"}) {{Antwort: {a1.replace("%","$$%").replace("XXX",strNW(z3))}}};'.replace('$$','\\'))
        lsg.insert(len(lsg) - 3, F'\\node[right] at (0.9,{verschiebung}-2.25{"" if z2<10 else "-1"}) {{{a2.replace("%","$$%").replace("XXX",strNW(z3))}}};'.replace('$$','\\'))
    else:
        lsg.insert(len(lsg) - 3, F'\\node[right] at (-1,{verschiebung}-1.75{"" if z2<10 else "-1"}) {{Antwort: {antwortsatz.replace("%","$$%").replace("XXX",strNW(z3))}}};'.replace('$$','\\'))
    return [[ersetzePlatzhalterMitSymbolen(x) for x in [afg]], [ersetzePlatzhalterMitSymbolen(x) for x in lsg], []]

def erzeugeSchriftAddiSubtrakAufgabe(addi=True):
    z1=random.choice([random.randint(11,999),random.randint(1001,9999)])
    z2=random.choice([random.randint(11,99),random.randint(100,999)])
    z3=z1+z2
    if not addi:
        z1,z3=z3,z1
    e=random.choice(einheiten)
    client = ladeOpenAi()
    typ='Additionsaufgabe' if addi else 'Subktraktionsaufgabe'
    chatgptFrage=F'Erstell mir eine ausführliche {typ} mit {z1} {e} und {z2} {e}.'
    completion = client.chat.completions.create(model=openAiModel,  messages=[    {"role": "user", "content": F'{chatgptFrage} {chatGptAnweisung()}'}  ])
    afg=completion.choices[0].message.content.split('Antwortsatz:')[0].replace('%','\\%').replace('^','').replace('Frage:','')
    antwortsatz=completion.choices[0].message.content.split('Antwortsatz:')[1].replace('^','')
    lsg=schreibeRechnungStellengerecht([['','+' if addi else '-',''],[z1,z2,z3]])
    if len(antwortsatz.split(' '))>10:
        trenn=int(len(antwortsatz.split(' '))/2)
        a1=' '.join(antwortsatz.split(' ')[0:trenn])
        a2=' '.join(antwortsatz.split(' ')[trenn:])
        lsg.insert(len(lsg) - 3, F'\\node[right] at (-1,-2.25) {{Antwort: {a1.replace("%","$$%").replace("XXX",strNW(z3))}}};'.replace('$$','\\'))
        lsg.insert(len(lsg) - 3, F'\\node[right] at (0.9,-2.75) {{{a2.replace("%","$$%").replace("XXX",strNW(z3))}}};'.replace('$$','\\'))
    else:
        lsg.insert(len(lsg) - 3, F'\\node[right] at (-1,-2.25) {{Antwort: {antwortsatz.replace("%","$$%").replace("XXX",strNW(z3))}}};'.replace('$$','\\'))
    return [[ersetzePlatzhalterMitSymbolen(x) for x in [afg]], [ersetzePlatzhalterMitSymbolen(x) for x in lsg], []]



def erzeugeProzentwertTextAufgabe(ges='',HS=False,umformen=False):
    werte=erzeugeProzentRechnungen(HS=HS)
    art=werte[3]
    varis={'G':[werte[0],art],'W':[werte[1],art],'p':[werte[2],'\\%']}
    benennung={'G':'Grundwert','W':'Prozentwert','p':'Prozentsatz'}
    geg=list(varis.keys())
    if len(ges)<1:
        ges=random.choice(geg)
    geg.remove(ges)
    client=ladeOpenAi()
    formel='W=G*p/100'
    if ges=='W':
        aufgabe=F'Prozentsatz ist {strNW(varis[geg[1]][0])} {varis[geg[1]][1]} und Grundwert ist {strNW(varis[geg[0]][0])} {varis[geg[0]][1]} und gesucht ist der {benennung[ges]}'.replace('\\','')
    if ges=='G':
        aufgabe=F'Prozentwert {strNW(varis[geg[0]][0])} {varis[geg[0]][1]} und Prozentsatz {strNW(varis[geg[1]][0])} {varis[geg[1]][1]}  und gesucht ist der {benennung[ges]}'.replace('\\','')
    if ges=='p':
        aufgabe=F'Prozentwert {strNW(varis[geg[1]][0])} {varis[geg[1]][1]} und Grundwert {strNW(varis[geg[0]][0])} {varis[geg[0]][1]}  und gesucht ist der {benennung[ges]}'.replace('\\','')
    chatgptFrage=F'Erstell mir eine Prozentwertaufgabe in mit {aufgabe}. Schreibe nur die Frage und den Antwortsatz auf. Schreibe Frage vor der Frage und Antwortsatz vor dem Antwortsatz. Schreibe XXX im Antwortsatz, anstatt der Zahlen'
    print(chatgptFrage)
    completion = client.chat.completions.create(model=openAiModel,  messages=[    {"role": "user", "content": chatgptFrage}  ])
    afg=completion.choices[0].message.content.split('Antwortsatz:')[0].replace('%','\\%').replace('^','').replace('Frage:','')
    antwortsatz=completion.choices[0].message.content.split('Antwortsatz:')[1].replace('^','')
    if umformen:
        lsg=loeseFunktion(formel=formel, varis=varis, ges=ges, breite=5, kommaAusgabe=True)
        weite=[idx for idx, s in enumerate(lsg) if 'aligned' in s]
        lsg.insert(len(lsg) - 3, F'\\node[right] at (0,-1.75-{(weite[1]-weite[0])/2}) {{{antwortsatz.replace("%","$$%").replace("XXX",strNW(varis[ges][0]))}}};'.replace('$$','\\'))
    else:
        if ges=='W':
            lsg=ausgabeProzentwertBerechnenFuerTabelle(inhalte=[['',varis['G'][0],varis['p'][0],varis['G'][1]]],mitDreisatz=True,bez=['G','W','p'])
        if ges=='p':
            lsg=ausgabeProzentsatzBerechnenFuerTabelle(inhalte=[['',varis['G'][0],varis['W'][0],varis['G'][1]]],mitDreisatz=True,bez=['G','W','p'])
        if ges=='G':
            lsg=ausgabeGrundwertBerechnenFuerTabelle(inhalte=[['',varis['W'][0],varis['p'][0],varis['W'][1]]],mitDreisatz=True,bez=['G','W','p'])
        lsg.insert(len(lsg) - 3, F'\\node[right] at (-1,-7.75) {{{antwortsatz.replace("%","$$%").replace("XXX",strNW(varis[ges][0]))}}};'.replace('$$','\\'))
    return [[ersetzePlatzhalterMitSymbolen(x) for x in [afg]],[ersetzePlatzhalterMitSymbolen(x) for x in lsg],[]]

def erzeugeVermindVermehrtGrundwertAfg( HS=False,mitDreisatz=False):
    openAiModel='gpt-4-turbo'   #"gpt-3.5-turbo"
    werte=erzeugeProzentRechnungen(HS=HS)
    art=werte[3]
    varis={'G':[werte[0],art],'W':[werte[1],art],'p':[werte[2],'\\%']}
    benennung={'G':'Grundwert','W':'Prozentwert','p':'Prozentsatz'}
    ges=random.choice(['vermehrte','verminderte'])
    client=ladeOpenAi()
    chatgptFrage=F'Erstell mir eine {ges} Prozentwertaufgabe mit dem Grundwerte {varis["G"][0]} {varis["G"][1]} und dem {ges}n Prozentsatz {varis["p"][0]}. Schreibe nur die Frage und den Antwortsatz auf. Schreibe Frage vor der Frage und Antwortsatz vor dem Antwortsatz. Schreibe XXX im Antwortsatz, anstatt der Zahlen. Schreibe die Zahlen mit einem Dezimalkomma'
    completion = client.chat.completions.create(model=openAiModel,  messages=[    {"role": "user", "content": chatgptFrage}  ])
    afg=completion.choices[0].message.content.split('Antwortsatz:')[0].replace('%','\\%').replace('^','').replace('Frage:','')
    antwortsatz=completion.choices[0].message.content.split('Antwortsatz:')[1].replace('^','')
    if ges=='verminderte':
        lsg=ausgabeVerminderteGrundwertBerechnenFuerTabelle(inhalte=[['',varis['G'][0],varis['p'][0],varis['G'][1]]],mitDreisatz=mitDreisatz)
        erg=varis['G'][0]-varis['G'][0]*varis['p'][0]/100
    else:
        lsg=ausgabeVermehrterGrundwertBerechnenFuerTabelle(inhalte=[['',varis['G'][0],varis['p'][0],varis['G'][1]]],mitDreisatz=mitDreisatz)
        erg=varis['G'][0]+varis['G'][0]*varis['p'][0]/100
    lsg.insert(len(lsg) - 2, F'\\node[right] at (-1,-10.25{"" if mitDreisatz else "+3.5"}) {{Antwort: {antwortsatz.replace("%","$$%").replace("XXX",strNW(erg))}}};'.replace('$$','\\'))
    return [afg,lsg,[]]
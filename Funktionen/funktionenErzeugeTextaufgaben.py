#!/usr/bin/env python
# coding: utf8

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())

def ladeOpenAi():
    keyfile=F'{os.path.expanduser("~")}/OpenAiKey.txt'
    if os.path.isfile(keyfile):
        with open(keyfile, 'r') as datei:
            key = datei.read().replace('\n', '')

        client = openai.OpenAI(api_key=key, )
        return client
    else:
        return 'Kein Key'

def erzeugeProzentwertTextAufgabe(ges='',HS=False,umformen=False):
    openAiModel='gpt-4-turbo'   #"gpt-3.5-turbo"
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
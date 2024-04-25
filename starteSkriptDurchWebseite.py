#!/usr/bin/env python
# coding: utf8

import sys, errno
import inspect
from flask import Flask, flash, render_template_string, request, jsonify, send_from_directory,redirect,url_for
from flask_wtf import FlaskForm, Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, validators, BooleanField
from wtforms.fields.html5 import DateField, TimeField
from Funktionen.funktionenRechenBezeichnungen import MoeglicheRechnungen
import random
import string
import os
import subprocess
import shlex
import sys
import datetime
import psutil
import time
import re

app = Flask(__name__)
app.secret_key = '7a51514f04b8e8039965d1fd33ad6540'
maXAnzahlAuswahl = 12
anzahlAuswahl=6
globaleMitteilung=''

class Form(Form):
    titel=TextField("Titel",default='Tägliche Übungen',validators=[validators.Regexp(r'^[A-Za-z0-9öäüÖÄÜ ]+$',message="Titel: Bitte nur Buchstaben, Zahlen und Leerzeichen")])
    beschreibung=TextField("Beschreibung",default='',validators=[validators.Regexp(r'^[A-Za-z0-9öäüÖÄÜ.,?! ]+$',message="Beschreibung: Bitte nur Buchstaben, Zahlen, Leerzeichen und Satzzeichen")])
    datum=DateField("Datum",default=(datetime.date.today() + datetime.timedelta(days=1)))
    for i in range(maXAnzahlAuswahl):
        exec('auswahl'+str(i+1)+'=SelectField("auswahl'+str(i+1)+'",choices=MoeglicheRechnungen("keys"),default=MoeglicheRechnungen("keys")[0])')
        exec('rechnung'+str(i+1)+'=SelectField("rechnung'+str(i+1)+'",choices=MoeglicheRechnungen(MoeglicheRechnungen("keys")[0]),default=MoeglicheRechnungen(MoeglicheRechnungen("keys")[0]))')
        exec('anzahl'+str(i+1)+'=SelectField("anzahl'+str(i+1)+'",choices=[(str(i),str(i)) for i in range(27)])')
#    anzahlAlle=SelectField("anzahlAlle",choices=[(str(i),str(i)) for i in range(int(27/maXAnzahlAuswahl)+1)],default='0')
    anzahlAlle=SelectField("anzahlAlle",choices=[(str(i),str(i)) for i in range(5)],default='0')
    anzSpaltenAfg=SelectField("Aufgabe: Anzahl an Spalten",choices=[(str(i),str(i)) for i in range(1,3)],default='2')
    anzSpaltenLsg=SelectField("Lösung: Anzahl an Spalten",choices=[(str(i),str(i)) for i in range(1,3)],default='2')
    mitText=BooleanField('Mit Beschreibungstext in den Aufgaben',default='checked')
 #   aufgSeitenumbruch=BooleanField('Seitenumbruch bei den Aufgaben')
    anzAuswahlAufgaben=SelectField("Anzahl an auswählbaren Aufgaben",choices=[(str(i),str(i)) for i in range(1,maXAnzahlAuswahl+1)],default=str(anzahlAuswahl))
    karoBereich=SelectField("Karofeld in cm auf Aufgabenblatt ",choices=[(str(i),str(i)) for i in range(15)],default='0')
    extraKaroseite=BooleanField('Extra Karoseite einführen.')
    agfLsgGetrennt=BooleanField('Aufgaben und Lösungen getrennt ausgeben')
    erzeugeArbeit=BooleanField('Erzeuge eine Arbeitsvorlage.')
    texAusgabe=BooleanField('Gib eine LaTeX tex Datei mit aus.')
    submit = SubmitField("Senden")

@app.route('/', methods = ['GET', 'POST'])
def viewAuswahlRechnungen():
    global globaleMitteilung
    global maXAnzahlAuswahl
    global anzahlAuswahl
    form=Form()
    globaleMitteilung=''
    zugelassenZeichen=re.compile(r'^[A-Za-z0-9.,!?ö:äüÖÄÜ_ -]+$')
    if request.method== 'POST':
#Führe validet_on_submit aus, um auf Fehler zu schecken.
#Packe diesen Befehl aber nicht in die if-Abfrage, da die dynamische Erzeugung der Auswahlfelder zu falschen Fehlermeldung führen.
        print(form.validate_on_submit())
        if ((not len(form.titel.errors)>0) or (len(form.titel.data)==0)) and ((not len(form.beschreibung.errors)>0) or (len(form.beschreibung.data)==0)):   #form.validate_on_submit():
            auswahl=[]
            rechnungen=[]
            anzahl=[]
#Alle Auswahlfelder abarbeiten.
            for i in range(anzahlAuswahl):
                auswahl.append(eval('form.auswahl'+str(i+1)+'.data'))
                rechnungen.append(eval('form.rechnung'+str(i+1)+'.data'))
                anzahl.append(eval('form.anzahl'+str(i+1)+'.data') if form.anzahlAlle.data =='0' else form.anzahlAlle.data)
#Setzen der Eingabeparameter für das Skript
            datum=str(form.datum.data).split('-')
            datum="KeinDatum" if len(datum)<2 else (datum[2]+'.'+datum[1]+'.'+datum[0])
            titel=form.titel.data
            titel=titel+'_'+''.join(random.sample(string.ascii_letters,4))
            beschreibung=form.beschreibung.data
            anzSpalten=F'{form.anzSpaltenAfg.data},{form.anzSpaltenLsg.data}'
            karoBereich=F'karo-{form.karoBereich.data}'
            extraKaroseite=F'extraKaro-{form.extraKaroseite.data}'
            agfLsgGetrennt=F'afgLsg-{form.agfLsgGetrennt.data}'
            erzeugeArbeit=F'erzArbeit-{form.erzeugeArbeit.data}'
            texAusgabe=F'texAusgabe-{form.texAusgabe.data}'
#            seitenumbruch='Seitenumbruch-False'
#            if form.aufgSeitenumbruch.data:
#                seitenumbruch='Seitenumbruch-True'
            mitText='mitText-False'
            if form.mitText.data:
                mitText='mitText-True'
            script='Aufrufe/taeglicheUebungen/erzeugeTaeglicheRechnungenArgs.py'
            anzRech=[]
            for i in range(anzahlAuswahl):
                anzRech=anzRech+[rechnungen[i]]*int('0' if anzahl[i] is None else anzahl[i])
#Ich bin paranoid, und habe Angst, dass mir Leute durch manipulierte Browser auch Sonderzeichen durch das Datumfeld oder
#den Auswahlfeldern schicken können, die sonstwas machen, wenn ich mein Skript aufrufe. Von daher überprüfe ich, ob auch nur zugelassene Zeichen gesendet wurden.
            allesKorrekt=True
            if not bool(zugelassenZeichen.search(titel)):
                allesKorrekt=False
            if not bool(zugelassenZeichen.search(datum)):
                allesKorrekt=False
            if not bool(zugelassenZeichen.search(anzSpalten)):
                allesKorrekt=False
 #           if not bool(zugelassenZeichen.search(seitenumbruch)):
 #               allesKorrekt=False
            if not bool(zugelassenZeichen.search(mitText)):
                allesKorrekt=False
            if not bool(zugelassenZeichen.search(karoBereich)):
                allesKorrekt=False
            if not bool(zugelassenZeichen.search(extraKaroseite)):
                allesKorrekt=False
            if not bool(zugelassenZeichen.search(agfLsgGetrennt)):
                allesKorrekt=False
            if not bool(zugelassenZeichen.search(erzeugeArbeit)):
                allesKorrekt=False
            if not bool(zugelassenZeichen.search(texAusgabe)):
                allesKorrekt=False
            if not bool(zugelassenZeichen.search(''.join(anzRech))):
                allesKorrekt=False
#Wenn alles Korrekt ist und auch ein paar Aufgaben gefwählt wurde, Starte das Skript.
            if len(anzRech)>0 and allesKorrekt:
                warteZeit=300 if 'erzeugeAlleAtome' in anzRech else 90
                parameterListe=[sys.executable,script, titel,beschreibung,datum, anzSpalten,mitText, karoBereich,extraKaroseite, agfLsgGetrennt,erzeugeArbeit,texAusgabe]+anzRech
                print(parameterListe)
                filename,rc=run_command(['timeout',F'{warteZeit}'] + parameterListe)
                print('Run')
                if rc==0:
                    globaleMitteilung='Fertig.'
                    return send_from_directory(os.path.join(os.getcwd(),"Ausgabe"), filename, as_attachment=True)
                else:
                    globaleMitteilung='Fehler.'
                    return "<pre>Fehler bei der Erzeugung des Arbeitblatts.</pre>"
            else:
                if form.anzAuswahlAufgaben.data.isnumeric():
                    if not int(form.anzAuswahlAufgaben.data)==anzahlAuswahl:
                        anzahlAuswahl=int(form.anzAuswahlAufgaben.data)
                    else:
                        anzahlAuswahl=int(form.anzAuswahlAufgaben.data)
                        globaleMitteilung='Sie haben 0 Rechnungen ausgewählt.'
                else:
                    globaleMitteilung='Die gewählte Anzahl an Aufgaben ist nicht Numerisch.'
        else:
            globaleMitteilung=';'.join(form.titel.errors)+';'.join(form.beschreibung.errors)
    return render_template_string('\n'.join(htmlScriptAufrufSeite(anzahlAuswahl=anzahlAuswahl)),form=form)

@app.route('/hilfe', methods=['GET', 'POST'])
def hilfe_form():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('viewAuswahlRechnungen'))

    # show the form, it wasn't submitted
    return render_template_string('\n'.join(hilfeSeite()))

@app.route('/impressum', methods=['GET', 'POST'])
def impressum_form():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('viewAuswahlRechnungen'))

    # show the form, it wasn't submitted
    impressum=['']
    if os.path.isfile(os.path.join(os.path.expanduser('~'),'impressum.html')):
        with open(os.path.join(os.path.expanduser('~'),'impressum.html')) as datei:
            impressum=datei.read()
    return render_template_string(impressum)

@app.route('/wasistneu', methods=['GET', 'POST'])
def wasistneu_form():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('viewAuswahlRechnungen'))

    # show the form, it wasn't submitted
    impressum=['']
    if os.path.isfile('wasistneu.html'):
        with open('wasistneu.html') as datei:
            wasistneu=datei.read()
    return render_template_string(wasistneu)


@app.route('/rechnungen/<auswahl>')
def rechnungen(auswahl):
#Diese Funktion schreibt die möglichen Rechnungen in ein Array, welches als JSON an die Homepage gesendet wird.
    rechnungenAuswahl=MoeglicheRechnungen(auswahl)
    rechnungenArray=[]
    for rechnung in rechnungenAuswahl:
        rechnungObj = {}
        rechnungObj['id']=rechnung[0]
        rechnungObj['name']=rechnung[1]
        rechnungenArray.append(rechnungObj)
    return jsonify({'moeglicheRechnungen':rechnungenArray})

@app.route('/mitteilung/')
def flashMassege():
#Diese Funktion schreibt den Inhalt der Variabel globaleMitteilung in ein JSON und sendet dieses an die Homepage
    global globaleMitteilung
    return jsonify({'mitteilung':globaleMitteilung})

def hilfeSeite():
    html=[]
    html.append('<!doctype html>')
    html.append('<html>')
    html.append('<head>')
    html.append('<title>Hilfe zum Arbeitsblattgenerator.</title>')
    html.append('</head>')
    html.append('<style type="text/css">body{margin:40px auto;max-width:900px;line-height:1.6;font-size:18px;background-color:#EEEEEE;color:#444;padding:0 10px}h1,h2,h3{line-height:1.2}</style>')
    html.append('<body>')
    html.append('<h2>Idee</h2>')
    html.append('<p>Als ich als Lehrer anfing, wurde sehr schnell klar, dass meine Schülerinnen und Schüler Probleme haben, Inhalte zu bearbeiten, wenn zwischen der Einführung und erneuten Behandlung ein halbes Jahr oder mehr vergangen ist. Es fehlt die regelmäßige Übung, um die Lerninhalte zu festigen. Weiter fehlte es mir aber auch an Material, um den Schülerinnen regelmäßige Übungsaufgaben zur Verfügung zu stellen. Und bei den Aufgaben, die ich hatte, fehlten entweder die Lösungen oder diese waren nur sehr kurz und knapp gehalten. Ich wollte aber meinen Schülerinnen regelmäßige Übungsaufgaben mit sehr ausführlichen Lösungen zur Verfügung stellen, mit denen diese sich selber Schritt für Schritt kontrollieren können.</p>')
    html.append('<h2>Beschreibungen</h2>')
    html.append('<ul>')
    html.append('<li><u>Title:</u> Überschrift und Dateiname</li>')
    html.append('<li><u>Beschreibung:</u> Wenn man nicht im jeden Feld ein Text haben will, kann man hier eine allgemeine Beschreibung einfügen. Dann den Haken bei Beschreibungstext in den Aufgaben entfernen.</li>')
    html.append('<li><u>Datum:</u> Kann man auswählen oder leer lassen. Wird im Dateiname verwendet.</li>')
    html.append('<li><u>Alle Rechnungen gleiche Anzahl:</u> Man kann hier 0,1,2 auswählen. So braucht man bei Anzahl nicht individuell auswählen.</li>')
    html.append('<li><u>Anzahl Spalten für die Aufgaben:</u> 1 oder 2</li>. Bei Aufgaben, die viel Platz benötigen, empfiehlt sich eine Spalte zu nutzen.')
    html.append('<li><u>Anzahl Spalten für die Lösungen:</u> 1 oder 2</li>. Manche Lösungen brauchen viel Platz. Z.B. bei den Termen und Gleichungen. Dann nur eine Spalte nehmen.')
    html.append('<li><u>Mit Beschreibungstext in den Aufgaben:</u> Entferne diesen Haken, wenn kein Text in den Aufgaben erscheinen soll. Das Blatt wird unübersichtliche, wenn 20 mal der gleiche Text drin steht.</li>')
#    html.append('<li><u>Seitenumbruch in den Aufgaben:</u> Wenn man Aufgaben mit auswählt, die viel Platz benötigen, kann man hier den Seitenumbruch ermöglichen.</li>')
    html.append('<li><u>Karofeld unter dem Aufgaben:</u> Damit die Schüler direkt auf dem Aufgabenzettel arbeiten können, kann man hier ein Karofeld einfügen. Am besten die Aufgaben einmal ohne erzeugen lassen, damit man weiß, wieviel Platz auf der Seite über bleibt.</li>')
    html.append('<li><u>Extra Karoseite:</u> Wenn man beidseitig drucken will, kann man hier eine leere Karoseite einfügen lassen.</li>')
    html.append('<li><u>Aufgaben und Lösungen getrennt ausgeben:</u> Normal werden Aufgaben und Lösungen in einer Datei geschrieben. Wenn man die getrennt haben will, bekommt man eine Zip-Datei.</li>')
    html.append('<li><u>Anzahl an Auswählbaren Aufgaben:</u> Um die Webseite übersichtlich zu lassen, kann man anfangs nur 6 verschiedene Aufgabentypen aussuchen. Braucht man mehr, kann man die Anzahl hier wählen. Wichtig, erst Alle Anzahlen auf 0 bringen, damit die Seite neu geladen werden kann.</li>')
    html.append('</ul>')
    html.append('<h2>Arbeitsvorlage bearbeiten</h2>')
    html.append('Wer sich an LaTeX traut, kann mit dem Arbeitsblattgenerator Arbeiten erstellen. Es können dabei maximal <b>6</b> verschiedene Themen ausgewählt werden, da das 7. Thema eine Vorlage für eine Textaufgabe ist. <br>')
    html.append('Eine Installationsanleitung für XeLaTeX unter Windows findet sich z.B. hier:')
    html.append('<p><a href=http://www.texts.io/support/0002/>Install XeLaTeX on Windows</a></p>')
    html.append('LaTeX Dateien kann man mit einem einfachen Texteditor bearbeiten, es empfiehlt sich aber umfangreiche Editoren wie z.B. <a href=https://notepad-plus-plus.org/downloads/>Notepad++</a> zu verwenden. <br>')
    html.append('Hat man eine Arbeit passen erstellt, erzeugt man die Arbeit unter Eingabe des Befehls: <b>xelatex dateiname.tex</b><br>')
    html.append('Als Dateiname nimmt man die tex-Datei, welche keine Nummerierung enthält.<br>')
    html.append('Der Generator erzeugt eine Vorlage für eine Klassenarbeit. Diese besteht aus einer Kopfseite und mehreren Themen. Für die Kopfseite und jedes Thema wird eine Latex-Datei erzeugt, welche in einer')
    html.append('"Verlinkungsdatei" zusammengeführt werden Diese Verlinkungsdatei fügt einmal die Kopfseite und alle Themen zusammen und es wird in dieser Datei für jedes Thema')
    html.append('die Punkte gesetzt. Will man mit dem Arbeitsblattgenerator eine Arbeit erzeugen, müssen folgende Punkte durchgeführt werden:')
    html.append('<ul>')
    html.append('<li>Änder oder entferne den Beschreibungstext zu den einzelnen Themen/Aufgaben. Man erkennt ihn daran, dass er mit "Füge hier bitte einen Beschreibungstext ein. ..."</li>')
    html.append('<li>Änder die Reihenfolge der Themen, indem ihr die Dateien umbenennt. Sollen Thema 2 und Thema 4 die Position tauschen, benennt die folgendermaßen um:</li>')
    html.append('<ul>')
    html.append('<li>2023.04.20_terme_WLMd_Aufgabe02.tex &rarr; 2023.04.20_terme_WLMd_Aufgabe02x.tex</li>')
    html.append('<li>2023.04.20_terme_WLMd_Aufgabe04.tex &rarr; 2023.04.20_terme_WLMd_Aufgabe02.tex</li>')
    html.append('<li>2023.04.20_terme_WLMd_aufgabe02x.tex &rarr; 2023.04.20_terme_WLMd_aufgabe04.tex</li>')
    html.append('</ul>')
    html.append('<li>Passe die Punkte in der Verknüfpungsdatei an.')
    html.append('<li>Bei den Punkten gilt, dass alle Themen, die 0 Punkte haben, auf der Kopfseite nicht angezeigt werden.</li>')
    html.append('<li>Soll zwischen zwei Themen kein Seitenumbruch stattfinden, lösche das \\newpage am Anfang dem Folgethema.</li>')
    html.append('<li>In der Kopfseite-Datei muss theoretisch nichts verändert werden. Alle wichtigen Angaben werden in der Verknüpfungsdatei gesetzt.</li>')
    html.append('<li>Passe die Kopfseite an, indem in der Verknüpfungsdatei die Werte in den geschweiften Klammern zu \\datum, \\kurs, usw. den eigenen Bedürfnissen angepasst werden.</li>')
    html.append('<li>Das erlaubte Material wird beim Wert \\material in der geschweiften Klammern gesetzt. Beachte, dass die Verschiedenen Hilfsmittel durch Komma getrennt werden.</li>')
    html.append('<li>Wenn man möchte, kann man noch weitere Aufgaben der Arbeit hinzufügen. Dann kann man die Auswahl bei "Gib eine LaTeX tex Datei mit aus.:" bestätigen und man kriegt den LaTeX Code passend zum erzeugtem Arbeitsblatt. Aus diesem Code muss man sich dann den passenden Teil herauskopieren und in die Arbeit einfügen.</li>')
    html.append('</ul>')
    html.append('<h2>Source Code</h2>')
    html.append(F'Der Source-Code des Generators findet sich hier: <br>')
    html.append(F'    <p><a href=https://github.com/jochen-rath/Arbeitsblattgenerator>Source Code auf Github</a></p>')
    html.append('    <form method="post">')
    html.append('        <button type="submit" style="   padding: 12px 24px;background: rgb(220,220,220);font-weight: bold;color: rgb(0,0,0);">Zurück</button>')
    html.append('    </form>')
    html.append('</html>')
    return html

def htmlScriptAufrufSeite(anzahlAuswahl=4):
#Diese Funktion erzeugt eine Homepage
    html=[]
    html.append('<!DOCTYPE html>')
    html.append('<html lang="de">')
    html.append('<head>')
    html.append('    <meta charset="UTF-8">')
    html.append('    <meta name="viewport" content="width=device-width, initial-scale=1.0">')
    html.append('    <meta http-equiv="X-UA-Compatible" content="ie=edge">')
    html.append('    <title> Arbeitsblattgenerator </title>')
    html.append('</head>')
    html.append('')
    html.append('<style type="text/css">body{margin:40px auto;max-width:900px;line-height:1.6;font-size:18px;background-color:#EEEEEE;color:#444;padding:0 10px}h1,h2,h3{line-height:1.2}</style>')
    html.append('<body>')
    html.append('<b> Achtung, neue Internetadresse: <a href="https://abgenerator.de/">https://abgenerator.de/</a></b><p>')
    html.append('Die Alten werden in laufe der nächten Wochen/Monaten nichtmehr verfügbar sein.')
    html.append('    <form method="POST">')
    html.append('        {{ form.csrf_token }}')
    html=html+htmlTabelle(anzahlAuswahl)
    html.append('        {{ form.anzAuswahlAufgaben.label }}: {{ form.anzAuswahlAufgaben }}<br>')
    html.append('        Drücke auf "Senden", wenn bei jeder Rechnung die Anzahl 0 ist, um die Anzahl an auswählbaren Rechnungen zu verändern.<br>')
    html.append('        {{ form.submit(style="   padding: 12px 24px;background: rgb(220,220,220);font-weight: bold;color: rgb(0,0,0);")  }}')
    html.append('    </form>')
    html.append('    Status: <p id="p1"> </p>')
#    html.append('    Status2: <p id="p2"> </p>')
    html.append('    <script>')
    html=html+javascriptAuswahl(anzahlAuswahl)
    html=html+mitteilungenJava()
    html=html+setzeDropDownAnzahlJava(anzahlAuswahl)
    html.append('    </script>')
    html.append(F'    <p><a href="{{{{ url_for({chr(39)}hilfe_form{chr(39)}) }}}}">Hilfe und Beschreibung</a></p>')
    if os.path.isfile(os.path.join(os.path.expanduser('~'), 'impressum.html')):
        html.append(F'    <p><a href="{{{{ url_for({chr(39)}impressum_form{chr(39)}) }}}}">Impressum</a></p>')
    if os.path.isfile('wasistneu.html'):
        html.append(F'    <p><a href="{{{{ url_for({chr(39)}wasistneu_form{chr(39)}) }}}}">Was Ist Neu?</a> Letzte Änderung: 25.04.2024</p>')
    html.append('</body>')
    return html


def htmlTabelle(anzahlAuswahl=4):
    tabelle=[]
    tabelle.append('         <fieldset>')
    tabelle.append('            <legend>Rechnungsauswahl</legend>')
    tabelle.append('            {{ form.hidden_tag() }}')
    tabelle.append('            {{ form.titel.label }}: {{ form.titel }}<br>')
    tabelle.append('            {{ form.beschreibung.label }}: {{ form.beschreibung }}<br>')
    tabelle.append('            {{ form.datum.label }}: {{ form.datum }}<br>')
#    tabelle.append('            Achtung, es werden nur die ersten 26 Aufgaben geschrieben.<br>')
    tabelle.append('            <table cellspacing="0" cellpadding="0" align="left"  width="20%";>')
    tabelle.append('              <tr>')
    tabelle.append('                 <th>Thema</th><th>Auswahl</th><th>Anzahl</th>')
    tabelle.append('              </tr>')
    for i in range(anzahlAuswahl):
        tabelle.append('              <tr>')
        tabelle.append('                 <td>{{ form.auswahl'+str(i+1)+' }}</td><td>{{ form.rechnung'+str(i+1)+' }}</td><td>{{ form.anzahl'+str(i+1)+' }}</td>')
        tabelle.append('              </tr>')
    tabelle.append('            </table>')
    for i in range(anzahlAuswahl+2):
        tabelle.append('            <br>')
    tabelle.append('            Alle Rechnungen gleiche Anzahl: {{ form.anzahlAlle }}<br>')
    tabelle.append('            (Ignorierte bei Werte>0 individuelle Anzahl bei den gewählten Aufgaben) <br>')
    tabelle.append('            {{ form.anzSpaltenAfg.label }}: {{ form.anzSpaltenAfg }}<br>')
    tabelle.append('            {{ form.anzSpaltenLsg.label }}: {{ form.anzSpaltenLsg }}<br>')
    tabelle.append('            {{ form.mitText.label }}: {{ form.mitText }}<br>')
#    tabelle.append('            {{ form.aufgSeitenumbruch.label }}: {{ form.aufgSeitenumbruch }}<br>')
    tabelle.append('            {{ form.karoBereich.label }}: {{ form.karoBereich }}<br>')
    tabelle.append('            {{ form.extraKaroseite.label }}: {{ form.extraKaroseite }}<br>')
    tabelle.append('            {{ form.agfLsgGetrennt.label }}: {{ form.agfLsgGetrennt }}<br>')
    tabelle.append('            {{ form.erzeugeArbeit.label }}: {{ form.erzeugeArbeit }}<br>')
    tabelle.append('            {{ form.texAusgabe.label }}: {{ form.texAusgabe }}<br>')
    tabelle.append('         </fieldset>')
    return tabelle


def javascriptAuswahl(anzahlAuswahl=4):
    javascript=[]
    for i in range(anzahlAuswahl):
        javascript.append('        let themen_auswahl'+str(i+1)+'=document.getElementById('+chr(39)+'auswahl'+str(i+1)+chr(39)+');')
        javascript.append('        let rechnung_auswahl'+str(i+1)+'=document.getElementById('+chr(39)+'rechnung'+str(i+1)+chr(39)+');')
        javascript.append('        themen_auswahl'+str(i+1)+'.onchange = function(){')
        javascript.append('            thema=themen_auswahl'+str(i+1)+'.value;')
        javascript.append('            fetch('+chr(39)+'/rechnungen/'+chr(39)+' + thema).then(function(response) {')
        javascript.append('                response.json().then(function(data){')
        javascript.append('                    let optionHTML = '+chr(39)+''+chr(39)+';')
        javascript.append('                    for (let auswahl of data.moeglicheRechnungen){')
        javascript.append('                        optionHTML += '+chr(39)+'<option value="'+chr(39)+' + auswahl.id + '+chr(39)+'">'+chr(39)+' + auswahl.name + '+chr(39)+'</option>'+chr(39)+';')
        javascript.append('                    }')
        javascript.append('                    rechnung_auswahl'+str(i+1)+'.innerHTML = optionHTML;')
        javascript.append('                });')
        javascript.append('            });')
        javascript.append('        }')
    return javascript

def mitteilungenJava():
    javascript=[]
    javascript.append('        setInterval(function() {')
    javascript.append('            fetch('+chr(39)+'/mitteilung/'+chr(39)+').then(function(response) {')
    javascript.append('                response.json().then(function(data){')
    javascript.append('                     document.getElementById("p1").innerHTML = data.mitteilung;')
    javascript.append('                });')
    javascript.append('            });')
    javascript.append('        }, 1000);')
    return javascript

def setzeDropDownAnzahlJava(anzahlAuswahl=4):
#Diese Funktion passt die restlichen Anzahl-Felder so an, dass in Summe nur 26 Aufgaben ausgewählt werden können.
    javascript=[]
    
    for i in range(1,anzahlAuswahl+1):
        javascript.append('        let anzahl'+str(i)+' = document.getElementById("anzahl'+str(i)+'");')
        javascript.append('        let anz'+str(i)+' = 0;')
    javascript.append('        let gesamt = 0;')
    javascript.append('        let maxAnz = 0;')
    javascript.append('            let optionHTML = '+chr(39)+''+chr(39)+';')
    for i in range(1,anzahlAuswahl+1):
        javascript.append('        anzahl'+str(i)+'.onchange = function(){')
        for ii in range(1,anzahlAuswahl+1):
            javascript.append('            anz'+str(ii)+' = anzahl'+str(ii)+'.value;')
        javascript.append('            gesamt='+'+'.join(['parseInt(anz'+str(ii)+')' for ii in range(1,anzahlAuswahl+1)])+';')
        for ii in range(1,anzahlAuswahl+1):
            javascript.append('            optionHTML = '+chr(39)+''+chr(39)+';')
            javascript.append('            maxAnz = 26-gesamt+parseInt(anz'+str(ii)+');')
            javascript.append('            for (let i=0; i<=maxAnz; i++){')
            javascript.append('                optionHTML += '+chr(39)+'<option value="'+chr(39)+' + i.toString() + '+chr(39)+'">'+chr(39)+' +  i.toString()  +'+chr(39)+'</option>'+chr(39)+';')
            javascript.append('            }')
            javascript.append('            anzahl'+str(ii)+'.innerHTML = optionHTML;')
            javascript.append('            anzahl'+str(ii)+'.value = anz'+str(ii)+';')
#        javascript.append('                     document.getElementById("p2").innerHTML = anz1+" "+anz2+" "+anz3+" "+anz4+" "+gesamt.toString()+" "+maxAnz.toString();')
        javascript.append('        }')
    return javascript
#print('\n'.join(setzeDropDownAnzahlJava()))

def run_command(command):
#https://www.endpoint.com/blog/2015/01/28/getting-realtime-output-using-python
    form=Form()
    filename=''
    mussteWarte=False
    global globaleMitteilung
    if checkIfProcessRunning('erzeugeTaeglicheRechnungenArgs.py'):
        globaleMitteilung='Es laeuft derzeit ein Erstellungsjob. Ich warte.'
        mussteWarte=True
    while checkIfProcessRunning('erzeugeTaeglicheRechnungenArgs.py'):
        time.sleep(0.5)
    if mussteWarte:
        globaleMitteilung='Ich erzeuge jetzt die Aufgaben'
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    output='21'
    while  (not output == '') and process.poll() is None:
        output = str(process.stdout.readline())
        if output:
            if "This is XeTeX" in output:
                globaleMitteilung='Erzeuge PDF Datei'
            if "Dateiname" in output:
                filename=output.split(':')[1]
    rc = process.poll()
    return [filename[:-3],rc]

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


if __name__ == '__main__':
    app.run(debug = True)

def hebelTikz(pos1=-6,m1=100,pos2=6,m2=100,breite='!',E1='g',E2='g',mitResizebox=True):
    anzahlLoecherProSeize=6
    tikzcommand=[]
    if mitResizebox:
        tikzcommand.append(F"\\resizebox{{{breite}{' cm' if breite.isnumeric() else ''}}}{{!}}{{")
    tikzcommand.append("\\begin{tikzpicture}")
    tikzcommand.append("\\pgfmathsetmacro{\\gewichtLaenge}{2}")
    tikzcommand.append(F"\\pgfmathsetmacro{{\\gewichtEinsHoehe}}{{{m1/100}}}")
    tikzcommand.append(F"\\pgfmathsetmacro{{\\gewichtZweiHoehe}}{{{m2/100}}}")
    tikzcommand.append("\\pgfmathsetmacro{\\hebelLochbreite}{0.5}")
    tikzcommand.append(F"\\pgfmathsetmacro{{\\hebelLaenge}}{{{anzahlLoecherProSeize*2+1}}}")
    tikzcommand.append(F"\\pgfmathsetmacro{{\\gewichtPos}}{{{pos1+0.5+anzahlLoecherProSeize}}}")
    tikzcommand.append(F"\\pgfmathsetmacro{{\\gewichtZweiPos}}{{{pos2+0.5+anzahlLoecherProSeize}}}")
    tikzcommand.append(F"\\node at (\\gewichtPos,-1-\\gewichtEinsHoehe/2) {{{m1} {E1}}};")
    if pos2>0:
        tikzcommand.append(F"\\node[red] at (\\gewichtZweiPos,-1-\\gewichtZweiHoehe/2) {{{m2} {E2}}};")
    tikzcommand.append("\\draw (0,-\\hebelLochbreite/2) rectangle ++ (\\hebelLaenge,\\hebelLochbreite);")
    tikzcommand.append("\\foreach \\x in {1,2,...,\\hebelLaenge}")
    tikzcommand.append("{")
    tikzcommand.append("    \\draw (\\x-0.5,0) circle (0.1 cm);")
    tikzcommand.append("}")
    tikzcommand.append("\\draw[fill,black] (\\hebelLaenge/2,0) circle (0.1 cm);")
    tikzcommand.append("\\draw (\\hebelLaenge/2,0) -- (\\hebelLaenge/2,1);")
    tikzcommand.append("\\fill [pattern = north east lines] (\\hebelLaenge/2-1.5,1) rectangle ++(3,0.3);")
    tikzcommand.append("\\draw[thick] (\\hebelLaenge/2-1.5,1) -- ++(3,0);")
    tikzcommand.append("\\draw (\\gewichtPos,0) -- (\\gewichtPos,-1);")
    tikzcommand.append("\\draw (\\gewichtPos-\\gewichtLaenge/2,-1-\\gewichtEinsHoehe) rectangle ++(\\gewichtLaenge,\\gewichtEinsHoehe);")
    if pos2>0:  
        tikzcommand.append("\\draw[red] (\\gewichtZweiPos,0) -- (\\gewichtZweiPos,-1);")
        tikzcommand.append("\\draw[red] (\\gewichtZweiPos-\\gewichtLaenge/2,-1-\\gewichtZweiHoehe) rectangle ++(\\gewichtLaenge,\\gewichtZweiHoehe);")
    tikzcommand.append("\\end{tikzpicture}")
    if mitResizebox:
        tikzcommand.append("}")
    return tikzcommand


def erzeugeMultimeterStromkaster(IV=[0.5],stromstaerke=True,mitLsg=False):
#Diese Funktion erzeugt einen Latexeintrag zum Üben der Spannung und Stromstärke von dem Multimeter im
#Stromkasten.
#Beispiel:
#I=[random.randint(0,10)/10 for  i in range(4)]+[random.randint(0,100)/100 for  i in range(4)]
#erzeugeEinfachesLatexdokument(erzeugeMultimeterStromkaster(IV=I,stromstaerke=True,mitLsg=True),standalone=True)
    tikzcommand = []
    tikzcommand.append(F'\\begin{{tikzpicture}}')
    tikzcommand.append(F'\\pgfmathsetmacro{{\\R}}{{2}}   ')
    tikzcommand.append(F'\\def\\multimeter(#1,#2,#3){{')
    tikzcommand.append(F'	\\draw[thick,fill=black] (#1,#2) circle (0.1);')
    tikzcommand.append(F'	\\draw[thick] ($(#1,#2)+(45:\\R cm)$) arc (45:135:\\R);')
    tikzcommand.append(F'	\\foreach \\x/\\y  [count=\\xi]  in {{45/3,50/2.5,60/2,72/1.5,90/1,115.5/0.5,135/0}}')
    tikzcommand.append(F'	{{')
    tikzcommand.append(F'		\\draw[very thick] ($(#1,#2)+(\\x:\\R cm)$) -- ($(#1,#2)+(\\x:\\R+0.2+0.28*Mod(\\xi-1,2)$);')
    tikzcommand.append(F'		\\node[rotate=\\x-90] at ($(#1,#2)+(\\x:\\R+0.4+0.3*Mod(\\xi-1,2)$) {{\\y}};')
    tikzcommand.append(F'	}}')
    tikzcommand.append(F'	\\foreach \\x/\\y  [count=\\xi] in {{45/1,50/0.8,65/0.6,80/0.4,95/$~$,115.5/0.2,122/$~$,135/0}}')
    tikzcommand.append(F'	{{')
    tikzcommand.append(F'		\\draw[very thick] ($(#1,#2)+(\\x:\\R-0.2-0.28*Mod(\\xi-1,2)$) -- ($(#1,#2)+(\\x:\\R)$);')
    tikzcommand.append(F'		\\node[rotate=\\x-90] at ($(#1,#2)+(\\x:\\R-0.4-0.3*Mod(\\xi-1,2)$) {{\\y}};')
    tikzcommand.append(F'	}}')
    tikzcommand.append(F'	\\draw[thick,red] (#1,#2) -- ($(#1,#2)+(#3:\\R+0.5)$);')
    tikzcommand.append(F'	\\node at ($(#1,#2)+(90:\\R/2)$) {{A}};')
    tikzcommand.append(F'	\\node at ($(#1,#2)+(90:\\R+1)$) {{V}};')
    tikzcommand.append(F'}}')
    for  i,x in enumerate(IV):
        tikzcommand.append(F'\\multimeter({4.5*(i%4)},{int(i/4)*(-5)},{erzeugeWinkelFuerMultimeterStromkasten(x,stromstaerke=stromstaerke)})')
        if mitLsg:
            tikzcommand.append(F'\\node at ({4.5*(i%4)},{int(i/4)*(-5)-0.5}) {{${F"I_{i+1}={x} A" if stromstaerke else F"U_{i+1}={x} V"}$}};')
    tikzcommand.append(F'\\end{{tikzpicture}}')
    return tikzcommand

def erzeugeWinkelFuerMultimeterStromkasten(IV=0.5, stromstaerke=True):
    Ix=[0,0.1,0.2,0.3,0.4,0.6,0.8,1]
    Iy=[135,122,115.5,95,80,65,50,45]
    Vx=[0,0.5,1,1.5,2,2.5,3]
    Vy=[135,115.5,90,72,60,50,45]
    return np.interp(IV,Ix,Iy) if stromstaerke else np.interp(IV,Vx,Vy)

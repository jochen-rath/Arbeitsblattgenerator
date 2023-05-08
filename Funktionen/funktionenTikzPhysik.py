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
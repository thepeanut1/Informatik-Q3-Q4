class Knoten:
    def __init__(self, wert, vorname, klasse):
        self.wert = wert      # Wert des Knotens
        self.vorname = vorname
        self.klasse = klasse
        self.links = None     # Linker Nachfolger
        self.rechts = None    # Rechter Nachfolger

class Binaerbaum:
    def __init__(self):
        self.wurzel = None    # Wurzel des Baums

    def einfuegen(self, wert, vorname, klasse):
        """Fügt einen Wert in den Baum ein. Einstiegspunkt."""
        if self.wurzel is None:
            self.wurzel = Knoten(wert, vorname, klasse)  # Initialisiere die Wurzel, wenn der Baum leer ist
        else:
            self._einfuegen_rekursiv(self.wurzel, wert, vorname, klasse)

    def _einfuegen_rekursiv(self, aktueller_knoten, wert, vorname, klasse):
        """Fügt einen Wert rekursiv ein. Interne Methode."""
        if wert < aktueller_knoten.wert:
            if aktueller_knoten.links is None:
                aktueller_knoten.links = Knoten(wert, vorname, klasse)
            else:
                self._einfuegen_rekursiv(aktueller_knoten.links, wert, vorname, klasse)
        elif wert > aktueller_knoten.wert:
            if aktueller_knoten.rechts is None:
                aktueller_knoten.rechts = Knoten(wert, vorname, klasse)
            else:
                self._einfuegen_rekursiv(aktueller_knoten.rechts, wert, vorname, klasse)

    def suche(self, wert):
        return self._suche(self.wurzel, wert)

        """Öffentliche Methode: Sucht einen Wert im Baum und gibt den passenden Knoten zurück."""
        # Rufen Sie hier die rekursive Suchmethode auf, die die Wurzel und
        # den gesuchten Wert als Parameter erhält und geben Sie deren
        # Wert hier zurück.
        
    def _suche(self, knoten, wert):

        if knoten is None or wert == knoten.wert:
            print(f"\nValue:{wert} was found")
            return knoten

        elif wert > knoten.wert:
            if knoten.rechts == None:
                print(f"{wert} not found")
            else:
                return self._suche(knoten.rechts, wert)
        
        elif wert < knoten.wert:
            if knoten.links == None:
                print(f"{wert} not found")
            else:
                return self._suche(knoten.links,wert)
        
        """Private Methode: Sucht einen Wert im Baum und gibt den passenden Knoten zurück."""
        # 1. Falls kein Knoten vorhanden ist oder der Wert in der Wurzel enthalten ist,
        #    geben Sie den aktuellen Knoten zurück.
        # 2. Falls der Wert kleiner als der Wert im Knoten ist, führen Sie die Such links
        #    rekursiv durch. Denken Sie an die Rückgabe.
        # 3. Andernfalls rechts. Denken Sie an die Rückgabe.
        pass

    def inorder(self):
        """Öffentliche Methode für die In-Order-Traversierung."""
        self._inorder_rekursiv(self.wurzel)

    def _inorder_rekursiv(self, aktueller_knoten):
        """Rekursive In-Order-Traversierung."""
        if aktueller_knoten is not None:
            self._inorder_rekursiv(aktueller_knoten.links)
            print(aktueller_knoten.wert, aktueller_knoten.vorname, aktueller_knoten.klasse, end="\n")
            self._inorder_rekursiv(aktueller_knoten.rechts)

# Beispielnutzung
baum = Binaerbaum()
baum.einfuegen("bergmann", "ben", "Q3")
baum.einfuegen("vaidya", "pranit", "Q3")
baum.einfuegen("zhang", "sophie", "Q3")
baum.einfuegen("schröder", "jakob", "Q3")
baum.einfuegen("de Bucourt", "Noah", "Q3")

# Geordnete Ausgabe der enthaltenen Daten
# (In-Order-Traversierung)
baum.inorder()
# Wert suchen
wert1 = "bergmann"
gefundener_knoten = baum.suche(wert1)
if gefundener_knoten:
    print(f"\nGefundener Wert: {gefundener_knoten.wert}")
else:
    print("\nWert nicht gefunden.")

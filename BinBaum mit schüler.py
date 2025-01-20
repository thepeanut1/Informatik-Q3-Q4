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
baum.einfuegen("bergmann", "ben", "7eu1") 
baum.einfuegen("vaidya", "pranit", "9eu2") 
baum.einfuegen("zhang", "sophie", "Q1") 
baum.einfuegen("schröder", "jakob", "10e1") 
baum.einfuegen("de Bucourt", "Noah", "Q4") 
baum.einfuegen("müller", "lena", "7eu1") 
baum.einfuegen("schmidt", "max", "8eu2") 
baum.einfuegen("hofer", "anna", "9e1") 
baum.einfuegen("schneider", "emil", "10e2") 
baum.einfuegen("jung", "mario", "7eu2") 
baum.einfuegen("neumann", "paul", "8e1") 
baum.einfuegen("weber", "laura", "9eu1") 
baum.einfuegen("richter", "hannah", "10e1") 
baum.einfuegen("schulz", "tim", "7e2") 
baum.einfuegen("krüger", "nina", "8e2") 
baum.einfuegen("hofmann", "michael", "9e2") 
baum.einfuegen("peters", "sara", "10e2") 
baum.einfuegen("meyer", "jan", "7eu1") 
baum.einfuegen("bauer", "lara", "8eu1") 
baum.einfuegen("frank", "oliver", "9eu2") 
baum.einfuegen("wagner", "ella", "10eu1") 
baum.einfuegen("hartmann", "samuel", "7e1") 
baum.einfuegen("hoffmann", "fiona", "8e1") 
baum.einfuegen("taylor", "benjamin", "9eu2") 
baum.einfuegen("koch", "hanna", "10e1") 
baum.einfuegen("fischer", "moritz", "7e2") 
baum.einfuegen("mayer", "lara", "8eu2") 
baum.einfuegen("steiner", "sophia", "9e1") 
baum.einfuegen("langer", "florian", "10e2") 
baum.einfuegen("richter", "georg", "7eu1") 
baum.einfuegen("ziegler", "louisa", "8eu1") 
baum.einfuegen("beck", "emilia", "9e2") 
baum.einfuegen("thomas", "noah", "10eu1") 
baum.einfuegen("petersen", "elena", "7eu2") 
baum.einfuegen("rauscher", "florian", "8e1") 
baum.einfuegen("kramer", "luisa", "9eu1") 
baum.einfuegen("kraft", "anika", "10e2") 
baum.einfuegen("wilke", "eva", "7e2") 
baum.einfuegen("möller", "julian", "8eu1") 
baum.einfuegen("roth", "julia", "9e2") 
baum.einfuegen("neubauer", "maximilian", "10e1") 
baum.einfuegen("schwarz", "olivia", "7e1") 
baum.einfuegen("hartwig", "felix", "8e2") 
baum.einfuegen("seidel", "tobias", "9eu2") 
baum.einfuegen("brunner", "leo", "10e1") 
baum.einfuegen("wagner", "mika", "7eu1") 
baum.einfuegen("heinrich", "sofia", "8eu2") 
baum.einfuegen("knapp", "paulina", "9e1") 
baum.einfuegen("scheller", "florian", "10e2") 
baum.einfuegen("vogel", "max", "7eu2") 
baum.einfuegen("reiter", "lars", "8e1") 
baum.einfuegen("hess", "tanja", "9e2") 
baum.einfuegen("sander", "arthur", "10eu1") 
baum.einfuegen("berger", "mia", "7e1") 
baum.einfuegen("neff", "janine", "8e2") 
baum.einfuegen("klotz", "oscar", "9eu1") 
baum.einfuegen("fink", "verena", "10e2") 
baum.einfuegen("berger", "lucas", "7eu2") 
baum.einfuegen("meyer", "elise", "8e1") 
baum.einfuegen("schröder", "tim", "9e2") 
baum.einfuegen("zimmermann", "luca", "10e1") 
baum.einfuegen("neumann", "julian", "7e1") 
baum.einfuegen("schneider", "isabelle", "8eu2") 
baum.einfuegen("frank", "leon", "9e1") 
baum.einfuegen("schulz", "sophie", "10e2") 
baum.einfuegen("steiner", "ben", "7eu2") 
baum.einfuegen("heinz", "amalia", "8e1") 
baum.einfuegen("taylor", "martin", "9eu1") 
baum.einfuegen("hahn", "tess", "10e2") 
baum.einfuegen("krüger", "vincent", "7e1") 
baum.einfuegen("becker", "annika", "8eu2") 
baum.einfuegen("hartmann", "paul", "9e1") 
baum.einfuegen("hoffer", "rosa", "10eu1") 
baum.einfuegen("jones", "martha", "7e2") 
baum.einfuegen("bauer", "oliver", "8eu1") 
baum.einfuegen("maier", "leandro", "9e2") 
baum.einfuegen("hartwig", "lisa", "10e1") 
baum.einfuegen("petersen", "noel", "7eu2") 
baum.einfuegen("becker", "anja", "8e2") 
baum.einfuegen("zimmermann", "josef", "9eu1") 
baum.einfuegen("vogt", "marie", "10e2") 
baum.einfuegen("kraft", "maximilian", "7e1") 
baum.einfuegen("beck", "aline", "8eu2") 
baum.einfuegen("meyer", "georg", "9e1") 
baum.einfuegen("bauer", "robin", "10eu1") 
baum.einfuegen("richter", "anna", "7e2") 
baum.einfuegen("reiter", "david", "8eu1") 
baum.einfuegen("seidel", "amélie", "9e2") 
baum.einfuegen("vogt", "victor", "10e1")

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

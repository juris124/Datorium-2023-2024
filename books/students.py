# Uzdevums:
# Izveido klasi "Students", kas apraksta vidusskolas skolēnu. Katrs skolēns ir aprakstāms ar vārdu, uzvārdu, klasi, kurā viņš mācās, un sarakstu ar viņa mācību priekšmetiem. Izveido trīs metodes šai klasei:

# Metode, kas izvada skolēna informāciju (vārds, uzvārds, klase).
# Metode, kas pievieno jaunu priekšmetu skolēna mācību sarakstam.
# Metode, kas aprēķina skolēna vidējo atzīmi visos priekšmetos.

class Students:
    def __init__(self, vards, uzvards, klase):
        self.vards = vards
        self.uzvards = uzvards
        self.klase = klase
        self.maciibu_prieksmeti = []

    def print_info(self):
        print("Skolēns: {} {}, Klase: {}".format(self.vards, self.uzvards, self.klase))

    def pievienot_prieksmetu(self, prieksmets):
        self.maciibu_prieksmeti.append(prieksmets)

    def videja_atzime(self):
        if not self.maciibu_prieksmeti:
            return "Nav atzīmju"
        else:
            summa = sum(self.maciibu_prieksmeti)
            return summa / len(self.maciibu_prieksmeti)

# Izveidojam skolēnu objektu
skolens1 = Students("Jānis", "Bērziņš", "10.a")
skolens1.print_info()  # Izvada informāciju par skolēnu

# Pievienojam priekšmetus
skolens1.pievienot_prieksmetu(8)
skolens1.pievienot_prieksmetu(7)
skolens1.pievienot_prieksmetu(9)

# Aprēķinam vidējo atzīmi
print("Skolēna vidējā atzīme:", skolens1.videja_atzime())

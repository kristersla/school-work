class Kubiks:
    def __init__(self, malas_garums, krasa):
        if malas_garums < 2 or malas_garums > 10:
            raise ValueError("Malas garums jabut intervala no 2 lidz 10 ieskaitot")
        if len(krasa.split()) > 1:
            raise ValueError("Krasas nosaukums jabut viena varda")
        self.malas_garums = malas_garums
        self.krasa = krasa

    def aprekinat_tilpumu(self):
        return self.malas_garums ** 3

    def likvidet_objektu(self):
        print(f"Objekts ar krasu {self.krasa} ir likvidets.")

class Bloks(Kubiks):
    def __init__(self, malas_garums, krasa, kubu_skaits, forma):
        super().__init__(malas_garums, krasa)
        if kubu_skaits < 1 or kubu_skaits > 4:
            raise ValueError("Kubu skaits bloka jabut intervala no 1 lidz 4 ieskaitot")
        if forma not in [11, 12, 13, 14, 22]:
            print("Formas numurs neatbilst nosacijumiem")
            self.derigums = 0
        else:
            self.derigums = 1
        self.kubu_skaits = kubu_skaits
        self.forma = forma

    def nosaukums(self):
        return f"{self.krasa}{self.kubu_skaits}"

    def tilpums(self):
        return self.kubu_skaits * self.aprekinat_tilpumu()

# Izveido jaunu klases bloks objektu kubg
kubg = Bloks(10, "zala", 3, 13)

# Izveido jaunu klases bloks objektu kubr
try:
    kubr = Bloks(1, "sarkana", 5, 23)
except ValueError as e:
    print(e)

# Izvadit kubg nosaukumu un tilpumu
print("Objekta kubg nosaukums:", kubg.nosaukums())
print("Objekta kubg tilpums:", kubg.tilpums())

# Izvadit kubr malas garumu
print("Objekta kubr malas garums:", kubr.malas_garums)

# Dzest objektu kubr
del kubr

# Parbaudit, vai objekts kubr vairs nav pieejams
try:
    print("Objekta kubr nosaukums:", kubr.nosaukums())
except NameError:
    print("Objekts kubr vairs nav pieejams")

# Izvadit kubg malas garumu
print("Objekta kubg malas garums:", kubg.malas_garums)

# Izveidot jaunu klases bloks objektu kubg, kas sastav no 3 oranzas krasas kubiem ar malas garumu 5 centimetri un formas numuru 13
kubg = Bloks(5, "oranza", 3, 13)

# Izveidot jaunu klases bloks objektu kubz, kas sastav no 5 zilas krasas kubiem ar malas garumu 7 centimetri un formas numuru 23
kubz = Bloks(7, "zila", 5, 23)

# Izvadit kubg nosaukumu un tilpumu
print("Objekta kubg nosaukums un tilpums:", kubg.nosaukums(), kubg.tilpums())

# Izvadit kubz nosaukumu un derigumu
print("Objekta kubz nosaukums un derigums:", kubz.nosaukums(), kubz.derigums)

# Nomainit kubz formas numuru uz 12
kubz.forma = 12

# Izvadit kubz nosaukumu un derigumu
print("Objekta kubz nosaukums un derigums:", kubz.nosaukums(), kubz.derigums)

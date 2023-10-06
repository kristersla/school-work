# 1. uzd. Lai uztādītu sākuma vētības var izmantot def __init__(): funkciju.
# 2. uzd. Izmantoju python - 
# class Klients:
#     def __init__(self, attributes):

#         self.vards = attributes
# 3. uzd. Izmantoju Python -

# class Prece:
    
#     cena = 10
# 4. uzd. B - Atslēgvārds izveido jaunu mainīgo. 
# 5. uzd. izmantoju Python - 
import json
import keyboard

class PersonalPC:

    def __init__(self, veids, modelis, cena):
        self.veids = veids
        self.modelis = modelis
        self.cena = cena

    def get_veids(self):
        return self.veids
    
    def get_modelis(self):
        return self.modelis
    
    def get_cena(self):
        return self.cena

    def set_veids(self, veids):
        self.veids = veids
    
    def set_modelis(self, modelis):
        self.modelis = modelis
    
    def set_cena(self, cena):
        self.cena = cena

    def __repr__(self):
        return f"-Personālā datora sastāvdaļas-\nVeids: {self.veids}\nModelis: {self.modelis}\nCena: {self.cena}"
    
class komponentes(PersonalPC):
    pass

print("Ko vēlaties darīt?\n")
print("parādīt esošo info - 1")
print("rediģēt - 2")
print("veidot jaunu - 3")
print("Vēlos beigt - 4\n")

while True:

    atbilde = input("izvēle: ")

    if atbilde == '1':
        with open('OOP\komponentes.json', 'r') as f:
            komponentes_json = f.read()
            komponentes = json.loads(komponentes_json)
            print("\n-komponentes-\n")

            print(f"{komponentes['veids']} - 1\n")
            print("Vēlos beigt - 4\n")

            atbilde2 = input("izvēle: ")

            if atbilde2 == '1':
                with open('OOP\komponentes.json', 'r') as f:
                    komponentes_json = f.read()
                    komponentes = json.loads(komponentes_json)
                    print("\n-komponentes-\n")
                    print(f"Veids: : {komponentes['veids']}\nModelis: {komponentes['modelis']}\nCena: {komponentes['cena']}\n")
                
                print("Ko vēlaties darīt?\n")
                print("parādīt esošo info - 1")
                print("rediģēt - 2")
                print("veidot jaunu - 3")
                print("Vēlos beigt - 4\n")
    
    if atbilde == '2':
        veids = input("Ievadiet jauno veidu: ")
        modelis = input("Ievadiet jauno modeli: ")
        cena = float(input("Ievadiet jauno cenu: "))
        komponentes_saraksts = {
            "veids": veids,
            "modelis": modelis,
            "cena": cena
        }

        with open('OOP\komponentes.json', 'w') as json_file:
            json.dump(komponentes_saraksts, json_file)
            print("Ko vēlaties darīt?\n")
            print("parādīt esošo info - 1")
            print("rediģēt - 2")
            print("veidot jaunu - 3")
            print("Vēlos beigt - 4\n")

    if atbilde == '3':
        veids = input("Ievadiet jauno veidu: ")
        modelis = input("Ievadiet jauno modeli: ")
        cena = float(input("Ievadiet jauno cenu: "))
        komponentes_saraksts = {
            "veids": veids,
            "modelis": modelis,
            "cena": cena
        }

        with open('OOP\komponentes.json', 'w') as json_file:
            json.dump(komponentes_saraksts, json_file)
            print("Ko vēlaties darīt?\n")
            print("parādīt esošo info - 1")
            print("rediģēt - 2")
            print("veidot jaunu - 3")
            print("Vēlos beigt - 4\n")

    if atbilde == '4': 
        break





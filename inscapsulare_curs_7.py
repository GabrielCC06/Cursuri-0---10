"""
Incapsulare - posibilitatea de a proteja atributele sau metodele unei clase, folosinf modificatorii de vizibilitate

private (privat) - adica atributul/metoda, poate fi accesata doar din interiorul clasei in care a fost definit
            --- se defineste cu underscore in fata (__variabila sau __metoda():     )

protected (protejat) - atributul / metoda poate fi accesata din clasa in care a fost definita dar
                        si din clasele copil ale acesteia, INSA NU din ecetrior

Atunci cand avem un atribut ascunt putem folosi metode speciale pentru a interactiona cu el:
Numite getter, setter, si deleter

getter - pt al vedea  sau a avea acces la atribut
settet - pentru a- i schimba valoarea
deleter - pentru a sterge valoara

Conventie : -acete metode trebuie denumite cu set_d, delete_, si get_ + numele variabilei

"""
class Car:

    variabila_privata = "privat"
    _variabila_protected = "protected"

    def init(self,var_protected):
        self._variabila_protected = var_protected
    #getter
    def get_variabila_privata(self):
        return self.variabila_privata
    #setter
    def set_variabila_privata(self,var):
       self.variabila_privata = var

    #deleter
    def delete_variabila_privata(self):
        self.variabila_privata = None


masina = Car('Update Protected')
# print(masina._variabila_protected)   # convetie ca aceasta variabila sa nu fie accesata.

# print(masina.__variabila_privata)   #-> eroare, variabilele private nu avem acces

print(masina.get_variabila_privata())
masina.set_variabila_privata("Update Private")

print(masina.get_variabila_privata())
masina.delete_variabila_privata()

print(masina.get_variabila_privata())


"""
Mostenire - este capacitatea unei clase de a impartasi atat metode cat si atribute din alta clasa
Clasa copil  mosteneste clasa parinte, astfel clasa copil preia metodele si atributle din clasa parinte.
Clasa copil poate avea oricate metode sau atribute in plus fata de clasa parinte
!!!!!!!----Clasa parinte - nu mosteneste nimic de la clasele copil-------!!!!
!!!---In python!!! O clasa copi; poate mosteni mai multe clase parinte ex : class Copil(Parinte), Parinte2, Parinte3, ....)

"""

class Person:
    def __int__(self, nume, varsta, adresa):
        self.nume = nume
        self.varsta = varsta
        self.adresa = adresa

    def anul_nasterii(self):
        return 2023 - self.varsta

    def descriere(self):
        print(self.nume, self.varsta, self.adresa)


class Student(Person):
    def __init__(self, nume, varsta, adresa, facultate, an_studiu):
        # super() reprezinta clasa parinte( Person)
        # cu super () apelam cosntructorul clasei parinte
        super().__init__(nume, varsta, adresa)
        self.facultate = facultate
        self.an_studiu = an_studiu
    def descriere(self): # fac suprascriere la metoda " descriere" clasa parintelui
        super().descriere()
        print(self.facultate, self.an_studiu)
class Angajat(Person):
    def __init__(self, nume, varsta, adresa, companie, salariu):
        super().__init__(nume, varsta, adresa)
        self.companie = companie
        self.salariu = salariu

    def salariu_anual(self):
        return self.salariu * 12

class Profesor(Angajat):
    def __init__(self, nume, varsta, adresa, companie, salariu, curs, nr_ore):
        super().__init__(nume, varsta, adresa, companie, salariu)
        self.curs = curs
        self.nr_ore = nr_ore



# student = Student('Vlad', 22,'adresa', 'UTCN', 5 )
# print(sudent.nume)
# print(sudent.facultate)

profesor = Profesor('Vlad', 33, 'Adresa', 'IT Factory', 1000, ' Testare Automata', 160)
profesor.descriere()
print(str(profesor,salariu_anual()))
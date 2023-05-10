"""
Polimorfism - poli ( mai multe)- morfism (forma/forme) - ceva care poate lua mai multe forme
In cazul OOP, o metoda poate sa aibe acelasi nume in clasa diferite dar imprementari_logica diferita in interior

Abstractizarea este un proces prin care putem sa ascundem o anuminte functionalitate specifica facte de utiliz
De asemena putem forta un anumit comportament in clasele copil.
In JAVA exista INTERFACE
Utilizatorul stie ce face functionalitatetea, dar nu si cum.

Clasa parinte care este o clasa abstracta, nu putem sa creeam obiecte din ea, ci doar sa folosim ca un
template pentru clasele copil

In abstractizare avem 2 concepte:
 - Interfata - contine doar metode abstracte
 - clasa Abstracta - contine atat metode abstracte cat si metode proprii, cu logica.

 Clasa abdstracta trebuie sa mosteneasca clasa ABC ( Abstract Class Method)
 Fiecare metoda  a clasei abstracte trebuie sa arunce exceptia NotImplementedError sau pass
 Clasa abstracta NU are constrctor pentru ca nu creeam obiecte din ea. O metoda abstracta e o metoda ce nu are corp fara logica
"""
#
# def add(a,b,c=0):
#     return(a+b+c)
#
# print(add(1,2,3))
# print(add(1,2))

from abc import ABC, abstractmethod

class Vehicul (ABC):

    @abstractmethod # decorator ca sa marcam aceasta metoda abstracta
    def nr_roti(self):
        raise NotImplementedError

    @abstractmethod
    def nr_locuri(self):
        pass        #metode abstracte neavand logica si pentru a preveni anumite erori
                    # scriem in corpul metodelor pass, sau NotImplemendetError

    @classmethod
    def metoda_logica_proprie(self):
        print('Aici este o metoda cu logica proprie, nu trebuie imprementata in clasa copil')

clss Masina(Vehicul):

    def __init__(self, culoare):
        self.culoare = culoare

    def nr_roti(self):
        return 4

    def nr_locuri(self):
        return 5


masina = Masina("Verde")

# MINUTUL 19 51


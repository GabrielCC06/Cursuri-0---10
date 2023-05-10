# Ex 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
        #  O variabila este - o parte din memoria calculatorului ce detine date de diferite tipuri. Cutiuta cu valori.

# Am initializat si declarat variabila jucarie

# Ex 2 -  String Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
# variabilă :
# - string
# - int
# - float
# - bool
# Observație: Valorile vor fi alese de tine după preferințe.
jucarie = 'minge cu buline'
culoare = 'albastru cu alb'
albastra_cu_buline = 'alba'
proprietar = 'Ciprian'

#  Integer
buline = 15
jucarii = 10
#  Float
buline_mici = 10.5
buline_mari = 4.5
#  Boolean
minge_sparta = False
buline_mari >buline_mici

# Ex 3 Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
print (type (jucarie))
print (type (buline))
print (type (buline_mari))
print (type (minge_sparta))

# Ex 4 Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
# aceeași variabilă (suprascriere):
# - Verifică tipul acesteia.
buline_mici = round(buline_mici)
print(buline_mici)

# Ex 5 Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
# Rezolvă nepotrivirile de tip prin ce modalitate dorești.

print(f'Am gasit o jucarie: {jucarie}')
print(f'Are culoarea: {culoare}')
print(f'Cate buline are mingea: {buline}')
print(f'Cate buline si ce culoare: {buline} {albastra_cu_buline}')
print(f'{proprietar} are jucarii la numar {jucarii} din care si o {jucarie} cu {culoare}, unde bulinele au culoarea, {albastra_cu_buline} si la numar sunt {buline}')
buline = (buline_mici  + buline_mari)
print(buline)
buline_mari = round(buline_mari)
print(buline_mari)

# Ex 6 Citește de la tastatură:
# - numele;
# - prenumele.
# Afișează: 'Numele complet are x caractere'.

#name = input('Introduceti numele')
#prenume = input('Introduceti prenumele')

#print(f'Numele complet are {int(len(name)) + int(len(prenume))} caractere')

# Ex 7 Citește de la tastatură:
# - lungimea;
# - lățimea.
# Afișează: 'Aria dreptunghiului este x'.

#lungimea = input('lungimea =')
#latimea = input('latimea = ')
#aria = int(lungimea) * int(latimea)
#print(f'Aria dreptunghiului este egal cu {aria}')

# Ex 8 Având stringul: 'Coral is either the stupidest animal or the smartest rock':
# - afișează de câte ori apare cuvântul 'the';

a = 'Coral is either the stupidest animal or the smartest rock'
print(a.count('the'))

# Ex 9 Același string.
# ● Afișează de câte ori apare cuvântul 'the';
# ● Printează rezultatul.

afirmatie = 'Coral is either the stupidest animal or the smartest rock'
afirmatie.count('the')


#  Ex 10 assert a.isdigit(), 'Stringul nu contine doar numere.'
afirmatie = 'Coral is either the stupidest animal or the smartest rock'
afirmatie.count('the')
de_cate_ori_se_repeta_the: int = afirmatie.count('the')
print(f'Cuvantul the se repeta de {de_cate_ori_se_repeta_the} ori in propozitia de mai sus')
assert type(de_cate_ori_se_repeta_the) == int


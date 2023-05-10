# Ex 1
# def suma_numere(lista_numere):
#     suma = 0
#     for numar in lista_numere:
#         suma += numar
#     return suma
# lista_1 = [3,5]
# print(suma_numere(lista_1))

# Ex 2
# def is_even(numar):
#     if numar %2 ==0:
#         return True
#     else:return False
# numar = int(input('Introduceti un numar: '))
# y = is_even(numar)
# print(y)

# Ex 3

# def numar_total_caractere(nume, prenume, nume_mijlociu):
#     nume = len(nume)
#     prenume =len(prenume)
#     nume_mijlociu = len(nume_mijlociu)
#     print(f'Suma caracterelor este: {nume + prenume + nume_mijlociu}')
# numar_total_caractere('Curcuta', 'Gabriel', 'Ciprian')

# Ex 4

# def arie_dreptunghi (x, y):
#     return (f'Aria dreptunghiului este: {x * y}')
# print(arie_dreptunghi(4,5))

# Ex 5

# def aria_cerc(r):
#     pi = 3.14
#     aria = pi * r**2
#     return aria
# raza_cerc = int(input('Introduceti raza cerculuiu: '))
# arie_c = aria_cerc(raza_cerc)
# print(f'Aria cercului este: {arie_c}')

# Ex 6

# def caracter_in_string(a, b):
#     if a in b:
#         return True
#     else:
#         return False
# print(caracter_in_string('a', 'acasa'))

# Ex 7

# def search_upper_lower(sir_caractere_2):
#     nr_upper = 0
#     nr_lower = 0
#     for litera in sir_caractere_2:
#         if litera == litera.upper() and litera != ' ' and not litera.isdigit():
#             nr_upper += 1
#         elif litera == litera.lower() and litera != ' ':
#             nr_lower += 1
#     print(f' Numarul de caractere upper este: {nr_upper}')
#     print(f' Numarul de caractere lower este: {nr_lower}')
# string = 'Tema Numarul 5 Obligatorie'
# nr_caractere = search_upper_lower(string)

# Ex 8

# def lista_numere(lista):
#     lista_numere_pozitive = []
#     for numar in lista:
#         if numar > 0:
#             lista_numere_pozitive.append(numar)
#     return print(lista_numere_pozitive)
#
# lista_numere([3, 5, -2, -7, 8, 1])

# Ex 9

# def comparare_numere(x,y):
#     if x > y:
#         print('Primul număr x este mai mare decat al doilea nr y')
#     elif x < y:
#         print('Al doilea nr y este mai mare decat primul nr x')
#     else:
#         print('Numerele sunt egale')
# comparare_numere(22,8)

# Ex 10

# def numar_in_set(numar,set_de_numere):
#     if numar in set_de_numere:
#         print('nu am adaugat numărul în set. Acesta există deja')
#         return False
#     else:
#         set_de_numere.add(numar)
#         print('am adaugat numărul nou în set')
#         return set_de_numere
# print(numar_in_set(7,{5,7,-20}))

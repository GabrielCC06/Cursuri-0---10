
# 1. Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else
# If else = e o functie, conditionata avand un rezultat unic.

# 2. Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural
# daca este numar intreg mai mare ca 0)

x = int(input ('Introduceti numarul x : '))
if x > 0:
    print('Numarul este natural ')
else:
    print('NUmarul nu este natural ')

# 3. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

x = int(input ('Introduceti numarul x : '))
if x > 0:
    print('Un numar pozitiv')
elif x < 0:
    print('Un numar negativ')
else:
    print('Un numar neutru')

# 4. Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).

x = int(input ('Introduceti numarul x : '))
if x >= -2 and x <=13:
    print ('Numarul este in intervalul (-2,13) ')
else:
    print ('Numarul nu este in intervalul (-2,13) ')


# 5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5 (diferenta inseamna
# cate numere sunt intre x si y, nu rezultatul diferentei intre x si y). Hint: Se va folosi functia
# abs
x = int(input ('Introduceti numarul x: '))
y = int(input ('Introduceti numarul y: '))
if abs(x-y) < 5:
    print ('Diferenta dintre x si y este mai mica de 5 ')
else:
    print ('Diferenta dintre x si y nu este mai mica de 5 ')


# 6. Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)

x = int(input ('Introduceti numarul x: '))
if not (x>=5 and x<=27 ):
    print('X nu este regasit in intervalul inchis [5,27] ')
else:
    print('X regasit in intervalul inchis [5,27] ')

# 7. Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale,
# daca nu, afiseaza care din ele este mai mare
x = int(input ('Introduceti numarul x: '))
y = int(input ('Introduceti numarul y: '))
if x == y:
    print('Numerele sunt egale')
elif x>y:
    print ('X este mai mare decat y')
else:
    print('Y este mai mare decat x')


# 8. Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca
# triunghiul este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau
# oarecare (nicio latura nu e egala).

x = int(input ('Introduceti latura 1: '))
y = int(input ('Introduceti latura 2: '))
z = int(input ('Introduceti latura 3: '))
if x == y == z:
    print('Triunghiul este echilateral ')
elif x == y or y == z or z == x:
    print('Triunghiul este isoscel ')
else:
    print('Triunghiul este oarecare ')

# 9. Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie!
# Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.

# litera = input('Introduceti o litera: ')
# if litera == 'a' or 'A' or 'e' or 'E' or 'i' or 'I' or 'o' or 'O' or 'u' or 'U' or 'â' or 'Â' or 'î' or 'Î':
#     print('Litera este vocala')
# else:
#     print('Litera nu este vocala')

# 10. Transforma si printeaza notele din sistem românesc in sistem american dupa cum
# urmeaza:
#    a. Peste 9 => A
#    b. Peste 8 => B
#    c. Peste 7 => C
#    d. Peste 6 => D
#    e. Peste 4 => E
#    f. 4 sau sub => F

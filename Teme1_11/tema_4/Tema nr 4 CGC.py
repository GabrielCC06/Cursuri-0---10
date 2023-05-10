# Ex 1
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for masina in range(len(masini)):
    print(f'Masina mea preferata este {masini[masina]}')
    masina += 1

for masina in masini:
    print(f'Masina mea preferata este {masina}')

i = 0
while i < len(masini):
    print(f'Masina mea preferata este {masini[i]}')
    i += 1

# Ex 2

for masina in range(len(masini)):
  if masina in range(1,len(masini)-1):
    masini[masina] = masini[masina].upper()
else:
  print(masini)

# Ex 3

for masina in masini:
    print(f'Am gasit masina {masina}')
    if masina == "Mercedes":
        print('Am gasit masina aleasa de DVS')
        break
print(f'Am gasit masina {masina}, mai cautam?')

# Ex 4

index = 0
while index < len(masini):
    if masini[index] == 'Trabant' or masini[index] == 'Lastun':
        index += 1
        continue
    print(f'S-ar putea sa va placa masina: {masini[index]} ')
    index += 1

# Ex 5

masini_vechi = []
for i in range(len(masini)):
    if masini[i] == 'Trabant' or masini[i] == 'Lastun':
        masini_vechi.append(masini[i])
        masini[i] = 'Tesla'
print(f'Modele vechi: {masini_vechi}')
print(f'Modele noi: {masini}')

# Ex 6

pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
buget = 15000
for masina, pret in pret_masini.items():
  if pret <= buget:
    print(f"Pentru un buget de sub {buget} euro puteți alege mașina {masina} la pretul de {pret} euro")

# Ex 7

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

contor = 0
for numar in numere:
  if numar == 3:
    contor += 1
print(f"Numărul 3 apare de {contor} ori în listă.")

# Ex 8

suma = 0
for numar in numere:
  suma += numar

print(f"Suma este: {suma}.")

# Ex 9

maxim = 0
for numar in numere:
  if numar > maxim:
    maxim = numar
print(f"Numarul cel mai mare din listă este: {maxim}.")

# Ex 10


for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = -numere[i]
print(numere)
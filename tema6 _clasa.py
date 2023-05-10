class Cont():
    def init(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.')

    def debitare_cont(self):
        suma_retrasa = int(input('Introduceti suma pe care doriti sa o debitati: '))
        while suma_retrasa >= self.sold:
            suma_retrasa = int(input('Introduceti suma pe care doriti sa o debitati: '))
            self.sold = 7000
            self.sold = self.sold - suma_retrasa
            print('Suma pe care doresti sa o retragi este mai mare decat suma din cont')
        else:
            print(f'Soldul in urma debitarii este {self.sold}')

    def creditare_sold(self):
        self.sold = self.sold + int(input('Introduceti suma pe care doriti sa o depuneti in cont: '))
        print(f'Soldul in urma depunerii este {self.sold}')

persoana_1 = Cont(1234, 'Fogoros Florin', 7000)
persoana_2 = Cont(1213, 'Asaftei Mihai', 9000)

persoana_1.afisare_sold()
persoana_1.debitare_cont()
persoana_1.creditare_sold()

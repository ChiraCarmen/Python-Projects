from datetime import datetime, timedelta


class Persoana:
    def __init__(self, nume, prenume, varsta):
        self.nume = nume
        self.prenume = prenume
        self.varsta = varsta


class Membru(Persoana):
    def __init__(self, nume, prenume, varsta, id, lista_carti):
        super().__init__(nume, prenume, varsta)
        self.id = id
        self.lista_carti = lista_carti

    def imprumuta_carte(self, cartefizica):
        self.lista_carti.append(cartefizica)
        cartefizica.data_retur = datetime.now() + timedelta(weeks=4)
        cartefizica.status = 'imprumutata'

    def returneaza_carte(self, cartefizica):
        self.lista_carti.remove(cartefizica)
        cartefizica.status = 'neimprumutata'


class Bibliotecar(Persoana):
    def __init__(self, nume, prenume, varsta, data_angajare):
        super().__init__(nume, prenume, varsta)
        self.data_angajare = data_angajare

    def check_carte(self, cartefizica):
        if cartefizica.status == 'neimprumutata':
            print(f'Cartea {cartefizica.titlu} de {cartefizica.autor} este disponibila')
            return True
        else:
            print(f'Cartea {cartefizica.titlu} de {cartefizica.autor} nu este disponibila')
            return False


class Carte:
    def __init__(self, titlu, autor):
        self.titlu = titlu
        self.autor = autor


class CarteFizica(Carte):
    def __init__(self, titlu, autor, locatie, status, editura, data_retur):
        super().__init__(titlu, autor)
        self.locatie = locatie
        self.status = status
        self.editura = editura
        self.data_retur = data_retur


class Notificare:
    def __init__(self, adresa_from, adresa_to, subiect, text_mail):
        self.adresa_from = adresa_from
        self.adresa_to = adresa_to
        self.subiect = subiect
        self.text_mail = text_mail

    def trimite_notificare(self):
        import smtplib

        server = smtplib.SMTP('localhost', 4444)   # conexiune cu serverul din cmd
        server.sendmail(from_addr=self.adresa_from,
                        to_addrs=self.adresa_to,
                        msg=f'{self.subiect}\n\n{self.text_mail}')
        server.quit()   # inchidem serverul

if __name__ == '__main__':
    membru = Membru('Ion', 'George', 25, 1234, [])
    bibliotecar = Bibliotecar('Voiculescu', 'Emanuel', 45, datetime(2008, 1, 1))
    cartefizica = CarteFizica('Ion', 'Liviu Rebreanu', 'raftul R2', 'neimprumutata', 'paralela 45', datetime.now())


    if bibliotecar.check_carte(cartefizica):
        membru.imprumuta_carte(cartefizica)

        if cartefizica.data_retur < datetime.now() + timedelta(weeks=10):
            notificare = Notificare('sala5@cotroceni.com', 'ion.george@company.com', 'Retur urgent',
                                    f'Va rugam sa returnati cartea {cartefizica.titlu} de {cartefizica.autor}')
            notificare.trimite_notificare()
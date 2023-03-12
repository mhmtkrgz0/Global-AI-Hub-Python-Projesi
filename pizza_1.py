class Pizza:
    def get_cost(self):
        return self.component.get_cost() \
            + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() \
            + ' ' + Pizza.get_description(self)

    class Klasik:
        name = 'Klasik Pizza'
        cost = 11

    class Margarita:
        name = 'Margarita'
        cost = 22

    class Turk:
        name = 'Türk Pizza'
        cost = 33

    class Sade:
        name = 'Sade Pizza'
        cost = 44


class Sos:
    class Zeytin:
        name = 'Zeytin'
        cost = 1

    class Mantar:
        name = 'Mantarlar'
        cost = 2

    class KeciPeyniri:
        name = 'Keçi Peyniri'
        cost = 3

    class Et:
        name = 'Et'
        cost = 4

    class Sogan:
        name = 'Soğan'
        cost = 5

    class Misir:
        name = 'Mısır'
        cost = 6


with open('Menu.txt', encoding='utf-8') as f:
    menu = f'{f.read()} \n 0 ile çıkış yapınız \n'
cost = 0
while True:
    menu_choice = int(input(f'{menu} \n'))
    match menu_choice:
        case 1:
            print(Pizza.Klasik.name)
            cost += Pizza.Klasik.cost
        case 2:
            print(Pizza.Margarita.name)
            cost += Pizza.Margarita.cost
        case 3:
            print(Pizza.Turk.name)
            cost += Pizza.Turk.cost
        case 4:
            print(Pizza.Sade.name)
            cost += Pizza.Sade.cost

        case 11:
            print(Sos.Zeytin.name)
            cost += Sos.Zeytin.cost
        case 12:
            print(Sos.Mantar.name)
            cost += Sos.Mantar.cost
        case 13:
            print(Sos.KeciPeyniri.name)
            cost += Sos.KeciPeyniri.cost
        case 14:
            print(Sos.Et.name)
            cost += Sos.Et.cost
        case 15:
            print(Sos.Sogan.name)
            cost += Sos.Sogan.cost
        case 16:
            print(Sos.Misir.name)
            cost += Sos.Misir.cost

        case 0:
            ccn = input('Kart Numarası: ')
            pw = input('Şifre: ')
            print('Ödeme Başarılı!')
            break

        case _:
            print('Yanlış Seçim yaptınız')
            menu_choice = input(menu)
    print(cost)

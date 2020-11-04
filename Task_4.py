from abc import abstractmethod


class IncorrectItem(Exception):
    def __init__(self, txt):
        self.txt = txt


class Storage:
    def __init__(self, location):
        self.location = location

    stored_items = {}

    # Функция принятия на склад техники
    def to_store(self, obj, amount):
        technic = f'{obj.function} {obj.technic_type}'
        print(f'{technic} arrived to the {self.location} storage \n')
        if technic not in self.stored_items:
            self.stored_items.update(obj.get_stored(amount))
        else:
            self.stored_items.update({technic: self.stored_items.pop(technic) + amount})

    # Функция отправки в другую компанию
    def to_send(self, company, obj, amount):
        technic = f'{obj.function} {obj.technic_type}'
        if technic in self.stored_items:
            if amount == self.stored_items.get(technic):
                if technic not in company.company_items:
                    company.company_items.update({technic: self.stored_items.pop(technic)})
                else:
                    company.company_items.update(
                        {technic: self.stored_items.pop(technic) + company.company_items.get(technic)})
                print(f'{technic} was sent to the {company.company_name} company \n')
            elif amount < self.stored_items.get(technic):
                if technic not in company.company_items:
                    company.company_items.update({technic: amount})
                else:
                    company.company_items.update(
                        {technic: amount + company.company_items.get(technic)})
                self.stored_items.update({technic: self.stored_items.pop(technic) - amount})
                print(f'{technic} was sent to the {company.company_name} company \n')
            else:
                print(f'There is only {self.stored_items.get(technic)} {technic} in storage, change the amount')
        else:
            print(f'There is no such item in storage')

    def __str__(self):
        stored_str = f'Items in {self.location} storage: \n'
        for i in self.stored_items.items():
            stored_str += f'{i[0]} - {i[1]} \n'
        return stored_str


class Company:
    def __init__(self, company_name):
        self.company_name = company_name

    company_items = {}

    def __str__(self):
        stored_str = f'{self.company_name} items: \n'
        for i in self.company_items.items():
            stored_str += f'{i[0]} - {i[1]} \n'
        return stored_str


class OfficeTechnics:
    @abstractmethod
    def __init__(self, technic_type, brand, function):
        # Не получилось сделать так, чтобы supply_type определялся в этом классе
        self.technic_type = technic_type
        self.brand = brand
        self.function = function

    def __str__(self):
        return f'{self.function} {self.technic_type}'

    def get_stored(self, amount):
        return {f'{self.function} {self.technic_type}': amount}


class Printer(OfficeTechnics):
    def __init__(self, brand, printer_type, technic_type='printer', function='printing'):
        super().__init__(brand, function, technic_type)
        self.printer_type = printer_type


class Xerox(OfficeTechnics):
    def __init__(self, brand, xerox_type, technic_type='xerox', function='copying'):
        super().__init__(brand, function, technic_type)
        self.is_compact = xerox_type


class Scanner(OfficeTechnics):
    def __init__(self, brand, scanner_type, technic_type='scanner', function='scanning'):
        super().__init__(brand, function, technic_type)
        self.scanner_type = scanner_type


printer_1 = Printer('Brother', 'laser')
xerox_1 = Xerox('Xerox', 'compact')
scanner_1 = Scanner('Epson', 'stationary')

trans_dict = {
    "printer": printer_1,
    "scanner": scanner_1,
    "xerox": xerox_1
}

storage_1 = Storage('London')
company_1 = Company('Hawlett Packard')

print(f'Here is the list of items you can interact: \n{printer_1} \n{xerox_1} \n{scanner_1}')
print('-'*300)
print(f'You can send them to the storage in {storage_1.location} and then to the company {company_1.company_name}.')
print('-'*300)
print('If you want to quit, please, input "q", the program will be finished after full iteration.')
print('-'*300)

# Реализовал выявление ошибки и через while, и через новый класс
while True:
    try:
        where_to = input(f'Please, input a place to send the item (storage, company): ').lower()
        if where_to != 'company' and where_to != 'storage' and where_to != 'q':
            raise IncorrectItem('You can input only "storage" or "company"')

        while True:
            user_item = input('Please, input the name of the item (printer, xerox, scanner), \n'
                              'which you would like to send somewhere: ').lower()
            if user_item == 'printer' or user_item == 'scanner' or user_item == 'xerox':
                tech_obj = trans_dict.get(user_item)
                break
            elif user_item == 'q':
                break
            else:
                print('You can input only "printer", "scanner" or "xerox"!')

        while True:
            how_many = input(f'Please, input, how much of {user_item}{"s" if user_item == "printer" or user_item == "scanner" else "es"} '
                             f'you would like to send to the {where_to}: ').lower()
            if how_many.isdecimal():
                how_many = int(how_many)
                break
            elif how_many == 'q':
                break
            else:
                print('You can input only positive numbers!')

        if where_to == 'q' or user_item == 'q' or how_many == 'q':
            break

        if where_to == 'storage':
            storage_1.to_store(tech_obj, how_many)
            print(storage_1)
        else:
            storage_1.to_send(company_1, tech_obj, how_many)
            print(company_1)
    except IncorrectItem as err:
        print(err)

print(storage_1)
print(company_1)

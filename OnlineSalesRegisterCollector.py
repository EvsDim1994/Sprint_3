import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items
    
    @property
    def number_items(self):
        return self.__number_items
    
    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.__name_items.append(name)
            self.__number_items += 1

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__name_items.remove(name)
            self.__number_items -= 1

    def check_amount(self):
        total = []
        for key in self.__item_price.keys():
            if key in self.__name_items:
                total.append(self.__item_price.get(key))
        if len(total) + 1 > 10:
            total_sum = sum(total) - sum(total)*0.1
        else:
            total_sum = sum(total)

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for key, value in self.__tax_rate.items():
            if key in self.__name_items and value == 20:
                twenty_percent_tax.append(key)
        for key in self.__item_price.keys():
            if key in twenty_percent_tax:
                total.append(self.__item_price.get(key))
        if len(total) + 1 > 10:
            total_tax = (sum(total) - sum(total)*0.1)*0.2
        else:
            total_tax = sum(total)*0.2
        return total_tax
    
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for key, value in self.__tax_rate.items():
            if key in self.__name_items and value == 10:
                ten_percent_tax.append(key)
        for key in self.__item_price.keys():
            if key in ten_percent_tax:
                total.append(self.__item_price.get(key))
        if len(total) + 1 > 10:
            total_tax = (sum(total) - sum(total)*0.1)*0.1
        else:
            total_tax = sum(total)*0.1
        return total_tax
    
    def total_tax(self):
        total = self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()
        return total

    @staticmethod
    def get_telephone_number(telephone_number):
        if not str(telephone_number).isdigit():
            raise ValueError('Необходимо ввести цифры')
        elif len(str(telephone_number)) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        else:
            phone = f'+7{telephone_number}'
            return phone
        
    @staticmethod
    def get_date_and_time():
        date_and_time = []
        now = datetime.datetime.now()
        date = [
                ["часы", (lambda x: x.hour)], 
                ["минуты", (lambda x: x.minute)], 
                ["день", (lambda x: x.day)], 
                ["месяц", (lambda x: x.month)], 
                ["год", (lambda x: x.year)]
                ]
        for i in date:
            date_and_time.append(f'{i[0]}: {i[1](now)}')
        return date_and_time
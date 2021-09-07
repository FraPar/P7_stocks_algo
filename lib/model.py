class Stocks_name:

    all_around_data = "I'm all around data!"

    def __init__(self, name):
        self.__name = name
        self.name_status = []

    def add__name_status(self, status):
        self.name_status.append(status)

    @property
    def name(self):
        print('Get called...')
        return self.__name
    
    @name.setter
    def name(self, value):
        print('Set called...')
        self.__name=value


class Stocks_price:

    all_around_data = "I'm all around data!"

    def __init__(self, price):
        self.__price = price
        self.price_status = []

    def add_price_status(self, status):
        self.price_status.append(status)

    @property
    def price(self):
        print('Get called...')
        return self.__price
    
    @price.setter
    def price(self, price):
        print('Set called...')
        self.__price=price


class Stocks_profit:

    all_around_data = "I'm all around data!"

    def __init__(self, profit):
        self.__profit = profit
        self.profit_status = []

    def add_status(self, status):
        self.profit_status.append(status)

    @property
    def profit(self):
        print('Get called...')
        return self.__profit
    
    @profit.setter
    def profit(self, profit):
        print('Set called...')
        self.__profit=profit


class All_Data:

    all_around_data = "I'm all around data!"

    def __init__(self, name, price, profit):
        self.__name = name
        self.__price = price
        self.__profit = profit
        
        self.data_status = []

    def add_status(self, status):
        self.data_status.append(status)

    @property
    def data(self):
        print('Get called...')
        return self.__name, self.__price, self.__profit,
    
    @data.setter
    def data(self, name, price, profit):
        print('Set called...')
        self.__name=name
        self.__price=price
        self.__profit=profit


d = Stocks_name('action-1')
e = Stocks_price('10.25')
f = Stocks_profit('210')
g = All_Data('action-1', '10.25','210')
# d = Stocks_name('action-1'), 
# e = Finance('action-2', '20.25','210')

print(Stocks_name)
print("d.***")
print(d.name)
d.name = "Didier"
print("d.name")
print(d.name)
print("e.***")
print(e.price)
e.price = "100.25"
print("e.price")
print(e.price)
print("f.***")
print(f.profit)
f.profit = "1200"
print("f.profit")
print(f.profit)

print("g.data")
print(g.data)
print(g.data[2])
print(All_Data(1,1,1).all_around_data)

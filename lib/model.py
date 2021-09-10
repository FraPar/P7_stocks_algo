class Stocks_name(object):
    """
    This class is for the Stocks name
    """

    stocks_name_public = "I'm a real stocks_name_public !"

    def __init__(self, name):
        self._name = name
        self.name_status = []

    def add_name_status(self, status):
        self.name_status.append(status)

    def _getname(self):
        print('Get called...')
        try:
            return self._name
        except AttributeError:
            print("There is no name in there")

    def _setname(self, new_name):
        print('Set called...')
        print(new_name)
        if len(new_name) < 0:
            self._name = "No name typed"
        else:
            self._name = new_name

    name = property(_getname, _setname)


class Stocks_price(object):

    stocks_price_public = "I'm a real stocks_price_public !"

    def __init__(self, price):
        self._price = price
        self.price_status = []

    def add_price_status(self, status):
        self.price_status.append(status)

    def _getprice(self):
        # print('Get called...')
        try:
            return self._price
        except AttributeError:
            print("There is no price for this")

    def _setprice(self, new_price):
        # print('Set called...')
        print(new_price)
        if len(new_price) <= 0:
            self._price = "No price tag"
        else:
            self._price = new_price

    price = property(_getprice, _setprice)


class Stocks_profit(object):

    stocks_profit_public = "I'm a real stocks_profit_public !"

    def __init__(self, profit):
        self._profit = profit
        self.profit_status = []

    def add_status(self, status):
        self.profit_status.append(status)

    def _getprofit(self):
        # print('Get called...')
        try:
            return self._profit
        except AttributeError:
            print("There is no money!")

    def _setprofit(self, new_profit):
        # print('Set called...')
        print(new_profit)
        if len(new_profit) < 0:
            self._profit = "No pain, no gain"
        else:
            self._profit = new_profit

    profit = property(_getprofit, _setprofit)


class All_Data(object):

    all_around_data = "I'm all around data!"

    def __init__(self, name, price, profit):
        self._name = name
        self._price = price
        self._profit = profit
        

    def add_status(self, status):
        self.data_status.append(status)

    def _getNameFromClass(self):
        return "blabla je veux son nom : {}".format(Stocks_name(self._name).name)

    def _getStocksData(self):
        # print('Get called...')
        try:
            return self._name, self._price, self._profit
        except AttributeError:
            print("There is a problem on the data")

    def _setStocksData(self, new_profit):
        # print('Set called...')
        print(new_profit)
        if len(new_profit) < 0:
            
            self._profit = "No data inside!"
        else:
            self._profit = new_profit

    stocks_data = property(_getStocksData, _setStocksData)


# d = Stocks_name('action-1')
# e = Stocks_price('10.25')
# f = Stocks_profit('210')
g = All_Data('action-1', '10.25','210')
# d = Stocks_name('action-1'), 
e = All_Data('action-2', '20.50','420')
print("e._name")
print(e._name)
# print(Stocks_name)
# print("d.***")
# print(d.name)
# d.name = "Didier"
# print("d.name")
# print(d.name)
# print("e.***")
# print(e.price)
# e.price = "100.25"
# print("e.price")
# print(e.price)
# print("f.***")
# print(f.profit)
# f.profit = "1200"
# print("f.profit")
# print(f.profit)



print("g.data")
print(g.stocks_data)
print(g.stocks_data[2])
print(g.all_around_data)
print(g._getNameFromClass())

print("e.data")
print(e.stocks_data)
print(e.stocks_data[2])
print(e.all_around_data)
print(e._getNameFromClass())
# FAIRE UNE SAVE DES DONNEES. LES TRAITEES ET SAUVER LE RESULTAT.



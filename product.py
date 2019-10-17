class Product:

    def __init__(self, name, description, price, stock):
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    def decrement_stock(self):
        self.stock = self.stock - 1

    def increment_stock(self):
        self.stock = self.stock + 1


class Toy(Product):

    def __init__(self, name, description, price, stock, manufacturer, recommendedAge, educational, chokingHazard):
        Product.__init__(name, description, price, stock)
        self.manufacturer = manufacturer
        self.recommendedAge = recommendedAge
        self.educational = educational
        self.chokingHazard = chokingHazard


class Book(Product):

    def __init__(self, name, description, price, stock, author, publisher, pageCount, hardCover):
        Product.__init__(name, description, price, stock)
        self.author = author
        self.publisher = publisher
        self.pageCount = pageCount
        self.hardCover = hardCover


class Household(Product):

    def __init__(self, name, description, price, stock, color, kitchenItem, bathroomItem):
        Product.__init__(name, description, price, stock)
        self.color = color
        self.kitchenItem = kitchenItem
        self.bathroomItem = bathroomItem


class Electronic(Product):

    def __init__(self, name, description, price, stock, batteryType, rechargeable, requiresAssembly):
        Product.__init__(name, description, price, stock)
        self.batteryType = batteryType
        self.rechargeable = rechargeable
        self.requiresAssembly = requiresAssembly



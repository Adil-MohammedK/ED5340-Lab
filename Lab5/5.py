class Bill:
    def __init__(self, name, purchase):
        self.name = name
        self.purchase = purchase

    def getPurchase(self):
        array = []
        items = self.purchase.split(",")
        # print(items)
        for item in items:
            array.append(item.split(" x "))
        # print(array)
        return array


class RestBill(Bill):
    def __init__(self, name, purchase, menu):
        super().__init__(name, purchase)
        self.menu = menu

    def getMenu(self):
        array = []
        items = self.menu.split(",")
        # print(items)
        for item in items:
            array.append(item.split(" - "))
        # print(array)
        return array

    def billTotal(self):
        orders = self.getPurchase()
        menus = self.getMenu()
        total = 0
        for x in range(len(orders)):
            if orders[x][0] == menus[x][0]:
                total += int(orders[x][1]) * int(menus[x][1])
        self.total = total
        print("Restaurant Bill total: ", total)


class GrocBill(Bill):
    def __init__(self, name, purchase, price_list):
        super().__init__(name, purchase)
        self.price_list = price_list

    def getPrice(self):
        array = []
        items = self.price_list.split(",")
        # print(items)
        for item in items:
            array.append(item.split(" "))
        # print(array)
        return array

    def billTotal(self):
        orders = self.getPurchase()
        menus = self.getPrice()
        total = 0
        for x in range(len(orders)):
            if orders[x][0] == menus[x][0]:
                total += int(orders[x][1]) * int(menus[x][1])
        self.total = total
        print("Grocery Bill total: ", total)


obj1 = RestBill("Hinata", "Item1 x 1,Item2 x 3,Item3 x 1",
                "Item1 - 100,Item2 - 70,Item3 - 250")

print(obj1.getMenu())
obj2 = GrocBill("Hinata", "Item1 x 1,Item2 x 3,Item3 x 1",
                "Item1 100,Item2 70,Item3 400")
print(obj2.getPrice())
obj1.billTotal()
obj2.billTotal()

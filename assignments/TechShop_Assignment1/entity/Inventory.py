class Inventory:
    def __init__(self, inventory_id, product, quantity_in_stock, last_stock_update):
        self.__InventoryID = inventory_id
        self.__Product = product
        self.__QuantityInStock = quantity_in_stock
        self.__LastStockUpdate = last_stock_update

    @property
    def Product(self):
        return self.__Product

    @property
    def QuantityInStock(self):
        return self.__QuantityInStock

    @QuantityInStock.setter
    def QuantityInStock(self, quantity):
        if quantity >= 0:
            self.__QuantityInStock = quantity
        else:
            raise Exception("Quantity must be a non-negative integer.")

    def AddToInventory(self, quantity):
        if quantity > 0:
            self.__QuantityInStock += quantity
        else:
            raise Exception("Quantity must be a positive integer.")

    def RemoveFromInventory(self, quantity):
        if 0 < quantity <= self.__QuantityInStock:
            self.__QuantityInStock -= quantity
        else:
            raise Exception("Invalid quantity to remove from inventory.")

    def UpdateStockQuantity(self, new_quantity):
        if new_quantity >= 0:
            self.__QuantityInStock = new_quantity
        else:
            raise Exception("New quantity must be a non-negative integer.")

    def IsProductAvailable(self, quantity_to_check):
        return quantity_to_check <= self.__QuantityInStock

    def GetInventoryValue(self):
        return self.__QuantityInStock * self.__Product.Price

    def ListLowStockProducts(self, threshold):
        if self.__QuantityInStock < threshold:
            return self.__Product

    def ListOutOfStockProducts(self):
        if self.__QuantityInStock == 0:
            return self.__Product

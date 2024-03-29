import random


# This class represents an object that contains two attributes: 
class Item:
    def __init__(self, size, value):
        self.size = size
        self.value = value

    def get_size(self):
        return self.size

    def get_value(self):
        return self.value
    
    def __str__(self):
        return '[s={};v={}]'.format(self.size, self.value)
    
    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.size == other.size and self.value == other.value


# This class contains the programming solution
class NonGASolutions: 
    @staticmethod
    def by_value_then_size(item_collection):
        sorted_items = sorted(item_collection.get_items(), key=lambda x: (x.get_value(), -x.get_size()), reverse=True)
        return ItemCollection(items=sorted_items)
    
    @staticmethod
    def by_size_then_value(item_collection):
        sorted_items = sorted(item_collection.get_items(), key=lambda x: (x.get_size(), -x.get_value()))
        return ItemCollection(items=sorted_items)
        
    @staticmethod
    def by_ratio_value_size(item_collection):
        sorted_items = sorted(item_collection.get_items(), key=lambda x: (x.get_value()/x.get_size()), reverse=True)
        return ItemCollection(items=sorted_items)


# This class represents a collection of items with sorting methods
class ItemCollection:
    def __init__(self, no_items=10, size=(1, 100), value=(1, 100), items=None):
        if items is None:
            self.items = self._generate_random_items(no_items, size, value)
        else:
            self.items = items
        
    def get_items(self):
        return self.items
    
    @staticmethod
    def _generate_random_items(no_items=10, size=(1, 100), value=(1, 100)):
        return [Item(random.randint(size[0], size[1]), random.randint(value[0], value[1])) for i in range(no_items)]
    
    def __repr__(self):
        return self.__str__()
        
    def __str__(self):
        response = ''
        for item in self.get_items():
            response += str(item) + '\t'
        return response

    def __eq__(self, other):
        if len(self.items) != len(other.items):
            return False
        for i in range(len(self.items)):
            if self.items[i] != other.items[i]:
                return False
        return True


# This class represents a container to place items in.
class Container:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []
    
    def set_items(self, items):
        self.items = items
        
    def get_items(self):
        return self.items
    
    def get_capacity(self):
        return self.capacity
    
    def get_total_size(self):
        if len(self.items) > 0:
            return sum(i.get_size() for i in self.items)
        else:
            return 0
    
    def fit_items(self, itemCollection):
        self.items = []
        size_used=0
        for item in itemCollection.get_items():
            if (size_used + item.get_size()) <= self.capacity:
                self.items.append(item)
                size_used += item.get_size()
    
    def get_total_value(self):
        if len(self.items) > 0:
            return sum(i.get_value() for i in self.items)
        else:
            return 0
        
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return 'Items:{}\nTotal Occupied Size:{}\nTotal Value:{}'.format(
            self.get_items(), self.get_total_size(), self.get_total_value())

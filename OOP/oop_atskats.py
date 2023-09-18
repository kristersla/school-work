class Menu:

    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
    
    def __repr__(self):
        return repr(f"Name = {self.name}, start time = {self.start_time}, end time = {self.end_time}")

    def calculate_bill(self, purchased_items):
        price = 0
        for i in purchased_items:
            price += self.items.get(i)
        return price

brunch = Menu("brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 11, 16)
early_bird = Menu("Early bird",{'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, 15, 18)
dinner = Menu("Dinner",{'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, 17, 18)
kids_menu = Menu("Kids menu",{'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 11, 21)


print(brunch)
print(brunch.calculate_bill(["pancakes", "home fries", "coffee"]))
print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))

class Franchise:

    def __init__(self, address, menus):

        self.address = address
        self.menus = menus
    
    def __repr__(self):
        return repr(f"Address = {self.address}")
    
    def available_menus(self, time):
        for i in self.menus:
            if i.start_time <= time and i.end_time >= time:
                print(i.name)

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids_menu])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids_menu])

flagship_store.available_menus(11)
new_installment.available_menus(16)

print(flagship_store)


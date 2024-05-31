class Computer:
    name = "Computer"

    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def set_name(self, new_name):
        self.name = new_name

    def make_sound(self):
        print(f"{self.name} makes sounds")


class Processor:
    def __init__(self, name, cores, clock_speed):
        self.__name = name
        self.__cores = cores
        self.__clock_speed = clock_speed

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_cores(self):
        return self.__cores

    def set_cores(self, cores):
        self.__cores = cores

    def get_clock_speed(self):
        return self.__clock_speed

    def set_clock_speed(self, clock_speed):
        self.__clock_speed = clock_speed


class GraphicsCard:
    def __init__(self, name, memory, clock_speed):
        self.__name = name
        self.__memory = memory
        self.__clock_speed = clock_speed

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_memory(self):
        return self.__memory

    def set_memory(self, memory):
        self.__memory = memory

    def get_clock_speed(self):
        return self.__clock_speed

    def set_clock_speed(self, clock_speed):
        self.__clock_speed = clock_speed


class Ram:
    def __init__(self, capacity, speed):
        self.__capacity = capacity
        self.__speed = speed

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed


class Macbook(Computer):
    def __init__(self, brand, model, year, weight, battery_life, graphics_card, processor, ram):
        super().__init__(brand, model, year)
        self.weight = weight
        self.battery_life = battery_life
        self.graphics_card = graphics_card
        self.processor = processor
        self.ram = ram

f = Macbook("Apple Macbookpro 13", "m1", 2021, "1.25 kg", "8 hours", GraphicsCard("M1 Pro 14-Core GPU", "16 GB", "3.2 GHz"), Processor("Apple M1", 8, "3.2 GHz"), Ram("16 GB", "3200 MHz"))
g = Macbook("Apple Macbookpro 13", "m1", 2021, "2 kg", "16 hours", GraphicsCard("M2 Pro 14-Core GPU", "32 GB", "5 GHz"), Processor("Apple M2", 16, "4 GHz"), Ram("32 GB", "4600 MHz"))

def compare_components(f, g):
    print("Weight:")
    if f.weight > g.weight:
        print(f"{f.weight} kg > {g.weight} kg")
    elif f.weight < g.weight:
        print(f"{f.weight} kg < {g.weight} kg")
    else:
        print(f"{f.weight} kg == {g.weight} kg")

    print("\nBattery life:")
    if f.battery_life > g.battery_life:
        print(f"{f.battery_life} hours > {g.battery_life} hours")
    elif f.battery_life < g.battery_life:
        print(f"{f.battery_life} hours < {g.battery_life} hours")
    else:
        print(f"{f.battery_life} hours == {g.battery_life} hours")

    print("\nGraphics Card Clock Speed:")
    if f.graphics_card.get_clock_speed() > g.graphics_card.get_clock_speed():
        print(f"{f.graphics_card.get_clock_speed()} GHz < {g.graphics_card.get_clock_speed()} GHz")
    elif f.graphics_card.get_clock_speed() < g.graphics_card.get_clock_speed():
        print(f"{f.graphics_card.get_clock_speed()} GHz > {g.graphics_card.get_clock_speed()} GHz")
    else:
        print(f"{f.graphics_card.get_clock_speed()} GHz == {g.graphics_card.get_clock_speed()} GHz")
    
    print("\nProcessor Clock Speed:")
    if f.processor.get_clock_speed() > g.processor.get_clock_speed():
        print(f"{f.processor.get_clock_speed()} GHz > {g.processor.get_clock_speed()} GHz")
    elif f.processor.get_clock_speed() < g.processor.get_clock_speed():
        print(f"{f.processor.get_clock_speed()} GHz < {g.processor.get_clock_speed()} GHz")
    else:
        print(f"{f.processor.get_clock_speed()} GHz == {g.processor.get_clock_speed()} GHz")

    print("\nRAM Speed:")
    if f.ram.get_speed() > g.ram.get_speed():
        print(f"{f.ram.get_speed()} MHz < {g.ram.get_speed()} MHz")
    elif f.ram.get_speed() < g.ram.get_speed():
        print(f"{f.ram.get_speed()} MHz > {g.ram.get_speed()} MHz")
    else:
        print(f"{f.ram.get_speed()} MHz == {g.ram.get_speed()} MHz")

compare_components(f, g)
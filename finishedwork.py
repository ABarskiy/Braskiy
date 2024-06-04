class Computer:
    def __init__(self, brand, model, year, weight, battery_life, graphics_card, processor, ram):
        self._brand = brand
        self._model = model
        self._year = year
        self._weight = weight
        self._battery_life = battery_life
        self.graphics_card = graphics_card
        self.processor = processor
        self.ram = ram

class Processor:
    def __init__(self, brandcores: str, cores: int, frequencycores: float):
        self._brandcores = brandcores
        self._cores = cores
        self._frequencycores = frequencycores

    def set_brandcores(self, brandcores: str) -> None:
        self._brandcores = brandcores
        
    def get_brandcores(self) -> str:
        return self._brandcores

    def set_cores(self, cores: int) -> None:
        self._cores = cores
        
    def get_cores(self) -> int:
        return self._cores

    def set_frequencycores(self, frequencycores: float) -> None:
        self._frequencycores = frequencycores

    def get_frequencycores(self) -> float:
        return self._frequencycores

    def __str__(self) -> str:
        return f"Процессор: {self._brandcores}\nКоличество ядер: {self._cores}\nЧастота: {self._frequencycores} ГГц"


class GraphicsCard:
    def __init__(self, brandvideocard: str, videocardgb: int, frequencyvideocard: float):
        self._brandvideocard = brandvideocard
        self._videocardgb = videocardgb
        self._frequencyvideocard = frequencyvideocard
    
    def set_brandvideocard(self, brandvideocard: str) -> None:
        self._brandvideocard = brandvideocard
    
    def get_brandvideocard(self) -> str:
        return self._brandvideocard

    def set_videocardgb(self, videocardgb: int) -> None:
        self._videocardgb = videocardgb
    
    def get_videocardgb(self) -> int:
        return self._videocardgb

    def set_frequencyvideocard(self, frequencyvideocard: float) -> None:
        self._frequencyvideocard = frequencyvideocard
    
    def get_frequencyvideocard(self) -> float:
        return self._frequencyvideocard


    def __str__(self) -> str:
        return f"Бренд видеокарты: {self._brandvideocard}\nКол-во гигабайт видеокарты: {self._videocardgb}\nЧастота видеокарты: {self._frequencyvideocard} ГГц"



class RAM:
    def __init__(self, gigabytes: str, frequency: float):
        self._gigabytes = gigabytes
        self._frequency = frequency
    
    def set_brand(self, gigabytes: str) -> None:
        self._gigabytes = gigabytes
    
    def get_brand(self) -> str:
        return self._gigabytes

    def set_cores(self, cores: int) -> None:
        self._cores = cores
    
    def get_cores(self) -> int:
        return self._cores

    def set_frequency(self, frequency: float) -> None:
        self._frequency = frequency
    
    def get_frequency(self) -> float:
        return self._frequency


    def __str__(self) -> str:
        return f"Кол-во гигабайт: {self._gigabytes}\nЧастота: {self._frequency} ГГц"

class Macbook(Computer):
    def __init__(self, brand, model, year, weight, battery_life, graphics_card, processor, ram):
        super().__init__(brand, model, year, weight, battery_life, graphics_card, processor, ram)
      
    def print_info_computer(self):
        print("Характеристика макбука")
        print(f"Бренд: {self._brand}")
        print(f"Модель: {self._model}")
        print(f"Год выпуска: {self._year}")
        print(f"Вес макбука: {self._weight}")
        print(f"Время работы батареи: {self._battery_life}")
        print(self.graphics_card)
        print(self.processor)
        print(self.ram)
        
class Macbook2(Computer):
    def __init__(self, brand, model, year, weight, battery_life, graphics_card, processor, ram):
        super().__init__(brand, model, year, weight, battery_life, graphics_card, processor, ram)
      
    def print_info_computer(self):
        print("Характеристика макбука")
        print(f"Бренд: {self._brand}")
        print(f"Модель: {self._model}")
        print(f"Год выпуска: {self._year}")
        print(f"Вес макбука: {self._weight}")
        print(f"Время работы батареи: {self._battery_life}")
        print(self.graphics_card)
        print(self.processor)
        print(self.ram)
        
    def compare_computer(self, other_computer):
        differences = []

        def compare_attributes(attr_name, attr_value, other_value):
            if attr_value != other_value:
                differences.append(f"{attr_name}: {attr_value} не совпадает с {other_value}")

        print(f"Сравнение макбука {self._brand} {self._model} и {other_computer._brand} {other_computer._model}:")

        compare_attributes("Год", self._year, other_computer._year)
        
        compare_attributes("Вес ноутбука", self._weight, other_computer._weight)
        compare_attributes("Время работы батареи", self._battery_life, other_computer._battery_life)

        compare_attributes("Графический процессор", self.graphics_card.get_brandvideocard(),  other_computer.graphics_card.get_brandvideocard())
        compare_attributes("Кол-во гигабайт видеокарты", self.graphics_card.get_videocardgb(),  other_computer.graphics_card.get_videocardgb())
        compare_attributes("Частота видеокарты", self.graphics_card.get_frequencyvideocard(),  other_computer.graphics_card.get_frequencyvideocard())
        
        
        compare_attributes("Процессор", self.processor.get_brandcores(), other_computer.processor.get_brandcores())
        compare_attributes("Кол-во ядер процессора", self.processor.get_cores(), other_computer.processor.get_cores())
        compare_attributes("Частота процессора", self.processor.get_frequencycores(), other_computer.processor.get_frequencycores())
        
        compare_attributes("RAM", self.ram.get_brand(), other_computer.ram.get_brand())

        if differences:
            print("Обнаружены различия:")
            for difference in differences:
                print(difference)
        else:
            print("Все характеристики совпадают.")

graphics_card1 = GraphicsCard("M1 Pro 14-Core GPU", "16 GB", "3.2 GHz")
processor1 = Processor("Apple M1", "8", "3.2 GHz")
ram1 = RAM("16 GB", "3200 MHz")

graphics_card2 = GraphicsCard("M2 Pro 14-Core GPU", "32 GB", "5 GHz")
processor2 = Processor("Apple M2", "16", "4 GHz")
ram2 = RAM("32 GB", "4600 MHz")

macbook = Macbook("Apple Macbookpro 13", "M1", "2021", "1.25 kg", "8 hours", graphics_card1, processor1, ram1)
macbook2 = Macbook2("Apple Macbookpro 15", "M2", "2022", "2 kg", "16 hours", graphics_card2, processor2, ram2)

macbook.print_info_computer()
print()
macbook2.print_info_computer()
print()
print("Сравнение двух макбуков: ")
macbook2.compare_computer(macbook)
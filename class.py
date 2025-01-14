# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Bottle:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Бутылка"

        :param capacity_volume: Объем бутылки
        :param occupied_volume: Объем занимаемой жидкости

        Примеры:
        >>> bottle = Bottle(750, 250)
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем бутылки должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем бутылки должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def is_empty_bottle(self) -> bool:
        """
        Функция которая проверяет является ли бутылка пустой

        :return: Является ли бутылка пустой

        Примеры:
        >>> bottle = Bottle(750, 0)
        >>> bottle.is_empty_bottle()
        """
        ...

    def add_water_to_bottle(self, water: float) -> None:
        """
        Добавление воды в бутылку.
        :param water: Объем добавляемой жидкости

        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в бутылке, то вызываем ошибку

        Примеры:
        >>> bottle = Bottle(750, 250)
        >>> bottle.add_water_to_bottle(300)
        """
        ...

    def remove_water_from_bottle(self, estimate_water: float) -> None:
        """
        Извлечение воды из бутылки.

        :param estimate_water: Объем извлекаемой жидкости
        :raise ValueError: Если количество извлекаемой жидкости превышает количество воды в бутылке,
        то возвращается ошибка.

        :return: Объем реально извлеченной жидкости

        Примеры:
        >>> bottle = Bottle(750, 500)
        >>> bottle.remove_water_from_bottle(200)
        """
        ...

class Account:
    def __init__(self, account_number: str, balance: float):
        """
        Создание и подготовка к работе объекта "Счет"
        :param account_number: Номер счета
        :param balance: Баланс счета

        Примеры:
        >>> account = Account("1234567890", 1000.50)
        """
        if not isinstance(account_number, str):
            raise TypeError("Номер счета должен быть типа str")
        self.account_number = account_number

        if not isinstance(balance, (int, float)):
            raise TypeError("Баланс счета должен быть типа int или float")
        self.balance = balance

    def is_empty_account(self) -> bool:
        """
        Функция которая проверяет пуст ли счет

        :return: Является ли счет пустым

        Примеры:
        >>> account = Account("1234567890", 0)
        >>> account.is_empty_account()
        """
        ...

    def deposit(self, amount: float) -> None:
        """
        Внесение денег на счет.
        :param amount: Сумма для внесения

        Примеры:
        >>> account = Account("1234567890", 1000.50)
        >>> account.deposit(500.25)
        """
        ...

    def withdraw(self, amount: float) -> None:
        """
        Снятие денег со счета.

        :param amount: Сумма для снятия
        :raise ValueError: Если запрашиваемая сумма для снятия превышает баланс счета,
        то возвращается ошибка.

        Примеры:
        >>> account = Account("1234567890", 1000.50)
        >>> account.withdraw(200.75)
        """
        ...

class House:
    def __init__(self, area: float, floors: int, location: str):
        """
        Создание и подготовка к работе объекта "Дом"
        :param area: Площадь дома
        :param floors: Количество этажей
        :param location: Местоположение дома

        Примеры:
        >>> house = House(150.5, 2, "City Center")  # инициализация объекта класса
        """
        if not isinstance(area, (int, float)):
            raise TypeError("Площадь дома должна быть типа int или float")
        if area <= 0:
          raise ValueError("Площадь дома должна быть положительным числом")
        self.area = area

        if not isinstance(floors, int):
            raise TypeError("Количество этажей должно быть типа int")
        if floors <= 0:
            raise ValueError("Количество этажей должно быть положительным числом")
        self.floors = floors

        if not isinstance(location, str):
            raise TypeError("Местоположение дома должно быть типа str")
        self.location = location

    def is_house_empty(self) -> bool:
        """
        Функция, которая проверяет является ли дом пустым

        :return: Является ли дом пустым

        Примеры:
        >>> house = House(150.5, 2, "City Center")
        >>> house.is_house_empty()
        """
        ...

    def build_additional_floor(self) -> None:
        """
        Построение дополнительного этажа

        Примеры:
        >>> house = House(150.5, 2, "City Center")
        >>> house.build_additional_floor()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass

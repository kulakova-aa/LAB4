
class TransportVehicle:
    """
    Базовый класс для транспортных средств.
    Реализует основные свойства и методы для всех типов транспортных средств.
    """

    def __init__(self, make: str, model: str, year: int):
        """
        Инициализация транспортного средства.

        :param make: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска.
        """
        self._make = make
        self._model = model
        self._year = year

    def display_info(self) -> str:
        """
        Возвращает строку с основной информацией о транспортном средстве.

        :return: Строка с информацией.
        """
        return f"{self._year} {self._make} {self._model}"

    def __str__(self) -> str:
        """
        Магический метод для строкового представления объекта.
        """
        return self.display_info()

    def __repr__(self) -> str:
        """
        Магический метод для строкового представления объекта в отладке.
        """
        return (f"{self.__class__.__name__}(make={self._make!r}, "
                f"model={self._model!r}, year={self._year!r})")


class Car(TransportVehicle):
    """
    Класс для легковых автомобилей, наследующий от TransportVehicle.
    """

    def __init__(self, make: str, model: str, year: int, doors: int):
        """
        Инициализация легкового автомобиля.

        :param make: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска.
        :param doors: Количество дверей.
        """
        super().__init__(make, model, year)
        self.__doors = doors  # инкапсулируемый атрибут

    def display_info(self) -> str:
        """
        Расширение отображения информации о машине.
        """
        base_info = super().display_info()
        return f"{base_info}, doors: {self.__doors}"

    def get_doors(self) -> int:
        """
        Получить количество дверей автомобиля.

        :return: количество дверей.
        """
        return self.__doors

    def __str__(self) -> str:
        """
        Перегрузка метода для более подробного вывода.
        """
        return f"Car: {self.display_info()}"

    def __repr__(self) -> str:
        """
        Обеспечивает точное представление объекта.
        """
        return (f"{self.__class__.__name__}(make={self._make!r}, model={self._model!r}, "
                f"year={self._year!r}, doors={self.__doors!r})")


class Truck(TransportVehicle):
    """
    Класс для грузовых автомобилей, наследующий от TransportVehicle.
    """

    def __init__(self, make: str, model: str, year: int, payload_capacity: float):
        """
        Инициализация грузового автомобиля.

        :param make: Марка грузовика.
        :param model: Модель.
        :param year: Год выпуска.
        :param payload_capacity: Грузоподъемность в тоннах.
        """
        super().__init__(make, model, year)
        self.__payload_capacity = payload_capacity  # инкапсулированный атрибут

    def display_info(self) -> str:
        """
        Расширение информации для грузовика.
        """
        base_info = super().display_info()
        return f"{base_info}, payload capacity: {self.__payload_capacity} tons"

    def get_payload_capacity(self) -> float:
        """
        Получить грузоподъемность.

        :return: грузоподъемность в тоннах.
        """
        return self.__payload_capacity

    def __str__(self) -> str:
        """
        Перегрузка __str__ для более информативного вывода.
        """
        return f"Truck: {self.display_info()}"

    def __repr__(self) -> str:
        """
        Более точное представление объекта для отладки.
        """
        return (f"{self.__class__.__name__}(make={self._make!r}, model={self._model!r}, "
                f"year={self._year!r}, payload_capacity={self.__payload_capacity!r})")

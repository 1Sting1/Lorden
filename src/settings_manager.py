import os
import json
import uuid
from settings import settings

class settings_manager(object):
    __file_name = "../settings.json"
    __unique_number = 1
    __data = {}
    __settings = settings()

    #создание экземляра класса и контроль, что он будет только один
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(settings_manager, cls).__new__(cls)
        return cls.instance


    def __init__(self) -> None:
        self.__unique_number = uuid.uuid4()

    #получение уникального значения в формате строки
    @property
    def unique_number(self) -> str:
        return str(self.__unique_number.hex)

    #открытие файла с настройками
    #проверка на ошибки при подаче аргумента,

    def opener(self, file_name: str) -> bool:
        if not isinstance(file_name, str):
            raise Exception("Проверьте аргумент!")

        if file_name == "":
            raise Exception("Проверьте аргумент!!")

        self.__file_name = file_name.strip()

        try:
            self.__open()
        except:
            return False

        return True

    #получение словаря с настройками
    @property
    def data(self) -> {}:
        return self.__data

    #приватная функция для создания экземляра класса settings
    def __convert(self):

        #данных нет
        if len(self.__data) == 0:
            raise Exception("Проблема создания класса settings")

        fields = self.__settings.get_data_keys

        #данные неполные, счтиатем то что есть, и исключим Exception
        if len(self.__data) < len(fields):
            for field in fields:
                if field in self.__data:
                    value = self.__data[field]
                    setattr(self.__settings, field, value)
            raise Exception("Мало входных данных")

        #иначе мы заполняем все поля без лишних сравнений
        else:
            for field in fields:
                value = self.__data[field]
                setattr(self.__settings, field, value)

    @property
    def __open(self):
        #os.path для построения путей
        file_path = os.path.split(__file__)
        settings_file = "%s/%s" % (file_path[0], self.__file_name)
        if not os.path.exists(settings_file):
            raise Exception(
                "Проверьте аргумент",
                settings_file)

        with open(settings_file, "r") as read_file:
            self.__data = json.load(read_file)
            self.__convert()
            print(self.__data)


import unittest
from src.settings import settings
from src.settings_manager import settings_manager

class TestSettings(unittest.TestCase):

    def test_check_create_manager(self):
        manager1 = settings_manager()
        manager2 = settings_manager()

        self.assertEqual(manager1.unique_number, manager2.unique_number)

    def test_check_json_invalid_path(self):
        #создание экземпляра класса
        man = settings_manager()

        #неправильный путь к файлу и проба на считывание
        file_name = "lo/other_dir/settings.json"
        self.assertTrue(man.opener(file_name))
        self.assertEqual(man.data, {})

    def test_check_json_valid_path(self):
        #создание экземпляра класса
        man = settings_manager()

        #путь к файлу и проба на считывание
        file_name = "../settings.json"
        self.assertFalse(man.opener(file_name))
        self.assertNotEqual(man.data, {})

    def test_settings_properties_initial_values(self):
        #создание экземпляра класса settings
        settings_obj = settings()

        #проверка начальных значений полей
        self.assertEqual(settings_obj.inn, "")
        self.assertEqual(settings_obj.bank_account, "")
        self.assertEqual(settings_obj.kor_bank_account, "")
        self.assertEqual(settings_obj.bik, "")
        self.assertEqual(settings_obj.product, "")
        self.assertEqual(settings_obj.company, "")

    def test_settings_properties_set_values(self):
        #создание экземпляра класса settings
        settings_obj = settings()

        #проверка сеттеров и геттеров
        settings_obj.inn = "123456789012"
        settings_obj.bank_account = "12345678901"
        settings_obj.kor_bank_account = "12345678901"
        settings_obj.bik = "123456789"
        settings_obj.product = "Product A"
        settings_obj.company = "ABC Corp"

        self.assertEqual(settings_obj.inn, "123456789012")
        self.assertEqual(settings_obj.bank_account, "12345678901")
        self.assertEqual(settings_obj.kor_bank_account, "12345678901")
        self.assertEqual(settings_obj.bik, "123456789")
        self.assertEqual(settings_obj.product, "Product A")
        self.assertEqual(settings_obj.company, "ABC Corp")

    def test_settings_exceptions_invalid_values(self):
        #создание экземпляра класса settings
        settings_obj = settings()

        #проверка некорректных данных
        with self.assertRaises(Exception):
            settings_obj.inn = "12345678901" # Некорректная длина
        with self.assertRaises(Exception):
            settings_obj.bank_account = "123456"  # Некорректная длина
        with self.assertRaises(Exception):
            settings_obj.kor_bank_account = "123456"  # Некорректная длина
        with self.assertRaises(Exception):
            settings_obj.bik = "12345678" # Некорректная длина
        with self.assertRaises(Exception):
            settings_obj.company = "ABC"  # Некорректная длина

    def test_settings_manager_exceptions_nonexistent_file(self):
        #несуществующий файл
        man = settings_manager()
        with self.assertRaises(Exception):
            man.opener("nesush.json")

    def test_settings_manager_exceptions_invalid_settings_file(self):
        #некорректный форматом данных
        man = settings_manager()
        with self.assertRaises(Exception):
            man.opener("invalid_settings.json")

    def test_unique_number_type(self):
        #уникальный ли номера менеджера настроек
        manager = settings_manager()
        self.assertIsInstance(manager.unique_number, str)

    def test_settings_manager_opener_type(self):
        #проверка типа возвращаемого значения метода opener
        man = settings_manager()
        self.assertIsInstance(man.opener("settings.json"), bool)

    def test_settings_manager_singleton(self):
        #проверка, что менеджер настроек является синглтоном
        manager1 = settings_manager()
        manager2 = settings_manager()
        self.assertIs(manager1, manager2)

    def test_settings_opener_invalid_argument(self):
        #проверка выброса исключения при передаче некорректного аргумента в метод opener
        man = settings_manager()
        with self.assertRaises(Exception):
            man.opener(123)

if __name__ == "__main__":
    unittest.main()

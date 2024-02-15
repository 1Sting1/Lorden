

class settings:
    __inn = ""
    __bank_account = ""
    __kor_bank_account = ""
    __bik = ""
    __product = ""
    __company = ""

    #получение поля inn
    @property
    def inn(self):
        return self.__inn

    #получение поля bank_account
    @property
    def bank_account(self):
        return self.__bank_account

    #получение поля korr_bank_account
    @property
    def kor_bank_account(self):
        return self.__kor_bank_account

    #получение поля bik
    @property
    def bik(self):
        return self.__bik

    #получение поля product
    @property
    def product(self):
        return self.__product

    #получения поле company
    @property
    def company(self):
        return self.__company


        # Сеттер inn
    @inn.setter
    def inn (self, value: str):
        if not isinstance(value, str) and len(value) == 12 and value.isnumeric():
            raise Exception("Проверьте аргумент!")

        self.__inn = value.strip()

    # Сеттер для bank_account
    @bank_account.setter
    def bank_account(self, value: str):
        if not isinstance(value, str) and len(value) == 11 and value.isnumeric():
            raise Exception("Проверьте аргумент!")

        self.__bank_account = value.strip()

    # Сеттер для kor_bank_account
    @kor_bank_account.setter
    def kor_bank_account(self, value: str):
        if not isinstance(value, str) and len(value) == 11 and value.isnumeric():
            raise Exception("Проверьте аргумент!")

        self.__kor_bank_account = value.strip()

    # Сеттер для bik
    @bik.setter
    def bik(self, value: str):
        if not isinstance(value, str) and len(value) == 9 and value.isnumeric():
            raise Exception("Проверьте аргумент!")

        self.__bik = value.strip()

    # Сеттер для product
    @product.setter
    def product(self, value: str):
        if not isinstance(value, str):
            raise Exception("Проверьте аргумент")

        self.__product = value.strip()

    # Сеттер для company
    @company.setter
    def company(self, value: str):
        if not isinstance(value, str) and len(value) == 5:
            raise Exception("Проверьте аргумент")

        self.__company = value.strip()
        
        
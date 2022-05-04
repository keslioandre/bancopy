from datetime import date
from utils.helper import str_para_date, date_para_str

class Cliente:

    contador: int = 101

    def __init__(self: object, nome: str, cpf: str, email: str, data_nascimento: str) -> None:
        self.__codigo = Cliente.contador
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__data_nascimento: date = str_para_date(data_nascimento)
        self.__data_cadastro: date = date.today()
        Cliente.contador += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def email(self: object) -> str:
        return self.__email

    @property
    def cpf(self: object) -> str:
        return self.__cpf

    @property
    def data_nascimento(self: object) -> str:
        return date_para_str(self.__data_nascimento)

    @property
    def data_cadastro(self: object) -> str:
        return date_para_str(self.__data_cadastro)

    def __str__(self: object) -> str:
        return f'Código: {self.codigo}\n Nome: {self.nome}\n Data Nascimento: {self.data_nascimento} ' \
               f'\n Cadastro: {self.data_cadastro}'

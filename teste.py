from models.cliente import Cliente
from models.conta import Conta

jose: Cliente = Cliente('Jose Maria', '123.456.789-99', 'jose@email.com', '04/10/1980')
# print(jose)

contaf: Conta = Conta(jose)
print(contaf)
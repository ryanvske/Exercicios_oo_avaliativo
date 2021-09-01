from classes.conta_bancaria import Conta_bancaria
from classes.conta_corrente import Conta_corrente
from classes.conta_poupanca import Conta_poupanca

print('         Menu')
print('1.Cadastrar conta poupança')
print('2.Cadastrar conta corrente')
print('3.Aumentar limite')
print('4.Realizar deposito')
print('5.Fazer saque')
print()

escolha_menu = input('Número:')

if escolha_menu == '1':
    Conta_bancaria.cadastrar_poupanca(str)
if escolha_menu == '2':
    Conta_bancaria.cadastrar_corrente(str)
if escolha_menu == '4':
    Conta_bancaria.depositar(str)
else:
    print('Opção não encontrada no menu.')


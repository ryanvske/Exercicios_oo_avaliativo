from classes.conta_bancaria import Conta_bancaria
from classes.conta_corrente import Conta_corrente
from classes.conta_poupanca import Conta_poupanca

print('         Menu')
print('1.Cadastrar conta poupança')
print('2.Cadastrar conta corrente')
print('3.Aumentar limite')
print('4.Realizar deposito')
print('5.Fazer saque')
print('6.Listar contas poupança')
print('0.Sair')
print()

while True:
    escolha_menu = input('Número:')
    print()

    if escolha_menu == '1':
        Conta_bancaria.cadastrar_poupanca(str)
    elif escolha_menu == '2':
        Conta_bancaria.cadastrar_corrente(str)
    elif escolha_menu == '3':
        Conta_bancaria.aumentar_limite(str)
    elif escolha_menu == '4':
        Conta_bancaria.depositar(str)
    elif escolha_menu == '5':
        Conta_bancaria.sacar(str)
    elif escolha_menu == '0':
        break


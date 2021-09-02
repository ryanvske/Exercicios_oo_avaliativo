class Conta_bancaria:

    def __init__(self):
        super(Conta_bancaria, self).__init__()
        self.nome = ''
        self.numero = ''
        self.cpf = ''
        self.limite = ''
        self.saldo = ''


    def depositar(self):
        input('Quanto deseja depositar?>')

    def sacar(self):
        input('Quanto deseja sacar?>')

    def cadastrar_poupanca(self):
        print('Cadastrando conta poupança.')
        poupanca_nome = input('Nome:')
        poupanca_numero =input('Número:')
        poupanca_cpf =input('cpf:')

    def cadastrar_corrente(self):
        print('Cadastrando conta corrente.')
        corrente_nome =input('Nome:')
        corrente_numero =input('Número:')
        corrente_cpf = input('cpf:')
        
    def aumentar_limite(self):
        print('Aumentar limite.')
        limite = input('Limite: ')

    def dados_poupanca(self):
        print('Cadastro concluido: '+ poupanca_nome,'/'+ poupanca_numero,'/' + poupanca_cpf)

    def dados_corrente(self):
        print('Cadastro concluido: ' + corrente_nome, '/' + corrente_numero,'/' + corrente_cpf)

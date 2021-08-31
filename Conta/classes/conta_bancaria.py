class Conta_bancaria:

    def __init__(self,nome,numero,cpf):
        super(Conta_bancaria, self).__init__()
        self.nome = nome
        self.numero = numero
        self.cpf = cpf

    def set_nome(self):
        input('Nome:')
        return

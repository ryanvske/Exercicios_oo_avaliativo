class Unidade_federativa:

    def __init__(self):
        self.__lista_uf = []
        self.__uf = ''

        self.lista_uf = ['SantaCatarina-SC',
                         'SãoPaulo-SP',
                         'Sergipe-SE',
                         'Tocantins-TO']


    def get_lista_uf(self):
        return self.__lista_uf

    def get_uf(self):
        return self.__uf

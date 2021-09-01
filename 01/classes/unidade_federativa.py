class Unidade_federativa:
    @staticmethod
    def get_lista_uf():
        ufs =['Santa_Catarina-SC', 'Sao_Paulo-SP', 'Rio_de_Janeiro-RJ']
        print(ufs)
    @staticmethod
    def get_uf():
        ufs =['Santa_Catarina-SC', 'Sao_Paulo-SP', 'Rio_de_Janeiro-RJ']
        uf=input('Qual UF devo retornar?>')

        if (uf=='SC'):
            print(ufs[0])
        elif (uf=='SP'):
            print(ufs[1])
        elif (uf=='RJ'):
            print(ufs[2])
        else:
            print('UF não reconhecida.')

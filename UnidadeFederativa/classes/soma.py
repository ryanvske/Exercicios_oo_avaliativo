class soma:
    @staticmethod
    def soma(vetor_valores):
        if len(vetor_valores) < 1:
            return None

        total = 0
        for valor in vetor_valores:
            total = total + valor

        return total
    
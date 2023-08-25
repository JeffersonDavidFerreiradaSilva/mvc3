class cadastro:
    @staticmethod
    def obter_dados_aluno():
        nome = input("DIGITE O NOME DO ALUNO: ")
        idade = int(input("DIGITE A IDADE DO ALUNO: "))
        peso = float(input("DIGITE O PESO DO ALUNO: "))
        return nome,idade,peso
    @staticmethod
    def mostrar_menssagem(menssagem):
        print(menssagem)
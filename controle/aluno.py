from model.aluno import aluno_model
from view.pagina_cadastro_aluno import cadastro

class aluno():

    def __init__(self):

        self.model = aluno_model
        self.view = cadastro()
    

    def salvando_aluno(self):
        nome,idade,peso = self.view.obter_dados_aluno()
        self.model.salvar_aluno()
        self.view.mostrar_menssagem("ALUNO CADASTRDO COM SUCESSO!")
        
        
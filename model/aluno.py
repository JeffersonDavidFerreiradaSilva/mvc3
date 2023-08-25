import pymysql.cursors

class aluno_model():

    def __init__(self):
        self.conexao = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = '@Cursos21',
            database= 'serpro',
            cursorclass= pymysql.cursors.DictCursor

        )
      
    def salvar_aluno(self,nome,idade,peso):
        self.cursor = self.conexao.cursor()
        self.cursor.execute("INSERT INTO tb_alunos (nome,idade,peso) VALUES (%s,%s,%s)",(nome,idade,peso)) 
        self.conexao.commit()
        self.cursor.close()         
from flask import Flask, request, jsonify, render_template
from peewee import *
from swagger_config import create_swagger

app = Flask(__name__)

# Configuração do banco de dados
db = MySQLDatabase('escola', user='root', password='1234', host='127.0.0.1', port=3306)

class Aluno(Model):
    nome = CharField()
    idade = IntegerField()
    nota_primeiro_semestre = FloatField()
    nota_segundo_semestre = FloatField()
    nome_professor = CharField()
    numero_sala = IntegerField()

    class Meta:
        database = db

# Cria as tabelas se ainda não existirem
db.connect()
db.create_tables([Aluno])

# Configura o Swagger usando o arquivo separado
swagger = create_swagger(app)

@app.route('/')
def index():
    """
    Página inicial que mostra a lista de alunos.
    ---
    responses:
      200:
        description: Página inicial
    """
    return render_template('index.html')

@app.route('/alunos', methods=['GET'])
def get_alunos():
    """
    Recupera a lista de alunos
    ---
    responses:
      200:
        description: Lista de alunos
        schema:
          type: array
          items:
            $ref: '#/definitions/Aluno'
    """
    alunos = Aluno.select()
    return jsonify([aluno_to_dict(aluno) for aluno in alunos])

@app.route('/alunos', methods=['POST'])
def add_aluno():
    """
    Adiciona um novo aluno
    ---
    parameters:
      - name: aluno
        in: body
        required: true
        schema:
          id: Aluno
          properties:
            nome:
              type: string
            idade:
              type: integer
            nota_primeiro_semestre:
              type: number
              format: float
            nota_segundo_semestre:
              type: number
              format: float
            nome_professor:
              type: string
            numero_sala:
              type: integer
    responses:
      201:
        description: Aluno criado com sucesso
        schema:
          $ref: '#/definitions/Aluno'
    """
    data = request.get_json()
    novo_aluno = Aluno.create(**data)
    return jsonify(aluno_to_dict(novo_aluno)), 201

def aluno_to_dict(aluno):
    return {
        'id': aluno.id,
        'nome': aluno.nome,
        'idade': aluno.idade,
        'nota_primeiro_semestre': aluno.nota_primeiro_semestre,
        'nota_segundo_semestre': aluno.nota_segundo_semestre,
        'nome_professor': aluno.nome_professor,
        'numero_sala': aluno.numero_sala
    }

if __name__ == '__main__':
    app.run(debug=True)

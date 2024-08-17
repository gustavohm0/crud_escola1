from flask import Flask, render_template, request, redirect, url_for
from models import Aluno, db
from flasgger import Swagger
import os
from peewee import MySQLDatabase

DATABASE_URL = os.getenv('JAWSDB_URL')  

db = MySQLDatabase(
    'q7iglsidj32el9k1',  
    user='ckk6h3o3gb5v2ezc',  
    password='eysfvw1pzsc618nv',
    host='alv4v3hlsipxnujn.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
    port=3306
)


app = Flask(__name__)
swagger = Swagger(app)

@app.route('/')
def index():
    alunos = Aluno.select()
    return render_template('index.html', alunos=alunos)

@app.route('/alunos', methods=['GET', 'POST'])
def listar_alunos():
    """
    Lista ou adiciona alunos.
    ---
    get:
      description: Lista todos os alunos
      responses:
        200:
          description: Lista de alunos
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Aluno'
    post:
      description: Adiciona um novo aluno
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Aluno'
      responses:
        201:
          description: Aluno criado com sucesso
    """
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        nota_primeiro_semestre = request.form['nota_primeiro_semestre']
        nota_segundo_semestre = request.form['nota_segundo_semestre']
        nome_professor = request.form['nome_professor']
        numero_sala = request.form['numero_sala']
        
        Aluno.create(
            nome=nome,
            idade=idade,
            nota_primeiro_semestre=nota_primeiro_semestre,
            nota_segundo_semestre=nota_segundo_semestre,
            nome_professor=nome_professor,
            numero_sala=numero_sala
        )
        return redirect(url_for('listar_alunos'))
    
    alunos = Aluno.select()
    return render_template('index.html', alunos=alunos)

@app.route('/create', methods=['GET', 'POST'])
def create():
    """
    Cria um novo aluno.
    ---
    post:
      description: Cria um novo aluno
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Aluno'
      responses:
        201:
          description: Aluno criado com sucesso
    """
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        nota_primeiro_semestre = request.form['nota_primeiro_semestre']
        nota_segundo_semestre = request.form['nota_segundo_semestre']
        nome_professor = request.form['nome_professor']
        numero_sala = request.form['numero_sala']
        
        Aluno.create(
            nome=nome,
            idade=idade,
            nota_primeiro_semestre=nota_primeiro_semestre,
            nota_segundo_semestre=nota_segundo_semestre,
            nome_professor=nome_professor,
            numero_sala=numero_sala
        )
        return redirect(url_for('listar_alunos'))
    
    return render_template('create.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    """
    Atualiza as informações de um aluno.
    ---
    post:
      description: Atualiza as informações de um aluno
      parameters:
        - name: id
          in: path
          required: true
          description: ID do aluno a ser atualizado
          schema:
            type: integer
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Aluno'
      responses:
        200:
          description: Aluno atualizado com sucesso
    """
    aluno = Aluno.get_or_none(Aluno.id == id)
    if request.method == 'POST':
        aluno.nome = request.form['nome']
        aluno.idade = request.form['idade']
        aluno.nota_primeiro_semestre = request.form['nota_primeiro_semestre']
        aluno.nota_segundo_semestre = request.form['nota_segundo_semestre']
        aluno.nome_professor = request.form['nome_professor']
        aluno.numero_sala = request.form['numero_sala']
        aluno.save()
        return redirect(url_for('listar_alunos'))
    
    return render_template('update.html', aluno=aluno)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    """
    Deleta um aluno.
    ---
    post:
      description: Deleta um aluno pelo ID
      parameters:
        - name: id
          in: path
          required: true
          description: ID do aluno a ser deletado
          schema:
            type: integer
      responses:
        204:
          description: Aluno deletado com sucesso
    """
    aluno = Aluno.get_or_none(Aluno.id == id)
    if aluno:
        aluno.delete_instance()
    return redirect(url_for('listar_alunos'))

swagger.definition('Aluno', {
    'type': 'object',
    'properties': {
        'id': {
            'type': 'integer',
            'description': 'ID do aluno'
        },
        'nome': {
            'type': 'string',
            'description': 'Nome do aluno'
        },
        'idade': {
            'type': 'integer',
            'description': 'Idade do aluno'
        },
        'nota_primeiro_semestre': {
            'type': 'number',
            'format': 'float',
            'description': 'Nota do primeiro semestre'
        },
        'nota_segundo_semestre': {
            'type': 'number',
            'format': 'float',
            'description': 'Nota do segundo semestre'
        },
        'nome_professor': {
            'type': 'string',
            'description': 'Nome do professor'
        },
        'numero_sala': {
            'type': 'integer',
            'description': 'Número da sala'
        }
    }
})

if __name__ == '__main__':
    app.run(debug=True)

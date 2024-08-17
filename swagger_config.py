from flasgger import Swagger

def create_swagger(app):
    swagger = Swagger(app)  # Configura o Swagger

    # Definir a definição de 'Aluno' no Swagger
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
    return swagger

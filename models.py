from peewee import *
import pymysql

db = MySQLDatabase(
    'q7iglsidj32el9k1',  
    user='ckk6h3o3gb5v2ezc',
    password='eysfvw1pzsc618nv',  
    host='alv4v3hlsipxnujn.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',  
    port=3306  
)


class Aluno(Model):
    nome = CharField(max_length=100)
    idade = IntegerField()
    nota_primeiro_semestre = FloatField()
    nota_segundo_semestre = FloatField()
    nome_professor = CharField(max_length=100)
    numero_sala = CharField(max_length=10)

    class Meta:
        database = db

db.connect()
db.create_tables([Aluno])

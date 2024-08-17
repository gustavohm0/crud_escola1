from peewee import *
import pymysql

db = MySQLDatabase('escola', user='root', password='1234', host='127.0.0.1', port=3306)

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

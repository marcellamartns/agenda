# -*- coding: utf-8 -*-

from cadastro import Cadastro
from contatos import Contatos
from pymongo import MongoClient
from bson.objectid import ObjectId


class Conexao(object):

    def __init__(self, banco):

        conexao_banco = MongoClient('mongodb://localhost:27017/')
        nome_banco = conexao_banco[banco]
        self._colecao = nome_banco["usuario"]

    def inserir_usuario(self, usuario):

        self._colecao.insert_one(usuario.dicionario_inserir())

    def inserir_contato(self, id_usuario, contato):

        qry = {"_id": ObjectId(id_usuario)}
        fld = {"$push": {"contatos": contato.dicionario_inserir_contato()}}
        a = self._colecao.update_one(qry, fld)
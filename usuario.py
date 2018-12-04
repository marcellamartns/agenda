# -*- coding: utf-8 -*-

from bson.objectid import ObjectId

class Usuario(object):

    def __init__(self, id_=None, nome_usuario=None, senha=None, contatos=None):

        self._id = id_ if id_ else ObjectId()
        self._nome_usuario = nome_usuario
        self._senha = senha
        self._contatos = contatos

    @property
    def id_(self):
        return self._id

    @property
    def nome_usuario(self):
        return self._nome_usuario

    def dicionario_inserir(self):

        return {
            "_id": self._id,
            "nome_usuario": self._nome_usuario,
            "senha": self._senha,
            "contatos": []
        }
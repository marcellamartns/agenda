# -*- coding: utf-8 -*-

from bson.objectid import ObjectId

class Contato(object):

    def __init__(self, id_=None, id_usuario=None, nome_contato=None, telefone=None, email=None,
                 complemento=None):

        self.id_ = id_ if id_ else ObjectId()
        self._nome_contato = nome_contato
        self._telefone = telefone
        self._email = email
        self._complemento = complemento
        self._id_usuario = id_usuario

    def dicionario_inserir_contato(self):

        return {
            "_id": self.id_,
            "id_usuario": self._id_usuario,
            "nome_contato": self._nome_contato,
            "telefone": self._telefone,
            "email": self._email,
            "complemento": self._complemento
        }
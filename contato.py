# -*- coding: utf-8 -*-

from bson.objectid import ObjectId


class Contato(object):

    def __init__(self, id_=None, nome_contato=None, telefone=None, email=None,
                 complemento=None):

        self._id = id_ if id_ else ObjectId()
        self._nome_contato = nome_contato
        self._telefone = telefone
        self._email = email
        self._complemento = complemento


    @property
    def id_(self):
        return self._id

    @property
    def nome_contato(self):
        return self._nome_contato

    @property
    def telefone(self):
        return self._telefone

    @property
    def email(self):
        return self._email

    @property
    def complemento(self):
        return self._complemento

    def dicionario_inserir_contato(self):

        return {
            "_id": self.id_,
            "nome_contato": self._nome_contato,
            "telefone": self._telefone,
            "email": self._email,
            "complemento": self._complemento
        }

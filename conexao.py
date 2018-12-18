# -*- coding: utf-8 -*-

from usuario import Usuario
from contato import Contato
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
        # print(a.matched_count)

    def atualizar_contato(self, id_usuario, contato):

        qry = {"_id": ObjectId(id_usuario), "contatos._id": ObjectId(contato.id_)}
        fld = {"$set": {
            "contatos.$.nome_contato": contato.nome_contato,
            "contatos.$.telefone": contato.telefone,
            "contatos.$.email": contato.email,
            "contatos.$.complemento": contato.complemento
            }
        }
        a = self._colecao.update_one(qry, fld)
        # print(a.matched_count)

    def busca_usuario(self, usuario, senha):

        qry = {"nome_usuario": usuario, "senha": senha}

        return self._colecao.find_one(qry)

    def busca_nome_usuario(self, nome_usuario):

        return self._colecao.find_one({"nome_usuario": nome_usuario})

    def busca_contatos(self, idusuario):

        usuario = self._colecao.find_one({"_id": ObjectId(idusuario)})
        contatos_lista = []
        for contatos in usuario["contatos"]:

            contato = Contato(contatos["_id"], contatos["nome_contato"],
                              contatos["telefone"], contatos["email"],
                              contatos["complemento"])
            # print(contato)
            contatos_lista.append(contato)
        return contatos_lista

    def busca_contato(self, id_usuario, id_contato):

        qry = {"_id": ObjectId(id_usuario)}
        fld = {
            "contatos": {
                "$elemMatch": {"_id": ObjectId(id_contato)}
            }
        }
        usuario = self._colecao.find_one(qry, fld)
        # print(usuario)
        for contatos in usuario["contatos"]:

            return Contato(contatos["_id"], contatos["nome_contato"],
                           contatos["telefone"], contatos["email"],
                           contatos["complemento"])

    def deleta_contato(self, id_usuario, id_contato):

        qry = {"_id": ObjectId(id_usuario)}
        fld = {"$pull": {"contatos": {"_id": ObjectId(id_contato)}}}
        self._colecao.update_one(qry, fld)


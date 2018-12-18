# -*- coding: utf-8 -*-


from usuario import Usuario
from contato import Contato
from conexao import Conexao

contato = Contato(nome_contato="Joana", telefone="9988721341",
                  email="joana@123.com", complemento="trabalho")
usuario = Usuario(nome_usuario="marcella", senha="123", contatos=contato)


conexao = Conexao("agenda")

# id_usuario=usuario.id_
# conexao.inserir_usuario(usuario)
# print("Usuario ok")

# print(usuario.id_)
# conexao.inserir_contato("5c067bbf9dc6d619bd718da1", contato)
# print("Inserir contato ok")

# conexao.buca_usuario("marcela", "123")

# conexao.atualizar_contato(usuario.id_, contato)

# s = conexao.busca_contatos("5c0811a49dc6d64c51d17e1b")
# for contato in s:
#     print(contato.nome_contato)

# a= conexao.busca_contato("5c0811a49dc6d64c51d17e1b", "5c08180a9dc6d653b70bfc8e")
# print(a)

conexao.deleta_contato("5c0811a49dc6d64c51d17e1b", "5c08180a9dc6d653b70bfc8e")
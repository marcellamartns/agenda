# -*- coding: utf-8 -*-


from cadastro import Cadastro
from contatos import Contatos
from conexao import Conexao

contato = Contatos(id_usuario="5c052d029dc6d64aee784cf1", nome_contato="kiara", telefone="33223322", email="marce@123k")
usuario = Cadastro(nome_usuario="marcella", senha="123", contatos=contato)


conexao = Conexao("agenda")

conexao.inserir_contato("5c052d029dc6d64aee784cf1", contato)
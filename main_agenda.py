# -*- coding: utf-8 -*-

from usuario import Usuario
from contato import Contato
from conexao import Conexao
import json
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        itens = ["marcella", "marcelo", "kiara"]
        self.render("template.html", itens=itens)

    def post(self):

        conexao = Conexao("agenda")
        jsonn = json.loads(self.request.body.decode('utf-8'))
        usuario = Usuario(**jsonn)
        conexao.inserir_usuario(usuario)
        self.write("ok")


class Cadastro(tornado.web.RequestHandler):

    def get(self):
        self.write("cadastro ok")


class Agenda(tornado.web.RequestHandler):

    def get(self):
        self.write("agenda ok")


class AdicionarContatos(tornado.web.RequestHandler):

    def get(self):
        self.write("cadastro contatos ok")

    def post(self):

        conexao = Conexao("agenda")
        jsonn = json.loads(self.request.body.decode('utf-8'))
        contato = Contato(**jsonn)
        usuarioid = Usuario()
        conexao.inserir_contato(usuarioid.id_, contato)
        self.write("ok")





def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/cadastro", Cadastro),
        (r"/agenda", Agenda),
        (r"/contatos", AdicionarContatos),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
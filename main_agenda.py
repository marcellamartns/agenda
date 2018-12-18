# -*- coding: utf-8 -*-

from usuario import Usuario
from contato import Contato
from conexao import Conexao
import json
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):

    def get(self):

        if not self.get_cookie("cookieagenda"):
            self.redirect("/autenticar")
        else:
            self.render("principal.html")

class Cadastro(tornado.web.RequestHandler):

    def get(self):

        self.render("cadastro.html")

    def post(self):

        conexao = Conexao("agenda")
        usuario = self.get_argument("nomeusuario")
        senha = self.get_argument("senhausuario")
        usuarios = conexao.busca_nome_usuario(usuario)
        print("AQUI")

        if usuarios:
                print("usuario existe")
                self.render("cadastro.html")

        else:
            print("usuario ok")
            novo_usuario = Usuario(nome_usuario=usuario, senha=senha)
            conexao.inserir_usuario(novo_usuario)
            self.redirect("/autenticar")

class Agenda(tornado.web.RequestHandler):

    def get(self):

        conexao = Conexao("agenda")
        id_usuario = self.get_secure_cookie("cookieagenda").decode("utf-8")
        contatos = conexao.busca_contatos(id_usuario)
        self.render("agenda.html", contatos=contatos)

    def post(self):

        self.render("agenda.html", contatos="")

class ContatoHandler(tornado.web.RequestHandler):

    def get(self, contato_id):

        conexao = Conexao("agenda")
        id_usuario = self.get_secure_cookie("cookieagenda").decode("utf-8")
        contato = conexao.busca_contato(id_usuario, contato_id)

        self.render("atualiza_contato.html", contato=contato)

    def put(self, contato_id):

        conexao = Conexao("agenda")

        id_usuario = self.get_secure_cookie("cookieagenda").decode("utf-8")

        json_data = json.loads(self.request.body.decode("utf-8"))
        print(json_data)
        contato = Contato(contato_id, json_data["nome"], json_data["telefone"],
                          json_data["email"], json_data["complemento"])

        conexao.atualizar_contato(id_usuario, contato)
        self.render("atualiza_contato.html", contato=contato)

    def delete(self, contato_id):

        conexao = Conexao("agenda")
        id_usuario = self.get_secure_cookie("cookieagenda").decode("utf-8")

        conexao.deleta_contato(id_usuario, contato_id)

        self.write("ok")

class AdicionarContatos(tornado.web.RequestHandler):

    def get(self):

        self.render("add_contato.html")

    def post(self):

        conexao = Conexao("agenda")
        nome = self.get_argument("nomecontato")
        telefone = self.get_argument("telefone")
        email = self.get_argument("email")
        complemento = self.get_argument("complemento")
        contato = Contato(nome_contato=nome, telefone=telefone, email=email,
                          complemento=complemento)
        id_usuario = self.get_secure_cookie("cookieagenda").decode("utf-8")

        conexao.inserir_contato(id_usuario, contato)
        self.redirect("/")

class Autenticar(tornado.web.RequestHandler):

    def get(self):

        self.render("autenticar.html", teste="bibi")

    def post(self):

        conexao = Conexao("agenda")
        nome = self.get_argument("usuario")
        senha = self.get_argument("senha")

        usuario = conexao.busca_usuario(nome, senha)

        if usuario:
            self.set_secure_cookie("cookieagenda", str(usuario["_id"]))
            self.redirect("/")
        else:
            self.render("autenticar.html", teste="invalido")

class Sair(tornado.web.RequestHandler):

    def get(self):

        self.clear_cookie("cookieagenda")
        self.redirect("/autenticar")

def make_app():
    return tornado.web.Application([
        (r"/cadastro", Cadastro),
        (r"/autenticar", Autenticar),
        (r"/sair", Sair),
        (r"/contato/([a-z0-9]+)", ContatoHandler),

        (r"/", MainHandler),
        (r"/agenda", Agenda),
        (r"/contatos", AdicionarContatos),
    ],
    cookie_secret="jhlhçgguilyojhlfhlfyupfyoupfyufy",
    static_path="static"
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
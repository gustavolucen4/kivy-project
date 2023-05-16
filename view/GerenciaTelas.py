from kivy.properties import StringProperty, ListProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from view.TelaClient import ViewClient


class TelaInicial(Screen):
    pass

class CadastroClient(Screen):
    pass


class ListarClients(Screen):
    pass


class GerenciaTelas(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._telaClient = ViewClient(self)

    def telaInicial(self):
        self.current = "TelaInicial"

    def telaCadastroClient(self):
        self.current = "CadastroClient"

    def telaListarClients(self):
        self._telaClient.alternarPesq("id")
        self.current = "ListarClients"

    def cadastrarAtualizarClient(self):
        self._telaClient.cadAtualClient()

    def buscarClients(self):
        self._telaClient.buscaClient()

    def buscarClientById(self):
        self._telaClient.buscaClient()

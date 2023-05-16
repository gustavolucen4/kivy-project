import locale

from kivy.uix.button import Button
from kivy.uix.label import Label
from model.Client import Client
from service.ClientDAO import ClientDAO


class ClientController:
    def salvarAtualizarClient(self, id=None, treatmentStatus="", gender="", age="", race="", employmentStatus="", mentalHealthDiagnosis="", substanceUseDiagnosis=""):
        daoClient = ClientDAO()
        if len(treatmentStatus) > 3:
            inseriuAtualizou = False
            client = Client(id=id, treatmentStatus=treatmentStatus, gender=gender, age=age, race=race, employmentStatus=employmentStatus, mentalHealthDiagnosis=mentalHealthDiagnosis, substanceUseDiagnosis=substanceUseDiagnosis)

            if id:
                client.id = id
                inseriuAtualizou = daoClient.update(client)
            else:
                inseriuAtualizou = daoClient.create(client)
            if inseriuAtualizou:
                return "Cliente inserido ou atualizado com sucesso!!!"
            else:
                return "Clinete não pôde ser inserido ou atualizado!"
        else:
            return "O treatmentStatus deve ter mais de 3 caracteres"

    def excluirClient(self,id):
        client = ClientDAO()
        excluiu = client.excluirClient(str(id))
        if excluiu:
            return "Client excluido com sucesso!!!"
        else:
            return "O Client não pôde ser excluído!"



    def buscarClient(self, id="", quant=10):
        dao = ClientDAO()
        res=""
        if id != "":
            res = dao.buscarClientById(id=id)
        else:
            res = dao.buscarClients(quant=quant)
        itens=[]
        if type(res) is Client:
            client = []
            client.append(self._criarLabel(res.id, 0.1))
            client.append(self._criarLabel(res.treatmentStatus, 0.5))
            client.append(self._criarLabel(res.gender, 0.5))
            client.append(self._criarLabel(res.age, 0.5))
            client.append(self._criarLabel(res.race, 0.5))
            client.append(self._criarLabel(res.employmentStatus, 0.5))
            client.append(self._criarLabel(res.mentalHealthDiagnosis, 0.5))
            client.append(self._criarLabel(res.substanceUseDiagnosis, 0.5))

            client.append(self._criarBotao("Atualizar", res.id))
            client.append(self._criarBotao("Excluir", res.id))
            itens.append(client)
        if type(res) is list:
            for client in res:
                umClient = []
                umClient.append(self._criarLabel(client.id, 0.1))
                umClient.append(self._criarLabel(client.treatmentStatus, 0.5))
                umClient.append(self._criarLabel(client.gender, 0.5))
                umClient.append(self._criarLabel(client.age, 0.5))
                umClient.append(self._criarLabel(client.race, 0.5))
                umClient.append(self._criarLabel(client.employmentStatus, 0.5))
                umClient.append(self._criarLabel(client.mentalHealthDiagnosis, 0.5))
                umClient.append(self._criarLabel(client.substanceUseDiagnosis, 0.5))

                umClient.append(self._criarBotao("Atualizar", client.id))
                umClient.append(self._criarBotao("Excluir", client.id))
                itens.append(umClient)
        return itens


    def _criarLabel(self, texto, tam):
        label = Label()
        label.text = str(texto)
        label.size_hint_y = None
        label.size_hint_x = tam
        label.height = '30dp'
        return label

    def _criarBotao(self, texto, id):
        botao = Button()
        botao.text = texto
        botao.id = "bt"+str(id)
        botao.font_size = '10sp'
        botao.size_hint_y = None
        botao.height = '30dp'
        botao.size_hint_x = .1
        return botao

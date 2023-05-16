from kivy.uix.label import Label
from kivy.uix.popup import Popup

from service.ClientController import ClientController


class ViewClient:

    def __init__(self, gerencTela):
        self._gerencTela = gerencTela


    def cadAtualClient(self):
        result = ""
        tela = self._gerencTela.get_screen("CadastroClient")

        try:
            idClient = tela.ids.lblIdClient.text
            treatmentStatus = tela.ids.txtTreatmentStatus.text
            gender = tela.ids.txtGender.text
            age = tela.ids.txtAge.text
            race = tela.ids.txtRace.text
            employmentStatus = tela.ids.txtEmploymentStatus.text
            mentalHealthDiagnosis = tela.ids.txtMentalHealthDiagnosis.text
            substanceUseDiagnosis = tela.ids.txtSubstanceUseDiagnosis.text
            control = ClientController()

            if tela.ids.btCadAtualClient.text == "Excluir":
                result = control.excluirClient(idClient)
            else:
                result = control.salvarAtualizarClient(id=idClient, treatmentStatus=treatmentStatus, gender=gender, age=age, race=race, employmentStatus=employmentStatus, mentalHealthDiagnosis=mentalHealthDiagnosis, substanceUseDiagnosis=substanceUseDiagnosis)
                self._popJanela(result)
                self._limparTela(tela)
        except Exception as e:
            print(str(e))

    def _limparTelaListar(self,tela):
        cabecalho = [
            tela.ids.colIdClient,
            tela.ids.colTreatmentStatus,
            tela.ids.colGender,
            tela.ids.colAge,
            tela.ids.colRace,
            tela.ids.colEmploymentStatus,
            tela.ids.colMentalHealthDiagnosis,
            tela.ids.colSubstanceUseDiagnosis,
            tela.ids.lblAtual,
            tela.ids.lblExcluir
        ]
        tela.ids.listaClients.clear_widgets()
        for c in cabecalho:
            tela.ids.listaClients.add_widget(c)


    def buscaClient(self):
        control = ClientController()
        tela = self._gerencTela.get_screen("ListarClients")
        idPesq = tela.ids.inputIdClient.text
        resultado = control.buscarClient(id=idPesq)
        self._limparTelaListar(tela)
        for res in resultado:
            for r in res:
                r.bind(on_release=self.montarTelaAt)
                tela.ids.listaClients.add_widget(r)

    def montarTelaAt(self,botao):
        telaCad = self._gerencTela.get_screen("CadastroClient")
        self._limparTela(telaCad)
        clients=[]
        try:
            if botao.id is not None:
                id = str(botao.id).replace("bt", "")
                control = ClientController()
                clients = control.buscarClient(id=id)
        except Exception as ex:
            print(ex)

        for a in clients:
            telaCad.ids.lblIdClient.text = a[0].text
            telaCad.ids.txtTreatmentStatus.text = a[1].text
            telaCad.ids.txtGender.text = a[2].text
            telaCad.ids.txtAge.text = a[3].text
            telaCad.ids.txtRace.text = a[4].text
            telaCad.ids.txtEmploymentStatus.text = a[5].text
            telaCad.ids.txtMentalHealthDiagnosis.text = a[6].text
            telaCad.ids.txtSubstanceUseDiagnosis.text = a[7].text

        telaCad.ids.btCadAtualClient.text = botao.text
        self._limparTelaListar(self._gerencTela.get_screen("ListarClients"))
        self._gerencTela.telaCadastroClient()

    def _limparTela(self, tela):
        tela.ids.lblIdClient.text = ""
        tela.ids.txtTreatmentStatus.text = ""
        tela.ids.txtGender.text = ""
        tela.ids.txtAge.text = ""
        tela.ids.txtRace.text = ""
        tela.ids.txtEmploymentStatus.text = ""
        tela.ids.txtMentalHealthDiagnosis.text = ""
        tela.ids.txtSubstanceUseDiagnosis.text = ""
        tela.ids.btCadAtualClient.text = "Cadastrar"

    def _popJanela(self, texto=""):
        popup = Popup(title='Informação', content=Label(text=texto), auto_dismiss=True)
        popup.size_hint = (0.98, 0.4)
        popup.open()

    def alternarPesq(self, tipo):
        tela = self._gerencTela.get_screen("ListarClients")
        if tela.ids.inputIdClient is not None:
            tela.ids.inputIdClient.text = ""
        pesqId = tela.ids.pesqId
        tela.ids.pesquisas.remove_widget(pesqId)
        if tipo == "id":
            pesqId.active = True
            tela.ids.pesquisas.add_widget(tela.ids.pesqId,2)


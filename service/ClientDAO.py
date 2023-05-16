from model.Client import Client
from model.Conexaobd import Conexaobd


class ClientDAO:
    __slots__ = (
        '_con'
    )

    def __init__(self):
        self._con = Conexaobd.conect()

    def create(self, client):
        sql = "INSERT INTO client (treatmentStatus, gender, age, race, employmentStatus, mentalHealthDiagnosis, substanceUseDiagnosis) "
        sql +=  "VALUES (?,?,?,?,?,?,?);"
        valores = (
            client.treatmentStatus,
            client.gender,
            client.age,
            client.race,
            client.employmentStatus,
            client.mentalHealthDiagnosis,
            client.substanceUseDiagnosis
        )

        res = Conexaobd.execute(sql, valores)
        return res == 1

    def update(self, client):
        sql = "UPDATE client SET treatmentStatus=?, gender=?, age=?, race=?, employmentStatus=?, mentalHealthDiagnosis=?, substanceUseDiagnosis=? WHERE id=? "
        valores = (
            client.treatmentStatus,
            client.gender,
            client.age,
            client.race,
            client.employmentStatus,
            client.mentalHealthDiagnosis,
            client.substanceUseDiagnosis,
            client.id
        )

        res = Conexaobd.execute(sql, valores)
        return res == 1

    def excluirClient(self, idClient):

        sql = "DELETE FROM client WHERE id = " + str(idClient)
        cursor = self._con.cursor()
        cursor.execute(sql)
        self._con.commit()
        res = cursor.rowcount
        return res == 1

    def buscarClientById(self, id):
        try:
            sql = "SELECT id, treatmentStatus, gender, age, race, employmentStatus, mentalHealthDiagnosis, substanceUseDiagnosis FROM client WHERE id = " + str(id)+ ";"
            cursor = self._con.cursor()
            cursor.execute(sql)
            res = cursor.fetchone()
            client = self.montarClientBanco(res)
            return client
        except Exception as e:
            print(str(e))
            return None

    def buscarClients(self, quant=100):
        clients = []
        try:
            sql = "SELECT id, treatmentStatus, gender, age, race, employmentStatus, mentalHealthDiagnosis, substanceUseDiagnosis FROM client "
            cursor = self._con.cursor()
            cursor.execute(sql)
            res = cursor.fetchmany(quant)
            clients = self.montarResultado(res)
            return clients
        except Exception as e:
            print(e)
            return clients

    def montarResultado(self, res):
        clients = []
        for linha in res:
            client = self.montarClientBanco(linha)
            clients.append(client)
        return clients


    def montarClientBanco(self, res):
        client = Client(id=res[0], treatmentStatus=res[1], gender=res[2], age=res[3], race=res[4], employmentStatus=res[5],
                        mentalHealthDiagnosis=res[6], substanceUseDiagnosis=res[7])
        return client

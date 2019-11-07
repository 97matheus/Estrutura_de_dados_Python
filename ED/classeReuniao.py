class Reuniao:
    def __init__(self, assunto = "", data = "", hora = "", local = "", participantes = "", confcoordenador = "", convcoordenador = ""):
        self.assunto = assunto
        self.data = data
        self.hora = hora
        self.local = local
        self.participantes = participantes
        self.confcoordenador = confcoordenador
        self.convcoordenador = convcoordenador

    def setAssunto(self,assunto):
        self.assunto = assunto

    def setData(self,data):
        self.data = data

    def setHora(self,hora):
        self.hora = hora

    def setLocal(self,local):
        self.local = local

    def setParticipantes(self,participantes):
        self.participantes = participantes

    def setConfcoordenador(self,confcoordenador):
        self.confcoordenador = confcoordenador

    def setConvcoordenador(self, convcoordenador):
        self.convcoordenador = convcoordenador

    def getAssunto(self):
        return self.assunto

    def getData(self):
        return self.data

    def getHora(self):
        return self.hora

    def getLocal(self):
        return self.local

    def getParticipantes(self):
        return self.participantes

    def getConfcoordenador(self):
        return self.confcoordenador

    def getConvcoordenador(self):
        return self.convcoordenador

    def criarReuniao(self):
        self.setAssunto(input('Informe o assunto da Reunião:'))
        self.setData(input("Qual a data da reuniao?:"))
        self.setHora(input("Qual a hora da reuniao?:"))
        self.setLocal(input("Qual o local da reuniao?:"))
        self.setParticipantes(input("Adicionar participantes:"))
        self.setConvcoordenador(input("Convidar Coordenador? (SIM/NAO):"))

    def criarReuniaoCoord(self):
        self.setAssunto(input('Informe o assunto da Reunião:'))
        self.setData(input("Qual a data da reuniao?:"))
        self.setHora(input("Qual a hora da reuniao?:"))
        self.setLocal(input("Qual o local da reuniao?:"))
        self.setParticipantes(input("Adicionar participantes:"))
        self.setConfcoordenador(input("Confimar presença na reunião?: (SIM/NAO)"))

    def mostrarInf(self):
        print(self.getAssunto())
        print(self.getData())
        print(self.getHora())
        print(self.getLocal())
        print(self.getParticipantes())
        print(self.getConfcoordenador())

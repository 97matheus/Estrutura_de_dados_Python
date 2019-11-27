import menuCoord
import menuUsuario
import menuG
import csv

#SENHAS PREDEFINIDAS DO COORDENADOR E GESTOR
logincoordenador = "coord"
senhacoordenador = "123"
logingestor = "gestor"
senhagestor = "456"


def login():

    print("=-"*10)

    login = False

    while login == False:

        #armazena dados nas variaveis
        cpf = input("Digite o seu cpf(só números):")
        senha = input("Digite sua senha:")

    # de acordo com o login e senha digitado, vai chamar o menu especifico, usuario,gestor,ou coordenador.
        with open('usuario.csv') as csvfile: #abre o arquivo usuario.csv
            reader = csv.DictReader(csvfile, delimiter= ';')
            for row in reader:
                if row['cpf'] == cpf and row['senha'] == senha: #verificação/autenticação de login e senha digitado com os dados salvos no arquivo
                    print("Logado com sucesso")
                    menuUsuario.menuUser() #após autenticar login e senha, chama o menu do usuario
                    login = True

        if cpf == logincoordenador and senha == senhacoordenador: #verificação/autenticação da senha digitada
            login = True
            print("Logado com Sucesso!")
            menuCoord.menuCoordenador()# após autenticar o login e senha,chama o menu do coordenador

        elif cpf == logingestor and senha == senhagestor: #verificação/autenticação da senha digitada
            login = True
            print("Logado com Sucesso!")
            menuG.menuGestor() # após autenticar o login e senha,chama o menu do gestor

        elif (cpf != logincoordenador and senha != senhacoordenador) or (cpf != logingestor and senha != senhagestor):
            print("Login ou Senha incorreto!")

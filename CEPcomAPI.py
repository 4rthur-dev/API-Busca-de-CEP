import requests
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QMessageBox

try:
    resultado = 10/0
except ZeroDivisionError:
    print("Erro: divisão por zero")


def limpaCampos():
    boxtxtCEP.clear()
    boxtxtRua.clear()
    boxtxtBair.clear()
    boxtxtCid.clear()
    boxtxtUF.clear()
    boxtxtCEP.setFocus()

def validaCampos():
    codigoCEP = boxtxtCEP.text()

    #Fazer a validação de preenchimento do CEP
    if codigoCEP == '':
        QMessageBox.critical(tela, "Atenção", "CEP precisa ser informado, verifique.")
        boxtxtCEP.setFocus()
    else:
        #Chamar a rotina de verificação do CEP
        tratarCEP(codigoCEP)

def tratarCEP(codigoCEP):
    #URL da API
    url = "https://viacep.com.br/ws/{}/json/".format(codigoCEP)

    try:
        #Fazendo a requisição GET
        response = requests.get(url)

        #Verificando o resultado
        if response.status_code == 200:
            dados = response.json()

            #Verifica se a chave "erro" existe e se o valor é "trua"
            if dados.get("erro") == "true":
                QMessageBox.critical(tela, "Deu ruim", "CEP não encontrado na base de dados do VIACEP.")
            else:
                #Colocando os objetos  de retorno nas caixas de texto
                boxtxtRua.setText(dados.get('logradouro', ''))
                boxtxtBair.setText(dados.get('bairro', ''))
                boxtxtCid.setText(dados.get('cidade', ''))
                boxtxtUF.setText(dados.get('uf', ''))

                QMessageBox.information(tela, 'Consulta de CEP', 'Endereço encontrado')

        else:
            QMessageBox.critical(tela, 'Deu ruim', 'Erro na requisição. Código de status: {}'.format(response.status_code))

    except Exception as e:
        QMessageBox.critical(tela, 'Erro', 'Ocorreu uma exceção: {str}'.format(e) )
#Criando aplicação
app = QApplication(sys.argv)

#Janela Principal
tela = QWidget()
tela.setWindowTitle('Verificação de CEP')
tela.setGeometry(650, 400, 800, 120)

#Criando um label
#CEP
txtCEP = QLabel('CEP:', tela)
txtCEP.move(10,10)

#Rua
txtRua = QLabel('Rua:', tela)
txtRua.move(300,10)

#Bairro
txtBair = QLabel('Bairro:' , tela)
txtBair.move(10, 60)

#Cidade
txtCid = QLabel('Cidade:', tela)
txtCid.move(270, 60)

#UF
txtUF = QLabel('UF:', tela)
txtUF.move(530, 60)
#------------------------------------------------
#Criando caixa de texto
#CEP
boxtxtCEP = QLineEdit(tela)
#Tamnho da caixa de texto
boxtxtCEP.setFixedWidth(80)
#Coloca mascara de CEP 
boxtxtCEP.setInputMask("00000-000") #Mascara de CEP
boxtxtCEP.move(10, 30)

#Rua
boxtxtRua = QLineEdit(tela)
boxtxtRua.setFixedWidth(260)
boxtxtRua.move(300, 30)
boxtxtRua.setEnabled(False)

#Bairro
boxtxtBair = QLineEdit(tela)
boxtxtBair.setFixedWidth(250)
boxtxtBair.move(10, 80)
boxtxtBair.setEnabled(False)

#Cidade
boxtxtCid = QLineEdit(tela)
boxtxtCid.setFixedWidth(250)
boxtxtCid.move(270, 80)
boxtxtCid.setEnabled(False)

#UF
boxtxtUF = QLineEdit(tela)
boxtxtUF.setFixedWidth(30)
boxtxtUF.move(530, 80)
boxtxtUF.setEnabled(False)
#------------------------------------------------

#Criando o botao de busca de CEP
btnBuscarCEP = QPushButton('Buscar CEP', tela)
btnBuscarCEP.move(100, 28)

#Conectando o clique do botao a função
btnBuscarCEP.clicked.connect(validaCampos)

#Criando o botao de limpar
btnLimpar = QPushButton('Limpar busca', tela)
btnLimpar.move(190, 28)
btnLimpar.clicked.connect(limpaCampos)

#Exibir a janela
tela.show()

#Loop infinito
sys.exit(app.exec_())

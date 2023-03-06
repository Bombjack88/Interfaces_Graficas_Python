import requests

def ver_cotacao(codigo_moeda):
    try:
        requisicao = requests.get(f"https://economia.awesomeapi.com.br/last/{codigo_moeda}-BRL")

        requisicao_dic = requisicao.json()

        cotacao = requisicao_dic[f'{codigo_moeda}BRL']['bid']

        return cotacao
    except:
        print("Codigo de Moeda Inválido")
        return None



#print(ver_cotacao('EUR'))

import PySimpleGUI as sg

layout = [
[sg.Text("Cotação Atual das Moedas")],
[sg.InputText(key="nome_cotacao")],
[sg.Button("Ver Cotação"), sg.Button("Cancelar")],
[sg.Text("",key="texto_cotacao")]
]

janela=sg.Window("Sistema de Cotações", layout)

while True:
    evento, valores=janela.read()
    if evento==sg.WIN_CLOSED or evento=="Cancelar":
        break

    if evento == "Ver Cotação":
        codigo_cotacao=valores["nome_cotacao"]
        cotacao = ver_cotacao(codigo_cotacao)
        janela["texto_cotacao"].update(f'A cotação do {codigo_cotacao} é de R${cotacao}')

      

janela.close()


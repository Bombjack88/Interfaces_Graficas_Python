
from PySimpleGUI import (
    Window, Button, Image, Input, Text,
    Column, VSeparator, Push,
    theme, popup
    )

#theme('DarkPurple')

layout_esquerda=[
[Image(filename=r"C:\Users\fiu126\Desktop\Impressionador\Criar um Tela no Python [Interface Gráfica]\Live_PySimpleGUI\avatar.png", key='-IMAGEM-')]
]



layout_direita=[
    [Text('E-mail:'), Input(key='-EMAIL-'),],
    [Text('Senha:'), Input(password_char='*',key='-SENHA-')],
    [Push(),Button('Login'),Push(),Button('Esqueci a senha !'), Push()],
]


layout=[
    [Column(layout_esquerda), VSeparator(), Column(layout_direita)],
]

window=Window(
    'Janela da Live de Python',
    layout=layout,
  
)

while True:
    event, values=window.read()
    #print(event, values)

    match(event):
        case 'Login':
            #popup('Login feito com sucesso')
            window['-IMAGEM-'].update(filename=r"C:\Users\fiu126\Desktop\Impressionador\Criar um Tela no Python [Interface Gráfica]\Live_PySimpleGUI\avatar_2.png")
        case None:
            break
        case 'Esqueci a senha !':
            popup(f' o seu email é {values["-EMAIL-"]}')
        case _:
            print(event, values)



window.close()


# Procurar um arquivo atarvés do browser e reter o caminho

from PySimpleGUI import (
    Window, FileBrowse
    )


layout=[
[FileBrowse(enable_events=True, key='-BROWSER-')],

]

window=Window('Exemplo Playground', layout=layout)


while True:
    event, values=window.read()
    if event=='-BROWSER-':
        #print(event, values)
        caminho=values['-BROWSER-']
        print(caminho)
    else:
       break


window.close()
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import popup_no_titlebar
import configuracoes
import enviarEmail

tamanhoDoBotao = 40
padding = 5
paddingEspecial = 20
h1Color = 'DarkBlue'

sg.theme('DarkGrey7')
# All the stuff inside your window.
layout = [  [sg.Text('4utoMail', font='Verdana', pad=(120, paddingEspecial), text_color=h1Color)],
            [sg.Button('Enviar email', s=tamanhoDoBotao, pad=(0, padding))],
            [sg.Button('Configurações', s=tamanhoDoBotao, pad=(0, padding))],
            [sg.Button('Ajuda', s=tamanhoDoBotao, pad=(0, padding))],
            [sg.Button('Fechar', s=tamanhoDoBotao, pad=(0, paddingEspecial))]
            ]

# Create the Window
window = sg.Window('4utoMail', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Fechar': # if user closes window or clicks cancel
        break
    elif event == 'Ajuda':
        popup_no_titlebar("...")
    elif event == 'Configurações':
        configuracoes.windowConfig()
    elif event == 'Enviar email':
        enviarEmail.windowEnviarEmail()

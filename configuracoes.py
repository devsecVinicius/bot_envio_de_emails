import PySimpleGUI as sg

def windowConfig():

    tamanhoDoBotao = 40
    padding = 5
    paddingEspecial = 20
    h1Color = 'Purple'
    pColor = 'Black'

    sg.theme('DarkGrey7')
    # All the stuff inside your window.

    layout = [  [sg.Text('4utoMail', font='Verdana', pad=(120, paddingEspecial), text_color=h1Color)],
                [sg.Text('Endereço:', pad=(0, padding), s=8, text_color=pColor), sg.InputText(s=35, pad=(0, padding))],
                [sg.Text('Senha:', pad=(0, padding), s=8, text_color=pColor), sg.InputText(s=35, pad=(0, padding))],
                [sg.Button('Salvar', s=tamanhoDoBotao, pad=(0, padding))],
                [sg.Button('Fechar', s=tamanhoDoBotao, pad=(0, padding))]
                ]

    # Create the Window
    window = sg.Window('Configurações', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Fechar': # if user closes window or clicks cancel
            break
        if event == 'Salvar':
            f = open("config.py", "w")
            f.write(f"endereco = '{values[0]}'\n")
            f.write(f"senha = '{values[1]}'")
            f.close()

    window.close()

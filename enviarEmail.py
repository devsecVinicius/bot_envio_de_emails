import os
import smtplib
from email.message import EmailMessage

from PySimpleGUI.PySimpleGUI import popup_no_titlebar
from config import senha, endereco
import PySimpleGUI as sg

def windowEnviarEmail():

    tamanhoDoBotao = 40
    padding = 5
    paddingEspecial = 20
    h1Color = 'Yellow'
    pColor = 'Black'

    sg.theme('DarkGrey7')
    layout = [  [sg.Text('4utoMail', font='Verdana', pad=(120, paddingEspecial), text_color=h1Color)],
                [sg.Text('Título:', pad=(0, padding), s=8, text_color=pColor), sg.InputText(s=35, pad=(0, padding))],
                [sg.Text('Conteúdo:', pad=(0, padding), s=8, text_color=pColor), sg.InputText(s=35, pad=(0, padding))],
                [sg.Button('Enviar', s=tamanhoDoBotao, pad=(0, padding))],
                [sg.Button('Fechar', s=tamanhoDoBotao, pad=(0, padding))]
                ]

    # Create the Window
    window = sg.Window('Enviar Email', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Fechar': # if user closes window or clicks cancel
            break
        if event == 'Enviar':
            # Configurar email, senha
            EMAIL_ADDRESS = endereco
            EMAIL_PASSWORD = senha

            # Criar email
            msg = EmailMessage()
            msg['Subject'] = values[0]
            msg['From'] = endereco
            msg.set_content(values[1])
            f = open('emails.txt', 'r')

            for x in f:
                msg['To'] = x
                #Enviar um email
                with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
                    smtp.send_message(msg)
                del msg['To']

        popup_no_titlebar("Emails enviados")

    window.close()

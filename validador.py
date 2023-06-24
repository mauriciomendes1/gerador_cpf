import PySimpleGUI as sg
import back

#programinha pra válidar e gerar cpf's
#por Maurício Mendes
sg.theme('Dark2')
def principal():
    layout = [
        [sg.Text('Validador e gerador de CPF')],
        [sg.InputText('', size=(12,1), key='-CPF-'), sg.Text('', size=(30,1), key='-RESULT-')],
        [sg.Button('Check', key='-CHECK-')],
        [sg.Text('Gerar CPF')],
        [sg.Input('', key='-INPUTGEN-', size=(12,1), disabled=True), sg.Text('', size=(20, 1), key='-GENERATED-')],
        [sg.Button('Generate', key='-GENERATE-')]
    ]

    window = sg.Window('CPF', layout, size=(300, 200), element_justification='left')

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == '-CHECK-':
            if len(values['-CPF-']) < 11 or len(values['-CPF-']) > 11:
                window['-RESULT-'].update(values['-CPF-'] + ' não é um número de CPF!')
            else:
                if back.validar_cpf(values['-CPF-']):
                    window['-RESULT-'].update(values['-CPF-'] + ' é válido!')
                else:
                    window['-RESULT-'].update(values['-CPF-'] + ' não é válido!')
        
        if event == '-GENERATE-':
            window['-INPUTGEN-'].update(back.gerar_cpf())
            window['-GENERATED-'].update('Gerado com sucesso!')

principal()
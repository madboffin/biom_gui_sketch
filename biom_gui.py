import PySimpleGUI as sg
from PIL import Image
import io
import cv2


def main():

    # Buttons
    sg.theme('Reddit')
    BLUE_BUTTON_COLOR   = '#FFFFFF on #2196f2'
    GREEN_BUTTON_COLOR  = '#FFFFFF on #00c851'
    L_GRAY_BUTTON_COLOR = '#212021 on #e0e0e0'
    a = 58

    # Static images
    bio1 = io.BytesIO()
    bio2 = io.BytesIO()
    logo1 = Image.open("logo_escuela.png")
    logo2 = Image.open("logo_rosario.png")
    logo1.thumbnail((100, 100))
    logo2.thumbnail((100, 100))
    logo1.save(bio1, format="PNG")
    logo2.save(bio2, format="PNG")

    texto = f"""Estas son las pruebas realizadas para evaluar la severidad de los síntomas de la ataxia. Un mayor puntaje indica mayor severidad de los síntomas.

ICARS
Capacidad de parado, ojos abiertos (0-6): {a}
Inclinación de cuerpo con pies juntos, ojos abiertos (0-4): {a}
Inclinación de cuerpo con pies juntos, ojos cerrados (0-4): {a}

SARA
Postura : Se pide probando que se pare en posición natural, con los pies juntos en paralelo y en tandem con los ojos abiertos (0-6): {a}
Sentada: Se pide a Proband que se siente en una camilla de exploración sin apoyo de los pies, con los ojos abiertos y los brazos extendidos hacia el frente (0-4): {a}

BARS
Extensión de pies en posición natural sin apoyo, ojos abiertos (0-4): {a}
Balanceo del cuerpo con los pies juntos y los ojos abiertos (0-4): {a}
Balanceo del cuerpo con los pies juntos y los ojos cerrados (0-4): {a}
Calidad de la posición sentada (0-4): {a}
Prueba rodilla-tibia (descomposición del movimiento y temblor intencional) (:0-4) {a}
"""

    layout = [[ 
                sg.Col([[sg.T(" ")]], element_justification='r', k='-TOP COLL-' ),
                sg.Col([
                    # /////////// HEADER ///////////
                    [sg.T()],
                    [sg.Image(data=bio1.getvalue(), key="-IMAGE1-"),
                     sg.T('    Detección de Ataxia    ', font=("Roboto", 24)),
                     sg.Image(data=bio2.getvalue(), key="-IMAGE2-")],
                    [sg.T()],
                    [sg.T()],

                    # /////////// MIDSECTION ///////////
                    [sg.T(f"SARA: {a}", font=("Roboto", 14))],
                    [sg.T(f"BARS: {a}", font=("Roboto", 14))],
                    [sg.T(f"ICARS: {a}", font=("Roboto", 14))],
                    [sg.T(f"Puntaje general:", font=("Roboto", 18)), sg.T("17", font=("Roboto", 18))],
                    [sg.T()],
                    [sg.B('Captura 30 seg', size=(14,2), button_color=BLUE_BUTTON_COLOR),
                     sg.B('Captura 1 min', size=(14,2), button_color=GREEN_BUTTON_COLOR),
                     sg.B('Detalles', size=(14,2), button_color=L_GRAY_BUTTON_COLOR)],
                    [sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"), sg.FolderBrowse()],
                    [sg.T()], 
                    ], element_justification='c', k='-TOP COL-'),

                sg.Col([[sg.T(" ")]], element_justification='r', k='-TOP COLR-' )
                ]]

    window = sg.Window('Proyecto BIOM Ataxia', layout, resizable=True)  # 

    # Main GUI loop
    while True:            
        event, values = window.read(timeout=100)
        if event == sg.WIN_CLOSED:
            break
        if event == 'Detalles':
            sg.Popup("Detalles", texto, background_color='white', text_color='grey')
        elif event == 'Captura 30 seg':
            pass
        elif event == 'Captura 1 min':
            pass

    window.close()

if __name__ == '__main__':
    main()

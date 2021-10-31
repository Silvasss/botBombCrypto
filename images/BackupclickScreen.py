import time
import pyautogui

# https://pyautogui.readthedocs.io/en/latest/mouse.html


def moveMouse(x, y):
    # Move o mouse para a posição X e Y.
    pyautogui.moveTo(x, y, 2)

    return True


def mouseLeftClick():
    # Configurado para clicar em qualquer tela com o botão esquerdo do mouse.
    pyautogui.click()

    return True


# Configurado só para funcionar na tela "Character".
def mouseDragCharacter():
    # Recebe a posição do cursor do mouse.
    x, y = pyautogui.position()

    pyautogui.click()

    # Movimento do scroll para baixo.
    pyautogui.scroll(-7000)

    # Tempo para terminar a animação
    time.sleep(2)

    # Move o mouse novamente para a posição inicial e clica no último personagem.
    pyautogui.click(x, y - 100, duration=2)

    time.sleep(2)

    # Posiciona o mouse em "Work".
    pyautogui.moveTo(x + 230, y, 2)

    return True


def mouseRepeatClick(number):
    n = 0

    while n < number:
        mouseLeftClick()

        time.sleep(2)

        n +=1

    return True

#time.sleep(2)
#mouseDragCharacter()
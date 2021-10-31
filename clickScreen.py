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
    # Recebe a posição do cursor do mouse que está no "work".
    x, y = pyautogui.position()

    pyautogui.click()

    # Movimento de puxar para baixo.
    pyautogui.dragRel(0, -y, 1)

    moveMouse(x, y)

    # Tempo para terminar a animação
    time.sleep(2)

    # Move o mouse novamente para a posição inicial e clica no último personagem.
    pyautogui.click(x, y - 100, duration=2)

    time.sleep(2)

    # Posiciona o mouse em "Work".
    pyautogui.moveTo(x + 230, y, 2)

    return True


# Configurado só para funcionar na tela "Character".
def mouseDragUpCharacterHouse():

    time.sleep(2)

    # Recebe a posição do cursor do mouse.
    x, y = 847, 437

    n = 0
    while n < 2:
        # Posiciona o mouse no primeiro.
        moveMouse(x, y)

        # Clica para libera o movimento.
        mouseLeftClick()

        # Movimento de puxar para baixo.
        pyautogui.dragRel(0, 350, 2)

        n += 1

    # Posiciona o mouse no primeiro.
    moveMouse(x, y)

    # Posiciona o mouse em "House".
    pyautogui.moveTo(x + 160, y, 2)

    for i in range(4):
        # Clica em "House".
        mouseLeftClick()

        time.sleep(2)

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
#mouseDragUpCharacterHouse()
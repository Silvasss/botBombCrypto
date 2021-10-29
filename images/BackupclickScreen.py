import time, mouse


def moveMouse(x, y):
    # Move o mouse para a posição X e Y.
    mouse.move(x, y)

    return True


def mouseLeftClick():
    # Configurado para clicar em qualquer tela com o botão esquerdo do mouse.
    mouse.click()

    return True


# Configurado só para funcionar na tela "Character".
def mouseDragCharacter():
    # Recebe a posição do cursor do mouse.
    x, y = mouse.get_position()

    # Movimento de segurar e arrastar para baixo.
    mouse.drag(x, y, x, y - 550, True, 1)

    # Faz um movimento para liberar o click.
    moveMouse(x, y)

    # Tempo para terminar a animação
    time.sleep(2)

    mouseLeftClick()

    # Move o mouse novamente para a posição inicial.
    moveMouse(x, y - 100)

    time.sleep(2)

    # Clica no último personagem.
    mouseLeftClick()

    # Posiciona o mouse em "Work".
    moveMouse(x + 230, y)
#"""
#"""
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
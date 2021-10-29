import time, mouse
import pyautogui
import pyscreenshot as ImageGrab
from functools import partial
import mss
from positionsObjectsScreen import sleepingQuantity
import positionsObjectsScreen as objectsScreen
import clickScreen as click
from printScreen import printScreem

"""
mouse.move(668, 736)

# Movimento de segurar e arrastar para baixo.
# Configurado só para funcionar na tela "Character".

x, y = mouse.get_position()

mouse.drag(x, y, x, y - 600, True, 1)

# Configurado para clicar em qualquer tela com o botão esquerdo do mouse.
mouse.move(x, y + 100)

time.sleep(2)

mouse.move(x, y)

mouse.click()

mouse.move(x + 230, y)

from datetime import datetime, timedelta

now = datetime.now() + timedelta(minutes=50)

current_time = now.strftime('%H:%M:%S')

now2 = datetime.now()

current_time2 = now2.strftime('%H:%M:%S')

if current_time2 < current_time:
    print(current_time)


pyautogui.moveTo(768, 236, 2)

x, y = pyautogui.position()

print(x, y)

pyautogui.scroll(7000)

pyautogui.click(x, y - 100, duration=2)


output_filename = 'screenShot.jpg'
monitor = 2  # Save a screenshot of monitor 2

with mss.mss() as mss_instance:
    mss_instance.shot(mon=monitor, output=output_filename)
"""


def backScreenRound():
    try:
        printScreem()

        # Posição do botão "Treasure Hunt", na tela inicial.
        x, y = objectsScreen.positionButtonHunt()
        print("Posição do botão incial: {}, {}".format(x, y))

        # Move o mouse para a posição do botão "Treasure Hunt", na tela inicial.
        click.moveMouse(x, y)

        # Clicar no botão "Treasure Hunt", na tela inicial.
        click.mouseLeftClick()
    except IndexError:
        print("objectsScreen.positionButtonHunt()")

#backScreenRound()

"""
def screenRoundNewMap():
    try:
        time.sleep(2)

        printScreem()

        # Posição do texto "New Map".
        x, y = objectsScreen.positionTextNewMap()

        # Move o mouse para o botão "New Map".
        click.moveMouse(x, y)

        # Clica no botão
        click.mouseLeftClick()

        return True
    except IndexError:
        printScreem()

        # Verifica se existe a palavra "Unknown" na tela.
        if objectsScreen.positionErroUnknown():
            # Posição da palavra "Ok".
            x, y = objectsScreen.positionOkErro()

            # Move o mouse para o botão "Ok".
            click.moveMouse(x, y)

            # Clica no botão
            click.mouseLeftClick()

            # Tempo para retorna a página inicial.
            time.sleep(20)

            printScreem()

            # Posição da frase "Connect Wallet".
            x, y = objectsScreen.positionConnectWallet()

            # Move o mouse para a frase "Connect Wallet".
            click.moveMouse(x, y)

            # Clica no botão
            click.mouseLeftClick()

            # Tempo para carregar
            time.sleep(10)

            printScreem()

            # Posição da palavra "MetaMask".
            x, y = objectsScreen.positionSelectWallet()

            # Move o mouse para a palavra "MetaMask".
            click.moveMouse(x, y)

            # Clica no botão
            click.mouseLeftClick()

            # Tempo para carregar
            time.sleep(10)

            printScreem()

            # Posição da palavra "Sign".
            x, y = objectsScreen.positionConfirmSign()

            # Move o mouse para a palavra "Sign".
            click.moveMouse(x, y)

            # Clica no botão
            click.mouseLeftClick()

            # Tempo para carregar
            time.sleep(20)

            printScreem()

            # Posição do botão "Treasure Hunt", na tela inicial.
            x, y = objectsScreen.positionButtonHunt()
            print("Posição do botão incial: {}, {}".format(x, y))

            # Move o mouse para a posição do botão "Treasure Hunt", na tela inicial.
            click.moveMouse(x, y)

            # Clicar no botão "Treasure Hunt", na tela inicial.
            click.mouseLeftClick()

            return True
        else:
            pass
    else:
        pass


screenRoundNewMap()
"""

time.sleep(5)

pyautogui.scroll(-7000)
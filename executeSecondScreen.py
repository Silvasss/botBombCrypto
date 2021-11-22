import time

import pyautogui

from execute import computerSleep
import clickScreen as click
import positionsObjectsScreen as objectsScreen
from positionsObjectsScreen import sleepingQuantity
from printScreen import printScreem


# Função que coloca todos os personagens para trabalhar.
def execMain():
    printScreem(2)

    # Quantidade de bonecos dormindo.
    if sleepingQuantity() >= 0:

        # Manipulação da tela round
        def screenRound():
            try:
                printScreem(2)

                # Posição do botão "volta"
                x, y = objectsScreen.positionButtonBack()

                # Move o cursos do mouse para o botão "volta".
                click.moveMouse(-abs(x) - 850, y)

                # Clicar no botão "voltar".
                click.mouseLeftClick()

                return True
            except:
                return False

        # Manipulação da tela home
        def screenHome():
            printScreem(2)
            try:
                printScreem(2)

                # Posição do botão "Heroes".
                x, y = objectsScreen.positionButtonHeroes()

                time.sleep(1)
                # Move o mouse para o botão "Heroes".
                click.moveMouse(-abs(x) + 840, y)

                time.sleep(1)
                # Clicar no botão "Heroes".
                click.mouseLeftClick()

                return True
            except:
                return False

        # Função que volta para a tela round
        def backScreenRound():
            try:
                # Posição do botão "close", na tela personagens.
                x, y = objectsScreen.positionButtonClose()

                # Move o mouse para a posição do botão "Close", na tela personagens.
                click.moveMouse(-abs(x) + 140, y)

                # Clicar no botão "Close", na tela personagens.
                click.mouseLeftClick()

                time.sleep(2)

                printScreem(2)

                # Posição do botão "Treasure Hunt", na tela inicial.
                x, y = objectsScreen.positionButtonHunt()

                # Move o mouse para a posição do botão "Treasure Hunt", na tela inicial.
                click.moveMouse(-abs(x) + 100, y)

                # Clicar no botão "Treasure Hunt", na tela inicial.
                click.mouseLeftClick()

                return True
            except:
                pass

        # Manipulação da tela dos personagens
        def screenCharacter():
            try:
                time.sleep(10)

                printScreem(2)

                # Posição da palavra "Work".
                x, y = objectsScreen.positionButtonWork()

                # Move o mouse para o último boneco da primeira parte da lista.
                click.moveMouse(-abs(x) - 380, y + 15)

                # Movimento de segurar e arrastar e posicionar o cursos em "work".
                click.mouseDragCharacter()

                time.sleep(2)

                # Clica 15 vezes no botão "work".
                click.mouseRepeatClick(15)

                if backScreenRound():
                    return True
                else:
                    return False
            except:
                return False

        # Caso ele tente chama uma vez a função, e de erro e executada novamente.
        def validacaoFuncoes():
            if screenRound():
                print("screen round: True")
            else:
                print("Função ScreenRound: False")
                computerSleep()

            if screenHome():
                print("ScreenHome: True")
            else:
                print("Função ScreenHome: False")
                computerSleep()

            if screenCharacter():
                print("ScreenCharacter: True")
            else:
                print("Função ScreenCharacter: False")
                computerSleep()

        validacaoFuncoes()
    else:
        pass


# Função para mudar de mapa.
def screenRoundNewMap():
    try:
        time.sleep(2)

        printScreem(2)

        # Posição do texto "New Map".
        x, y = objectsScreen.positionTextNewMap()

        # Move o mouse para o botão "New Map".
        click.moveMouse(-abs(x), y)

        # Clica no botão
        click.mouseLeftClick()

        return True
    except IndexError:
        pass


# Tela login.
def screenErroCore():
    printScreem(2)

    # Verifica se existe a palavra "Failed" na tela.
    if objectsScreen.positionErroCore():
        # Simula a tecla "F5".
        pyautogui.press("f5")

        time.sleep(60)

        # Função que faz o login.
        loginFunction()

        return True
    else:
        pass


# Função que faz o login e vai para tela "round".
def loginFunction():
    try:
        # Tempo para retorna a página inicial.
        time.sleep(30)

        printScreem(2)

        # Posição da frase "Connect Wallet".
        x, y = objectsScreen.positionConnectWallet()

        # Move o mouse para a frase "Connect Wallet".
        click.moveMouse(-abs(x), y)

        # Clica no botão
        click.mouseLeftClick()

        # Tempo para carregar
        time.sleep(5)

        printScreem(2)

        # Posição da palavra "MetaMask".
        x, y = objectsScreen.positionSelectWallet()

        # Move o mouse para a palavra "MetaMask".
        click.moveMouse(-abs(x), y)

        # Clica no botão
        click.mouseLeftClick()

        # Tempo para carregar
        time.sleep(5)

        printScreem(2)

        # Posição da palavra "Sign".
        x, y = objectsScreen.positionConfirmSign()

        # Move o mouse para a palavra "Sign".
        click.moveMouse(-abs(x) + 1740, y)

        # Clica no botão
        click.mouseLeftClick()

        # Tempo para carregar
        time.sleep(80)

        printScreem(2)

        # Posição do botão "Treasure Hunt", na tela inicial.
        x, y = objectsScreen.positionButtonHunt()

        # Move o mouse para a posição do botão "Treasure Hunt", na tela inicial.
        click.moveMouse(-abs(x) + 100, y)

        # Clicar no botão "Treasure Hunt", na tela inicial.
        click.mouseLeftClick()
    except:
        pass


# Função que verifica se existe o erro "Unknown", na tela round.
def screenErroUnknown():
    printScreem(2)

    try:
        # Verifica se existe a palavra "Unknown" na tela.
        objectsScreen.positionErroUnknown()
        # Posição da palavra "Ok".
        x, y = objectsScreen.positionOkErro()

        # Move o mouse para o botão "Ok".
        click.moveMouse(-abs(x), y)

        # Clica no botão
        click.mouseLeftClick()

        # Função que faz o login.
        loginFunction()

        return True
    except IndexError:
        return False


def screenErroOverloaded():
    printScreem(2)

    try:
        # Verifica se existe a palavra "Overloaded" na tela.
        objectsScreen.positionErroOverloaded()
        # Simula a tecla "F5".
        pyautogui.press("f5")

        # Função que faz o login.
        loginFunction()

        return True
    except IndexError:
        return False


def screenErroManual():
    # Verifica se existe a palavra "Manual" na tela.
    if objectsScreen.positionErroManual(2):
        # Simula a tecla "F5".
        pyautogui.press("f5")

        # Função que faz o login.
        loginFunction2()

        return True
    else:
        return False


# Função que faz o login quando ocorre algum erro e o jogo fica parado na tela de login.
def loginFunction2():

    printScreem(2)

    # Posição da frase "Connect Wallet".
    x, y = objectsScreen.positionConnectWallet()

    # Move o mouse para a frase "Connect Wallet".
    click.moveMouse(-abs(x), y)

    # Clica no botão
    click.mouseLeftClick()

    # Tempo para carregar
    time.sleep(5)

    printScreem(2)

    # Posição da palavra "MetaMask".
    x, y = objectsScreen.positionSelectWallet()

    # Move o mouse para a palavra "MetaMask".
    click.moveMouse(-abs(x), y)

    # Clica no botão
    click.mouseLeftClick()

    # Tempo para carregar
    time.sleep(5)

    printScreem(2)

    # Posição da palavra "Sign".
    x, y = objectsScreen.positionConfirmSign()

    # Move o mouse para a palavra "Sign".
    click.moveMouse(-abs(x) + 1740, y)

    # Clica no botão
    click.mouseLeftClick()

    # Tempo para carregar
    time.sleep(80)

    printScreem(2)

    # Posição do botão "Treasure Hunt", na tela inicial.
    x, y = objectsScreen.positionButtonHunt()
    # print("Posição do botão incial: {}, {}".format(x, y))

    # Move o mouse para a posição do botão "Treasure Hunt", na tela inicial.
    click.moveMouse(-abs(x) + 100, y)

    # Clicar no botão "Treasure Hunt", na tela inicial.
    click.mouseLeftClick()


def notAfk():
    # Move o mouse para o meio da tela da principal.
    click.moveMouse(964, 488)

    # Posição do mouse
    x, y = pyautogui.position()

    pyautogui.moveTo(x - 20, y, 2)

    click.mouseLeftClick()

    pyautogui.moveTo(x + 10, y, 2)

    # Move o mouse para o meio da tela da secundaria.
    click.moveMouse(-964, 488)

    # Posição do mouse
    x, y = pyautogui.position()

    pyautogui.moveTo(x - 20, y, 2)

    click.mouseLeftClick()

    pyautogui.moveTo(x + 10, y, 2)


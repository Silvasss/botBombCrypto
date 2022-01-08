import os
import time

import pyautogui

import clickScreen as click

import positionsObjectsScreen as objectsScreen
from positionsObjectsScreen import sleepingQuantity
from printScreen import printScreem
from playsound import playsound


# Função que coloca todos os personagens para trabalhar.
def execMain(functionAll):
    printScreem(0)

    # Quantidade de bonecos dormindo.
    if sleepingQuantity() >= 0:

        # Manipulação da tela round
        def screenRound():
            try:
                printScreem(0)

                # Posição do botão "volta"
                x, y = objectsScreen.positionButtonBack()

                # Move o cursos do mouse para o botão "volta".
                click.moveMouse(x, y)

                # Clicar no botão "voltar".
                click.mouseLeftClick()

                return True
            except:
                return False

        # Manipulação da tela home
        def screenHome():
            printScreem(0)
            try:
                printScreem(0)

                # Posição do botão "Heroes".
                x, y = objectsScreen.positionButtonHeroes()

                time.sleep(1)
                # Move o mouse para o botão "Heroes".
                click.moveMouse(x, y)

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
                click.moveMouse(x, y)

                # Clicar no botão "Close", na tela personagens.
                click.mouseLeftClick()

                time.sleep(2)

                printScreem(0)

                # Posição do botão "Treasure Hunt", na tela inicial.
                x, y = objectsScreen.positionButtonHunt()

                # Move o mouse para a posição do botão "Treasure Hunt", na tela inicial.
                click.moveMouse(x, y)

                # Clicar no botão "Treasure Hunt", na tela inicial.
                click.mouseLeftClick()

                return True
            except:
                pass

        # Manipulação da tela dos personagens
        def screenCharacter():
            try:
                time.sleep(10)

                printScreem(0)

                # Posição da palavra "Work".
                x, y = objectsScreen.positionButtonWork()

                # Move o mouse para o último boneco da primeira parte da lista.
                click.moveMouse(x - 240, y + 10)

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

        # Manipulação da tela dos personagens
        def screenCharacterAll():
            try:
                time.sleep(10)

                printScreem(0)

                # Posição da palavra "all".
                x, y = objectsScreen.positionButtonAll()

                # Move o mouse para o botão.
                click.moveMouse(x, y)

                # Clica no botão "all".
                click.mouseRepeatClick(1)

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

            if screenHome():
                print("ScreenHome: True")
            else:
                print("Função ScreenHome: False")

            if functionAll:
                if screenCharacterAll():
                    print("ScreenCharacterAll: True")
                else:
                    print("Função ScreenCharacterAll: False")
            else:
                if screenCharacter():
                    print("ScreenCharacter: True")
                else:
                    print("Função ScreenCharacter: False")

        validacaoFuncoes()
    else:
        pass


# Função para mudar de mapa.
def screenRoundNewMap():
    try:
        time.sleep(2)

        printScreem(0)

        # Posição do texto "New Map".
        x, y = objectsScreen.positionTextNewMap()

        # Move o mouse para o botão "New Map".
        click.moveMouse(x, y)

        # Clica no botão
        click.mouseLeftClick()

        return True
    except IndexError:
        pass


# Função que faz o login e vai para tela "round".
def loginFunction():

    # Tempo para retorna a página inicial.
    time.sleep(30)

    printScreem(0)

    # Posição da frase "Connect Wallet".
    x, y = objectsScreen.positionConnectWallet()

    # Move o mouse para a frase "Connect Wallet".
    click.moveMouse(x, y)

    # Clica no botão
    click.mouseLeftClick()

    # Tempo para carregar
    time.sleep(5)

    printScreem(0)

    # Posição da palavra "MetaMask".
    x, y = objectsScreen.positionSelectWallet()

    # Move o mouse para a palavra "MetaMask".
    click.moveMouse(x, y)

    # Clica no botão
    click.mouseLeftClick()

    # Tempo para carregar
    time.sleep(5)

    printScreem(0)

    # Posição da palavra "Sign".
    x, y = objectsScreen.positionConfirmSign()

    # Move o mouse para a palavra "Sign".
    click.moveMouse(x, y)

    # Clica no botão
    click.mouseLeftClick()

    # Tempo para carregar
    time.sleep(60)

    printScreem(0)

    # Posição do botão "Treasure Hunt", na tela inicial.
    x, y = objectsScreen.positionButtonHunt()
    # print("Posição do botão incial: {}, {}".format(x, y))

    # Move o mouse para a posição do botão "Treasure Hunt", na tela inicial.
    click.moveMouse(x, y)

    # Clicar no botão "Treasure Hunt", na tela inicial.
    click.mouseLeftClick()


# Tela login.
def screenErroCore():
    printScreem(0)

    time.sleep(2)

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


# Função que verifica se existe o erro "Unknown", na tela round.
def screenErroUnknown():

    time.sleep(2)

    printScreem(0)

    # Verifica se existe a palavra "Unknown" na tela.
    objectsScreen.positionErroUnknown()

    # Posição da palavra "Ok".
    x, y = objectsScreen.positionOkErro()

    # Move o mouse para o botão "Ok".
    click.moveMouse(x, y)

    # Clica no botão
    click.mouseLeftClick()

    # Função que faz o login.
    loginFunction()


# Função que verifica se existe o erro "Unstable", na tela.
def screenErroUnstable():
    time.sleep(2)

    printScreem(0)

    # Posição da palavra "Ok".
    x, y = objectsScreen.positionOkErro()

    # Move o mouse para o botão "Ok".
    click.moveMouse(x, y)

    # Clica no botão
    click.mouseLeftClick()

    # Função que faz o login.
    loginFunction()


def screenErroOverloaded():
    printScreem(0)

    time.sleep(2)

    # Verifica se existe a palavra "Overloaded" na tela.
    objectsScreen.positionErroOverloaded()

    # Simula a tecla "F5".
    pyautogui.press("f5")

    # Função que faz o login.
    loginFunction()


def screenErroManual():
    time.sleep(2)

    # Verifica se existe a palavra "Manual" na tela.
    if objectsScreen.positionErroManual(0):
        # Posição da palavra "Ok".
        x, y = objectsScreen.positionOkErro()

        # Move o mouse para o botão "Ok".
        click.moveMouse(x, y)

        # Clica no botão
        click.mouseLeftClick()

        # Função que faz o login.
        loginFunction()

        return True
    else:
        return False


def computerSleep():
    # Faz o computador entrar no modo hibernação.
    os.system(r"shutdown /h")


def soundErro():
    playsound("sound/ClockSound.mp3")

    playsound("sound/ClockSound.mp3")

    playsound("sound/ClockSound.mp3")

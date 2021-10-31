import pyautogui

import positionsObjectsScreen
import positionsObjectsScreen as objectsScreen
import clickScreen as click
from printScreen import printScreem

import time

# Funções que manipula os comandos até chega na tela personagens. Sendo utilizado como auxilio para função
# "screenCharacterSuperRaroLegend()".


# Manipulação da tela round
def screenRound():
    try:
        printScreem()

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
    try:
        printScreem()

        time.sleep(3)

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

        printScreem()

        # Posição do botão "Treasure Hunt", na tela inicial.
        x, y = objectsScreen.positionButtonHunt()
        #print("Posição do botão incial: {}, {}".format(x, y))

        # Move o mouse para a posição do botão "Treasure Hunt", na tela inicial.
        click.moveMouse(x, y)

        # Clicar no botão "Treasure Hunt", na tela inicial.
        click.mouseLeftClick()

        return True
    except:
        pass


# Manipulação da tela dos personagens
def screenCharacterVersion2():
    try:
        time.sleep(2)

        printScreem()

        x, y = positionsObjectsScreen.positionButtonWork()

        #click.moveMouse(x - 240, y + 15)
        click.moveMouse(x + 30, y)
        # Puxa para baixo
        click.mouseDragCharacter()

        time.sleep(2)

        printScreem()

        if objectsScreen.positionTipoBonecoSuperRaroLegend():
            # Posição da palavra "SuperRaro" ou "Legend".
            tipoX, tipoY = objectsScreen.positionTipoBonecoSuperRaroLegend()

            print("Encontrou ------------ SuperRaro ou Legend")
        else:
            print("Não encontrou ------------ SuperRaro ou Legend")
            return False

        # Move o mouse para o nome do tipo do boneco.
        click.moveMouse(tipoX, tipoY)

        pyautogui.moveTo(tipoX + 230, tipoY)

        for i in range(4):
            # Clica no botão "work".
            click.mouseLeftClick()

            time.sleep(2)

        # Manda o boneco para "House".
        click.mouseDragUpCharacterHouse()
        
        if backScreenRound():
            print("Sucesso na função: backScreenRound")
            return True
        else:
            print("Falha na função: backScreenRound")
            return False
    except:
        return False


def screenCharacterSuperRaroLegend():
    # Caso ele tente chama uma vez a função, e de erro e executada novamente.
    def validacaoFuncoes():
        if screenRound() and screenHome():
            print("ScreenRound e ScreenHome: True")

            # Quantidade de personagens que tem que ir para casa.
            for i in range(1):
                print("Entro no FOR: {}".format(i))
                time.sleep(3)
                if screenCharacterVersion2():
                    print("ScreenCharacterVersion2: True")
                else:
                    print("ScreenCharacterVersion2: False")
        else:
            return False

    validacaoFuncoes()
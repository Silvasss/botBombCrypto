import pyautogui

import positionsObjectsScreen as objectsScreen
import clickScreen as click
from printScreen import printScreem

import time

# Funções que manipula os comandos até chega na tela personagens. Sendo utilizado como auxilio para função
# "screenCharacterSuperRaroLegend()".


# Manipulação da tela round.
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
        # Utilizado no for.
        n = 0

        time.sleep(2)

        printScreem()

        # Lista que armazena a posição dos bonecos "SuperRaro" e "Legend".
        listaBonecosEspeciais = []

        if objectsScreen.positionTipoBonecoSuperRaroLegend():
            # Posição das palavras "SuperRaro" ou "Legend".
            listaBonecosEspeciais.append(objectsScreen.positionTipoBonecoSuperRaroLegend())

            # Pegando só a primeira lista
            listaBonecosEspeciais = listaBonecosEspeciais[0]

            # Retirando o terceiro item.
            listaBonecosEspeciais.pop(2)

            print("Encontrou ------------ SuperRaro ou Legend")
        else:
            print("Não encontrou ------------ SuperRaro ou Legend")
            return False

        # Que percorre a lista que contém as posições dos bonecos.
        for i in listaBonecosEspeciais:
            if i:
                # Posição da palavra "SuperRaro" ou "Legend".
                tipoX, tipoY = i[0], i[1]

                # Move o mouse para o nome do tipo do boneco.
                click.moveMouse(tipoX, tipoY)

                pyautogui.moveTo(tipoX + 230, tipoY)

                # Clica no botão "work".
                click.mouseLeftClick()

                time.sleep(2)

                n += 1

            if n > 1:
                printScreem()

                # Zera as posições da lista.
                listaBonecosEspeciais = []

                # Adicionado as posições dos bonecos.
                listaBonecosEspeciais.append(objectsScreen.positionTipoBonecoSuperRaroLegend())

                # Posição da palavra "SuperRaro" ou "Legend".
                tipoX, tipoY = listaBonecosEspeciais[0][-1]

                # Move o mouse para o nome do tipo do boneco.
                click.moveMouse(tipoX, tipoY)

                # Move o mouse para o botão "Work".
                pyautogui.moveTo(tipoX + 230, tipoY)

                # Clica no botão "work".
                click.mouseLeftClick()

                time.sleep(2)

                n += 1

                # Recebe a posição do cursor do mouse.
                x, y = pyautogui.position()

                # Move o curso para o lado do botão "Work".
                click.moveMouse(x - 100, y)

                # Movimento de arrastar para baixo.
                pyautogui.dragRel(0, -y, 1)

                time.sleep(2)

                printScreem()

                # Adicionado as posições dos bonecos.
                listaBonecosEspeciais = objectsScreen.positionTipoBonecoSuperRaroLegend()

                # Posição da palavra "SuperRaro" ou "Legend".
                tipoX, tipoY = listaBonecosEspeciais

                # Move o mouse para o nome do tipo do boneco.
                click.moveMouse(tipoX, tipoY)

                # Move o curso.
                pyautogui.moveTo(tipoX + 230, tipoY)

                # Clica no botão "work".
                click.mouseLeftClick()

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

            if screenCharacterVersion2():
                print("ScreenCharacterVersion2: True")
            else:
                print("ScreenCharacterVersion2: False")
                exit()
        else:
            exit()

    validacaoFuncoes()

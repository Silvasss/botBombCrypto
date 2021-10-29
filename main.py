import pyautogui

from positionsObjectsScreen import sleepingQuantity
import positionsObjectsScreen as objectsScreen
import clickScreen as click
from printScreen import printScreem
from datetime import datetime, timedelta

import time


# Executar o sript na tela do round.
def main():

    def exec():
        # Quantidade de bonecos dormindo.
        if sleepingQuantity() >= 8:

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
                    print("Posição do botão incial: {}, {}".format(x, y))

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
                    time.sleep(2)

                    printScreem()

                    # Posição da palavra "common".
                    x, y = objectsScreen.positionTipoBoneco()

                    # Move o mouse para o último boneco da primeira parte da lista.
                    click.moveMouse(x, y)

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

            print(screenRound(), screenHome(), screenCharacter())

        else:
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
                except:
                    pass

            screenRoundNewMap()

    def verifyTimeFuture():
        # Calculo da hora atual mais 60 minutos.
        # Tempo que o código vai esperar carregar a energia dos bonecos para chamar o próximo passo.
        timeFuture = datetime.now() + timedelta(minutes=1)
        # Formatando o hora futura
        future_time = timeFuture.strftime('%H:%M:%S')

        while True:
            # Recebe a hora atual.
            now = datetime.now()

            # Formatando hora.
            current_time = now.strftime('%H:%M:%S')

            # Verifica se a hora atual e menor que o tempo para rodar o script.
            if current_time > future_time:
                exec()

                return True
            else:
                print("Pausa de 1 minuto: {}".format(datetime.now().strftime('%H:%M:%S')))
                time.sleep(10)
                x, y = pyautogui.position()
                pyautogui.moveTo(x + 20, y + 20, 2)
                click.mouseLeftClick()
                pyautogui.moveTo(x - 20, y - 20, 2)

    while True:
        print("Ciclo completo: {}".format(verifyTimeFuture()))


# For com loop eterno, com sleep de 3m.
if __name__ == "__main__":
    main()

    # Toda vez que ocorrer um erro, fecha e abrir novamente o jogo em uma nova aba.


"""
exec()
print("Pausa de 1 minuto: {}".format(datetime.now().strftime('%H:%M:%S')))
time.sleep(1)
"""
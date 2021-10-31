import pyautogui
import execute, executeSuperRaroLegend
import clickScreen as click
from datetime import datetime, timedelta
import time


# Executar o sript na tela do round.
def main(homeCasa):

    def verifyTimeFuture():
        casa = homeCasa

        # Calculo da hora atual mais 60 minutos.
        # Tempo que o código vai esperar carregar a energia dos bonecos para chamar o próximo passo.
        timeFuture = datetime.now() + timedelta(minutes=60)
        # Formatando o hora futura
        future_time = timeFuture.strftime('%H:%M')

        # Calculo da hora atual mais 20 minutos.
        # Tempo que o código vai esperar os bonecos "SuperRaros" e "Legend" cansarem, para mandar eles para casa.
        timeFutureRaroLegend = datetime.now() + timedelta(minutes=20)
        # Formatando o hora futura dos raros e lendas.
        futureRaroLegend_time = timeFuture.strftime('%H:%M')

        # While com loop eterno, com sleep de 3m.
        while True:
            # Recebe a hora atual.
            now = datetime.now()

            # Formatando hora.
            current_time = now.strftime('%H:%M')

            # Verifica se a hora atual e menor que o tempo para rodar o script.
            if current_time > future_time:
                execute.execMain()

                return True
            else:
                # Verifica se a hora atual e igual a hora futura e a função "Home" e true.
                if current_time >= futureRaroLegend_time and casa:
                    # Função que vai navegar até a tela "Character" e manipular os comandos necessários.
                    executeSuperRaroLegend.screenCharacterSuperRaroLegend()

                    casa = False
                try:
                    # Verifica se tem que mudar de mapa.
                    execute.screenRoundNewMap()

                    # Verifica se deu erro o "Unknown".
                    execute.screenErroUnknown()
                except:
                    pass

                print("Pausa de 3 minuto: {}".format(datetime.now().strftime('%H:%M:%S')))
                time.sleep(180)

                # Move o mouse, não AFK.
                x, y = pyautogui.position()
                pyautogui.moveTo(x - 20, y, 2)
                click.mouseLeftClick()
                pyautogui.moveTo(x + 10, y, 2)

    while True:
        print("Ciclo completo: {}".format(verifyTimeFuture()))


if __name__ == "__main__":
    # Ativar função "Home".
    home = False
    executeSuperRaroLegend.screenCharacterSuperRaroLegend()
    #main(home)

    # Toda vez que ocorrer um erro, fecha e abrir novamente o jogo em uma nova aba.


"""
exec()
print("Pausa de 1 minuto: {}".format(datetime.now().strftime('%H:%M:%S')))
time.sleep(1)
"""